# Project Index

This file keeps track of every file and directory in this project to help understand the project step-by-step. It should be updated as new files and directories are added.

## Directory Structure

This index reflects files tracked in the repository. Local-only folders such as `.venv/` and `.vscode/` are not part of the tracked tree.

### Learning examples

- `Day01(Assistant)/`: `assistant.py`, `hello_ai.py`
- `Day02(Memory)/`: `memory.py`
- `Day03(Prompt_engineering)/`: `system_prompts.py`
- `Day04(Tools)/`: `assistant.py`, `test_tool_manager.py`, `test_tools.py`, `tool_manager.py`, `tools.py`
- `Day05(Document_reading)/`: `assistant1.py`, `test_file_tool.py`, `test_tool_manager.py`, `tool_manager.py`, `tools.py`
  - `Data/`: `notes.txt`, `project.txt`, `sample.pdf`

### Root files

- `.envexample`: Example environment configuration; copy and adapt it for local use.
- `.gitignore`: Excludes local or generated files from Git.
- `.mcp.json`: MCP server configuration.
- `.python-version`: Project Python version setting.
- `LICENSE`: MIT license.
- `README.md`: Project overview, architecture, capabilities, and setup notes.
- `embedding.py`: Embedding and retrieval implementation.
- `mlx_testing.py`: Example local MLX model inference script.
- `project_index.md`: This tracked-file index and Git workflow guide.
- `pyproject.toml`: Python project and build configuration.
- `pyrefly.toml`: Pyrefly type-checker configuration.
- `requirements.txt`: Python dependencies.
- `skills-lock.json`: Skill dependency lockfile.
- `start_mlx_server.py`: Starts a local MLX model server.

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
