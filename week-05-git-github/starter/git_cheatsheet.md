# Git Cheatsheet

Quick reference for the commands used in TECH 85. Every command runs in your terminal.

---

## Setup (do once per computer)

```bash
# Tell Git who you are
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

# Check your settings
git config --list
```

---

## Starting a Repository

```bash
# Turn the current folder into a Git repository
git init

# Clone an existing repository from GitHub to your computer
git clone https://github.com/username/repo-name.git
```

---

## Daily Workflow

```bash
# See what has changed
git status

# See exactly what changed inside a file
git diff filename.py

# Stage a file for the next commit
git add filename.py

# Stage all changed files at once (use carefully)
git add .

# Take a snapshot (commit)
git commit -m "Your message here"

# Stage and commit in one step (only works for already-tracked files)
git commit -am "Your message here"
```

---

## Looking at History

```bash
# See all commits, one per line
git log --oneline

# See all commits with full details
git log

# See what changed in a specific commit (replace abc1234 with real hash)
git show abc1234

# See the history of one file
git log --oneline filename.py
```

---

## Undoing Things

```bash
# Discard changes in a file (go back to last commit) — CANNOT BE UNDONE
git checkout -- filename.py

# Unstage a file (keep the changes, just remove from staging area)
git restore --staged filename.py

# Go back and look at an old commit (you are in "detached HEAD" state)
git checkout abc1234

# Come back to the present
git checkout main

# Create a new commit that reverses a previous commit (safe — keeps history)
git revert abc1234
```

---

## Branches

```bash
# See all branches
git branch

# Create a new branch
git branch new-feature

# Switch to an existing branch
git checkout new-feature

# Create and switch in one step
git checkout -b new-feature

# Merge a branch into the current branch
git merge new-feature

# Delete a branch (after merging)
git branch -d new-feature

# Delete a branch (even if not merged — be careful)
git branch -D new-feature
```

---

## Working with GitHub (Remote)

```bash
# Link your local repo to a GitHub repo
git remote add origin https://github.com/username/repo-name.git

# See what remotes are configured
git remote -v

# Push your commits to GitHub for the first time
git push -u origin main

# Push after the first time
git push

# Pull the latest changes from GitHub
git pull

# Fetch changes without merging them
git fetch
```

---

## Checking What Is Ignored

```bash
# See which files Git is ignoring
git status --ignored

# See the contents of the ignore rules file
cat .gitignore
```

---

## Common `.gitignore` Entries

Add a `.gitignore` file to your repo root with entries like these to keep junk out of your commits:

```
# Virtual environments
venv/
.venv/

# Python compiled files
__pycache__/
*.pyc

# Editor settings
.vscode/
.idea/

# Environment variable files (never commit these!)
.env

# OS files
.DS_Store        # Mac
Thumbs.db        # Windows
```

---

## The Most Common Sequence

Starting fresh on a new feature:

```bash
git checkout -b my-new-feature
# ... edit files ...
git add changed_file.py
git commit -m "Add new feature"
git checkout main
git merge my-new-feature
git push
```

---

## When Things Go Wrong

| Situation | Command |
|---|---|
| "I staged the wrong file" | `git restore --staged filename.py` |
| "I want to throw away my edits" | `git checkout -- filename.py` |
| "I committed to the wrong branch" | Ask the AI: explain the situation in detail |
| "I see 'detached HEAD state'" | `git checkout main` to get back to normal |
| "My push was rejected" | `git pull` first to get any changes, then `git push` again |
| "I accidentally deleted a file" | `git checkout -- deleted_file.py` |
