"""Content loader for the InkuA website.

The website is a *view* over this repository's own files — there is no CMS and
no database. It reads:

- ``areas/**/PROJECT.md``  -> the project/spaces index
- ``areas/**/README.md``   -> a space's description
- ``about/*.md``           -> institutional pages (fallback: the root README)
- ``news/**/*.md``         -> the news room

Because the source is plain markdown with no YAML frontmatter, the parser
extracts what it can from headings and task lists and degrades gracefully.
"""

from __future__ import annotations

import glob
import os
import re

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

_IGNORED = {"README.md", "AI.md"}


def _read(path: str) -> str:
    with open(path, encoding="utf-8") as handle:
        return handle.read()


def _first_heading(text: str, level: int = 1) -> str:
    match = re.search(rf"^{'#' * level}\s+(.*)$", text, re.MULTILINE)
    return match.group(1).strip() if match else ""


def parse_project(project_md: str, readme: str = "") -> dict:
    """Extract a project record from a Space's PROJECT.md (+ README)."""
    name = ""
    match = re.search(r"^##\s*🚀\s*(.+)$", project_md, re.MULTILINE)
    if match:
        name = match.group(1).strip()
    if not name or name.lower() in {"project name", "[describe the project]"}:
        name = _first_heading(readme, 1) or name

    done = len(re.findall(r"^\s*-\s*\[x\]", project_md, re.MULTILINE | re.IGNORECASE))
    total = len(re.findall(r"^\s*-\s*\[[ x]\]", project_md, re.MULTILINE | re.IGNORECASE))

    deliverables: list[str] = []
    block = re.search(
        r"^##\s*📦\s*Deliverables\s*$(.*?)(?=^##\s|\Z)",
        project_md,
        re.MULTILINE | re.DOTALL,
    )
    if block:
        for line in block.group(1).splitlines():
            line = line.strip()
            if line.startswith("- "):
                deliverables.append(line[2:].strip())

    return {"name": name or "Untitled project", "done": done, "total": total, "deliverables": deliverables}


def load_projects() -> list[dict]:
    """One record per Space (any folder under areas/ that has a PROJECT.md)."""
    projects: list[dict] = []
    areas_dir = os.path.join(REPO_ROOT, "areas")
    pattern = os.path.join(areas_dir, "**", "PROJECT.md")
    for project_file in sorted(glob.glob(pattern, recursive=True)):
        space_dir = os.path.dirname(project_file)
        rel = os.path.relpath(space_dir, areas_dir)
        parts = rel.split(os.sep)
        project_md = _read(project_file)
        readme_path = os.path.join(space_dir, "README.md")
        readme = _read(readme_path) if os.path.exists(readme_path) else ""
        meta = parse_project(project_md, readme)
        projects.append(
            {
                "slug": rel.replace(os.sep, "-").lower(),
                "area": parts[0],
                "space": parts[-1],
                "name": meta["name"],
                "readme": readme,
                "project_md": project_md,
                "done": meta["done"],
                "total": meta["total"],
                "deliverables": meta["deliverables"],
            }
        )
    return projects


def load_news() -> list[dict]:
    news: list[dict] = []
    news_dir = os.path.join(REPO_ROOT, "news")
    for path in sorted(glob.glob(os.path.join(news_dir, "**", "*.md"), recursive=True)):
        base = os.path.basename(path)
        if base in _IGNORED:
            continue
        body = _read(path)
        title = _first_heading(body, 1) or os.path.splitext(base)[0]
        news.append(
            {
                "slug": os.path.splitext(base)[0].lower().replace(" ", "-"),
                "title": title,
                "body": body,
            }
        )
    return news


def load_about() -> list[dict]:
    about_dir = os.path.join(REPO_ROOT, "about")
    pages: list[dict] = []
    if os.path.isdir(about_dir):
        for path in sorted(glob.glob(os.path.join(about_dir, "*.md"))):
            if os.path.basename(path) in _IGNORED:
                continue
            body = _read(path)
            title = _first_heading(body, 1) or os.path.splitext(os.path.basename(path))[0]
            pages.append({"title": title, "body": body})
    if not pages:
        pages = [{"title": "About InkuA", "body": _read(os.path.join(REPO_ROOT, "README.md"))}]
    return pages
