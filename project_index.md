# Project Index

This file keeps track of every file and directory in this project to help understand the project step-by-step. It should be updated as new files and directories are added.

## Directory Structure

### `Day01(Assistant)/`
This folder contains our first steps in creating a simple AI assistant.
*   **`.env`**: Stores secret settings, like your API keys and model details, so they are not shared publicly on GitHub.
*   **`hello_ai.py`**: A simple test script. It sends one question to the AI model ("Explain AI in 200 words") and prints the answer to make sure the connection works.
*   **`assistant.py`**: A basic chatbot in the terminal that lets you talk to the AI continuously until you type `"quit"`. It answers one message at a time without remembering past questions.

### `Day02(Memory)/`
This folder adds memory so the AI can remember past conversations.
*   **`memory.py`**: A chatbot that remembers past messages in the chat. In Day 01, the assistant forgot previous chats after each question. Here, both our messages and the AI's replies are saved in a list (`messages`) and sent back each time, so the AI remembers the conversation until you type `"quit"`.

### `Day03(Prompt_engineering))/`
This folder explores prompt engineering and system instructions.
*   **`system_prompts.py`**: An interactive assistant that uses system prompts to define persona and behavior. Users select a role (Maths teacher, Physics teacher, or Chemistry teacher), which sets the `"system"` message instruction. Maintains conversational memory throughout the session and prints the full chat history with role tags upon typing `"exit"`.

### `Day04(Tools)/`
This folder covers function calling and tool usage for AI agents.
*   **`tools.py`**: Implementation of agent tools and function calling, allowing the AI model to interact with external tools and execute custom Python functions.

### Root Files & Utilities
*   **`start_mlx_server.py`**: Helper script to launch a local MLX model server (hosting `Qwen/Qwen3-1.7B-MLX-4bit` on Apple Silicon) exposing an OpenAI-compatible API on port 8080.
*   **`lmx_testing.py`**: Test script for verifying local model inference directly via `mlx_lm.load` and `mlx_lm.generate`.
*   **`requirements.txt`**: Contains all installed Python packages and dependencies for the project.
*   **`pyrefly.toml`**: Environment and type-checker configuration.
*   **`git.txt`**: Quick reference cheat-sheet for daily git workflow commands.

### `.venv/`
*   The virtual environment folder where all installed Python packages (like `openai` and `python-dotenv`) are kept separate from your main system.

### `.vscode/`
*   Contains settings and preferences for VS Code (kept on your computer and ignored by Git).

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
