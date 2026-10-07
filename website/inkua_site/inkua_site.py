"""InkuA public website — a Reflex app that renders this repository's content.

The site is a view over ``areas/**/PROJECT.md``, ``about/*.md`` and
``news/**/*.md``. Edit those files and the site follows.
"""

from __future__ import annotations

import reflex as rx

from . import content

PROJECTS = content.load_projects()
NEWS = content.load_news()
ABOUT = content.load_about()

ACCENT = "#2e7d32"
MUTED = "#5f6368"
BORDER = "1px solid #eaeaea"


def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(rx.heading("InkuA", size="6"), href="/", text_decoration="none", color=ACCENT),
        rx.spacer(),
        rx.link("Projects", href="/projects"),
        rx.link("News", href="/news"),
        rx.link("About", href="/about"),
        rx.link("GitHub", href="https://github.com/inkua/inkua"),
        width="100%",
        padding="1em 2em",
        border_bottom=BORDER,
        align="center",
        spacing="5",
    )


def footer() -> rx.Component:
    return rx.box(
        rx.text(
            "InkuA gUG — an open source hybrid organization where humans and AI agents collaborate.",
            font_size="0.85em",
            color=MUTED,
        ),
        rx.link("github.com/inkua/inkua", href="https://github.com/inkua/inkua", font_size="0.85em"),
        width="100%",
        padding="2em",
        border_top=BORDER,
        text_align="center",
    )


def layout(*children: rx.Component) -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.box(*children, width="100%", max_width="1100px", margin="0 auto", padding="2em"),
        footer(),
        spacing="0",
        width="100%",
        min_height="100vh",
    )


def _progress(done: int, total: int) -> str:
    return f"{done}/{total} phases done" if total else "No roadmap yet"


def _stat(value: str, label: str) -> rx.Component:
    return rx.vstack(rx.heading(value, size="7"), rx.text(label, color=MUTED), align="center")


def _project_card(project: dict) -> rx.Component:
    return rx.box(
        rx.link(
            rx.heading(project["name"], size="4"),
            href=f"/projects/{project['slug']}",
            text_decoration="none",
        ),
        rx.text(f"Area: {project['area']} · Space: {project['space']}", font_size="0.8em", color=MUTED),
        rx.text(_progress(project["done"], project["total"]), font_size="0.85em"),
        padding="1em",
        border=BORDER,
        border_radius="10px",
        width="100%",
    )


def home() -> rx.Component:
    return layout(
        rx.heading("InkuA", size="9"),
        rx.text(
            "A non-profit where humans and AI agents build social impact projects together, in the open.",
            font_size="1.2em",
            color=MUTED,
        ),
        rx.hstack(
            rx.link(rx.button("Explore projects"), href="/projects"),
            rx.link(rx.button("Read the news", variant="soft"), href="/news"),
            spacing="3",
            padding_top="1em",
        ),
        rx.divider(padding_top="1.5em"),
        rx.hstack(
            _stat(str(len(PROJECTS)), "Spaces"),
            _stat(str(len(NEWS)), "News posts"),
            _stat("Open", "Source"),
            spacing="6",
            padding_top="1em",
        ),
        spacing="3",
        align="start",
        width="100%",
    )


def projects_index() -> rx.Component:
    children: list[rx.Component] = [
        rx.heading("Projects & Spaces", size="7"),
        rx.text("Every Space in the repository is a self-contained workbench.", color=MUTED),
    ]
    if PROJECTS:
        children += [_project_card(p) for p in PROJECTS]
    else:
        children.append(rx.text("No spaces with a PROJECT.md yet.", color=MUTED))
    return layout(*children, spacing="3", align="start", width="100%")


def project_detail(project: dict) -> rx.Component:
    children: list[rx.Component] = [
        rx.link("← All projects", href="/projects"),
        rx.heading(project["name"], size="7"),
        rx.text(f"Area: {project['area']} · Space: {project['space']}", color=MUTED),
        rx.heading("Overview", size="5", padding_top="0.5em"),
        rx.markdown(project["readme"] or "_No README yet._"),
        rx.heading("Project tracking", size="5", padding_top="0.5em"),
        rx.markdown(project["project_md"]),
    ]
    if project["deliverables"]:
        children.append(rx.heading("Deliverables", size="5", padding_top="0.5em"))
        children.append(rx.unordered_list(*[rx.list_item(d) for d in project["deliverables"]]))
    return layout(*children, spacing="2", align="start", width="100%")


def news_index() -> rx.Component:
    children: list[rx.Component] = [rx.heading("News", size="7")]
    if NEWS:
        for item in NEWS:
            children.append(
                rx.box(
                    rx.heading(item["title"], size="5"),
                    rx.markdown(item["body"]),
                    padding="1em",
                    border=BORDER,
                    border_radius="10px",
                    width="100%",
                )
            )
    else:
        children.append(rx.text("No news yet.", color=MUTED))
    return layout(*children, spacing="3", align="start", width="100%")


def about_page() -> rx.Component:
    children: list[rx.Component] = [rx.heading("About InkuA", size="7")]
    for page in ABOUT:
        children.append(rx.heading(page["title"], size="5", padding_top="0.5em"))
        children.append(rx.markdown(page["body"]))
    return layout(*children, spacing="2", align="start", width="100%")


app = rx.App()
app.add_page(home, route="/", title="InkuA — Open Source Hybrid Organization")
app.add_page(projects_index, route="/projects", title="Projects · InkuA")
app.add_page(news_index, route="/news", title="News · InkuA")
app.add_page(about_page, route="/about", title="About · InkuA")
for _project in PROJECTS:
    app.add_page(
        project_detail(_project),
        route=f"/projects/{_project['slug']}",
        title=f"{_project['name']} · InkuA",
    )
