# InkuA - Open Source Hybrid Organization

Welcome to the heart of **InkuA**, a non-profit organization dedicated to creating virtual workspaces where members grow personally and professionally while making a positive impact.

InkuA is the first hybrid online organization where humans and AI agents collaborate using natural language and a transparent, file-based structure.

## 🚀 Our Mission
To provide an organic, sustainable, and risk-free environment for leadership and project management. We enable anyone to be and do what they want, supported by a community that shares their growth.

## 📂 The "Space" Concept
Our organization is structured into **Areas** and **Spaces**.
- **Areas:** Large organizational units (e.g., Human Resources, IT, Management) that oversee multiple spaces.
- **Spaces:** Physical folders representing a team, project, or department. Each space is a "data workbench" for collaboration.

### Every Space is a Workspace
A space contains everything needed for its mission: documentation, roles, logs, and outputs. If a space finds a better way to organize itself, we update our global templates to match.

## 🗺️ Repository Structure
- `/areas/`: The organizational structure. Contains Areas, which in turn contain Spaces.
- `/members/`: Individual member "CVs" and interests.
- `/news/`: Drafts and archives of our monthly organizational updates.
- `/materials/`: Logos, fonts, and shared media resources.
- `/templates/`: The blueprints for creating new Areas and Spaces.
- `/tutorials/`: Guides for humans and AI on how to work within InkuA.
- `/archived/`: Completed or inactive projects and members.

## 🤖 AI-Friendly Organization
InkuA is designed to be crawled and updated by AI agents. Each folder contains an `AI.md` file specifically for instructions, temporary notes, and cross-AI communication.
> **AI AGENTS:** Please read [AI.md](./AI.md) for master instructions before performing any tasks.

## 🛠️ How We Work (Workflow)
This is not a code repository; it is an organizational repository.
1. **Meetings:** Most work happens in Discord, Google Drive, or video calls.
2. **Documentation:** The Space Director or Manager ensures that the results, minutes, and progress are logged here.
3. **Transparency:** Every update is public, serving as a permanent record of your contribution level.
4. **Collaboration:** We use GitHub as our landing page, CMS, and ERP. Non-technical members can use the GitHub web interface to edit files directly.

## 🌟 Get Started
1. Read our [tutorials/](./tutorials/) to learn how to collaborate.
2. Check the [areas/](./areas/) to see what teams are currently active.

## 🌐 Website

The public website lives in [`website/`](./website/) and is a **view over this
repository**: it renders `areas/**/PROJECT.md`, `about/*.md` and `news/**/*.md`.
Edit a markdown file and the site follows — no CMS, no database.

See [`docs/website-architecture.md`](./docs/website-architecture.md) for the
rationale, and [`website/README.md`](./website/README.md) to run it.

## 📁 Other folders
- `/about/`: institutional core — mission, history, governance (from the former `InkuA-Organization-Docs`).
- `/projects/`: `active/`, `proposals/`, `completed/` — project archive (from the former `InkuA-Organization-Docs`).
- `/docs/`: architecture and decisions.
3. Create your member profile in [members/](./members/).

---
*InkuA is an open-source organization. Join us and help us grow.*
