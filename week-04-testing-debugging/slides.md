---
marp: true
theme: default
paginate: true
footer: "TECH 85 · Week 4 · Stanford Continuing Studies"
---

<!-- _class: lead -->
# Week 4: Claude Code + Git
### TECH 85: Vibe Coding
Stanford Continuing Studies · February 10

---

## Agenda

1. Recap: Project 1 demos
2. Claude Code as a full coding agent
3. The bug description formula
4. Git: commits as save states
5. The break-fix loop
6. Lab Part 1: Git setup
7. Guest Speaker: Steve
8. Lab Part 2: Break your app, fix it

---

## Recap: what you have shipped

By now every student has:
- A Project 1 app running at a live Streamlit Cloud URL
- A BRIEF.md that specifies what it does
- A CLAUDE.md that gives Claude Code memory of the project

That is a deployable web application. Built in two weeks. With no prior programming experience.

This week we add two things that make the ongoing development work safer and faster: **precise debugging** and **Git checkpoints**.

---

## Claude Code is not a chatbot

You have been using Claude Code to write code. Let us look at what it is actually doing.

When you give Claude Code a task — "add a delete button to each note" — here is what happens:

1. It reads your `app.py` file (and `CLAUDE.md` if it exists)
2. It reasons about what needs to change
3. It writes the changes directly to your file
4. It runs `streamlit run app.py` to verify the change
5. It reads the terminal output
6. If there is an error, it reads the error and fixes it — without being asked
7. It reports back to you

Steps 4–6 are what make it an **agent**, not a chatbot. It takes actions and observes results. You do not copy and paste anything.

---

## This means your job changed

Because Claude Code takes real actions:

- Changes happen to your actual files, immediately
- A bad prompt can cause a large, fast change that is hard to untangle
- You need a way to undo — quickly and reliably

Enter: **Git**.

Git is a version control system. It saves snapshots of your code over time. Each snapshot is a **commit**.

Before every significant Claude Code task: commit.
After every Claude Code task: review, then commit again if it worked.

If something goes wrong, you roll back to the last good commit.

---

## Git: commits as save states

Think of Git the way you think about saving a game.

You are about to fight a difficult boss. You save first. You lose. You load the save and try again.

In code:
```bash
git add .
git commit -m "Working version before adding login feature"
```

Now you ask Claude Code to add login. It goes wrong. You undo:
```bash
git checkout -- .
```

This restores every file to its state at the last commit. The bad changes are gone.

No more "I can't remember what it looked like before" or "I accidentally deleted something that was working."

---

## The four Git commands you actually need

```bash
git status
```
Shows which files have changed since the last commit. Run this often.

```bash
git add .
git commit -m "A short description of what changed"
```
Saves a snapshot. The message should be specific: "Fix: delete button crashes on empty list" not "update code."

```bash
git push
```
Uploads your commits to GitHub. Run this at the end of every session.

```bash
git log --oneline
```
Shows your commit history. Each line is one save state you can go back to.

---

## The bug description formula

The single most important skill for AI-assisted debugging.

**Weak:** "It doesn't work."
Claude Code will guess. Slowly.

**Formula:**
> "When I [do X], I expect [Y], but I get [Z]."

Include:
- The exact steps you took
- The exact behavior you expected
- The exact error message (copy-paste the whole thing)
- The relevant code section (ask Claude Code: "what code is responsible for this?")

**Strong:** "When I click Delete on the last item in my notes list, I expect the item to be removed. Instead, I get this error on line 47: `IndexError: list index out of range`. Here is the delete function: [paste it]."

One precise bug report. One fix. No back-and-forth.

---

## The break-fix loop

The best way to get good at debugging is to do it on purpose.

**The loop:**
1. Make a clean Git commit (your safe state)
2. Give Claude Code a bad prompt — vague, contradictory, or too ambitious
3. Watch it break
4. Read the error message
5. Write a precise bug description using the formula
6. Give it to Claude Code
7. Verify the fix works
8. Commit the fixed version

Why this works: you are practicing error reading and precise description in a safe context where you know exactly what you broke and why. That is very different from encountering a mysterious bug you did not cause.

---

## Demo: the bug description formula in action

*[Live demo — instructor walks through:]*

1. Show a working app with a clean Git commit
2. Give Claude Code a vague, bad prompt
3. Watch it break (show the error)
4. Fill out `starter/bug_description_template.md`
5. Give the precise description to Claude Code
6. Watch it fix the bug in one pass
7. Commit the fix: `git commit -m "Fix: [describe the fix]"`

Key observation: the quality of the fix is directly proportional to the quality of the bug description.

---

## Lab overview

**What you are doing today (65 min)**

| Part | Time | What you do |
|---|---|---|
| Part 1 | 20 min | Git setup: init, .gitignore, first commit, push to GitHub |
| Guest: Steve | 45 min | Practitioner talk on AI in real software projects |
| Part 2 | 25 min | Break your Project 1 app on purpose; fix it using the bug description formula; commit |

Templates in `starter/`: `bug_description_template.md`

---

## Guest Speaker: Steve

Steve builds software for a living and uses AI coding tools every day. Tonight he will share:
- What his AI-assisted workflow actually looks like
- Where AI tools genuinely save time
- Where they require more human judgment than people expect
- What he wishes he had understood earlier

Steve will speak for approximately 45 minutes, followed by questions and the lab.

---

## Key takeaways

- Claude Code is an agent — it takes real actions on your files, not just answers in a chat window
- Commit before every significant change; this is your safety net
- The bug description formula: "When I do X, I expect Y, but I get Z" — always include the exact error message
- The break-fix loop builds debugging skills faster than waiting for real bugs
- Four Git commands: `status`, `add + commit`, `push`, `log --oneline`

---

## Reading for next week

**Before Wednesday, February 17:**

1. *Beyond Vibe Coding* — Chapter 7 (~20 min). This chapter covers data persistence patterns and repo structure for AI-assisted projects.

2. Stanford CS146S Week 4 notes at [themodernsoftware.dev/fall2025](https://themodernsoftware.dev/fall2025) (~10 min)

**Also:** Think about what you want to build for Project 2. It will use SQLite and an external API. Come with a rough idea next week.
