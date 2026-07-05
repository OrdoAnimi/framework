# Dynamic Article Publishing Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Auto-generate reader pages and update sidebar listings whenever a `.md` file is added to `research/` or `publications/`.

**Architecture:** A Python script (`tools/generate_pages.py`) scans for `.md` files without matching `subfolder/index.html`, extracts title/description from markdown content, generates reader pages from embedded HTML templates, and inserts new sidebar buttons into `research/index.html` via comment markers. A GitHub Actions workflow runs this script on every push and auto-commits generated files.

**Tech Stack:** Python 3.x (stdlib only — no pip required), GitHub Actions, GitHub Pages (static HTML)

---

## File Map

| File | Action | Responsibility |
|------|--------|----------------|
| `tools/generate_pages.py` | Create | Metadata extraction, HTML generation, sidebar injection |
| `tools/tests/test_generate_pages.py` | Create | Unit + integration tests |
| `.github/workflows/publish-articles.yml` | Create | Trigger → test → generate → commit |
| `research/index.html` | Modify | Add `<!-- AUTO-PAPERS -->`, `<!-- AUTO-SERIES -->`, `<!-- AUTO-EXTENDED -->` markers |

---

### Task 1: Add comment markers to research/index.html

**Files:**
- Modify: `research/index.html:53-55`

The generator needs stable insertion points. Add three comment markers — one per sidebar section — immediately before each section's closing `</div>`.

- [ ] **Step 1: Edit research/index.html line 53**

Find (on line 53):
```
...Trans-Pacific Architecture Addendum</button></div>
```
Replace that `</div>` with:
```
...Trans-Pacific Architecture Addendum</button><!-- AUTO-PAPERS --></div>
```

- [ ] **Step 2: Edit line 54**

Find (on line 54):
```
...04 — Value Over Time</button></div>
```
Replace with:
```
...04 — Value Over Time</button><!-- AUTO-SERIES --></div>
```

- [ ] **Step 3: Edit line 55**

Find (on line 55):
```
...EA Value Over Time Analysis</button></div>
```
Replace with:
```
...EA Value Over Time Analysis</button><!-- AUTO-EXTENDED --></div>
```

- [ ] **Step 4: Verify markers exist**

```bash
grep -c "AUTO-PAPERS\|AUTO-SERIES\|AUTO-EXTENDED" research/index.html
```
Expected output: `3`

- [ ] **Step 5: Commit**

```bash
git add research/index.html
git commit -m "feat: add auto-insert markers to research sidebar"
```

---

### Task 2: Create the generator script

**Files:**
- Create: `tools/generate_pages.py`
- Create: `tools/tests/test_generate_pages.py`
- Create: `tools/__init__.py` (empty, makes tools a package for test imports)
- Create: `tools/tests/__init__.py` (empty)

- [ ] **Step 1: Write the failing tests**

Create `tools/tests/test_generate_pages.py`:

