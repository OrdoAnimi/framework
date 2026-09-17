#!/usr/bin/env python3
"""Import a raw draft (.docx/.txt/.md) into a collection.

Handles the mechanical part of publishing an already-classified piece: it
does not decide which series a draft belongs to (that's a judgement call -
read the piece, compare it to what's already in each collection) - it takes
the collection and title as given and does everything after that reliably:
placing the file under the right source path with the right name, writing
frontmatter (Field Notes) or adding a manifest row (Signal / Thought Series),
then regenerating the static reader pages, feeds and sitemap.

Usage:
  python tools/import_draft.py DRAFT --collection signal --title "..."
  python tools/import_draft.py DRAFT --collection field-notes --title "..." --subtitle "..." [--tags a,b,c]
  python tools/import_draft.py DRAFT --collection thought-series-03 --title "..." [--id 3.4]

Only Signal, Field Notes and the Thought Series are supported - these are the
ongoing serials new posts actually land in. The three books are structured,
planned works edited directly, not ad-hoc imports.

After a successful import the draft is moved to _drafts/processed/ so it
can't be imported twice by accident. Nothing is committed or pushed - review
`git diff` and the regenerated page, then commit by hand.
"""
import argparse
import datetime
import io
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

# ------------------------------------------------------------------- reading
def read_docx(path):
    from docx import Document
    doc = Document(str(path))
    lines = []
    for p in doc.paragraphs:
        text = "".join(
            (f"**{r.text}**" if r.bold and not r.italic else
             f"*{r.text}*" if r.italic and not r.bold else
             f"***{r.text}***" if r.bold and r.italic else
             r.text)
            for r in p.runs
        ) or p.text
        text = text.strip()
        if not text:
            lines.append("")
            continue
        style = (p.style.name or "").lower()
        if "heading 1" in style or style == "title":
            lines.append(f"# {text}")
        elif "heading 2" in style:
            lines.append(f"## {text}")
        elif "heading 3" in style:
            lines.append(f"### {text}")
        elif "list bullet" in style or "list paragraph" in style:
            lines.append(f"- {text}")
        elif "list number" in style:
            lines.append(f"1. {text}")
        elif "quote" in style:
            lines.append(f"> {text}")
        else:
            lines.append(text)
    # collapse to markdown-paragraph form (blank line between blocks)
    out, prev_blank = [], True
    for ln in lines:
        blank = (ln == "")
        if blank and prev_blank:
            continue
        out.append(ln)
        prev_blank = blank
    return "\n".join(out).strip("\n") + "\n"

def read_draft(path):
    ext = path.suffix.lower()
    if ext == ".docx":
        return read_docx(path)
    return path.read_text(encoding="utf-8-sig")

# --------------------------------------------------------------------- slug
def slugify(title):
    s = title.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")

# ------------------------------------------------------------- manifest I/O
_ROW = re.compile(
    r"""^\s*\[\s*
        (['"])(?P<id>.*?)\1\s*,\s*
        (['"])(?P<title>.*?)\3\s*,\s*
        (['"])(?P<file>.*?)\5\s*
        \]""",
    re.VERBOSE,
)

def read_manifest_rows(shell_path):
    rows = []
    text = shell_path.read_text(encoding="utf-8")
    nl = "\r\n" if "\r\n" in text else "\n"
    for i, line in enumerate(text.splitlines()):
        m = _ROW.match(line)
        if m and m.group("file").endswith(".md"):
            rows.append(dict(id=m.group("id"), title=m.group("title"), file=m.group("file")))
    return rows, nl

def append_manifest_row(shell_path, row_id, title, filename):
    """Insert a new CH row just before the manifest's closing `];`, giving the
    previous last row a trailing comma if it didn't have one."""
    with io.open(shell_path, "r", encoding="utf-8", newline="") as f:
        lines = f.read().splitlines(keepends=True)

    last_row_idx = None
    for i, ln in enumerate(lines):
        if _ROW.match(ln.strip()):
            last_row_idx = i
    if last_row_idx is None:
        raise SystemExit(f"no manifest rows found in {shell_path}")

    ending = "\r\n" if lines[last_row_idx].endswith("\r\n") else "\n"
    body = lines[last_row_idx].rstrip("\r\n")
    if not body.rstrip().endswith(","):
        lines[last_row_idx] = body + "," + ending

    safe_title = title.replace('"', '\\"')
    new_row = f'[\'{row_id}\',"{safe_title}","{filename}"]{ending}'
    lines.insert(last_row_idx + 1, new_row)

    with io.open(shell_path, "w", encoding="utf-8", newline="") as f:
        f.write("".join(lines))

# --------------------------------------------------------------- collections
SIGNAL = dict(
    shell=ROOT / "publications" / "signal" / "index.html",
    md_dir=ROOT / "signals-series",
    filename=lambda id_, slug: f"post-{id_}-{slug}.md",
)
THOUGHT_SERIES = {
    "thought-series-01": ("series-01-foundations", "1"),
    "thought-series-02": ("series-02-decision-velocity", "2"),
    "thought-series-03": ("series-03-the-architecture-operating-system", "3"),
    "thought-series-04": ("series-04-architecture-as-a-decision-system", "4"),
    "thought-series-05": ("series-05-the-implementation-arc", "5"),
    "thought-series-06": ("series-06-before-the-decision", "6"),
}

