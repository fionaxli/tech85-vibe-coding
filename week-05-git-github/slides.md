---
marp: true
theme: default
paginate: true
footer: "TECH 85 · Week 5 · Stanford Continuing Studies"
---

<!-- _class: lead -->
# Week 5: Version Control with Git and GitHub
### TECH 85: Vibe Coding
Stanford Continuing Studies · Feb 16, 2027

---

## Agenda

1. Why version control matters for vibe coders
2. Git's three-zone model
3. Commits as save-states
4. Branches: safe spaces to break things
5. GitHub: your code's online home
6. Demo: breaking something and recovering
7. Lab: from zero to GitHub

---

## The Problem This Solves

You have ever done this:

```
my_tool.py
my_tool_v2.py
my_tool_v2_fixed.py
my_tool_v2_fixed_FINAL.py
my_tool_v2_fixed_FINAL_actually_final.py
```

That is version control by hand. It is worse than it looks — which "final" is the one that works?

Git solves this. One file. All the history. Every version recoverable.

---

## What Git Does

Git takes **snapshots** of your project over time.

Each snapshot is called a **commit**. A commit contains:
- All the files in your project at that moment
- A timestamp
- Your name
- A short message describing what changed

You can go back to any commit at any time. You never lose work unless you choose to delete it.

---

## The Three-Zone Model

```
Working directory     Staging area       Repository
(what you edit)       (what you plan     (permanent
                       to commit)         history)

   [edit files]  →   [git add]   →   [git commit]
```

- **Working directory**: your actual files on disk — edit freely
- **Staging area**: a waiting room where you decide what goes into the next commit
- **Repository**: the permanent record, stored in the hidden `.git` folder

Why a staging area? So you can commit only some changes, not everything at once.

---

## Your First Four Commands

```bash
git init              # start tracking a folder
git status            # what has changed since last commit?
git add filename.py   # stage a file for the next commit
git commit -m "msg"   # take the snapshot
```

That is the entire daily workflow. You will do this loop dozens of times.

```bash
git log --oneline     # see your history
git diff filename.py  # see what changed since last commit
```

---

## Commits Are Save-States

In a video game: you save before a boss fight. If you die, you reload.

In Git: you commit before making a risky change. If you break something, you `git checkout` the previous commit.

```bash
# See your commits
git log --oneline

# Go back to any commit (replace abc1234 with the real hash)
git checkout abc1234

# Come back to the present
git checkout main
```

The key mental shift: **commit often**. Small commits are easier to undo than large ones.

---

## What Makes a Good Commit Message

Bad:  `"stuff"`
Bad:  `"fix"`
Bad:  `"final version"`

Good: `"Add error message when file is not found"`
Good: `"Fix word count to handle apostrophes"`
Good: `"Improve CSV output format for readability"`

**Rule of thumb:** complete the sentence — "If applied, this commit will: ___"

See `starter/commit_message_guide.md` for more examples.

---

## Branches: Safe Spaces to Break Things

A branch is a parallel copy of your project.

```
main:       A ── B ── C
                  \
experiment:        D ── E   ← break things here freely
```

When the experiment works, you merge it back into `main`.
When it doesn't work, you delete the branch — `main` is untouched.

```bash
git checkout -b experiment   # create + switch to new branch
# ... make changes, commit ...
git checkout main            # return to main (experiment changes disappear)
git branch -d experiment     # delete the branch
```

---

## GitHub: Your Code's Online Home

Git is local — it lives on your laptop.
GitHub is remote — it lives in the cloud.

**Why push to GitHub:**
- Backup: your laptop dies, your code survives
- Sharing: send anyone a URL to your project
- Collaboration: others can propose changes via pull requests
- Portfolio: show future employers or collaborators what you have built

```bash
git remote add origin https://github.com/YOU/repo.git
git push -u origin main
```

---

## Demo: Breaking Something and Recovering

*Watch me work through the lab scenario live.*

1. Initialize a repo, make two commits
2. Create an `experiment` branch
3. Delete the error handling code — the script gets worse
4. Commit the breaking change
5. Switch back to `main` — the file is restored instantly
6. Delete the experiment branch
7. Push to GitHub

---

## Lab Overview (45 min)

| Time | Activity |
|------|----------|
| 0–10 min | Part 1: `git init`, first commit |
| 10–20 min | Part 2: Make a change, commit it |
| 20–35 min | Part 3: Break on a branch, recover on main |
| 35–45 min | Part 4: Push to GitHub |

Reference files in `starter/`:
- `git_cheatsheet.md` — every command you need today
- `commit_message_guide.md` — how to write useful messages

---

## Key Takeaways

1. **Commits are save-states** — small, frequent commits give you more to recover from
2. **Branches are free** — create one before any risky change
3. **`git status` is your friend** — run it constantly; it tells you exactly where you are
4. **GitHub is your backup** — push at the end of every work session
5. **Git does not delete things** — almost everything is recoverable with the right command

---

## Before Next Week

- Push your project to GitHub if you have not yet
- Bring a CSV or spreadsheet file you would be willing to use in class (no sensitive data)
- Optional: browse other students' repos on GitHub — you can see their code!

**Next session:** Feb 23 — Working with files and data
