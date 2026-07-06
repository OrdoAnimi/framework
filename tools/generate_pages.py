#!/usr/bin/env python3
"""
Generate reader pages for new .md files in research/ and publications/.
Run from repo root: python tools/generate_pages.py
"""
import html as _html
import json
import os
import re
import re as _re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
RAW_BASE = 'https://raw.githubusercontent.com/ZenCloudAU/velocity-architecture/main'
GITHUB_BASE = 'https://github.com/ZenCloudAU/velocity-architecture/blob/main'
SKIP_FILES = {'SOURCES.md', 'PUBLISHING.md', 'README.md', 'CITATION.cff', 'CONTRIBUTING.md'}

ECOSYSTEM_STRIP = (
''
)

SHARED_CSS = ':root{--bg:#f2ede0;--surface:#faf7ef;--surface-2:#ebe4d2;--border:#ded7c4;--text:#16231c;--text-2:#5a6354;--text-3:#8c9184;--orange:#b58a34;--orange-subtle:#f7f0dc;--navy:#16231c;--navy-2:#16231c;--r:10px;--shadow-md:0 4px 12px rgba(22,35,28,.08),0 2px 4px rgba(22,35,28,.04)}\n*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:auto}body{background:var(--bg);color:var(--text);font-family:\'DM Sans\',sans-serif;font-weight:300;line-height:1.65}a{color:var(--orange);text-decoration:none}a:hover{text-decoration:underline}nav{position:sticky;top:0;z-index:10;background:rgba(250,247,239,.95);backdrop-filter:blur(12px);border-bottom:1px solid var(--border);padding:0 2rem;min-height:64px;display:flex;align-items:center;justify-content:space-between;gap:1rem;flex-wrap:wrap}.brand{font-family:\'Playfair Display\',serif;font-weight:700;color:var(--text)}.brand sup{font-size:.5rem;color:var(--orange);vertical-align:super}.nav-links{display:flex;gap:1.25rem;flex-wrap:wrap}.nav-links a{font-size:.85rem;color:var(--text-2)}.nav-toggle{display:none;flex-direction:column;gap:5px;background:none;border:none;cursor:pointer;padding:8px;min-width:44px;min-height:44px;align-items:center;justify-content:center;flex-shrink:0}.nav-toggle span{display:block;width:22px;height:2px;background:var(--text-2);border-radius:2px;transition:transform .2s,opacity .2s}.nav-toggle.open span:nth-child(1){transform:translateY(7px) rotate(45deg)}.nav-toggle.open span:nth-child(2){opacity:0}.nav-toggle.open span:nth-child(3){transform:translateY(-7px) rotate(-45deg)}@media(max-width:768px){.nav-toggle{display:flex}.nav-links{display:none;position:absolute;top:64px;left:0;right:0;background:rgba(250,247,239,.97);backdrop-filter:blur(12px);border-bottom:1px solid var(--border);flex-direction:column;align-items:stretch;padding:12px 1.5rem 16px;gap:8px;z-index:99}.nav-links.open{display:flex}.nav-links a{display:block;padding:.6rem .5rem;font-size:.875rem;color:var(--text-2);text-decoration:none}}main{max-width:980px;margin:0 auto;padding:3rem 2rem}.breadcrumb{font-family:\'DM Mono\',monospace;font-size:.68rem;letter-spacing:.08em;color:var(--text-3);margin-bottom:1.5rem}.breadcrumb a{color:var(--text-3)}.breadcrumb a:hover{color:var(--orange)}.hero{background:var(--surface);border:1px solid var(--border);border-radius:var(--r);padding:2rem;box-shadow:var(--shadow-md);margin-bottom:1.5rem}.eyebrow{font-family:\'DM Mono\',monospace;font-size:.65rem;font-weight:500;letter-spacing:.18em;text-transform:uppercase;color:var(--orange);display:block;margin-bottom:.75rem}h1{font-family:\'Playfair Display\',serif;font-size:clamp(1.8rem,4vw,3rem);line-height:1.1;margin-bottom:.75rem}.lead{color:var(--text-2);max-width:760px;line-height:1.65}.reader-actions{display:flex;flex-wrap:wrap;gap:.75rem;margin:1.5rem 0}.reader-actions a{display:inline-flex;align-items:center;min-height:44px;padding:0 .9rem;border:1px solid var(--border);border-radius:7px;background:var(--surface);font-size:.82rem;color:var(--text-2)}.reader-actions a.primary{background:var(--orange);border-color:var(--orange);color:#faf7ef}.reader-actions a:hover{text-decoration:none;border-color:var(--orange);color:var(--orange)}.reader-actions a.primary:hover{background:#8c6a26;color:#faf7ef}.article{background:var(--surface);border:1px solid var(--border);border-radius:var(--r);padding:2.25rem;box-shadow:var(--shadow-md)}.loading,.error{font-family:\'DM Mono\',monospace;font-size:.85rem;color:var(--text-3)}.md{font-size:.96rem;color:var(--text-2);line-height:1.78}.md h1{font-family:\'Playfair Display\',serif;font-size:2.15rem;line-height:1.15;color:var(--text);margin-bottom:1rem}.md h2{font-family:\'Playfair Display\',serif;font-size:1.45rem;color:var(--text);margin:2.2rem 0 .8rem;padding-bottom:.5rem;border-bottom:1px solid var(--border)}.md h3{font-size:1.05rem;font-weight:700;color:var(--text);margin:1.6rem 0 .5rem}.md h4{font-family:\'DM Mono\',monospace;font-size:.75rem;font-weight:500;letter-spacing:.12em;text-transform:uppercase;color:var(--orange);margin:1.25rem 0 .35rem}.md p{margin-bottom:1rem}.md strong{color:var(--text);font-weight:700}.md ul,.md ol{margin:0 0 1rem 1.4rem}.md li{margin-bottom:.35rem}.md blockquote{border-left:3px solid var(--orange);background:var(--orange-subtle);border-radius:0 6px 6px 0;margin:1.5rem 0;padding:.8rem 1.2rem;color:var(--text)}.md blockquote p{margin:0;font-style:italic}.md hr{border:none;border-top:1px solid var(--border);margin:2rem 0}.md table{width:100%;border-collapse:collapse;margin:1.2rem 0;display:block;overflow-x:auto}.md th,.md td{border:1px solid var(--border);padding:.55rem .75rem;text-align:left}.md th{background:var(--surface-2);font-family:\'DM Mono\',monospace;font-size:.68rem;color:var(--text-2);text-transform:uppercase}.md code{font-family:\'DM Mono\',monospace;font-size:.82em;background:var(--surface-2);border:1px solid var(--border);padding:.1em .4em;border-radius:3px}.md pre{background:var(--navy-2);border-radius:8px;padding:1.25rem 1.5rem;overflow-x:auto;margin-bottom:1.25rem}.md pre code{background:none;border:none;padding:0;font-size:.82rem;color:#ded7c4;line-height:1.6}.md a{color:var(--orange)}.source{margin-top:1.5rem;font-family:\'DM Mono\',monospace;font-size:.72rem;color:var(--text-3)}footer{margin-top:3rem;background:var(--navy-2);color:rgba(222,215,196,.65);padding:2rem;border-radius:var(--r)}.footer-links{display:flex;flex-wrap:wrap;gap:1rem;margin-top:1rem}.footer-links a{color:#c9bfa6;font-size:.8rem}@media(max-width:720px){nav{align-items:flex-start;padding:1rem}main{padding:2rem 1rem}.article,.hero{padding:1.25rem}}'

