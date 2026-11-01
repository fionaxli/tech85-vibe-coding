# Week 2: Context Engineering & Your BRIEF
**TECH 85 · January 27 · Stanford Continuing Studies**

## Session Goals

- Understand why context engineering — not just prompting — is the skill that makes everything else work
- Write a complete BRIEF.md for your Project 1 idea
- Use your BRIEF.md to have Claude Code scaffold your project and generate a CLAUDE.md

## Before Class

- Finish the Week 1 reading (Chapters 1–2 of *Beyond Vibe Coding*)
- Come with a project idea — one sentence is enough. Examples: "a habit tracker that shows me a streak," "a tool that summarizes my meeting notes," "a reading list with ratings."
- If you have not finished setting up Claude Code, do it now. Week 2 lab requires it.

## Concepts (20 min)

- **Context engineering vs. prompting:** "Prompting" suggests a one-shot question. Context engineering is a discipline — you are designing the full information environment the AI works in: the goal, the constraints, the examples, the tone, the file it should read, the format of its output. The quality of that context determines the quality of what you get back.
- **Anatomy of a great context:** Four components — (1) a clear goal, (2) explicit constraints, (3) a concrete example of what "done" looks like, (4) relevant tone or style guidance. Missing any one of these is the most common reason Claude Code goes off in the wrong direction.
- **BRIEF.md:** Your spec artifact. A one-page document that describes your project to a coding agent. Students write this in class; it becomes the seed of their CLAUDE.md. It forces you to be specific about what you are building before you ask Claude Code to build it.
- **CLAUDE.md / AGENTS.md:** The industry-standard way to tell an AI coding agent about a project. Put this file in your project root; Claude Code reads it automatically at the start of every session. This is how you give the agent memory.
- **Common prompt anti-patterns:** Vague goals ("make it better"), missing constraints ("something with a nice UI"), no example of done ("add some features"), contradictory instructions. Each of these has a specific fix.

## Lab (65 min)

### Part 1: Critique and rewrite weak prompts (15 min)

Below are three weak prompts. For each one: read it, identify what is wrong, then rewrite it using the four-component model (goal, constraints, example, tone).

**Weak prompt 1:**
> "Build me an app."

What is wrong: no goal, no constraints, no example, no scope. Claude Code will make something, but it will not be what you had in mind.

**Weak prompt 2:**
> "Make the dashboard look better and add some charts."

What is wrong: "better" is not defined, "some charts" does not specify what data, no constraints on time or complexity.

**Weak prompt 3:**
> "Fix the bug in my code."

What is wrong: no description of what the bug is, no error message, no indication of what the correct behavior should be.

Rewrite each one. Compare your rewrites with a neighbor. There is no single right answer — but a good rewrite will be at least twice as long as the original.

### Part 2: Write your BRIEF.md (20 min)

Open `starter/BRIEF_template.md`. Fill it out for your Project 1 idea. Take it seriously — this document will be the only instruction Claude Code gets when it starts building your project.

As you write, pay particular attention to:
- **"Done means..."** — this is the section most people leave vague. Write at least two concrete things you will check to know the project is working.
- **"Out of scope"** — if you do not write this section, Claude Code may add features you did not ask for.
- **"Example interaction"** — show the input and the expected output. This is worth more than a paragraph of description.

You can see a completed example in `starter/example_BRIEF.md`.

### Part 3: Scaffold your project with Claude Code (20 min)

1. Open Claude Code in your terminal.
2. Navigate to a new folder where you want your project to live (outside this repo).
3. Tell Claude Code to read your BRIEF.md:
   ```
   Read this BRIEF.md and scaffold a Python project for it. Create the main app.py file, a requirements.txt, and a CLAUDE.md that summarizes the project. Do not build the full app yet — just the skeleton with placeholder functions and comments.
   ```
4. Review what Claude Code created. Does the structure match your vision? Does the CLAUDE.md accurately describe your project?
5. Ask Claude Code to explain each file it created in one sentence.

**If Claude Code goes off in a direction you did not want:** Stop it immediately and say: *"That is not what I meant. Here is what I actually want: [be more specific]."* It is faster to redirect early than to fix a large wrong implementation.

### Part 4: Polish your CLAUDE.md (10 min)

1. Open the CLAUDE.md that Claude Code generated for your project.
2. Compare it to `starter/CLAUDE_md_template.md`.
3. Add anything that is missing: tech stack details, coding conventions, things to watch out for.
4. This file will live in your project folder all term. Keep it updated as your project evolves.

## Project Milestone

**Project 1 launched.** By the end of today's class you should have:
- A completed BRIEF.md for your Project 1 idea
- A project folder with a scaffolded app.py, requirements.txt, and CLAUDE.md
- A clear sense of which track you are building (Track A, B, or C)

Submit your BRIEF.md to Canvas before next class. We will review a few of them at the start of Week 3.

## Reading for Next Week

1. *Beyond Vibe Coding* — Chapters 3 and 4 (~25 min). Chapter 3 covers the context engineering concepts from today in more depth. Chapter 4 introduces the review-refine-own cycle you will practice in Week 3.

2. Stanford CS146S Week 2 notes at [themodernsoftware.dev/fall2025](https://themodernsoftware.dev/fall2025) (~5 min). Skim the section on spec-writing. Notice what a professional specification looks like vs. a student BRIEF.
