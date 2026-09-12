#!/usr/bin/env python3
"""Generate static, crawlable reader pages for the live-fetch collections.

Signal, the Thought Series and the three books are read through single-page
shells that fetch their .md client-side. That reading experience is good and is
left untouched - but it means the prose never appears in served HTML, so ~190
pieces of writing were invisible to search engines and had no permalink to
share. This generator emits one static page per piece alongside each shell.

Ordering and titles come from the shell's own CH manifest, which stays the
single source of truth - add a chapter there (as before) and it gets a page.
Dates come from git (first commit that added the .md), so nothing needs
back-filling by hand.

Run from repo root:  python tools/generate_readers.py
Idempotent: re-running with unchanged .md and manifests produces identical
output.
"""
import io
from pathlib import Path
import re
import subprocess

from generate_field_notes import _attr, _inline, fmt_date, md_to_html

ROOT = Path(__file__).resolve().parent.parent

# ------------------------------------------------------------------ collections
# shell     - page carrying the CH manifest (also the collection's index URL)
# md_dir    - where the manifest's filenames resolve, relative to repo root
# label     - series name shown in the page eyebrow
# kicker    - what a piece is called ("Post", "Chapter", "Essay")
COLLECTIONS = [
    dict(key="signal", shell="publications/signal/index.html",
         md_dir="signals-series", label="Signal", kicker="Post",
         blurb="Unfiltered observations from the field - forensic, declarative, "
               "each post standing alone while building one argument about "
               "reality and decision-making."),
    dict(key="book", shell="publications/book/index.html",
         md_dir="book", label="Where Architecture Truly Creates Value",
         kicker="Chapter",
         blurb="The complete case for decision-first architecture - why the unit "
               "of architecture is the decision, and what that changes."),
    dict(key="holding-the-line", shell="publications/holding-the-line/index.html",
         md_dir="publications/holding-the-line", label="Holding the Line",
         kicker="Chapter",
         blurb="On leadership - the conviction to create clarity, extend trust, "
               "own the decision, protect people, and prepare others to lead "
               "without you."),
    dict(key="reading-the-map", shell="publications/reading-the-map/index.html",
         md_dir="publications/reading-the-map", label="Reading the Map",
         kicker="Chapter",
         blurb="A navigation guide to enterprise architecture - the frameworks, "
               "concepts and language of the territory architects work in."),
]

# the Thought Series is six sibling shells sharing one shape
_SERIES = [
    ("series-01", "series-01-foundations", "Thought Series I - Foundations"),
    ("series-02", "series-02-decision-velocity", "Thought Series II - Decision Velocity"),
    ("series-03", "series-03-the-architecture-operating-system",
     "Thought Series III - The Architecture Operating System"),
    ("series-04", "series-04-architecture-as-a-decision-system",
     "Thought Series IV - Architecture as a Decision System"),
    ("series-05", "series-05-the-implementation-arc",
     "Thought Series V - The Implementation Arc"),
    ("series-06", "series-06-before-the-decision",
     "Thought Series VI - Before the Decision"),
]
for _slug, _dir, _label in _SERIES:
    COLLECTIONS.append(dict(
        key=f"thought-series/{_slug}",
        shell=f"publications/thought-series/{_slug}/index.html",
        md_dir=f"series/{_dir}", label=_label, kicker="Essay",
        blurb="Part of the OrdoAnimi essay sequence - tracing the movement from "
              "documentation and governance theatre toward decision systems, "
              "constraint infrastructure and implementation.",
    ))

# --------------------------------------------------------------------- manifest
# Tolerates both quote styles, 3- or 4-field rows, and reading-the-map's
# `EXIST+'file.md'` prefix form.
_ROW = re.compile(
    r"""^\s*\[\s*
        (['"])(?P<id>.*?)\1\s*,\s*
        (['"])(?P<title>.*?)\3\s*,\s*
        (?:[A-Za-z_]+\s*\+\s*)?(['"])(?P<file>.*?)\5\s*
        (?:,\s*(['"])(?P<section>.*?)\7\s*)?
        \]""",
    re.VERBOSE,
)

