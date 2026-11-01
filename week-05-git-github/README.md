# Week 5: Version Control with Git and GitHub

**Session:** Tue Feb 16, 2027, 7:00–8:30 pm PT

## Goals

By the end of this session you will be able to:

- Put a project folder under Git version control
- Create commits to save versions of your work
- Create a branch to try a risky change, then recover using git
- Push your project to GitHub so others can see or use it

---

## Key Concepts

### What Git does

Git is a tool that tracks changes to files over time. Every time you run `git commit`, Git takes a snapshot of your project — all its files at that moment. You can go back to any snapshot at any time.

Think of commits like save-states in a video game. You can always load a save-state. You never lose work unless you choose to.

### The three-zone model

```
Working directory       Staging area          Repository
(files you are          (files queued         (saved snapshots)
 editing)                for next commit)

     [edit files]  →  [git add]  →  [git commit]
```

- **Working directory**: where you type and edit
- **Staging area**: a waiting room — you choose which changes to include in the next commit
- **Repository**: the permanent history, stored in the hidden `.git` folder

### Branches

A branch is a parallel copy of your project where you can make changes without affecting the original. The default branch is usually called `main`.

```
main:     A ── B ── C
                 \
my-change:        D ── E   (experimental — safe to break things here)
```

If the change works, you **merge** it back into `main`. If it does not work, you delete the branch — no harm done.

### Why GitHub

Git is a local tool — it saves history on your computer. GitHub is a website that stores a copy of your repository online. This gives you:

- A backup (if your laptop dies, your code is safe)
- A way to share code with others
- A way to collaborate without emailing files back and forth

---

## Setup Before Lab

If you have not installed Git yet, do this before the session (or at the start of lab):

- **Mac**: Open Terminal, run `git --version`. If Git is not installed, macOS will prompt you to install it.
- **Windows**: Download Git for Windows from [git-scm.com](https://git-scm.com) and install it with default settings.
- **All platforms**: After installing, set your name and email:
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "you@example.com"
  ```

You will also need a free GitHub account: [github.com/signup](https://github.com/signup)

---

## Lab: From Zero to GitHub

This lab takes about 45 minutes.

### Part 1 — Initialize a repository (10 min)

1. Open VS Code. Open the folder containing your `my_tool.py` from Week 2 (or use the `week-02-specs-and-prompts/starter/` folder).
2. Open a terminal in VS Code.
3. Initialize a Git repository:
   ```bash
   git init
   ```
   You will see a message like `Initialized empty Git repository in .../starter/.git/`.

4. Check the status of your new repository:
   ```bash
   git status
   ```
   Git will list all your files as "untracked" — it sees them but has not started tracking them yet.

5. Stage all your files for the first commit:
   ```bash
   git add my_tool.py
   ```
   If you have other files (like your spec), add them too:
   ```bash
   git add spec_template.md
   ```

6. Make your first commit:
   ```bash
   git commit -m "Initial commit: add my tool and spec"
   ```
   See `starter/commit_message_guide.md` for tips on writing good commit messages.

7. Run `git log` to see your commit history:
   ```bash
   git log --oneline
   ```
   You should see one entry.

### Part 2 — Make a change and commit it (10 min)

8. Open `my_tool.py`. Make a small change — for example, change the output format slightly, or add a comment at the top explaining what the script does. Save the file.

9. Run `git status` again. Git will show the file as "modified."

10. Run `git diff` to see exactly what changed:
    ```bash
    git diff my_tool.py
    ```
    Lines starting with `-` were removed; lines starting with `+` were added.

11. Stage and commit the change:
    ```bash
    git add my_tool.py
    git commit -m "Improve output format"
    ```

12. Run `git log --oneline` again. You now have two commits.

### Part 3 — Break it on a branch and recover (15 min)

13. Create a new branch called `experiment`:
    ```bash
    git checkout -b experiment
    ```
    You are now on the `experiment` branch. Your `main` branch is unchanged.

14. Open `my_tool.py` and make a change that breaks something — for example, delete the `try:` / `except:` block around the file-open call, or remove the `if __name__ == "__main__":` line. Save the file.

15. Commit the breaking change on the experiment branch:
    ```bash
    git add my_tool.py
    git commit -m "Experiment: remove error handling (intentionally broken)"
    ```

16. Try running the script on a file that does not exist:
    ```bash
    python my_tool.py nonexistent_file.txt
    ```
    It should crash in a worse way than before (no helpful error message).

17. Recover by switching back to `main`:
    ```bash
    git checkout main
    ```
    Open `my_tool.py` — the breaking change is gone. Your `main` branch is exactly as you left it in step 12.

18. Run the script again. It works. This is why branches exist.

19. Delete the experiment branch (we no longer need it):
    ```bash
    git branch -d experiment
    ```

### Part 4 — Push to GitHub (10 min)

20. Go to [github.com](https://github.com) and sign in.
21. Click the `+` button in the top-right corner → "New repository."
22. Name it something like `my-vibe-coding-tool`. Leave it public (or private — your choice). Do NOT check "Initialize with README" since you already have a repository.
23. Click "Create repository." GitHub will show you a set of commands. Find the section labeled "...or push an existing repository from the command line."
24. Run those commands in your terminal. They will look like:
    ```bash
    git remote add origin https://github.com/YOUR-USERNAME/my-vibe-coding-tool.git
    git branch -M main
    git push -u origin main
    ```
25. Refresh the GitHub page. You should see your files there.

---

## Expected Outputs

By the end of lab you should have:

- A Git repository with at least two commits
- Evidence that you created and deleted a branch (`git log --oneline` showing commits on both)
- Your project visible on GitHub at `github.com/YOUR-USERNAME/my-vibe-coding-tool`

---

## If Something Goes Wrong

| Problem | What to do |
|---|---|
| `git: command not found` | Git is not installed. Follow the setup instructions above. |
| `error: pathspec 'main' did not match any file(s)` | Your default branch may be called `master`. Try `git branch -M main` to rename it. |
| GitHub asks for a password but doesn't accept it | GitHub no longer accepts passwords for push. You need a Personal Access Token. See: github.com/settings/tokens — create one with `repo` scope. Use it as your password. |
| `fatal: remote origin already exists` | Run `git remote remove origin` and then add it again. |
| You committed to the wrong branch | Ask the AI: "I accidentally committed to main instead of my feature branch. How do I move this commit to a new branch?" |

---

## Reference Files

- `starter/git_cheatsheet.md` — quick command reference for everything covered today
- `starter/commit_message_guide.md` — how to write commit messages that are actually useful

---

## Before Next Week

Your project is now on GitHub. Next week we work with files and data — specifically CSV and JSON files. If you have a spreadsheet or CSV file from your own work that you are comfortable using in class, bring it (or a copy with any sensitive data removed). You will use it in the lab.

## Slides

See `slides.md` in this folder (also posted in Canvas).
