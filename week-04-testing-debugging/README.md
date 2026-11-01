# Week 4: Claude Code + Git
**TECH 85 · February 10 · Stanford Continuing Studies**

## Session Goals

- Use Git to checkpoint your project before making risky AI-assisted changes
- Describe bugs precisely so Claude Code can fix them quickly
- Understand Claude Code as a full coding agent — not just a chat interface

## Before Class

- Install Git: open your terminal and type `git --version`. If you get a "command not found" error, install from [git-scm.com](https://git-scm.com) and restart your terminal.
- Have a GitHub account (free at github.com). If you deployed last week, you already have one.
- Bring your Project 1 project folder — we will add Git to it in the first lab block.

## Concepts (20 min)

- **Claude Code as a full coding agent:** Claude Code is not a chatbot you paste code into. It reads your files, writes changes, runs your app to test them, reads the output, and decides what to do next — all without you copying and pasting anything. Understanding this loop changes how you use it: you give it a task, not a question.
- **Describing bugs precisely:** The single most important skill for AI-assisted debugging. The formula: "When I do X, I expect Y, but I get Z." Include the exact error message if there is one. Vague bug reports ("it doesn't work") waste time; precise ones ("when I click Delete on the last item, I get an IndexError on line 47") solve in one round.
- **Git as a checkpoint system for AI-generated code:** Git saves snapshots of your code. Think of each commit as a save state in a video game. Before you ask Claude Code to make a big change, commit. If the change makes things worse, you can roll back to the last good state with one command. This is especially important with AI-generated code because changes can be large and fast.
- **The break-fix loop:** A powerful learning practice. Make a commit, intentionally introduce a bug (by giving Claude Code a bad prompt), observe the failure, then fix it. Doing this deliberately builds your bug-reading skills faster than waiting for bugs to appear on their own.

## Lab (65 min)

### Part 1: Git setup — init, commit, and push (20 min)

We are doing this before our guest arrives so you have Git ready for the lab after.

1. Open your terminal and navigate to your Project 1 folder.
2. Initialize Git:
   ```
   git init
   git branch -M main
   ```
3. Create a `.gitignore` file. Ask Claude Code:
   > "Create a .gitignore file for a Python Streamlit project. Include: .env, __pycache__, *.db, .DS_Store, and any other common Python ignores."
4. Stage and commit your files:
   ```
   git add .
   git commit -m "Initial commit: Project 1 working version"
   ```
5. Create a new repository on GitHub (github.com → New repository). Copy the remote URL.
6. Push to GitHub:
   ```
   git remote add origin https://github.com/yourusername/your-repo.git
   git push -u origin main
   ```
7. Refresh the GitHub page and confirm your files are there.

**If something goes wrong:** Paste the exact error message into Claude Code. Git error messages are notoriously cryptic; Claude Code is good at translating them.

---

### Guest: Steve (~45 min)

Steve will speak on how he uses AI tools in real software projects — the parts that work well, the parts that require more judgment, and what he wishes he had known earlier. This is a practitioner's view of the tools you are learning.

Bring your questions. Good ones to ask:
- What does your AI-assisted workflow actually look like day to day?
- What is the thing AI is worst at that surprises people?
- What would you tell someone just starting to build with these tools?

---

### Part 2: Break your app and fix it (25 min)

This is the break-fix loop. You will intentionally introduce a bug, watch it fail, then fix it with Claude Code.

**Before you start:** Make sure you have a clean commit (from Part 1). Check with `git status` — it should say "nothing to commit."

**Step 1: Break it.**
Ask Claude Code for a feature with a deliberately bad prompt — vague, underspecified, or contradictory. Examples that reliably cause problems:
> "Add a button that does something with the data."

or

> "Make the app faster."

Let Claude Code make the change without being precise. Run the app. Observe what went wrong.

**Step 2: Describe the bug.**
Open `starter/bug_description_template.md`. Fill it out for the bug you just introduced.
- What were you trying to do?
- What did you expect to happen?
- What actually happened? (Paste the error message if there is one.)
- What are the steps to reproduce it?

**Step 3: Fix it.**
Give Claude Code your filled-out bug description:
> "Here is a bug in my app: [paste your bug description]. Fix it."

Compare the speed of diagnosis when you give Claude Code a precise bug report vs. a vague one.

**Step 4: Commit the fix.**
```
git add .
git commit -m "Fix: [describe the bug in past tense]"
```

Push to GitHub:
```
git push
```

## Reading for Next Week

1. *Beyond Vibe Coding* — Chapter 7 (~20 min). This chapter covers data persistence and the kind of repo structure that makes AI tools more effective.

2. Stanford CS146S Week 4 notes at [themodernsoftware.dev/fall2025](https://themodernsoftware.dev/fall2025) (~10 min). Skim the section on Git workflows for AI-assisted development.
