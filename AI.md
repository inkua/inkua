# Master AI Instructions - InkuA Organization

Welcome, Agent. You are interacting with the InkuA repository, a hybrid organizational system designed for human-AI collaboration. Your goal is to help maintain, organize, and grow this organization.

## 🎯 Core Directives
1. **Context Awareness:** Before making changes, always read the local `README.md` and `AI.md` of the folder you are in.
2. **Transparency:** Log every significant action in the relevant `LOG.md` file using the format: `YYYY-MM-DD: [Action Description]`.
3. **Persistence:** Use the `AI.md` file in each folder as a scratchpad for your current work, temporary notes, or messages to future agents in case you crash or lose context.
4. **Human-Centric:** Remember that this organization serves humans. Your changes should make it easier for humans to understand what is happening.
5. **Horizontal Structure:** InkuA promotes a horizontal hierarchy. Suggest connections between spaces (e.g., IT and HR) if you notice overlapping objectives.

## 📂 Structural Rules
- **Areas:** Root containers for spaces. They contain advisors and board members.
- **Spaces:** Individual work units. They must have a `README.md`, `LOG.md`, `PROJECT.md`, `NEWS/` folder, and `REPORTS/` folder.
- **Members:** Profiles are stored in `/members/FirstName-LastName.md`.

## 🔄 Workflow for AI
1. **Crawl:** Explore the `/areas/` directory to understand the current organizational state.
2. **Update:** If you perform a task, update the `LOG.md` of that specific space.
3. **Draft News:** If a space has significant progress, draft a news item in that space's `NEWS/outbox/` or directly in the root `/news/drafts/`.
4. **Coordinate:** If you are deleting or moving a folder, leave a message in that folder's `LOG.md` first to notify others.

## 📝 Hybrid File: LOG.md
The `LOG.md` is a shared space for humans and AI.
- Humans will log meeting minutes and high-level decisions.
- AI should log technical updates, file structure changes, and automated report generation.

## 🧠 The Scratchpad (AI.md)
Use the `AI.md` file in each folder to:
- Store intermediate thoughts.
- List tasks you are about to perform.
- Leave warnings or tips for the next agent.
- Document any "crashing" or "interrupted" work.

---
*Stay efficient, stay transparent. Let's build a better future together.*