```python
import sys, os, tempfile, shutil, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from tools.generate_pages import extract_meta, derive_eyebrow, render_research_page, render_publications_page, update_sidebar


class TestExtractMeta(unittest.TestCase):
    def test_h1_title(self):
        content = "# My Title\n## My Subtitle\n\n**Date:** May 2026\n"
        m = extract_meta(content, "my-paper-may-2026.md")
        self.assertEqual(m['title'], 'My Title')

    def test_h2_description(self):
        content = "# Title\n## The Subtitle Here\n"
        m = extract_meta(content, "foo.md")
        self.assertEqual(m['description'], 'The Subtitle Here')

    def test_date_extraction(self):
        content = "# T\n\n**Date:** June 2026\n"
        m = extract_meta(content, "foo.md")
        self.assertEqual(m['date'], 'June 2026')

    def test_slug_from_filename(self):
        content = "# T\n"
        m = extract_meta(content, "my-new-paper-june-2026.md")
        self.assertEqual(m['slug'], 'my-new-paper-june-2026')

    def test_title_fallback_from_slug(self):
        content = "no heading here\n"
        m = extract_meta(content, "my-slug.md")
        self.assertNotEqual(m['title'], '')


class TestDeriveEyebrow(unittest.TestCase):
    def test_addendum(self):
        self.assertIn('Addendum', derive_eyebrow('foo-addendum-may-2026', 'May 2026'))

    def test_working_paper(self):
        self.assertIn('Working Paper', derive_eyebrow('zencloud-governance-june-2026', 'June 2026'))

    def test_series(self):
        self.assertIn('Research Series', derive_eyebrow('05-new-topic', ''))

    def test_extended(self):
        self.assertIn('Extended', derive_eyebrow('EA-New-Analysis', ''))


class TestRenderPages(unittest.TestCase):
    def _meta(self, slug='test-paper-may-2026', title='Test Title', desc='Test desc', date='May 2026'):
        return {'title': title, 'description': desc, 'eyebrow': 'Working Paper · May 2026',
                'slug': slug, 'filename': slug + '.md', 'date': date}

    def test_research_page_contains_title(self):
        html = render_research_page(self._meta())
        self.assertIn('Test Title', html)

    def test_research_page_contains_raw_src(self):
        html = render_research_page(self._meta())
        self.assertIn('raw.githubusercontent.com', html)
        self.assertIn('test-paper-may-2026.md', html)

    def test_research_page_back_link(self):
        html = render_research_page(self._meta())
        self.assertIn('../../research/', html)

    def test_publications_page_back_link(self):
        html = render_publications_page(self._meta())
        self.assertIn('../../publications/', html)

    def test_publications_page_contains_title(self):
        html = render_publications_page(self._meta())
        self.assertIn('Test Title', html)


class TestUpdateSidebar(unittest.TestCase):
    def test_inserts_before_marker(self):
        html = '<div>existing</button><!-- AUTO-PAPERS --></div>'
        result = update_sidebar(html, '<!-- AUTO-PAPERS -->', '<button>New</button>')
        self.assertIn('<button>New</button><!-- AUTO-PAPERS -->', result)
        self.assertIn('existing', result)

    def test_no_marker_returns_unchanged(self):
        html = '<div>no marker here</div>'
        result = update_sidebar(html, '<!-- AUTO-PAPERS -->', '<button>New</button>')
        self.assertEqual(result, html)

    def test_idempotent_existing_entry(self):
        btn = '<button data-p="research/foo.md">Foo</button>'
        html = f'{btn}<!-- AUTO-PAPERS --></div>'
        result = update_sidebar(html, '<!-- AUTO-PAPERS -->', btn)
        self.assertEqual(result.count(btn), 1)


class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.research = os.path.join(self.tmp, 'research')
        os.makedirs(self.research)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def test_generates_subfolder_for_new_md(self):
        md = os.path.join(self.research, 'new-article-june-2026.md')
        with open(md, 'w') as f:
            f.write("# New Article\n## A subtitle\n\n**Date:** June 2026\n")
        
        from tools.generate_pages import process_directory
        process_directory(self.research, 'research', self.tmp)

        target = os.path.join(self.research, 'new-article-june-2026', 'index.html')
        self.assertTrue(os.path.exists(target))
        content = open(target).read()
        self.assertIn('New Article', content)
        self.assertIn('new-article-june-2026.md', content)

    def test_skips_existing_subfolder(self):
        md = os.path.join(self.research, 'existing.md')
        with open(md, 'w') as f:
            f.write("# Existing\n")
        subfolder = os.path.join(self.research, 'existing')
        os.makedirs(subfolder)
        sentinel = os.path.join(subfolder, 'index.html')
        with open(sentinel, 'w') as f:
            f.write('ORIGINAL')
        
        from tools.generate_pages import process_directory
        process_directory(self.research, 'research', self.tmp)

        self.assertEqual(open(sentinel).read(), 'ORIGINAL')

    def test_skips_excluded_files(self):
        for name in ['SOURCES.md', 'PUBLISHING.md', 'README.md']:
            with open(os.path.join(self.research, name), 'w') as f:
                f.write("# Skip me\n")
        
        from tools.generate_pages import process_directory
        generated = process_directory(self.research, 'research', self.tmp)
        self.assertEqual(generated, [])


if __name__ == '__main__':
    unittest.main()
```

- [ ] **Step 2: Run tests — verify they all fail**

```bash
python -m pytest tools/tests/test_generate_pages.py -v 2>&1 | head -40
```
Expected: `ImportError` or `ModuleNotFoundError` for `tools.generate_pages`.

- [ ] **Step 3: Create empty package files**

```bash
touch tools/__init__.py tools/tests/__init__.py
```

- [ ] **Step 4: Create tools/generate_pages.py**

