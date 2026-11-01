---
marp: true
theme: default
paginate: true
footer: "TECH 85 · Week 3 · Stanford Continuing Studies"
---

<!-- _class: lead -->
# Week 3: Read, Test & Ship
### TECH 85: Vibe Coding
Stanford Continuing Studies · February 3

---

## Agenda

1. Recap: BRIEF.md, CLAUDE.md, Project 1 status
2. The review-refine-own cycle
3. Reading AI code without writing it
4. Four categories of risky operations
5. The test checklist approach
6. Streamlit Cloud deployment walkthrough
7. Lab + Project 1 demo format

---

## Recap: the context engineering work pays off here

Last week you wrote a BRIEF.md and had Claude Code scaffold your project.

This week you face what everyone faces after AI-generated code: **it runs, but you are not sure it is right.**

The review-refine-own cycle is your answer to that situation.

It is not about memorizing syntax. It is about asking good questions until you understand what your code does.

---

## The review-refine-own cycle

**Review:** Read it. Ask Claude Code to explain every section you do not understand. You should be able to describe what each function does in one sentence.

**Refine:** Run it. Deliberately try to break it. Find the cases where it does not behave the way you expected. Ask Claude Code to fix them. Repeat until it passes your test checklist.

**Own:** Be able to explain it. If you cannot explain what your app does to a classmate in 60 seconds, you do not own it yet. Go back to Review.

This cycle takes longer than just shipping. It is also the difference between a tool you trust and a tool that surprises you at the worst moment.

---

## Reading code top-down

You do not need to understand every line. Here is the reading strategy that works for non-programmers:

**Step 1: Find the entry point.** Where does the code start? In a Streamlit app, it is the last few lines — the call to `st.run()` or the `if __name__ == "__main__"` block.

**Step 2: Follow the data.** What goes in? (user input, a file, an API call) What happens to it? (a function, a loop, a database write) What comes out? (what gets displayed, stored, or returned)

**Step 3: Ask about anything you do not recognize.** In Claude Code:
> "What does this line do? `conn = sqlite3.connect('habits.db')`"

You are reading for understanding, not for memorization.

---

## Four categories of risky operations

When reviewing AI-generated code, look for these four things. They are not necessarily wrong — but they are worth understanding.

| Category | What to look for | Question to ask |
|---|---|---|
| **File writes** | `open(path, 'w')`, `os.remove()` | What file is being modified? Could this overwrite something important? |
| **Network requests** | `requests.get()`, `requests.post()` | What URL is being called? What data is being sent? |
| **Subprocess calls** | `subprocess.run()`, `os.system()` | What command is being run? Who can trigger it? |
| **Secrets** | `os.getenv()`, `.env` access | Is the key being read safely? Is it being logged anywhere? |

Ask Claude Code: "Read my app.py and flag any file writes, network requests, subprocess calls, or places where secrets are used."

---

## The test checklist: simpler than it sounds

Automated tests are useful. They are also a new skill to learn.

A human test checklist is simpler and more useful for right now:

```
[ ] When I add a habit, it appears in the list immediately.
[ ] When I refresh the page, my habits are still there.
[ ] When I restart the app, my habits are still there.
[ ] When I delete a habit, it disappears from the list.
[ ] When I try to add an empty habit name, the app doesn't crash.
[ ] When I check off a habit, the streak count updates correctly.
```

Run each one manually. Mark pass or fail. For any failure, bring it to Claude Code with the exact behavior you observed.

The skill here is **defining what correct looks like before you run the test.**

---

## Streamlit Cloud: how it works

Streamlit Cloud is a free hosting service from the makers of Streamlit. It:
- Connects to a GitHub repository
- Reads your `app.py` (or whatever main file you specify)
- Installs your `requirements.txt` automatically
- Gives you a public URL: `your-project.streamlit.app`

Deploys in about 2 minutes. No server to manage. No command line on a remote machine. When you push a new commit to GitHub, the deployed app updates automatically.

This is your deployment target for all three projects.

---

## Deploying to Streamlit Cloud: the steps

1. **Make sure your code is in GitHub.** Public or private — both work.
2. **Make sure `requirements.txt` is in your repo root.** Ask Claude Code to generate it if it is not there: *"Generate a requirements.txt for my project."*
3. **Go to [share.streamlit.io](https://share.streamlit.io).** Sign in with your GitHub account.
4. **Click "New app."** Select your repository, your branch (usually `main`), and your main file path (usually `app.py`).
5. **Click Deploy.** Watch the logs. If it fails, the error is usually a missing package in `requirements.txt`.
6. **Share your URL.** Format: `https://your-app-name.streamlit.app`

Full step-by-step guide with troubleshooting in `starter/streamlit_deploy_guide.md`.

---

## Three most common deployment errors

**Error 1: `ModuleNotFoundError: No module named 'X'`**
A package in your code is not in `requirements.txt`. Add it: `echo "package-name" >> requirements.txt`, commit, push.

**Error 2: `FileNotFoundError: No such file or directory`**
Your code references a file by its local path (e.g., `open('data/notes.db')`). On Streamlit Cloud, relative paths work differently. Ask Claude Code: *"Fix any hardcoded file paths so they work on Streamlit Cloud."*

**Error 3: App runs but shows a blank screen**
Usually means your `app.py` runs but has no `st.` calls at the top level. Ask Claude Code: *"Add a simple st.title() call at the top of app.py to confirm it is loading."*

---

## The 3-minute demo format

Today and in Weeks 6 and 8, you have 3 minutes to demo your project. Here is the structure:

1. **Show the live URL** (15 sec) — open your browser, go to your app
2. **Explain what it does** (30 sec) — one sentence, like you are telling a friend
3. **Demo the core feature** (90 sec) — do the thing. Add an entry, check it off, show it persisting.
4. **Share one thing you are proud of** (30 sec) — a feature, a bug you fixed, a design decision
5. **Share one thing you would add next** (15 sec) — keep it specific

You will not be interrupted. Three minutes goes fast — practice once before class.

---

## Lab overview

**What you are doing today (65 min)**

| Part | Time | What you do |
|---|---|---|
| Part 1 | 20 min | Work through safety_checklist.md with Claude Code on your app.py |
| Part 2 | 15 min | Write 5 test cases; run them manually; fix any failures |
| Part 3 | 20 min | Deploy to Streamlit Cloud; paste your URL in Canvas |
| Part 4 | 10 min | 3-minute Project 1 demo |

---

## Key takeaways

- Review-refine-own: do not ship code you cannot explain
- Reading code means following the data — what goes in, what happens, what comes out
- Four risk categories to look for: file writes, network requests, subprocess calls, secrets
- Plain-English test checklists are the right testing tool for where you are right now
- Streamlit Cloud: free, deploys from GitHub, gives you a real public URL in 2 minutes
- The 3-minute demo is a skill — practice it before class

---

## Reading for next week

**Before Wednesday, February 10:**

1. *Beyond Vibe Coding* — Chapter 6 (~15 min). This chapter introduces the concepts around Git and version control for AI-generated code.

2. Make sure Git is installed before next class: open your terminal and type `git --version`. If you get a "command not found" error, install Git from [git-scm.com](https://git-scm.com) and let us know on Canvas.