def extract_meta(content: str, filename: str) -> dict:
    lines = content.split('\n')
    title = ''
    h2 = ''
    date_str = ''

    for line in lines:
        stripped = line.strip()
        if stripped.startswith('# ') and not title:
            title = stripped[2:].strip()
        elif stripped.startswith('## ') and not h2:
            h2 = stripped[3:].strip()
        if '**Date:**' in stripped and not date_str:
            date_str = stripped.split('**Date:**')[1].strip()

    description = h2
    if not description:
        for line in lines:
            stripped = line.strip()
            if stripped and not stripped.startswith('#') and not stripped.startswith('**') and stripped != '---':
                description = stripped[:200]
                break

    slug = Path(filename).stem
    if not title:
        title = slug.replace('-', ' ').title()

    return {
        'title': title,
        'description': description[:200] if description else title,
        'eyebrow': derive_eyebrow(slug, date_str),
        'slug': slug,
        'filename': filename,
        'date': date_str,
    }

def derive_eyebrow(slug: str, date_str: str) -> str:
    date_part = date_str or ''
    if re.match(r'^\d{2}-', slug):
        label = 'Research Series'
    elif re.match(r'^[A-Z]', slug):
        label = 'Extended Paper'
    elif 'addendum' in slug:
        label = 'Working Paper · Addendum'
    else:
        label = 'Working Paper'
    return (f'{label} · {date_part}' if date_part else label)

