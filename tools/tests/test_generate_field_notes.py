"""Tests for the field-note generator: markdown conversion, ordering, prev/next."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import generate_field_notes as g


def test_parse_frontmatter():
    meta, body = g.parse_frontmatter('---\ntitle: "X"\nnumber: 3\n---\n\nHello')
    assert meta["title"] == "X"
    assert meta["number"] == "3"
    assert body.strip() == "Hello"


def test_md_drops_leading_h1_title():
    html = g.md_to_html("# The Title\n\nFirst paragraph.")
    assert "The Title" not in html          # title lives in the page header, not the body
    assert "<p>First paragraph.</p>" == html


def test_md_headings_and_paragraphs():
    html = g.md_to_html("# T\n\nIntro line.\n\n## Section\n\nBody line.")
    assert "<h2>Section</h2>" in html
    assert "<p>Intro line.</p>" in html
    assert "<p>Body line.</p>" in html


def test_parse_frontmatter_unescapes_inner_quotes():
    meta, _ = g.parse_frontmatter('---\ntitle: "He said \\"go\\""\n---\nx')
    assert meta["title"] == 'He said "go"'


def test_md_images_render_before_links():
    html = g.md_to_html("# T\n\n![Diagram](/assets/images/x.png)")
    assert '<img src="/assets/images/x.png" alt="Diagram" loading="lazy"/>' in html
    # plain links still work alongside
    both = g.md_to_html("# T\n\n![a](/i.png) and [t](https://x.io)")
    assert '<img src="/i.png"' in both and '<a href="https://x.io">t</a>' in both


def _write_note(dirpath, slug, number, extra=""):
    (dirpath / f"{slug}.md").write_text(
        f'---\ntitle: "{slug}"\nsubtitle: "s"\ndate: "2026-06-01"\nnumber: {number}\n{extra}---\n\nBody.\n',
        encoding="utf-8",
    )


def test_load_notes_skips_malformed_number(tmp_path, monkeypatch, capsys):
    _write_note(tmp_path, "good", 1)
    (tmp_path / "bad.md").write_text('---\ntitle: "bad"\nnumber: ""\n---\nx', encoding="utf-8")
    monkeypatch.setattr(g, "FN_DIR", tmp_path)
    notes = g.load_notes()
    assert [n["slug"] for n in notes] == ["good"]
    assert "WARNING skipping bad.md" in capsys.readouterr().out


def test_load_notes_rejects_duplicate_numbers(tmp_path, monkeypatch):
    _write_note(tmp_path, "one", 3)
    _write_note(tmp_path, "two", 3)
    monkeypatch.setattr(g, "FN_DIR", tmp_path)
    try:
        g.load_notes()
        assert False, "expected SystemExit for duplicate numbers"
    except SystemExit as e:
        assert "duplicate number 3" in str(e)


def test_md_emphasis_links_lists():
    assert "<strong>bold</strong>" in g.md_to_html("# T\n\n**bold**")
    assert '<a href="https://x.io">t</a>' in g.md_to_html("# T\n\n[t](https://x.io)")
    ul = g.md_to_html("# T\n\n- one\n- two")
    assert ul == "<ul><li>one</li><li>two</li></ul>"


def test_typographic_glyphs_are_ascii_safe():
    # no raw non-ASCII should survive into the output
    html = g.md_to_html('# T\n\nA — B "q" it’s')
    assert "&mdash;" in html
    assert "&ldquo;" in html and "&rdquo;" in html
    assert "&rsquo;" in html
    html.encode("ascii")  # raises if any raw non-ASCII slipped through


def test_html_escaping():
    assert "&lt;script&gt;" in g.md_to_html("# T\n\n<script>")
    assert "a &amp; b" in g.md_to_html("# T\n\na & b")


def test_date_format():
    assert g.fmt_date("2026-06-04") == "4 June 2026"
    assert g.fmt_date("2026-06-15") == "15 June 2026"


def test_render_page_prev_next_and_ends():
    a = {"number": 1, "slug": "a", "title": "A", "subtitle": "sa", "date": "2026-06-01", "body_html": "<p>x</p>"}
    b = {"number": 2, "slug": "b", "title": "B", "subtitle": "sb", "date": "2026-06-02", "body_html": "<p>y</p>"}
    c = {"number": 3, "slug": "c", "title": "C", "subtitle": "sc", "date": "2026-06-03", "body_html": "<p>z</p>"}
    mid = g.render_page(b, a, c)
    assert 'href="a.html"' in mid and 'href="c.html"' in mid   # links to real neighbours
    assert "Field Note 02" in mid
    first = g.render_page(a, None, b)
    assert "&larr; Index" in first                              # first note wraps prev to index
    last = g.render_page(c, b, None)
    assert "Index &rarr;" in last                               # last note wraps next to index
    mid.encode("ascii")                                         # output stays ASCII-safe