```python
#!/usr/bin/env python3
"""
Generate reader pages for new .md files in research/ and publications/.
Run from repo root: python tools/generate_pages.py
"""
import os
import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
RAW_BASE = 'https://raw.githubusercontent.com/ZenCloudAU/velocity-architecture/main'
GITHUB_BASE = 'https://github.com/ZenCloudAU/velocity-architecture/blob/main'
SKIP_FILES = {'SOURCES.md', 'PUBLISHING.md', 'README.md', 'CITATION.cff', 'CONTRIBUTING.md'}

ECOSYSTEM_STRIP = (
    ''
)

SHARED_CSS = ''':root{--bg:#F1F5F9;--surface:#FFFFFF;--surface-2:#F8FAFC;--border:#E2E8F0;--text:#0F172A;--text-2:#475569;--text-3:#94A3B8;--orange:#E8630A;--orange-subtle:#FFF7ED;--navy:#0F172A;--navy-2:#162D4A;--r:10px;--shadow-md:0 4px 12px rgba(15,23,42,.08),0 2px 4px rgba(15,23,42,.04)}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:auto}body{background:var(--bg);color:var(--text);font-family:'DM Sans',sans-serif;font-weight:300;line-height:1.65}a{color:var(--orange);text-decoration:none}a:hover{text-decoration:underline}nav{position:sticky;top:0;z-index:10;background:rgba(255,255,255,.95);backdrop-filter:blur(12px);border-bottom:1px solid var(--border);padding:0 2rem;min-height:60px;display:flex;align-items:center;justify-content:space-between;gap:1rem;flex-wrap:wrap}.brand{font-family:'Playfair Display',serif;font-weight:700;color:var(--text)}.brand sup{font-size:.5rem;color:var(--orange);vertical-align:super}.nav-links{display:flex;gap:1.25rem;flex-wrap:wrap}.nav-links a{font-size:.85rem;color:var(--text-2)}.nav-cta{display:inline-block;padding:.45rem 1rem;background:var(--orange);color:#fff;font-size:.8rem;font-weight:500;text-decoration:none;border-radius:6px}.nav-cta:hover{background:#CC5508}@media(max-width:768px){.nav-links{display:none}.nav-cta{display:none}}main{max-width:980px;margin:0 auto;padding:3rem 2rem}.breadcrumb{font-family:'DM Mono',monospace;font-size:.68rem;letter-spacing:.08em;color:var(--text-3);margin-bottom:1.5rem}.breadcrumb a{color:var(--text-3)}.breadcrumb a:hover{color:var(--orange)}.hero{background:var(--surface);border:1px solid var(--border);border-radius:var(--r);padding:2rem;box-shadow:var(--shadow-md);margin-bottom:1.5rem}.eyebrow{font-family:'DM Mono',monospace;font-size:.65rem;font-weight:500;letter-spacing:.18em;text-transform:uppercase;color:var(--orange);display:block;margin-bottom:.75rem}h1{font-family:'Playfair Display',serif;font-size:clamp(1.8rem,4vw,3rem);line-height:1.1;margin-bottom:.75rem}.lead{color:var(--text-2);max-width:760px;line-height:1.65}.reader-actions{display:flex;flex-wrap:wrap;gap:.75rem;margin:1.5rem 0}.reader-actions a{display:inline-flex;align-items:center;min-height:36px;padding:0 .9rem;border:1px solid var(--border);border-radius:7px;background:var(--surface);font-size:.82rem;color:var(--text-2)}.reader-actions a.primary{background:var(--orange);border-color:var(--orange);color:#fff}.reader-actions a:hover{text-decoration:none;border-color:var(--orange);color:var(--orange)}.reader-actions a.primary:hover{background:#CC5508;color:#fff}.article{background:var(--surface);border:1px solid var(--border);border-radius:var(--r);padding:2.25rem;box-shadow:var(--shadow-md)}.loading,.error{font-family:'DM Mono',monospace;font-size:.85rem;color:var(--text-3)}.md{font-size:.96rem;color:var(--text-2);line-height:1.78}.md h1{font-family:'Playfair Display',serif;font-size:2.15rem;line-height:1.15;color:var(--text);margin-bottom:1rem}.md h2{font-family:'Playfair Display',serif;font-size:1.45rem;color:var(--text);margin:2.2rem 0 .8rem;padding-bottom:.5rem;border-bottom:1px solid var(--border)}.md h3{font-size:1.05rem;font-weight:700;color:var(--text);margin:1.6rem 0 .5rem}.md h4{font-family:'DM Mono',monospace;font-size:.75rem;font-weight:500;letter-spacing:.12em;text-transform:uppercase;color:var(--orange);margin:1.25rem 0 .35rem}.md p{margin-bottom:1rem}.md strong{color:var(--text);font-weight:700}.md ul,.md ol{margin:0 0 1rem 1.4rem}.md li{margin-bottom:.35rem}.md blockquote{border-left:3px solid var(--orange);background:var(--orange-subtle);border-radius:0 6px 6px 0;margin:1.5rem 0;padding:.8rem 1.2rem;color:var(--text)}.md blockquote p{margin:0;font-style:italic}.md hr{border:none;border-top:1px solid var(--border);margin:2rem 0}.md table{width:100%;border-collapse:collapse;margin:1.2rem 0;display:block;overflow-x:auto}.md th,.md td{border:1px solid var(--border);padding:.55rem .75rem;text-align:left}.md th{background:var(--surface-2);font-family:'DM Mono',monospace;font-size:.68rem;color:var(--text-2);text-transform:uppercase}.md code{font-family:'DM Mono',monospace;font-size:.82em;background:var(--surface-2);border:1px solid var(--border);padding:.1em .4em;border-radius:3px}.md pre{background:var(--navy-2);border-radius:8px;padding:1.25rem 1.5rem;overflow-x:auto;margin-bottom:1.25rem}.md pre code{background:none;border:none;padding:0;font-size:.82rem;color:#E2E8F0;line-height:1.6}.md a{color:var(--orange)}.source{margin-top:1.5rem;font-family:'DM Mono',monospace;font-size:.72rem;color:var(--text-3)}footer{margin-top:3rem;background:var(--navy-2);color:rgba(226,232,240,.65);padding:2rem;border-radius:var(--r)}.footer-links{display:flex;flex-wrap:wrap;gap:1rem;margin-top:1rem}.footer-links a{color:#cbd5e1;font-size:.8rem}@media(max-width:720px){nav{align-items:flex-start;padding:1rem}main{padding:2rem 1rem}.article,.hero{padding:1.25rem}}'''


def extract_meta(content: str, filename: str) -> dict:
    """Extract title, description, eyebrow, date from markdown content."""
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
    """Derive article type label from slug pattern and date."""
    date_part = date_str or ''
    if re.match(r'^\d{2}-', slug):
        label = 'Research Series'
    elif re.match(r'^[A-Z]', slug):
        label = 'Extended Paper'
    elif 'addendum' in slug:
        label = 'Working Paper · Addendum'
    else:
        label = 'Working Paper'
    return f'{label} · {date_part}'.strip(' ·') if date_part else label


def _reader_script(section: str, filename: str) -> str:
    src = f'{RAW_BASE}/{section}/{filename}'
    gh = f'{GITHUB_BASE}/{section}/{filename}'
    return (
        f"const SRC='{src}';\n"
        "async function load(){\n"
        "  const el=document.getElementById('article');\n"
        "  try{\n"
        "    const r=await fetch(SRC);\n"
        "    if(!r.ok)throw 0;\n"
        "    el.innerHTML='<div class=\"md\">'+marked.parse(await r.text())+'</div>';\n"
        "  }catch{\n"
        f"    el.innerHTML='<p class=\"error\">Could not load document. "
        f'<a href="{gh}" target="_blank" rel="noopener">View on GitHub ↗</a></p>\';\n'
        "  }\n"
        "}\n"
        "load();"
    )


def render_research_page(meta: dict) -> str:
    title = meta['title']
    description = meta['description']
    eyebrow = meta['eyebrow']
    slug = meta['slug']
    filename = meta['filename']

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — OrdoAnimi</title>
<meta name="description" content="{description}">
<link rel="icon" type="image/svg+xml" href="../../favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Mono:wght@300;400;500&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/marked@9/marked.min.js"></script>
<style>
{SHARED_CSS}
</style>
</head>
<body>
{ECOSYSTEM_STRIP}
<nav>
  <a class="brand" href="../../index.html">OrdoAnimi</a>
  <div class="nav-links">
    <a href="../../index.html">Framework</a>
    <a href="../../research/">Research</a>
    <a href="../../publications/">Publications</a>
    <a href="../../guides/">Guides</a>
  </div>
  <a href="https://velocityarchitectureframework.com/app/portal.html" class="nav-cta" target="_blank" rel="noopener">Open agent ↗</a>
</nav>
<main>
  <div class="breadcrumb">
    <a href="../../index.html">OrdoAnimi</a> ›
    <a href="../../research/">Research</a> ›
    {title}
  </div>
  <section class="hero">
    <span class="eyebrow">{eyebrow}</span>
    <h1>{title}</h1>
    <p class="lead">{description}</p>
  </section>
  <div class="reader-actions">
    <a class="primary" href="../">← Research library</a>
    <a href="../../index.html">The OrdoAnimi Framework</a>
    OrdoAnimi
  </div>
  <article class="article" id="article"><p class="loading">Loading document…</p></article>
  <footer>
    <strong>OrdoAnimi advises, builds, and decides.</strong>
    <div class="footer-links">
      <a href="../../research/">Research</a>
      <a href="../../index.html">The OrdoAnimi Framework</a>
      OrdoAnimi
      
    </div>
  </footer>
</main>
<script>
{_reader_script('research', filename)}
</script>
</body>
</html>"""


def render_publications_page(meta: dict) -> str:
    title = meta['title']
    description = meta['description']
    eyebrow = meta['eyebrow']
    slug = meta['slug']
    filename = meta['filename']

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — OrdoAnimi Publications</title>
<meta name="description" content="{description}">
<link rel="icon" type="image/svg+xml" href="../../favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Mono:wght@300;400;500&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/marked@9/marked.min.js"></script>
<style>
{SHARED_CSS}
</style>
</head>
<body>
{ECOSYSTEM_STRIP}
<nav>
  <a class="brand" href="../../index.html">OrdoAnimi</a>
  <div class="nav-links">
    <a href="../../index.html">Framework</a>
    <a href="../../publications/">Publications</a>
    <a href="../../guides/">Guides</a>
  </div>
  <a href="https://velocityarchitectureframework.com/app/portal.html" class="nav-cta" target="_blank" rel="noopener">Open agent ↗</a>
</nav>
<main>
  <div class="breadcrumb">
    <a href="../../index.html">OrdoAnimi</a> ›
    <a href="../../publications/">Publications</a> ›
    {title}
  </div>
  <section class="hero">
    <span class="eyebrow">{eyebrow}</span>
    <h1>{title}</h1>
    <p class="lead">{description}</p>
  </section>
  <div class="reader-actions">
    <a class="primary" href="../">← Publication library</a>
    <a href="../../index.html">The OrdoAnimi Framework</a>
    OrdoAnimi
  </div>
  <article class="article" id="article"><p class="loading">Loading document…</p></article>
  <footer>
    <strong>OrdoAnimi advises, builds, and decides.</strong>
    <div class="footer-links">
      <a href="../../publications/">Publications</a>
      <a href="../../index.html">The OrdoAnimi Framework</a>
      OrdoAnimi
      
    </div>
  </footer>
</main>
<script>
{_reader_script('publications', filename)}
</script>
</body>
</html>"""


def update_sidebar(html: str, marker: str, new_button: str) -> str:
    """Insert new_button before marker, only if not already present."""
    if marker not in html:
        return html
    if f'data-p="research/{Path(new_button).name}"' in html or new_button in html:
        return html
    return html.replace(marker, new_button + marker)


def _sidebar_button(meta: dict, section: str) -> str:
    return (
        f'<button class="file-btn" data-p="{section}/{meta["filename"]}" '
        f'data-href="{meta["slug"]}/" onclick="loadDoc(this.dataset.p)">'
        f'{meta["title"]}</button>'
    )


def _section_marker(slug: str) -> str:
    """Map filename pattern to the correct AUTO marker."""
    if re.match(r'^\d{2}-', slug):
        return '<!-- AUTO-SERIES -->'
    elif re.match(r'^[A-Z]', slug):
        return '<!-- AUTO-EXTENDED -->'
    else:
        return '<!-- AUTO-PAPERS -->'


def process_directory(section_dir: str, section: str, repo_root: str) -> list:
    """Generate reader pages for all new .md files. Returns list of generated slugs."""
    section_path = Path(section_dir)
    root_path = Path(repo_root)
    generated = []

    for md_path in sorted(section_path.glob('*.md')):
        if md_path.name in SKIP_FILES:
            continue

        slug = md_path.stem
        target = section_path / slug / 'index.html'
        if target.exists():
            continue

        content = md_path.read_text(encoding='utf-8')
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
    """Insert new sidebar buttons into research/index.html."""
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
```