def next_signal_id(rows):
    nums = [int(r["id"]) for r in rows if r["id"].isdigit()]
    return f"{(max(nums) + 1) if nums else 1:02d}"

def next_thought_series_id(rows, series_num):
    nums = []
    for r in rows:
        m = re.match(rf"^{series_num}\.(\d+)$", r["id"])
        if m:
            nums.append(int(m.group(1)))
    return f"{series_num}.{(max(nums) + 1) if nums else 1}"

def next_field_note_number():
    import generate_field_notes as gfn
    existing = gfn.load_notes()
    return (max((n["number"] for n in existing), default=0) + 1)

# -------------------------------------------------------------------- import
def import_signal(text, title):
    rows, _ = read_manifest_rows(SIGNAL["shell"])
    row_id = next_signal_id(rows)
    slug_title = slugify(title)
    filename = SIGNAL["filename"](row_id, slug_title)
    dest = SIGNAL["md_dir"] / filename
    if dest.exists():
        raise SystemExit(f"refusing to overwrite existing {dest}")
    dest.write_text(f"# {title.upper()}\n\n{text.strip()}\n", encoding="utf-8")
    append_manifest_row(SIGNAL["shell"], row_id, title, filename)
    print(f"  signal post {row_id}: {filename}")
    return SIGNAL["shell"]

def import_thought_series(text, title, collection_key, explicit_id=None):
    series_dir, series_num = THOUGHT_SERIES[collection_key]
    shell = ROOT / "publications" / "thought-series" / f"series-{series_num.zfill(2)}" / "index.html"
    md_dir = ROOT / "series" / series_dir
    rows, _ = read_manifest_rows(shell)
    row_id = explicit_id or next_thought_series_id(rows, series_num)
    filename = f"{row_id}-{slugify(title)}.md"
    dest = md_dir / filename
    if dest.exists():
        raise SystemExit(f"refusing to overwrite existing {dest}")
    dest.write_text(f"# {title}\n\n{text.strip()}\n", encoding="utf-8")
    append_manifest_row(shell, row_id, title, filename)
    print(f"  thought series {row_id}: {filename}")
    return shell

def import_field_note(text, title, subtitle, tags):
    dest_dir = ROOT / "publications" / "field-notes"
    slug = slugify(title)
    dest = dest_dir / f"{slug}.md"
    if dest.exists():
        raise SystemExit(f"refusing to overwrite existing {dest}")
    number = next_field_note_number()
    today = datetime.date.today().isoformat()
    tag_block = "\n".join(f'  - "{t.strip()}"' for t in tags) if tags else '  - "Practitioner Notes"'
    fm = (
        "---\n"
        f'title: "{title}"\n'
        f'subtitle: "{subtitle or ""}"\n'
        'author: "Phil Myint"\n'
        f'date: "{today}"\n'
        'series: "Coffee and Curiosity"\n'
        f"number: {number}\n"
        'category: "Field Notes"\n'
        "tags:\n"
        f"{tag_block}\n"
        "---\n\n"
    )
    body = text.strip()
    if body.startswith("# "):
        body = body.split("\n", 1)[1].lstrip("\n") if "\n" in body else ""
    dest.write_text(fm + body + "\n", encoding="utf-8")
    print(f"  field note {number:02d}: {slug}.md")
    return None  # regenerated via generate_field_notes.py, not a shell

# ------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("draft", type=Path)
    ap.add_argument("--collection", required=True,
                     choices=["signal", "field-notes"] + list(THOUGHT_SERIES))
    ap.add_argument("--title", required=True)
    ap.add_argument("--subtitle", default="")
    ap.add_argument("--tags", default="")
    ap.add_argument("--id", default=None, help="override the auto-assigned id (thought-series only)")
    args = ap.parse_args()

    if not args.draft.exists():
        raise SystemExit(f"draft not found: {args.draft}")

    text = read_draft(args.draft)
    if not text.strip():
        raise SystemExit("draft is empty after reading")

    if args.collection == "signal":
        import_signal(text, args.title)
    elif args.collection == "field-notes":
        tags = [t for t in args.tags.split(",") if t.strip()]
        import_field_note(text, args.title, args.subtitle, tags)
    else:
        import_thought_series(text, args.title, args.collection, args.id)

    # regenerate everything derived (static pages, feeds, sitemap)
    import generate_field_notes
    generate_field_notes.main()
    import generate_readers
    generate_readers.main()

    processed_dir = ROOT / "_drafts" / "processed"
    processed_dir.mkdir(exist_ok=True)
    dest = processed_dir / args.draft.name
    if dest.exists():
        dest = processed_dir / f"{args.draft.stem}-{datetime.date.today().isoformat()}{args.draft.suffix}"
    args.draft.rename(dest)
    print(f"\ndraft archived to {dest.relative_to(ROOT)}")
    print("Nothing committed - review `git diff`, then commit and push by hand.")

if __name__ == "__main__":
    main()
