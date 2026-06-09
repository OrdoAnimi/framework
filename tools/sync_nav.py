#!/usr/bin/env python3
"""
Sync canonical nav and footer across all Velocity Architecture HTML pages.

Run:  python tools/sync_nav.py
CI:   python tools/sync_nav.py --check   (exits 1 if any file would change)

Three page families are handled:
  kb      - section index pages that already have nav-brand/nav-links CSS
  lean    - simple section pages with minimal inline-styled nav
  reader  - auto-generated reader pages that use class="brand" nav

Publications, the root index.html, and .git are always skipped.
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent

SKIP_ABS = {REPO_ROOT / 'index.html'}
SKIP_DIR_PREFIXES = ('publications/', '.git/', 'app/')

# ── Ecosystem strip (shared across all families) ──────────────────────────────
_ECO = (
    '<nav class="ecosystem-strip" aria-label="Ecosystem navigation" '
    'style="background:#0f172a;color:#F8FAFC;display:flex;align-items:center;'
    "gap:2rem;padding:0.5rem 2rem;font-size:0.75rem;font-family:'DM Sans',sans-serif;"
    'border-bottom:1px solid #1e293b;flex-wrap:wrap;">'
    '<span style="color:#64748B;font-size:0.7rem;text-transform:uppercase;'
    'letter-spacing:0.08em;margin-right:auto;">ZenCloud Ecosystem</span>'
    '<a href="https://www.zencloud.com.au" style="color:#F8FAFC;text-decoration:none;opacity:0.8;">ZenCloud™</a>'
    '<a href="https://studiosix.com.au" style="color:#F8FAFC;text-decoration:none;opacity:0.8;">StudioSix™</a>'
    '<a href="https://velocityarchitectureframework.com" style="color:#F8FAFC;text-decoration:none;opacity:0.8;">Velocity™</a>'
    '</nav>'
)

# ── KB family ─────────────────────────────────────────────────────────────────
# Pages: research/index.html, guides/index.html, diagnostics/index.html,
#        examples/index.html, viewpoints/index.html, tools/templates/index.html

KB_NAV = (
    _ECO + '\n'
    '<nav>\n'
    '  <a href="/" class="nav-brand">Velocity<sup>™</sup>'
    '<span class="nav-brand-badge">Open Source</span></a>\n'
    '  <ul class="nav-links">\n'
    '    <li><a href="/frameworks/">Framework</a></li>\n'
    '    <li><a href="/research/">Research</a></li>\n'
    '    <li><a href="/publications/">Publications</a></li>\n'
    '    <li><a href="/guides/">Guides</a></li>\n'
    '    <li><a href="/diagnostics/">Diagnostics</a></li>\n'
    '    <li><a href="/examples/">Examples</a></li>\n'
    '    <li class="nav-mobile-cta"><a href="https://velocityarchitectureframework.com/app/portal.html" target="_blank" rel="noopener">Open agent ↗</a></li>\n'
    '  </ul>\n'
    '  <a href="https://velocityarchitectureframework.com/app/portal.html" '
    'class="nav-cta" target="_blank" rel="noopener">Open agent ↗</a>\n'
    '  <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false">'
    '<span></span><span></span><span></span></button>\n'
    '</nav>\n'
    '<script>(function(){'
    'var t=document.querySelector(".nav-toggle"),'
    'm=document.querySelector(".nav-links");'
    'if(t&&m)t.addEventListener("click",function(){'
    'var o=m.classList.toggle("open");'
    't.setAttribute("aria-expanded",o);'
    't.classList.toggle("open");'
    '});'
    '})();</script>'
)

KB_FOOTER = (
    '<footer>\n'
    '  <div class="footer-inner">\n'
    '    <div>\n'
    '      <p class="footer-brand">Velocity<sup>™</sup></p>\n'
    '      <p class="footer-copy">© 2026 ZenCloud Global Consultants · '
    'Free to use · Attribution appreciated</p>\n'
    '    </div>\n'
    '    <div class="footer-links">\n'
    '      <a href="/">Home</a>\n'
    '      <a href="/frameworks/">Framework</a>\n'
    '      <a href="/research/">Research</a>\n'
    '      <a href="/publications/">Publications</a>\n'
    '      <a href="/guides/">Guides</a>\n'
    '      <a href="/diagnostics/">Diagnostics</a>\n'
    '      <a href="/examples/">Examples</a>\n'
    '      <a href="/templates/">Templates</a>\n'
    '      <a href="/policies/">Policies</a>\n'
    '      <a href="https://velocityarchitectureframework.com/app/portal.html" '
    'target="_blank" rel="noopener">Velocity Agent ↗</a>\n'
    '    </div>\n'
    '  </div>\n'
    '</footer>'
)

# ── Lean family ───────────────────────────────────────────────────────────────
# Pages: frameworks/index.html, spec/index.html, foundation/index.html, etc.
# These inherit font/colour from the page's own <style> block; no extra CSS needed.

LEAN_NAV = (
    _ECO + '\n'
    '<nav>'
    '<a href="/" style="font-weight:bold;margin-right:1.5rem;">Velocity™</a>'
    '<a href="/frameworks/">Framework</a> · '
    '<a href="/research/">Research</a> · '
    '<a href="/publications/">Publications</a> · '
    '<a href="/guides/">Guides</a> · '
    '<a href="/diagnostics/">Diagnostics</a> · '
    '<a href="/examples/">Examples</a> · '
    '<a href="/policies/">Policies</a>'
    '</nav>'
)

LEAN_FOOTER = (
    '<footer>© 2026 ZenCloud Global Consultants  ·  '
    '<a href="/">Home</a>  ·  '
    '<a href="/frameworks/">Framework</a>  ·  '
    '<a href="/research/">Research</a>  ·  '
    '<a href="/publications/">Publications</a>  ·  '
    '<a href="/guides/">Guides</a>  ·  '
    '<a href="/diagnostics/">Diagnostics</a>  ·  '
    '<a href="/examples/">Examples</a>  ·  '
    '<a href="/templates/">Templates</a>  ·  '
    '<a href="/policies/">Policies</a>'
    '</footer>'
)

# ── Reader family ─────────────────────────────────────────────────────────────
# Pages: reader subpages that use class="brand" nav (generated or manual)
# These keep their existing nav structure — only relative paths become absolute.

READER_NAV = (
    _ECO + '\n'
    '<nav>\n'
    '  <a class="brand" href="/">Velocity<sup>™</sup></a>\n'
    '  <div class="nav-links">\n'
    '    <a href="/frameworks/">Framework</a>\n'
    '    <a href="/research/">Research</a>\n'
    '    <a href="/publications/">Publications</a>\n'
    '    <a href="/guides/">Guides</a>\n'
    '    <a href="https://velocityarchitectureframework.com/app/portal.html" class="nav-cta-mobile" target="_blank" rel="noopener">Open agent ↗</a>\n'
    '  </div>\n'
    '  <a href="https://velocityarchitectureframework.com/app/portal.html" '
    'class="nav-cta" target="_blank" rel="noopener">Open agent ↗</a>\n'
    '  <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false">'
    '<span></span><span></span><span></span></button>\n'
    '</nav>\n'
    '<script>(function(){'
    'var t=document.querySelector(".nav-toggle"),'
    'm=document.querySelector(".nav-links");'
    'if(t&&m)t.addEventListener("click",function(){'
    'var o=m.classList.toggle("open");'
    't.setAttribute("aria-expanded",o);'
    't.classList.toggle("open");'
    '});'
    '})();</script>'
)

READER_FOOTER = (
    '<footer>\n'
    '    <strong>ZenCloud advises. StudioSix produces. Velocity decides.</strong>\n'
    '    <div class="footer-links">\n'
    '      <a href="/research/">Research</a>\n'
    '      <a href="/">Velocity Framework</a>\n'
    '      <a href="https://www.zencloud.com.au/" target="_blank" rel="noopener">ZenCloud Advisory</a>\n'
    '      <a href="https://studiosix.com.au/" target="_blank" rel="noopener">StudioSix</a>\n'
    '    </div>\n'
    '  </footer>'
)

# ── Markers ───────────────────────────────────────────────────────────────────
_NAV_S = '<!-- SHARED-NAV-START -->'
_NAV_E = '<!-- SHARED-NAV-END -->'
_FTR_S = '<!-- SHARED-FOOTER-START -->'
_FTR_E = '<!-- SHARED-FOOTER-END -->'

_NAV_MARKER_RE = re.compile(
    r'<!-- SHARED-NAV-START -->.*?<!-- SHARED-NAV-END -->', re.DOTALL)
_FTR_MARKER_RE = re.compile(
    r'<!-- SHARED-FOOTER-START -->.*?<!-- SHARED-FOOTER-END -->', re.DOTALL)

# ── Nav/footer regex patterns (first-run migration) ───────────────────────────

# KB: ecosystem strip nav + following <nav> block (handles multiline)
_KB_NAV_RE = re.compile(
    r'<nav\s+class="ecosystem-strip"[^>]*>.*?</nav>\s*\n\s*<nav>.*?</nav>',
    re.DOTALL)
# KB: footer with footer-inner div
_KB_FTR_RE = re.compile(
    r'<footer>\s*\n?\s*<div class="footer-inner">.*?</footer>', re.DOTALL)

# Lean: ecosystem strip + simple one-liner <nav> (no nav-brand)
_LEAN_NAV_RE = re.compile(
    r'<nav\s+class="ecosystem-strip"[^>]*>.*?</nav>\s*\n?<nav>(?:(?!</nav>).)*</nav>',
    re.DOTALL)
# Lean: simple footer without footer-inner
_LEAN_FTR_SIMPLE_RE = re.compile(r'<footer>[^<]*(?:<a[^>]*>[^<]*</a>[^<]*)*</footer>')
_LEAN_FTR_STYLED_RE = re.compile(
    r'<footer style="[^>]*>.*?</footer>', re.DOTALL)

# Reader: ecosystem strip (inline-styled) + <nav> with class="brand"
_READER_NAV_RE = re.compile(
    r'<nav\s+class="ecosystem-strip"[^>]*>.*?</nav>\s*\n\s*<nav>.*?</nav>',
    re.DOTALL)
# Reader footer: dark navy footer inside <main>
_READER_FTR_RE = re.compile(r'<footer>\s*\n\s*<strong>.*?</footer>', re.DOTALL)


# ── Helpers ───────────────────────────────────────────────────────────────────

def _wrap_nav(nav_html):
    return f'{_NAV_S}\n{nav_html}\n{_NAV_E}'


def _wrap_ftr(ftr_html):
    return f'{_FTR_S}\n{ftr_html}\n{_FTR_E}'


def _replace(html, marker_re, first_run_re, canonical, wrap_fn):
    """Replace nav or footer block. Uses markers if present, regex otherwise."""
    if wrap_fn('x') in html or marker_re.search(html):
        new = marker_re.sub(wrap_fn(canonical), html)
    else:
        m = first_run_re.search(html)
        if not m:
            return html, False
        new = html[:m.start()] + wrap_fn(canonical) + html[m.end():]
    return new, new != html


def classify(html: str) -> str:
    if 'pub-nav' in html or 'pub-footer' in html:
        return 'skip'
    if 'class="nav-brand"' in html or ('class="nav-links"' in html and 'class="brand"' not in html):
        return 'kb'
    if 'class="brand"' in html and 'nav-brand' not in html:
        return 'reader'
    if '<nav class="ecosystem-strip"' in html:
        return 'lean'
    return 'skip'


def should_skip(path: Path) -> bool:
    if path in SKIP_ABS:
        return True
    rel = str(path.relative_to(REPO_ROOT)).replace('\\', '/')
    return any(rel.startswith(p) for p in SKIP_DIR_PREFIXES)


def sync(html: str, kind: str, path: Path) -> tuple[str, bool]:
    changed = False

    if kind == 'kb':
        html, c = _replace(html, _NAV_MARKER_RE, _KB_NAV_RE, KB_NAV, _wrap_nav)
        changed |= c
        html, c = _replace(html, _FTR_MARKER_RE, _KB_FTR_RE, KB_FOOTER, _wrap_ftr)
        changed |= c

    elif kind == 'lean':
        html, c = _replace(html, _NAV_MARKER_RE, _LEAN_NAV_RE, LEAN_NAV, _wrap_nav)
        changed |= c
        html, c = _replace(html, _FTR_MARKER_RE, _LEAN_FTR_STYLED_RE, LEAN_FOOTER, _wrap_ftr)
        if not c:
            html, c = _replace(html, _FTR_MARKER_RE, _LEAN_FTR_SIMPLE_RE, LEAN_FOOTER, _wrap_ftr)
        changed |= c

    elif kind == 'reader':
        html, c = _replace(html, _NAV_MARKER_RE, _READER_NAV_RE, READER_NAV, _wrap_nav)
        changed |= c
        html, c = _replace(html, _FTR_MARKER_RE, _READER_FTR_RE, READER_FOOTER, _wrap_ftr)
        changed |= c

    return html, changed


def main(check_only: bool = False) -> int:
    html_files = sorted(REPO_ROOT.rglob('*.html'))
    updated, skipped, failed = [], [], []

    for path in html_files:
        if should_skip(path):
            continue
        html = path.read_text(encoding='utf-8')
        kind = classify(html)
        if kind == 'skip':
            continue

        new_html, changed = sync(html, kind, path)

        if changed:
            if check_only:
                print(f'NEEDS UPDATE ({kind}): {path.relative_to(REPO_ROOT)}')
                failed.append(path)
            else:
                path.write_text(new_html, encoding='utf-8')
                print(f'Updated ({kind}): {path.relative_to(REPO_ROOT)}')
                updated.append(path)
        else:
            skipped.append(path)

    if check_only:
        print(f'\nCheck: {len(failed)} need update, {len(skipped)} already in sync')
        return 1 if failed else 0

    print(f'\nDone: {len(updated)} updated, {len(skipped)} already in sync')
    return 0


if __name__ == '__main__':
    check = '--check' in sys.argv
    sys.exit(main(check_only=check))
