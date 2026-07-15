#!/usr/bin/env python3
"""Generate self-contained Field Note reader pages from their .md source.

Unlike the research/publications generator (which emits runtime-fetch shells),
field-note pages EMBED their rendered content, so they must be regenerated
whenever the .md changes. Ordering, the "Field Note NN" number, the index
sequence and prev/next links all derive from the `number:` frontmatter field —
which makes the .md file the single source of truth.

Run from repo root:  python tools/generate_field_notes.py
Idempotent: re-running with unchanged .md produces identical output.
"""
from pathlib import Path
import re
import calendar

FN_DIR = Path(__file__).resolve().parent.parent / "publications" / "field-notes"
BASE = "/publications/field-notes/"

# ---------------------------------------------------------------- frontmatter
def parse_frontmatter(text):
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    fm_raw = text[3:end].strip("\n")
    body = text[end + 4:].lstrip("\n")
    meta = {}
    for line in fm_raw.split("\n"):
        m = re.match(r'^([A-Za-z_]+):\s*(.*)$', line)
        if m:
            val = m.group(2).strip()
            if len(val) >= 2 and val[0] == '"' and val[-1] == '"':
                val = val[1:-1]
            meta[m.group(1)] = val
    return meta, body

# ------------------------------------------------------------- inline markdown
def _inline(text):
    # 1. escape HTML structural chars
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    # 2. typographic glyphs -> ASCII-safe HTML entities (no raw non-ASCII in output)
    text = text.replace("—", "&mdash;").replace("–", "&ndash;").replace("…", "&hellip;")
    # 3. smart double quotes in prose, alternating open/close
    out, open_q = [], True
    for ch in text:
        if ch == '"':
            out.append("&ldquo;" if open_q else "&rdquo;")
            open_q = not open_q
        else:
            out.append(ch)
    text = "".join(out)
    # 4. apostrophes / single quotes -> right single quote
    text = text.replace("’", "&rsquo;").replace("'", "&rsquo;")
    # 5. markdown inline LAST, so the ASCII quotes in generated tags survive
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<em>\1</em>', text)
    return text

def _attr(text):
    return (text.replace("&", "&amp;").replace('"', "&quot;")
                .replace("<", "&lt;").replace(">", "&gt;"))

def md_to_html(body):
    """Focused Markdown -> HTML. Drops a single leading '# Title' (shown in the
    page header already). Supports h2/h3, paragraphs, lists, blockquote, hr."""
    body = body.strip("\n")
    lines = body.split("\n")
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    body = "\n".join(lines).strip("\n")
    out = []
    for block in re.split(r'\n\s*\n', body):
        b = block.strip("\n")
        s = b.strip()
        if not s:
            continue
        rows = [ln for ln in b.split("\n") if ln.strip()]
        if s.startswith("## "):
            out.append(f"<h2>{_inline(s[3:].strip())}</h2>")
        elif s.startswith("### "):
            out.append(f"<h3>{_inline(s[4:].strip())}</h3>")
        elif s.startswith("# "):
            out.append(f"<h2>{_inline(s[2:].strip())}</h2>")
        elif s == "---":
            out.append('<hr class="content-divider"/>')
        elif all(r.strip().startswith(("- ", "* ")) for r in rows):
            items = "".join(f"<li>{_inline(r.strip()[2:])}</li>" for r in rows)
            out.append(f"<ul>{items}</ul>")
        elif all(re.match(r'^\d+\.\s', r.strip()) for r in rows):
            def _oli(r):
                return "<li>" + _inline(re.sub(r'^\d+\.\s+', '', r.strip())) + "</li>"
            out.append("<ol>" + "".join(_oli(r) for r in rows) + "</ol>")
        elif s.startswith("> "):
            inner = " ".join(r.strip()[2:] if r.strip().startswith("> ") else r.strip() for r in rows)
            out.append(f"<blockquote><p>{_inline(inner)}</p></blockquote>")
        else:
            out.append(f"<p>{_inline(' '.join(r.strip() for r in rows))}</p>")
    return "\n".join(out)

def fmt_date(d):
    """'2026-06-15' -> '15 June 2026' (no leading zero, cross-platform)."""
    try:
        y, m, day = d.split("-")
        return f"{int(day)} {calendar.month_name[int(m)]} {int(y)}"
    except Exception:
        return d

# --------------------------------------------------------------- page template
NAV = (
    '<nav class="pub-nav">\n'
    '<a href="/" class="pub-nav-brand">OrdoAnimi</a>\n'
    '<ul class="pub-nav-links">\n'
    '<li><a href="/">Home</a></li>\n'
    '<li><a href="/publications/">Publications</a></li>\n'
    '<li><a href="/publications/thought-series/">Thought Series</a></li>\n'
    '<li><a href="/publications/signal/">Signal</a></li>\n'
    '<li><a href="/publications/field-notes/" class="active">Field Notes</a></li>\n'
    '</ul>\n'
    '</nav>'
)
FOOTER = (
    '<footer class="pub-footer">\n'
    '<div class="pub-footer-inner">\n'
    '<span class="pub-footer-copy">&copy; Phil Myint &middot; OrdoAnimi &middot; CC BY 4.0</span>\n'
    '<div class="pub-footer-links">\n'
    '<a href="/publications/field-notes/">Field Notes</a>\n'
    '<a href="/publications/">Publications</a>\n'
    '<a href="/">Framework</a>\n'
    '</div>\n'
    '</div>\n'
    '</footer>'
)
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"/>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,600&family=DM+Mono:wght@300;400;500&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet"/>')

def _nav_link(note, cls, direction, title):
    return (f'<a href="{note}" class="{cls}">\n'
            f'<span class="nav-direction">{direction}</span>\n'
            f'<span class="nav-title">{title}</span>\n'
            f'</a>')

