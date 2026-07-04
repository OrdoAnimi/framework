# Reading the Map — Publications Edition

This folder is the reader-facing, full-navigation edition of **Reading the Map** for
`https://velocityarchitectureframework.com/publications/reading-the-map/`.

It contains the complete book — Chapters 21–54 and Appendices A–F as Markdown — plus a
self-contained HTML book reader (`index.html`) with a table-of-contents sidebar,
chapter search, previous/next navigation, a reading-progress bar, and keyboard
navigation (← / →). Chapters 0–20, already published under `/reading-the-map/`, are
referenced by the reader at their existing location, so the full 54-chapter book reads
as one continuous work.

---

## What is in this folder

| File(s) | Purpose |
|---|---|
| `index.html` | The book reader. Open this to read the whole book with full navigation. |
| `21_*.md` … `54_*.md` | Chapters 21–54 (Markdown). |
| `appendix_a_*.md` … `appendix_f_*.md` | Appendices A–F (Markdown). |
| `README.md` | This file. |

Chapters 00–20 live in the repository's existing `/reading-the-map/` folder and are
**not** duplicated here. The reader links to them at `/reading-the-map/NN_*.md`.

---

## How the reader works

`index.html` is a single self-contained page styled to match the site's design system
(same fonts, colour tokens, ecosystem strip, nav, and footer as the
`generate_pages.py` template). It holds a manifest of all 60 entries (Introduction +
54 chapters + 6 appendices). When a chapter is opened it fetches that chapter's `.md`
file and renders it client-side with `marked.js` — exactly the pattern the existing
publication reader pages use.

- Chapters 0–20 are fetched from `/reading-the-map/…` (site-absolute paths).
- Chapters 21–54 and the appendices are fetched relative to this folder.

This means the reader works on the deployed site as soon as the folder is committed and
pushed. Deep links work: `…/publications/reading-the-map/#27` opens Chapter 27 directly.

---

## Notes on the existing tooling

- **`tools/generate_pages.py`** scans for `*.md` files *directly inside* `publications/`
  (non-recursive) and generates a per-file reader page for each. Because these chapter
  files live in the `reading-the-map/` **subfolder**, the generator will not touch them,
  and the custom book reader (`index.html`) is used instead. No conflict, no action
  needed.
- **`tools/sync_nav.py`** syncs the canonical nav/footer across site HTML pages. The
  book reader uses a bespoke two-column layout with its own nav markup. Before running
  `sync_nav.py --check` in CI, confirm whether it should treat `reading-the-map/index.html`
  as a standard page; if it rewrites the reader's nav, add this file to the script's
  skip list (the reader already includes the canonical ecosystem strip, brand nav, and
  footer, so it is visually consistent either way).

---

## Source of truth

The canonical chapter content is these Markdown files. The reader renders them; it does
not contain a second copy of the prose. To edit a chapter, edit its `.md` file — the
reader picks up the change on next load.

*Phil Myint · Principal Architect · OrdoAnimi · Brisbane*
