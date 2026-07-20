# andersontech-site — Project Entry

Public marketing site for Anderson Technologies LLC, served by GitHub Pages at
https://andersontechsupport.com. Static HTML/CSS/vanilla JS, no build step.

## Files
| Path | Purpose |
|------|---------|
| `index.html` | Home (hand-maintained) |
| `tools/gen_pages.py` | Emits every other page (services, process, projects, about, careers + 12 role pages, contact, thanks, privacy, 404) and sitemap.xml. Edit content HERE, then run `py tools/gen_pages.py`. Never hand-edit generated pages. |
| `_snippets.html` | Canonical nav/footer/CTA reference (unlinked) |
| `styles.css` / `app.js` | Single stylesheet (cache-busted via `?v=N`) and script |
| `assets/` | Images; licensing recorded in `LICENSES.md` |
| `docs/` | Git-ignored working docs (project state, plans) — local only |

## Conventions
- No em dashes anywhere. No client or employer names. Neutral captions on stock imagery.
- Careers salary ranges are load-bearing (CA pay transparency); JobPosting JSON-LD lives on
  `careers/<slug>.html` leaf pages only, re-date quarterly.
- Bump the CSS `?v=` in BOTH `tools/gen_pages.py` (CSSV) and `index.html` on any CSS change.
- Deploy = push to main. The site must never ship placeholder stats or unverified claims.

## Resume
Read `docs/PROJECT_STATE.md` first (local, git-ignored).