def render_page(n, prev, nxt):
    if prev:
        prev_a = _nav_link(f"{prev['slug']}.html", "article-nav-prev", "&larr; Previous", _inline(prev["title"]))
    else:
        prev_a = _nav_link(BASE, "article-nav-prev", "&larr; Index", "Field Notes")
    if nxt:
        next_a = _nav_link(f"{nxt['slug']}.html", "article-nav-next", "Next &rarr;", _inline(nxt["title"]))
    else:
        next_a = _nav_link(BASE, "article-nav-next", "Index &rarr;", "Field Notes")
    index_a = _nav_link(BASE, "article-nav-index", "&uarr;", "Field Notes Index")

    return (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n'
        '<link rel="icon" type="image/svg+xml" href="/favicon.svg">\n'
        '<link rel="apple-touch-icon" href="/apple-touch-icon.png">\n'
        '<meta charset="UTF-8"/>\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0"/>\n'
        f'<title>{_inline(n["title"])} &mdash; OrdoAnimi</title>\n'
        f'<meta name="description" content="{_attr(n["subtitle"])}"/>\n'
        f'{FONTS}\n'
        '<link rel="stylesheet" href="../pub.css"/>\n'
        '</head>\n<body>\n\n\n'
        f'{NAV}\n\n'
        '<header class="article-header">\n'
        '<div class="article-header-inner">\n'
        f'<span class="article-series-label">Coffee and Curiosity &middot; Field Note {n["number"]:02d}</span>\n'
        f'<h1 class="article-title">{_inline(n["title"])}</h1>\n'
        f'<p class="article-tagline">{_inline(n["subtitle"])}</p>\n'
        f'<p class="article-byline">Phil Myint &middot; OrdoAnimi &middot; {fmt_date(n["date"])}</p>\n'
        '</div>\n</header>\n\n'
        '<main>\n<div class="article-body">\n<div class="article-body-inner">\n\n'
        f'{n["body_html"]}\n\n'
        '<p class="article-byline-end">Phil Myint &middot; OrdoAnimi &middot; Coffee and Curiosity &mdash; Field Notes</p>\n'
        '</div>\n</div>\n\n'
        '<hr class="section-divider"/>\n\n'
        '<nav class="article-nav">\n'
        f'{prev_a}\n{index_a}\n{next_a}\n'
        '</nav>\n</main>\n\n'
        f'{FOOTER}\n\n'
        '</body>\n</html>\n'
    )

INDEX_DESC = ("Coffee and Curiosity field notes &mdash; first-person practitioner writing on "
              "AI-assisted delivery, executable architecture, and decision governance.")

def render_index(notes):
    items = []
    for n in notes:
        items.append(
            f'<a href="{BASE}{n["slug"]}.html" class="article-list-item">\n'
            f'<span class="article-num">{n["number"]:02d}</span>\n'
            '<div class="article-list-meta">\n'
            f'<p class="article-list-title">{_inline(n["title"])}</p>\n'
            f'<p class="article-list-tagline">{_inline(n["subtitle"])}</p>\n'
            '</div>\n'
            '<span class="article-list-status published">Published</span>\n'
            '</a>'
        )
    return (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n'
        '<link rel="icon" type="image/svg+xml" href="/favicon.svg">\n'
        '<link rel="apple-touch-icon" href="/apple-touch-icon.png">\n'
        '<meta charset="UTF-8"/>\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0"/>\n'
        '<title>Field Notes &mdash; OrdoAnimi</title>\n'
        f'<meta name="description" content="{INDEX_DESC}"/>\n'
        f'{FONTS}\n'
        '<link rel="stylesheet" href="../pub.css"/>\n'
        '</head>\n<body>\n\n\n'
        f'{NAV}\n\n'
        '<header class="pub-header">\n'
        '<div class="pub-header-inner">\n'
        '<span class="pub-eyebrow">OrdoAnimi &middot; Field Notes</span>\n'
        '<h1 class="pub-title">Field Notes</h1>\n'
        '<p class="pub-desc">First-person notes from the worksite &mdash; the Coffee and Curiosity '
        'series on executable architecture, FinRevDevOps, runtime governance, judgement, and order. '
        'Written while building, not after.</p>\n'
        '</div>\n</header>\n\n'
        '<main>\n<div class="article-list">\n\n'
        + "\n".join(items) +
        '\n\n</div>\n</main>\n\n'
        f'{FOOTER}\n\n'
        '</body>\n</html>\n'
    )

def load_notes():
    notes = []
    for md in sorted(FN_DIR.glob("*.md")):
        meta, body = parse_frontmatter(md.read_text(encoding="utf-8"))
        if "number" not in meta or "title" not in meta:
            continue  # not a numbered field note (e.g. linkedin-posts.md)
        notes.append({
            "slug": md.stem,
            "number": int(meta["number"]),
            "title": meta["title"],
            "subtitle": meta.get("subtitle", ""),
            "date": meta.get("date", ""),
            "body_html": md_to_html(body),
        })
    notes.sort(key=lambda n: n["number"])
    return notes

def main():
    notes = load_notes()
    if not notes:
        print("field-notes: no numbered .md files found")
        return
    for i, n in enumerate(notes):
        prev = notes[i - 1] if i > 0 else None
        nxt = notes[i + 1] if i < len(notes) - 1 else None
        (FN_DIR / f"{n['slug']}.html").write_text(render_page(n, prev, nxt), encoding="utf-8")
        print(f"  field-note {n['number']:02d}: {n['slug']}.html")
    (FN_DIR / "index.html").write_text(render_index(notes), encoding="utf-8")
    print(f"  field-note index: {len(notes)} notes")

if __name__ == "__main__":
    main()
