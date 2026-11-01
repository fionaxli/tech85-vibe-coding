# Git Cheatsheet

A quick reference for the Git commands used in TECH 85.

---

## The four commands you use every session

```bash
git status
```
Show which files have changed since the last commit. Run this before and after every Claude Code task.

```bash
git add .
git commit -m "Short description of what changed"
```
Save a snapshot. The `.` adds all changed files. The `-m` flag lets you write the commit message inline.

```bash
git push
```
Upload your commits to GitHub. Run at the end of every session.

```bash
git log --oneline
```
Show the commit history, one line per commit. Each line starts with a short ID (like `a3f92b1`) that you can use to go back to that state.

---

## Before every big Claude Code task

```bash
git add .
git commit -m "Checkpoint before [describe what you are about to do]"
```

Example: `git commit -m "Checkpoint before adding login feature"`

This is your save state. If the task goes wrong, you can roll back.

---

## Rolling back to the last commit

If something goes badly wrong and you want to undo all changes since your last commit:

```bash
git checkout -- .
```

**Warning:** this discards all uncommitted changes permanently. Only use it when you are sure you do not want to keep the current state.

---

## Checking what changed

See what has changed in your files since the last commit:
```bash
git diff
```

See a summary (which files changed, how many lines):
```bash
git diff --stat
```

---

## Working with GitHub

Set up the connection between your local repo and GitHub (do this once per project):
```bash
git remote add origin https://github.com/yourusername/repo-name.git
git branch -M main
git push -u origin main
```

After the first push, you just need:
```bash
git push
```

---

## When things go wrong

**"I accidentally committed a file I did not mean to commit"**
Ask Claude Code: *"I accidentally committed [file name]. How do I remove it from the repository without deleting it from my computer?"*

**"My push was rejected"**
Usually means your local repo is behind the remote. Ask Claude Code: *"My git push was rejected. The error says [paste error]. How do I fix this?"*

**"I don't know which version of my code is the right one"**
Run `git log --oneline` to see your commit history. Find the commit before things went wrong. Ask Claude Code: *"I want to go back to this commit: [paste the commit ID]. What is the safest way to do that?"*
