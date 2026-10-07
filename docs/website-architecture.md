# Website architecture

Decision (2026-10-07): the InkuA website lives **inside `inkua/inkua`**, as a
`website/` folder, and renders the repository's own files. It is a *view*, not a
separate system.

## Why

`inkua/inkua` is already the organization's single source of truth: an
Areas → Spaces structure where every Space is a self-contained folder holding
its docs, logs and `PROJECT.md`. Its README states that "we use GitHub as our
landing page, CMS, and ERP". Adding a website that reads those files keeps
everything self-contained and avoids a CMS, a database, and a sync job.

## Data model (repo → site)

| Source | Rendered as |
| ------ | ----------- |
| `areas/**/PROJECT.md` | project record (name, roadmap, deliverables) |
| `areas/**/README.md` | a Space's page body |
| `about/*.md` | institutional pages (mission, history, governance) |
| `news/**/*.md` | the News room |

Edit markdown → the site follows. `website/inkua_site/content.py` does the
reading; there is no frontmatter requirement (it parses headings and task lists
and degrades gracefully).

## Layout

```
website/
├── rxconfig.py
├── requirements.txt
└── inkua_site/
    ├── content.py      # reads areas/, about/, news/
    └── inkua_site.py   # Reflex app + pages
```

## Stack and hosting

- **Reflex (Python)** — consistent with Frank's `cv` site.
- Run locally with `reflex run`; build static with `reflex export --frontend-only`.
- Host behind a Cloudflare Tunnel (like `frank-escudero.com`) or on GitHub Pages.

## Rules

- **No PII in the public repo.** `members/` holds public CVs only. Contact
  details, finance and contracts stay in a private repo (or the Vault's
  `Private/`). The site never builds from a folder that contains PII.
- **Keep `website/` isolated** (own deps, own CI) so content edits don't couple
  to the app.
- **No legacy PHP.** The old `inkua-main-website-project` and `InkuA-Hub` are
  archived, not revived.
- **Binaries** (`materials/`) should move to Git LFS if they grow.

## Consolidation done

`InkuA-Organization-Docs` was folded in: its `projects/` → `projects/`, its
institutional core → `about/`, plus its brand guide, tutorials and templates.
