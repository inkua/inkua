# Onboarding Tutorial: Collaborating on InkuA Repository

Welcome to the InkuA Repository! This tutorial will guide you through the process of collaborating with us. Whether you are adding a new project, updating documentation, or fixing a bug, this guide will help you get started.

## Prerequisites

Before you begin, make sure you have:
1.  **A GitHub Account**: If you don't have one, [create one here](https://github.com/join).

That's it! You can contribute directly from your web browser.

---

## Method 1: Quickstart (Web Interface)
*Recommended for non-technical contributors or quick edits.*

You don't need to install anything to contribute. You can do everything through the GitHub website.

### Step 1: Find the File
Navigate through the folders in the repository to find the file you want to edit.
*   **[`templates/space-template/`](../../templates/space-template/)**: Structure for projects/spaces.
*   **[`tutorials/`](../)**: Guides and tutorials.

### Step 2: Edit the File
1.  Click on the file name to open it.
2.  Click the **Pencil icon** (Edit this file) in the top right corner of the file view.
3.  Make your changes in the text editor.
    *   **File Naming**: If creating a new file, follow our naming conventions: lowercase and dashes (e.g., `my-new-file.md`).

### Step 3: Propose Changes
1.  Scroll down to the **"Commit changes"** box.
2.  Write a short title explaining your change (e.g., "Update meeting notes").
3.  Add an optional extended description.
4.  **Important**: Select **"Create a new branch for this commit and start a pull request"**.
5.  Click **"Propose changes"**.

### Step 4: Create Pull Request
1.  You will be taken to a "Open a pull request" page.
2.  Review your title and description.
3.  Click **"Create pull request"**.
4.  A team member will review your changes and merge them!

---

## Method 2: Advanced (Command Line / Git)
*Recommended for developers and technical contributors.*

If you prefer working locally or need to make complex changes, follow these steps.

### Prerequisites
*   **Git Installed**: You'll need Git installed on your local machine.

### Step 1: Fork and Clone
1.  **Fork** the repository.
2.  **Clone** to your machine:
    ```bash
    git clone https://github.com/YOUR-USERNAME/inkua-repo-name.git
    cd inkua-repo-name
    ```

### Step 2: Create a Branch
```bash
git checkout -b feature/your-feature-name
```

### Step 3: Make Changes & Push
1.  Edit files locally.
2.  Stage and commit:
    ```bash
    git add .
    git commit -m "Add new onboarding tutorial"
    ```
3.  Push to your fork:
    ```bash
    git push origin feature/your-feature-name
    ```

### Step 4: Create Pull Request
Go to the original repository on GitHub and click **"Compare & pull request"**.

---

## Need Help?

Check the [`tutorials/`](../) folder for more specific guides or reach out to the team via the communication channels listed in the main [`README.md`](../../README.md).

Happy Collaborating!