def _reader_script(section: str, filename: str) -> str:
    src = f'{RAW_BASE}/{section}/{filename}'
    gh = f'{GITHUB_BASE}/{section}/{filename}'
    src_js = json.dumps(src)
    gh_js = json.dumps(gh)
    return (
        f"const SRC={src_js};\n"
        "async function load(){\n"
        " const el=document.getElementById('article');\n"
        " try{\n"
        " const r=await fetch(SRC);\n"
        " if(!r.ok)throw 0;\n"
        " el.innerHTML='<div class=\"md\">'+marked.parse(await r.text())+'</div>';\n"
        " }catch{\n"
        f" el.innerHTML='<p class=\"error\">Could not load document. '\n"
        f" +'<a href='+{gh_js}+' target=\"_blank\" rel=\"noopener\">View on GitHub ↗</a></p>';\n"
        " }\n"
        "}\n"
        "load();"
    )

def render_research_page(meta: dict) -> str:
    title = _html.escape(meta['title'])
    description = _html.escape(meta['description'])
    eyebrow = _html.escape(meta['eyebrow'])
    filename = meta['filename']

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} &#x2014; OrdoAnimi</title>
<meta name="description" content="{description}">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=DM+Mono:wght@300;400;500&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/marked@9/marked.min.js"></script>
<style>
{SHARED_CSS}
</style>
</head>
<body>
{ECOSYSTEM_STRIP}
<nav>
<a class="brand" href="/">OrdoAnimi</a>
<div class="nav-links">
<a href="/frameworks/">Framework</a>
<a href="/research/">Research</a>
<a href="/publications/">Publications</a>
<a href="/guides/">Guides</a>
</div>
<button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false"><span></span><span></span><span></span></button>
</nav>
<script>(function(){{var t=document.querySelector(".nav-toggle"),m=document.querySelector(".nav-links");if(t&&m)t.addEventListener("click",function(){{var o=m.classList.toggle("open");t.setAttribute("aria-expanded",o);t.classList.toggle("open")}});}})();</script>
<main>
<div class="breadcrumb">
<a href="/">OrdoAnimi</a> &#x203A;
<a href="/research/">Research</a> &#x203A;
{title}
</div>
<section class="hero">
<span class="eyebrow">{eyebrow}</span>
<h1>{title}</h1>
<p class="lead">{description}</p>
</section>
<div class="reader-actions">
<a class="primary" href="/research/">&#x2190; Research library</a>
<a href="/">The OrdoAnimi Framework</a>
</div>
<article class="article" id="article"><p class="loading">Loading document&#x2026;</p></article>
<footer>
<strong>OrdoAnimi advises, builds, and decides.</strong>
<div class="footer-links">
<a href="/research/">Research</a>
<a href="/">The OrdoAnimi Framework</a>
</div>
</footer>
</main>
<script>
{_reader_script('research', filename)}
</script>
</body>
</html>"""

def render_publications_page(meta: dict) -> str:
    title = _html.escape(meta['title'])
    description = _html.escape(meta['description'])
    eyebrow = _html.escape(meta['eyebrow'])
    filename = meta['filename']

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} &#x2014; OrdoAnimi Publications</title>
<meta name="description" content="{description}">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=DM+Mono:wght@300;400;500&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/marked@9/marked.min.js"></script>
<style>
{SHARED_CSS}
</style>
</head>
<body>
{ECOSYSTEM_STRIP}
<nav>
<a class="brand" href="/">OrdoAnimi</a>
<div class="nav-links">
<a href="/frameworks/">Framework</a>
<a href="/publications/">Publications</a>
<a href="/research/">Research</a>
<a href="/guides/">Guides</a>
</div>
<button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false"><span></span><span></span><span></span></button>
</nav>
<script>(function(){{var t=document.querySelector(".nav-toggle"),m=document.querySelector(".nav-links");if(t&&m)t.addEventListener("click",function(){{var o=m.classList.toggle("open");t.setAttribute("aria-expanded",o);t.classList.toggle("open")}});}})();</script>
<main>
<div class="breadcrumb">
<a href="/">OrdoAnimi</a> &#x203A;
<a href="/publications/">Publications</a> &#x203A;
{title}
</div>
<section class="hero">
<span class="eyebrow">{eyebrow}</span>
<h1>{title}</h1>
<p class="lead">{description}</p>
</section>
<div class="reader-actions">
<a class="primary" href="/publications/">&#x2190; Publication library</a>
<a href="/">The OrdoAnimi Framework</a>
</div>
<article class="article" id="article"><p class="loading">Loading document&#x2026;</p></article>
<footer>
<strong>OrdoAnimi advises, builds, and decides.</strong>
<div class="footer-links">
<a href="/publications/">Publications</a>
<a href="/">The OrdoAnimi Framework</a>
</div>
</footer>
</main>
<script>
{_reader_script('publications', filename)}
</script>
</body>
</html>"""