- [ ] **Step 5: Run tests — verify they pass**

```bash
python -m pytest tools/tests/test_generate_pages.py -v
```
Expected: all tests PASS. Fix any failures before proceeding.

- [ ] **Step 6: Run generator against the live repo — verify nothing new is generated**

```bash
python tools/generate_pages.py
git status
```
Expected: `nothing to commit` (all existing articles already have subfolders).

- [ ] **Step 7: Smoke test with a real new article**

```bash
echo "# Test Article\n## A test subtitle\n\n**Date:** June 2026\n" > research/test-article-june-2026.md
python tools/generate_pages.py
```
Expected output:
```
Generated research/test-article-june-2026/index.html
```
Verify:
```bash
grep "Test Article" research/test-article-june-2026/index.html
grep "test-article-june-2026.md" research/test-article-june-2026/index.html
grep "AUTO-PAPERS" research/index.html | grep -c "test-article-june-2026"
```
All three should return a match. Then clean up:
```bash
rm -rf research/test-article-june-2026 research/test-article-june-2026.md
git checkout research/index.html
```

- [ ] **Step 8: Commit**

```bash
git add tools/generate_pages.py tools/__init__.py tools/tests/test_generate_pages.py tools/tests/__init__.py
git commit -m "feat: add dynamic article page generator"
```

