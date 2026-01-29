# Onboarding Tutorial: Collaborating on InkuA Repository

Welcome to the InkuA Repository! This tutorial will guide you through the process of collaborating with us. Whether you are adding a new project, updating documentation, or fixing a bug, this guide will help you get started.

## Prerequisites

Before you begin, make sure you have:
1.  **A GitHub Account**: If you don't have one, [create one here](https://github.com/join).
2.  **Git Installed**: You'll need Git installed on your local machine to contribute.

## Step-by-Step Guide

### Step 1: Fork and Clone the Repository

1.  **Fork** the repository by clicking the "Fork" button at the top right of the repository page. This creates a copy of the repository in your own GitHub account.
2.  **Clone** your forked repository to your local machine:
    ```bash
    git clone https://github.com/YOUR-USERNAME/inkua-repo-name.git
    cd inkua-repo-name
    ```
    *(Replace `YOUR-USERNAME` and `inkua-repo-name` with the actual values)*

### Step 2: Understand the Structure

The repository follows a specific structure. Familiarize yourself with these key areas:
*   **[`templates/space-template/`](../../templates/space-template/)**: All projects, departments, or spaces should follow the structure defined here. Read [`templates/space-template/README.md`](../../templates/space-template/README.md) to understand the required files (`LOG.md`, `ROLES.md`, `PROJECT.md`, etc.).
*   **[`tutorials/`](../)**: Contains guides and tutorials like this one.
*   **[`README.md`](../../README.md)**: The main entry point for the repository.

### Step 3: Create a Branch

Never work directly on the `main` or `master` branch. Always create a new branch for your changes:

```bash
git checkout -b feature/your-feature-name
```

*   Use `feature/` for new content or features.
*   Use `fix/` for bug fixes.
*   Use `docs/` for documentation updates.

### Step 4: Make Your Changes

Now, you can edit files or add new ones.

*   **File Naming**: Please follow our naming conventions described in [`tutorials/02-Collaborating/naming-convention.md`](../02-Collaborating/naming-convention.md). Use lowercase and dashes (e.g., `my-new-file.md`), not spaces or CamelCase.
*   **Markdown**: We use Markdown for documentation. If you are new to Markdown, check out [`tutorials/01-Getting-Started/markdown.md`](./markdown.md).
*   **Space Structure**: If creating a new space or project, ensure you copy the `templates/space-template` content and fill it out.

### Step 5: Commit and Push

Once you are happy with your changes:

1.  **Stage** your changes:
    ```bash
    git add .
    ```
2.  **Commit** your changes with a descriptive message:
    ```bash
    git commit -m "Add new onboarding tutorial"
    ```
3.  **Push** the changes to your fork:
    ```bash
    git push origin feature/your-feature-name
    ```

### Step 6: Create a Pull Request (PR)

1.  Go to the original InkuA repository on GitHub.
2.  You should see a prompt to "Compare & pull request". Click it.
3.  Fill in the title and description of your PR. Explain what you changed and why.
4.  Submit the Pull Request.

### Step 7: Review and Merge

A team member (or potentially an AI agent) will review your PR. They might request changes or ask questions. Once everything is approved, your changes will be merged into the main repository.

## Need Help?

Check the [`tutorials/`](../) folder for more specific guides or reach out to the team via the communication channels listed in the main [`README.md`](../../README.md).

Happy Collaborating!
