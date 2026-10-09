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
- **Hosting (decided 2026-10-07): Cloudflare Tunnel.** Same pattern as
  `frank-escudero.com`: the app binds to `127.0.0.1` and is reached only through
  the tunnel — no open public port.
- Served from the **home datacenter**, which is currently **off**. It can be
  turned on when the site needs to go live, and **more domains can be created per
  project** from there.

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

## Quick chatbot — token-free explainer (idea, Frank 2026-10-09)

A small chatbot on the site that **explains the token-free concepts**: why the
swarm prefers deterministic software, cron, GitHub Actions, local models and free
tiers over paid LLM calls — "spend intelligence only where it changes the
result", "productive silence beats token-consuming slop".

- **Token-free by design.** The bot itself runs without paid tokens: rule-based,
  or retrieval over this repo's own markdown, or a local model on the GX10
  cluster. The demo *is* the concept.
- **Content source.** `about/` and `docs/`, plus a short FAQ ("why doesn't this
  cost money?"). Link, don't duplicate.
- **Showcase.** It doubles as a live demo of what the swarm can build.
- **Scope.** Quick: one widget/page, no accounts, no database, no paid API.
