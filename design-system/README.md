# OrdoAnimi design system

`oa-tokens.css` is the single source of truth for colour, type and shape
across every OrdoAnimi surface. Version 1.0, locked 2026-10-01.

| Token | Value | Use |
|---|---|---|
| `--oa-ink` | `#0b0e11` | Text, nav, footer, dark sections |
| `--oa-gold` | `#b8924e` | Fills, borders, focus rings |
| `--oa-gold-deep` | `#7b6030` | Gold text on light grounds (AA contrast) |
| `--oa-gold-light` | `#d4b36a` | Hover; gold text on dark grounds |
| `--oa-page` | `#f2ede0` | Page background |
| `--oa-card` | `#faf7ef` | Cards, panels, inputs |
| `--oa-radius` | `6px` | Buttons and controls |

Decisions behind v1.0:

1. **Palette.** The earlier spec (Obsidian `#0F1115`, Burnished Gold `#B59652`)
   is superseded by the values six surfaces already used.
2. **Grounds.** `#f2ede0` for pages, `#faf7ef` for cards.
3. **Buttons.** 6px radius everywhere, including the product apps.
4. **Wayfinding.** Product apps carry the thin `.oa-strip` linking home.
5. **Wordmark.** "OrdoAnimi", one word, everywhere.
6. **Voice.** The hub speaks for the practice ("we"). myint.ordoanimi.com
   is first person.

Every repo vendors a copy at its web root as `oa-tokens.css`. To change a
value, edit it here, then copy the file into each repo.
