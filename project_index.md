# Project Index

This file keeps track of every file and directory in this project to help understand the project step-by-step. It should be updated as new files and directories are added.

## Directory Structure

### `Day01(Assistant)/`
This directory contains the initial work related to building a basic AI assistant.
*   **`.env`**: Contains environment variables, such as API keys required for the assistant to function. (Make sure this is not checked into version control).
*   **`hello_ai.py`**: A basic script to test the setup and connection to the AI model. It likely contains a simple "Hello World" equivalent for AI.
*   **`assistant.py`**: The main script for the Day 01 assistant implementation.

### `Day02(Memory)/`
This directory contains the implementation of chat memory and persistent context for the AI assistant.
*   **`memory.py`**: Interactive chatbot loop maintaining message history in conversation context.

### `.venv/`
*   The Python virtual environment for the project, containing all installed dependencies.

### `.vscode/`
*   Contains Visual Studio Code workspace settings and configurations (ignored in version control).

---

## Git & GitHub Setup & Workflow Guide

### 1. One-Time Git Configuration (Per Machine)
Ensure commits are linked to your GitHub account and appear on your contribution heatmap:
```bash
git config --global user.name "Your Name"
git config --global user.email "your_github_email@example.com"
```

---

### 2. Initializing a New Project with Git
Whenever you start a brand new project folder:

1. **Create a `.gitignore` first** (to prevent accidental commits of sensitive or bulky files):
   ```text
   .venv/
   .env
   *.env
   .DS_Store
   __pycache__/
   .vscode/
   ```
2. **Initialize Git and make the first commit:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   ```

---

### 3. Connecting to a New GitHub Repository
1. Create a new repository on [GitHub](https://github.com/new).
2. Link your local project to GitHub:
   ```bash
   git remote add origin https://github.com/<username>/<repo-name>.git
   ```
3. Push your code:
   ```bash
   git push -u origin main
   ```

> **Note:** If GitHub created the repo with a README or License, resolve the conflict before pushing:
> ```bash
> git pull --rebase origin main
> git push -u origin main
> ```

---

### 4. Daily Development Workflow (Saving Changes)
Whenever you make progress or complete a feature:
```bash
# Check modified and untracked files
git status

# Stage all changes
git add .

# Save snapshot with a descriptive message
git commit -m "Describe what was added or changed"

# Push to GitHub
git push
```

---

### 5. Helpful Troubleshooting Commands
* **Untrack a file/folder without deleting it locally** (e.g., if `.env` or `.vscode` was accidentally committed):
  ```bash
  git rm -r --cached <file_or_directory>
  git commit -m "Untrack <file_or_directory>"
  git push
  ```
* **Check commit history:**
  ```bash
  git log --oneline -n 5
  ```
* **Verify remote repository URL:**
  ```bash
  git remote -v
  ```