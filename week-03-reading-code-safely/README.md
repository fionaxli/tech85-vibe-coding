# Week 3: Read, Test & Ship
**TECH 85 · February 3 · Stanford Continuing Studies**

## Session Goals

- Apply the review-refine-own cycle to your Project 1 code
- Write plain-English test cases and run them manually to verify your app works correctly
- Deploy your Project 1 app to Streamlit Cloud and get a live public URL

## Before Class

- Bring your Project 1 project folder with an `app.py` that runs — even if it is incomplete
- Make sure your code is in a GitHub repository (public or private). We will deploy from GitHub today. If you have not used GitHub before, create a free account at github.com and ask Claude Code to help you push your project.
- Have VS Code open with your project folder loaded

## Concepts (20 min)

- **The review-refine-own cycle:** When Claude Code writes code, your job is to (1) review it — read it top to bottom and ask Claude Code to explain anything you do not understand, (2) refine it — run it, catch anything wrong, ask Claude Code to fix it, (3) own it — be able to explain what it does to someone else. Do not ship code you cannot explain.
- **Reading AI code without writing it:** You do not need to understand every line. You need to understand what each section does. The key questions: What data goes in? What happens to it? What comes out? What could go wrong?
- **Four categories of risky operations:** File writes (can overwrite data), network requests (can send your data out), subprocess calls (can run system commands), environment variable reads (can expose secrets). Flag these when you see them.
- **Human test checklists:** Not pytest — a simple list of plain-English assertions you verify by hand. "When I add a habit, it appears in the list." "When I restart the app, my data is still there." These are more useful for beginners than automated tests because they force you to define what "correct" means.
- **Deploying with Streamlit Cloud:** Free, connects directly to your GitHub repository, gives you a real public URL in about two minutes. No server to manage, no command line on a remote machine. This is the deployment model you will use for all three projects.

## Lab (65 min)

### Part 1: Annotate your code with Claude Code's help (20 min)

Open `starter/safety_checklist.md`. Work through it with your Project 1 code open in VS Code.

1. Ask Claude Code to read your `app.py` and answer each question in the checklist.
   > "Read app.py and answer the questions in safety_checklist.md. Keep your answers concise — one sentence per item."
2. For any item Claude Code flags as risky, ask it to explain the risk in plain language.
3. For any section of code you do not understand, ask:
   > "Explain what lines 23–35 do in plain language. No jargon."
4. By the end of this part, you should be able to explain what your app does to a classmate in 60 seconds.

### Part 2: Write and run 5 test cases (15 min)

A test case is a plain-English sentence that describes something your app should do. You check it manually.

Write at least 5 test cases for your Project 1 app. Use this format:

```
[ ] When I [do something], the app [does something specific].
[ ] Example: When I add "Read for 20 minutes" as a habit, it appears in the list immediately.
[ ] Example: When I restart the app, all my habits are still there.
[ ] Example: When I try to add an empty habit name, the app does not crash.
[ ] Example: When I delete a habit, it is gone from the list.
[ ] Example: When I check off a habit twice, only one checkmark appears.
```

Run each test manually in your running app. Mark them pass or fail. For any failure:
> "My app fails this test: [paste the test case]. The actual behavior is [what actually happened]. Fix it."

### Part 3: Deploy to Streamlit Cloud (20 min)

Follow `starter/streamlit_deploy_guide.md` step by step. The guide covers every step from "make sure your code is in GitHub" through "share your URL."

The most common blocker is a missing `requirements.txt`. Ask Claude Code to generate it before you try to deploy:
> "Look at my project and generate a requirements.txt that lists all the Python packages it needs."

When your app is deployed, paste your public URL into the Canvas Week 3 thread.

### Part 4: 3-minute Project 1 demo (10 min)

Each student has 3 minutes. Show:
1. Your live app at its public URL
2. One thing it does that you are proud of
3. One thing you would add if you had more time

You are not being graded on completeness. You are practicing the demo format you will use in Week 6 and Week 8.

## Project Milestone

**Project 1 complete.** Submit to Canvas:
1. Your live Streamlit Cloud URL
2. A link to your GitHub repository
3. Two sentences: what your app does and what you learned building it

## Reading for Next Week

1. *Beyond Vibe Coding* — Chapter 5 (~15 min). This chapter covers testing concepts in more depth, including how to think about edge cases.

2. CMU 15-113 "Testing and Quality Assurance" notes — posted on Canvas (~15 min). Focus on the section on manual testing and test case design.