def parse_manifest(shell_path):
    rows = []
    for line in shell_path.read_text(encoding="utf-8").splitlines():
        m = _ROW.match(line)
        if m and m.group("file").endswith(".md"):
            rows.append(dict(id=m.group("id"), title=m.group("title"),
                             file=m.group("file")))
    return rows

# ------------------------------------------------------------------- git dates
_date_cache = {}

def first_commit_date(rel_path):
    """ISO date of the commit that added this file - i.e. when it was published."""
    if rel_path in _date_cache:
        return _date_cache[rel_path]
    try:
        out = subprocess.run(
            ["git", "log", "--diff-filter=A", "--format=%as", "-1", "--", rel_path],
            cwd=ROOT, capture_output=True, text=True, timeout=20,
        ).stdout.strip()
    except Exception:
        out = ""
    # a file added in the working tree but not yet committed has no date; the
    # page simply omits the byline date rather than inventing one
    _date_cache[rel_path] = out
    return out

# ------------------------------------------------------------------- rendering
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"/>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:'
         'ital,wght@0,500;0,600;0,700;1,600&family=DM+Mono:wght@300;400;500&'
         'family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet"/>')

def nav(active_href):
    def li(href, text):
        cls = ' class="active"' if href == active_href else ""
        return f'<li><a href="{href}"{cls}>{text}</a></li>'
    return (
        '<nav class="pub-nav">\n'
        '<a href="/" class="pub-nav-brand">OrdoAnimi</a>\n'
        '<ul class="pub-nav-links">\n'
        + li("/", "Home") + "\n"
        + li("/publications/", "Publications") + "\n"
        + li("/publications/thought-series/", "Thought Series") + "\n"
        + li("/publications/signal/", "Signal") + "\n"
        + li("/publications/field-notes/", "Field Notes") + "\n"
        + '</ul>\n</nav>'
    )

def footer(index_href, label):
    return (
        '<footer class="pub-footer">\n'
        '<div class="pub-footer-inner">\n'
        '<span class="pub-footer-copy">&copy; Phil Myint &middot; OrdoAnimi '
        '&middot; CC BY 4.0</span>\n'
        '<div class="pub-footer-links">\n'
        f'<a href="{index_href}">{_inline(label)}</a>\n'
        '<a href="/publications/">Publications</a>\n'
        '<a href="/">Framework</a>\n'
        '<a href="/admin/">Edit</a>\n'
        '</div>\n</div>\n</footer>'
    )

def _nav_link(href, cls, direction, title):
    return (f'<a href="{href}" class="{cls}">\n'
            f'<span class="nav-direction">{direction}</span>\n'
            f'<span class="nav-title">{title}</span>\n'
            f'</a>')

def summarise(body_html, limit=180):
    """First paragraph as plain text, for meta descriptions and feed summaries.

    body_html already carries HTML entities (&rsquo; etc). They are decoded back
    to characters here so that callers can escape once for their own context -
    escaping the entity itself would emit a literal '&rsquo;' to the reader.
    """
    import html
    m = re.search(r"<p>(.*?)</p>", body_html, re.DOTALL)
    if not m:
        return ""
    text = re.sub(r"<[^>]+>", "", m.group(1))
    text = html.unescape(text)
    text = " ".join(text.split())
    if len(text) > limit:
        text = text[:limit].rsplit(" ", 1)[0] + "..."
    return text