---

### Task 3: Create the GitHub Actions workflow

**Files:**
- Create: `.github/workflows/publish-articles.yml`

- [ ] **Step 1: Create the workflow**

```yaml
name: Publish New Articles

on:
  push:
    branches: [main]
    paths:
      - 'research/*.md'
      - 'publications/*.md'

jobs:
  generate:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Run tests
        run: python -m pytest tools/tests/ -v

      - name: Generate reader pages
        run: python tools/generate_pages.py

      - name: Commit generated pages
        run: |
          git config user.name "velocity-publisher[bot]"
          git config user.email "velocity-publisher[bot]@users.noreply.github.com"
          git add -A
          if git diff --cached --quiet; then
            echo "No new pages generated."
          else
            git commit -m "chore: auto-generate reader pages for new articles"
            git push
          fi
```

- [ ] **Step 2: Commit**

```bash
git add .github/workflows/publish-articles.yml
git commit -m "ci: add auto-publish workflow for new research and publication articles"
```

---

### Task 4: End-to-end verification

**Files:** None

- [ ] **Step 1: Push and trigger the workflow**

```bash
git push
```
Go to `https://github.com/ZenCloudAU/velocity-architecture/actions` and confirm the "Publish New Articles" workflow does NOT trigger (no `.md` files changed in this push — only `.yml` and `.py`).