def update_sidebar(html: str, marker: str, new_button: str) -> str:
    if marker not in html:
        return html
    m = _re.search(r'data-p="([^"]+)"', new_button)
    if m and f'data-p="{m.group(1)}"' in html:
        return html
    return html.replace(marker, new_button + marker)

def _sidebar_button(meta: dict, section: str) -> str:
    return (
        f'<button class="file-btn" data-p="{section}/{meta["filename"]}" '
        f'data-href="{meta["slug"]}/" onclick="loadDoc(this.dataset.p)">'
        f'{meta["title"]}</button>'
    )

def _section_marker(slug: str) -> str:
    if re.match(r'^\d{2}-', slug):
        return '<!-- AUTO-SERIES -->'
    elif re.match(r'^[A-Z]', slug):
        return '<!-- AUTO-EXTENDED -->'
    else:
        return '<!-- AUTO-PAPERS -->'

def process_directory(section_dir: str, section: str, repo_root: str) -> list:
    section_path = Path(section_dir)
    generated = []

    for md_path in sorted(section_path.glob('*.md')):
        if md_path.name in SKIP_FILES:
            continue

        slug = md_path.stem
        target = section_path / slug / 'index.html'
        if target.exists():
            continue

        content = md_path.read_text(encoding='utf-8', errors='replace')
        meta = extract_meta(content, md_path.name)

        if section == 'research':
            html = render_research_page(meta)
        else:
            html = render_publications_page(meta)

        target.parent.mkdir(exist_ok=True)
        target.write_text(html, encoding='utf-8')
        print(f'Generated {section}/{slug}/index.html')
        generated.append(meta)

    return generated

def update_research_index(repo_root: Path, new_entries: list) -> None:
    index_path = repo_root / 'research' / 'index.html'
    if not index_path.exists():
        return

    content = index_path.read_text(encoding='utf-8')
    for meta in new_entries:
        marker = _section_marker(meta['slug'])
        btn = _sidebar_button(meta, 'research')
        content = update_sidebar(content, marker, btn)

    index_path.write_text(content, encoding='utf-8')

def main() -> None:
    research_entries = process_directory(
        str(REPO_ROOT / 'research'), 'research', str(REPO_ROOT)
    )
    if research_entries:
        update_research_index(REPO_ROOT, research_entries)

    process_directory(
        str(REPO_ROOT / 'publications'), 'publications', str(REPO_ROOT)
    )

if __name__ == '__main__':
    main()
