---
marp: true
theme: default
paginate: true
footer: "TECH 85 · Week 2 · Stanford Continuing Studies"
---

<!-- _class: lead -->
# Week 2: Context Engineering & Your BRIEF
### TECH 85: Vibe Coding
Stanford Continuing Studies · January 27

---

## Agenda

1. Recap: Week 1 takeaways
2. Why context is the new source code
3. The four-component model of a great context
4. Common anti-patterns (with before/after examples)
5. BRIEF.md: your spec artifact
6. CLAUDE.md: giving the agent memory
7. Lab overview + Project 1 launch

---

## Recap: where we are

Last week: you ran an AI-generated tool and modified it.

You experienced the agent loop firsthand. You saw that Claude Code takes real actions — it edits files, runs code, reports back.

This week: we go one level deeper.

**The single biggest factor in whether Claude Code builds what you want:**
the quality of the context you give it.

Not your technical knowledge. Not the language you pick. The context.

---

## Context engineering: not just "prompting"

"Prompting" sounds like a one-shot question. You ask, it answers.

**Context engineering** is a discipline. You are designing the full information environment the AI works in:

- What is the goal?
- What are the constraints?
- What does "done" look like?
- What should it avoid?
- What files or examples should it consider?

A great context takes 10–15 minutes to write. It saves hours of back-and-forth.

A weak context produces correct-looking code that does the wrong thing.

---

## The four components of a great context

| Component | Question it answers | Example |
|---|---|---|
| **Goal** | What are we building? | "A Streamlit app that lets me log daily habits" |
| **Constraints** | What must / must not happen? | "Must work offline. No paid APIs. Use SQLite." |
| **Example of done** | What does success look like? | "I can add a habit, check it off, and see a 7-day streak." |
| **Tone / style** | How should the output look or feel? | "Simple, no jargon. One screen. Mobile-friendly." |

Every weak prompt is missing at least one of these.

Add all four and Claude Code knows what it is building, what the limits are, and how to know when it is finished.

---

## Anti-pattern #1: the vague goal

**Before:**
> "Build me a productivity app."

Claude Code will build something. It might be beautiful. It will almost certainly be wrong.

**After:**
> "Build a Streamlit app that shows me a list of tasks I add each day. Each task has a title and a done/not-done checkbox. When I check off a task, it moves to the bottom of the list. No login required. Use SQLite to store tasks."

What changed: specific domain (tasks), specific behavior (checkbox, reorder), specific constraints (no login, SQLite), implied done condition (tasks persist across sessions).

---

## Anti-pattern #2: missing constraints

**Before:**
> "Make the dashboard look better."

"Better" is unmeasurable. Claude Code will guess — and probably add things you did not ask for.

**After:**
> "Redesign the dashboard layout so the most recent entry appears at the top. Use a two-column layout on desktop (chart on the left, data table on the right). Keep the current color scheme. Do not add any new features — layout changes only."

What changed: measurable goal (most recent at top), specific layout (two-column), explicit scope limit (no new features), explicit constraint (keep colors).

---

## Anti-pattern #3: no example of done

**Before:**
> "Fix the bug in my code."

What bug? Claude Code will look — and may "fix" something that was not broken.

**After:**
> "When I run `python app.py` and type 'quit' at the prompt, the app crashes with this error: `IndexError: list index out of range`. The expected behavior is that typing 'quit' exits the app cleanly. Here is the relevant function: [paste the function]."

What changed: exact error message, exact trigger, explicit expected behavior, relevant code attached.

---

## The BRIEF.md format

A BRIEF.md is a one-page project specification you write before asking Claude Code to build anything.