- [ ] **Step 2: Add a real test article and push**

```bash
cat > research/test-e2e-june-2026.md << 'EOF'
# End-to-End Test Article
## Testing the auto-publish pipeline

**Date:** June 2026

This is a test article to verify the pipeline works end to end.
EOF
git add research/test-e2e-june-2026.md
git commit -m "test: add e2e test article"
git push
```

- [ ] **Step 3: Confirm workflow runs**

Watch `https://github.com/ZenCloudAU/velocity-architecture/actions` — "Publish New Articles" workflow should trigger, run, and create a new commit.

- [ ] **Step 4: Confirm the generated page is live**

After GitHub Pages deploys (~1 min), verify:
```
https://velocityarchitectureframework.com/research/test-e2e-june-2026/
```
Should render the article with title "End-to-End Test Article".

- [ ] **Step 5: Clean up test article**

```bash
git pull  # get the auto-generated commit
git rm research/test-e2e-june-2026.md
git rm -r research/test-e2e-june-2026/
# revert the sidebar entry added by the generator
git checkout research/index.html
git commit -m "chore: remove e2e test article"
git push
```

---

## Self-Review

**Spec coverage:**
- ✓ Push a `.md` to `research/` → reader page auto-generated
- ✓ Push a `.md` to `publications/` → reader page auto-generated
- ✓ Existing pages not overwritten (idempotent)
- ✓ Sidebar updated for new research papers
- ✓ Tests cover extract, render, sidebar update, integration

**Placeholder scan:** None found. All code blocks are complete.

**Type consistency:**
- `process_directory` returns `list` of `dict` — used in `update_research_index` which iterates dicts ✓
- `update_sidebar(html, marker, new_button)` signature consistent across tests and implementation ✓
- `extract_meta(content, filename)` → `render_research_page(meta)` → consistent dict keys ✓
