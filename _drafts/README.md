# Draft inbox

Drop a finished draft here — `.docx`, `.txt`, or `.md` — and tell Claude it's
ready. Nothing in this folder is ever published as-is; it's a staging area.

## What happens next

1. Claude reads the draft and decides which series it belongs to (Signal,
   Field Notes, Thought Series, or one of the books), based on tone and how
   it compares to the pieces already published in each — the same read a
   human editor would do. If it's genuinely ambiguous, Claude will ask.
2. Claude runs `tools/import_draft.py`, which does the mechanical part:
   places the file in the right source folder under the right filename,
   writes the frontmatter (Field Notes) or adds the manifest row (Signal /
   Thought Series / books), and regenerates the static reader pages, the
   feeds, and the sitemap.
3. Claude shows you the result — title, series, where it landed — before
   anything is committed or pushed.
4. The original file moves to `_drafts/processed/` so it doesn't get
   re-imported by mistake.

## What a draft needs

Just the writing. A first line that reads as a title helps but isn't
required — Claude will ask if one isn't obvious. Nothing in this folder is
tracked by git except this README, so there's no risk of a half-finished
draft going public by accident.