```markdown
# Project BRIEF: My Habit Tracker

## What I'm building
A simple Streamlit app for tracking daily habits...

## Core features (must-have)
- Add and remove habits
- Check off habits each day
- See a 7-day streak per habit

## Out of scope (not building this)
- User accounts or login
- Mobile app

## Example interaction
Input: I type "Drink water" and click Add
Output: "Drink water" appears in my habit list with a checkbox

## Technical constraints
- Language: Python 3.10+, UI: Streamlit, Data: SQLite

## Done means...
- I can add a habit and it appears immediately
- Checked habits are still checked after I restart the app
```

---

## Why "out of scope" matters

The most overlooked section of any spec.

If you do not tell Claude Code what you are NOT building, it will make decisions for you. Sometimes those decisions are fine. Often they are not.

Common examples of scope creep without an "out of scope" section:
- Claude Code adds user authentication when you just wanted a simple personal tool
- It adds a REST API when you just wanted a local script
- It uses a cloud database when you just wanted a local file

Write "out of scope" every time. It takes 30 seconds and saves significant cleanup.

---

## CLAUDE.md: giving the agent memory

Every new Claude Code session starts fresh. It does not remember last week's conversation.

`CLAUDE.md` is the fix. Put this file in your project folder. Claude Code reads it automatically every time it opens your project.

What to put in it:
- Two-sentence project summary
- Tech stack (language, UI, database, key libraries)
- File structure
- Coding conventions ("keep functions small," "never hardcode keys")
- Known issues the agent should know about

Think of it as the briefing you give a new developer who is joining your project mid-stream.

---

## BRIEF.md vs. CLAUDE.md

They are different artifacts that serve different purposes.

| | BRIEF.md | CLAUDE.md |
|---|---|---|
| **Purpose** | Spec for what to build | Ongoing memory for the agent |
| **Written** | Before you start | As you build, keep it updated |
| **Length** | 1 page | Half a page to 1 page |
| **Audience** | Claude Code (and you) | Claude Code (every session) |
| **Lives in** | Your course folder | Your project's root folder |

The BRIEF.md is the blueprint. The CLAUDE.md is the handbook.

---

## Project 1: launched today

Three track options. Pick one, or bring your own.

**Track A — Daily Habit Tracker**
A Streamlit app that lets you log habits, check them off daily, and see a streak. Stored in SQLite. No login required.

**Track B — Reading List Manager**
A Streamlit app where you add books, tag them (want to read / reading / done), write notes, and search your list.

**Track C — Bring your own**
You have an idea from Week 1. Today you write the BRIEF and commit to it.

By end of class: BRIEF.md written, project folder scaffolded, CLAUDE.md in place.

---

## Lab overview

**What you are doing today (65 min)**

| Part | Time | What you do |
|---|---|---|
| Part 1 | 15 min | Critique 3 weak prompts, rewrite them using the four-component model |
| Part 2 | 20 min | Write your BRIEF.md using the template |
| Part 3 | 20 min | Give your BRIEF.md to Claude Code, watch it scaffold your project |
| Part 4 | 10 min | Add and polish a CLAUDE.md in your project folder |

Templates in `starter/`: `BRIEF_template.md`, `example_BRIEF.md`, `CLAUDE_md_template.md`

---

## Key takeaways

- Context engineering is the discipline of designing the full information environment for an AI agent
- The four components: goal, constraints, example of done, tone/style
- Every weak prompt is missing at least one of these
- BRIEF.md is your spec artifact — write it before you build
- CLAUDE.md gives Claude Code persistent memory of your project
- "Out of scope" is the most overlooked section — write it every time

---

## Reading for next week

**Before Wednesday, February 3:**

1. *Beyond Vibe Coding* — Chapters 3 and 4 (~25 min). Chapter 4 introduces the review-refine-own cycle you will practice in Week 3's lab.

2. Stanford CS146S Week 2 notes at [themodernsoftware.dev/fall2025](https://themodernsoftware.dev/fall2025) (~5 min)

**Also:** Make progress on Project 1. Come to Week 3 with something running — even if it is just the scaffolded skeleton. Week 3 is your first demo day.