def render_page(coll, item, prev, nxt, depth):
    css = "../" * depth + "pub.css"
    index_href = "/" + coll["shell"][:-len("index.html")]
    canonical = f"https://framework.ordoanimi.com/{coll['shell'][:-len('index.html')]}{item['slug']}.html"

    prev_a = (_nav_link(f"{prev['slug']}.html", "article-nav-prev", "&larr; Previous",
                        _inline(prev["title"])) if prev else
              _nav_link(index_href, "article-nav-prev", "&larr; Index", _inline(coll["label"])))
    next_a = (_nav_link(f"{nxt['slug']}.html", "article-nav-next", "Next &rarr;",
                        _inline(nxt["title"])) if nxt else
              _nav_link(index_href, "article-nav-next", "Index &rarr;", _inline(coll["label"])))
    index_a = _nav_link(index_href, "article-nav-index", "&uarr;",
                        _inline(coll["label"]) + " Index")

    desc = _attr(summarise(item["body_html"]) or coll["blurb"])
    byline = "Phil Myint &middot; OrdoAnimi"
    if item["date"]:
        byline += f" &middot; {fmt_date(item['date'])}"

    return (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n'
        '<link rel="icon" type="image/svg+xml" href="/favicon.svg">\n'
        '<link rel="apple-touch-icon" href="/apple-touch-icon.png">\n'
        '<meta charset="UTF-8"/>\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0"/>\n'
        f'<title>{_inline(item["title"])} &mdash; {_inline(coll["label"])} &mdash; OrdoAnimi</title>\n'
        f'<meta name="description" content="{desc}"/>\n'
        f'<link rel="canonical" href="{canonical}"/>\n'
        f'<meta property="og:title" content="{_attr(item["title"])}"/>\n'
        f'<meta property="og:description" content="{desc}"/>\n'
        f'<meta property="og:url" content="{canonical}"/>\n'
        '<meta property="og:type" content="article"/>\n'
        f'{FONTS}\n'
        f'<link rel="stylesheet" href="{css}"/>\n'
        '</head>\n<body>\n\n'
        f'{nav(index_href)}\n\n'
        '<header class="article-header">\n'
        '<div class="article-header-inner">\n'
        f'<span class="article-series-label">{_inline(coll["label"])} &middot; '
        f'{coll["kicker"]} {_inline(item["id"])}</span>\n'
        f'<h1 class="article-title">{_inline(item["title"])}</h1>\n'
        f'<p class="article-byline">{byline}</p>\n'
        '</div>\n</header>\n\n'
        '<main>\n<div class="article-body">\n<div class="article-body-inner">\n\n'
        f'{item["body_html"]}\n\n'
        f'<p class="article-byline-end">Phil Myint &middot; OrdoAnimi &middot; '
        f'{_inline(coll["label"])}</p>\n'
        '</div>\n</div>\n\n'
        '<hr class="section-divider"/>\n\n'
        '<nav class="article-nav">\n'
        f'{prev_a}\n{index_a}\n{next_a}\n'
        '</nav>\n</main>\n\n'
        f'{footer(index_href, coll["label"])}\n\n'
        '</body>\n</html>\n'
    )

# ------------------------------------------------------------------------ main
def build(coll):
    shell = ROOT / coll["shell"]
    if not shell.exists():
        print(f"  {coll['key']}: SKIP (no shell at {coll['shell']})")
        return []
    out_dir = shell.parent
    # hops from the page's own directory up to publications/, where pub.css lives
    depth = len(Path(coll["shell"]).parts) - 2
    rows = parse_manifest(shell)
    if not rows:
        print(f"  {coll['key']}: WARNING no manifest rows parsed")
        return []

    items = []
    for r in rows:
        rel_md = f"{coll['md_dir']}/{r['file']}"
        md = ROOT / rel_md
        if not md.exists():
            print(f"  {coll['key']}: WARNING missing source {rel_md}")
            continue
        items.append(dict(
            id=r["id"], title=r["title"], slug=Path(r["file"]).stem,
            seq=len(items),  # manifest order = intended publication sequence
            date=first_commit_date(rel_md),
            body_html=md_to_html(md.read_text(encoding="utf-8")),
            url=f"/{coll['shell'][:-len('index.html')]}{Path(r['file']).stem}.html",
        ))

    for i, it in enumerate(items):
        prev = items[i - 1] if i > 0 else None
        nxt = items[i + 1] if i < len(items) - 1 else None
        (out_dir / f"{it['slug']}.html").write_text(
            render_page(coll, it, prev, nxt, depth), encoding="utf-8")
    inject_toc(shell, items)
    print(f"  {coll['key']}: {len(items)} pages")
    return items

