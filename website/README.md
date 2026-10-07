# Website

The public InkuA website — a thin **view** over this repository's own files.

There is no CMS and no database. The site reads:

| Source | Becomes |
| ------ | ------- |
| `areas/**/PROJECT.md` + `README.md` | the Projects index and each project page |
| `about/*.md` | the institutional pages (fallback: the root `README.md`) |
| `news/**/*.md` | the News room |

Edit a markdown file, and the website reflects it. See
`../docs/website-architecture.md` for the full rationale.

## Run locally

```bash
cd website
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
reflex run
```

Then open http://localhost:3000.

## Build for production

```bash
reflex export --frontend-only   # static build in web/build
```

Host it behind a Cloudflare Tunnel like `frank-escudero.com`, or on GitHub
Pages.

## Layout

```
website/
├── rxconfig.py            # Reflex config
├── requirements.txt
└── inkua_site/
    ├── content.py         # reads areas/, about/, news/ from the repo
    └── inkua_site.py      # the Reflex app and pages
```