# ------------------------------------------------------- crawlable shell index
_TOC_BLOCK = re.compile(r'(<nav id="tocList"[^>]*>)(.*?)(</nav>)', re.DOTALL)
_GUARD = "if (!tocList.querySelector('a.ch')) "

def inject_toc(shell_path, items):
    """Server-render the shell's chapter list and let its JS enhance rather than
    build it.

    The list was built entirely client-side, so crawlers saw an empty <nav> and
    never reached the chapters - the reason this corpus was unindexed. Rendering
    the same markup server-side keeps the sidebar, the search box (which filters
    these nodes) and the styling identical, while making every piece reachable
    without JS. Links point at the static pages, so a TOC click now lands on a
    real URL; the old #id routing still works for existing bookmarks.
    """
    with io.open(shell_path, "r", encoding="utf-8", newline="") as f:
        text = f.read()

    links = "\n".join(
        f'<a class="ch" href="{it["slug"]}.html" data-id="{_attr(it["id"])}">'
        f'<span class="num">{_inline(it["id"])}</span>'
        f'<span class="t">{_inline(it["title"])}</span></a>'
        for it in items
    )
    if not _TOC_BLOCK.search(text):
        print(f"    WARNING no #tocList in {shell_path.name}; skipped TOC injection")
        return False
    text = _TOC_BLOCK.sub(lambda m: m.group(1) + "\n" + links + "\n" + m.group(3),
                          text, count=1)

    # guard the JS builder so it does not duplicate the server-rendered links
    lines = text.splitlines(keepends=True)
    for i, ln in enumerate(lines):
        if "document.getElementById('tocList')" in ln:
            for j in range(i + 1, min(i + 4, len(lines))):
                stripped = lines[j].lstrip()
                if stripped.startswith("CH.forEach("):
                    indent = lines[j][: len(lines[j]) - len(stripped)]
                    lines[j] = indent + _GUARD + stripped
                    break
                if stripped.startswith(_GUARD):
                    break
            break
    text = "".join(lines)

    with io.open(shell_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return True

# ----------------------------------------------------------------------- feeds
SITE = "https://framework.ordoanimi.com"

def _rfc822(iso):
    """'2026-06-15' -> 'Sun, 15 Jun 2026 00:00:00 +0000' (RSS pubDate format)."""
    import datetime
    try:
        d = datetime.date.fromisoformat(iso)
    except Exception:
        return ""
    return d.strftime("%a, %d %b %Y 00:00:00 +0000")

def write_feed(path, title, description, link, items):
    """items: newest-first dicts of title/url/date/summary."""
    entries = []
    for it in items:
        pub = _rfc822(it["date"])
        entries.append(
            "<item>\n"
            f"<title>{_attr(it['title'])}</title>\n"
            f"<link>{SITE}{it['url']}</link>\n"
            f"<guid isPermaLink=\"true\">{SITE}{it['url']}</guid>\n"
            + (f"<pubDate>{pub}</pubDate>\n" if pub else "")
            + f"<description>{_attr(it['summary'])}</description>\n"
            "</item>"
        )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n<channel>\n'
        f"<title>{_attr(title)}</title>\n"
        f"<link>{SITE}{link}</link>\n"
        f"<description>{_attr(description)}</description>\n"
        "<language>en-AU</language>\n"
        f'<atom:link href="{SITE}/{path.name}" rel="self" type="application/rss+xml"/>\n'
        + "\n".join(entries) +
        "\n</channel>\n</rss>\n"
    )
    path.write_text(xml, encoding="utf-8")

def build_feeds(built):
    """One feed per serial. Books are omitted - a 60-chapter book dropping into
    a reader's timeline at once is noise, not a subscription."""
    def items_for(keys):
        out = []
        for k in keys:
            coll = next(c for c in COLLECTIONS if c["key"] == k)
            for it in built.get(k, []):
                out.append(dict(title=f"{coll['label']} - {it['title']}"
                                if k.startswith("thought-series") else it["title"],
                                url=it["url"], date=it["date"], seq=it["seq"],
                                summary=summarise(it["body_html"], 320)))
        # Newest first. Whole collections were often committed in one batch, so
        # git dates tie; manifest sequence is the real publication order and
        # breaks the tie deterministically.
        out.sort(key=lambda i: (i["date"] or "", i["seq"]), reverse=True)
        return out

    # Field Notes live in the other generator (real frontmatter dates), but the
    # feed belongs with the rest of them.
    from generate_field_notes import load_notes
    field_notes = sorted(
        (dict(title=n["title"], url=f"/publications/field-notes/{n['slug']}.html",
              date=n["date"], summary=n["subtitle"] or summarise(n["body_html"], 320))
         for n in load_notes()),
        key=lambda i: i["date"] or "", reverse=True,
    )

    feeds = [
        ("field-notes.xml", "OrdoAnimi - Field Notes",
         "First-person notes from the worksite - the Coffee and Curiosity series.",
         "/publications/field-notes/", field_notes),
        ("signal.xml", "OrdoAnimi - Signal",
         "Practitioner observations from the field.", "/publications/signal/",
         items_for(["signal"])),
        ("thought-series.xml", "OrdoAnimi - Thought Series",
         "Long-form essays on decision systems and architecture practice.",
         "/publications/thought-series/",
         items_for([c["key"] for c in COLLECTIONS if c["key"].startswith("thought-series")])),
    ]
    for name, title, desc, link, items in feeds:
        if not items:
            continue
        write_feed(ROOT / name, title, desc, link, items)
        print(f"  feed {name}: {len(items)} items")

# --------------------------------------------------------------------- sitemap
_SITEMAP_START = "<!-- GENERATED-READER-PAGES-START -->"
_SITEMAP_END = "<!-- GENERATED-READER-PAGES-END -->"
_SITEMAP_BLOCK = re.compile(
    re.escape(_SITEMAP_START) + r".*?" + re.escape(_SITEMAP_END), re.DOTALL)

def update_sitemap(urls):
    """Add every generated page to sitemap.xml, inside markers.

    The hand-written section entries above the markers are left alone - only the
    generated block is rewritten, so re-running never disturbs curated URLs.
    """
    path = ROOT / "sitemap.xml"
    if not path.exists():
        print("  sitemap.xml not found; skipped")
        return
    with io.open(path, "r", encoding="utf-8", newline="") as f:
        text = f.read()

    block = (_SITEMAP_START + "\n"
             + "\n".join(f"<url><loc>{SITE}{u}</loc></url>" for u in sorted(urls))
             + "\n" + _SITEMAP_END)

    if _SITEMAP_BLOCK.search(text):
        text = _SITEMAP_BLOCK.sub(block, text, count=1)
    else:
        text = text.replace("</urlset>", block + "\n</urlset>", 1)

    with io.open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"  sitemap.xml: {len(urls)} generated URLs")

def main():
    total = {}
    for coll in COLLECTIONS:
        total[coll["key"]] = build(coll)
    print(f"\nreaders: {sum(len(v) for v in total.values())} static pages across "
          f"{len(total)} collections")
    build_feeds(total)

    urls = [it["url"] for items in total.values() for it in items]
    try:
        from generate_field_notes import load_notes
        urls += [f"/publications/field-notes/{n['slug']}.html" for n in load_notes()]
    except Exception as exc:
        print(f"  field-note URLs unavailable for sitemap: {exc}")
    update_sitemap(urls)
    return total

if __name__ == "__main__":
    main()
