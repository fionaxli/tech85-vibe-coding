---
marp: true
theme: default
paginate: true
footer: "TECH 85 · Week 1 · Stanford Continuing Studies"
---

<!-- _class: lead -->
# Week 1: The Vibe Coding Mindset
### TECH 85: Vibe Coding
Stanford Continuing Studies · January 20

---

## Agenda

1. What vibe coding is — and where it came from
2. The agent loop: how Claude Code actually works
3. The 70% problem: what AI does vs. what you do
4. The director / reviewer / curator model
5. Programming with intent
6. Demo: Claude Code in action
7. Lab: your first tool, your first modification, your first CLAUDE.md

---

## Where did "vibe coding" come from?

In February 2025, Andrej Karpathy — co-founder of OpenAI, former Tesla AI lead — posted a thread describing a new way of working with AI tools:

> *"There's a new kind of coding I call 'vibe coding', where you fully give in to the vibes, embrace exponentials, and forget that the code even exists."*

He meant: describe what you want, let the AI write it, test whether it works, iterate.

The term caught on because it named something that was already happening. Millions of people were building real tools without learning to write code.

This course takes that idea seriously — and teaches you how to do it well.

---

## The agent loop

Claude Code is not a chatbot you type at. It is a **coding agent** — software that takes actions on your behalf.

Here is what happens when you give Claude Code a task:

```
You → "Add a sentence counter to word_counter.py"
        ↓
   Claude Code reads the file
        ↓
   Claude Code decides what to change
        ↓
   Claude Code writes the new code
        ↓
   Claude Code runs the script to verify it works
        ↓
   Claude Code reports back to you
```

**Model → Harness → Tools → Result → Repeat**

The model is the intelligence. The harness is the Claude Code software. The tools are file operations, terminal commands, web searches. Understanding this loop makes you a better director.

---

## The 70% problem

AI coding tools are astonishingly good at the first 70% of almost any task.

**What AI does brilliantly:**
- Writing code that follows known patterns
- Building standard features fast (forms, databases, APIs)
- Explaining what code does
- Finding bugs that match familiar error types
- Translating your intent into working syntax

**Where human judgment is irreplaceable:**
- Deciding what to build in the first place
- Recognizing when the output is subtly wrong
- Catching edge cases that do not fit the pattern
- Making privacy, security, and ethical calls
- Knowing when "good enough" is actually good enough

Your job is not to write code. Your job is to cover the 30%.

---

## Director · Reviewer · Curator

Think of yourself in three roles — not as a programmer.

**Director:** You decide what gets built. You describe the outcome you want, the constraints that matter, and what "done" looks like. The director sets the vision; the AI executes.

**Reviewer:** You read what the AI produces, check that it does what you asked, catch anything that looks wrong, and ask for corrections. You do not need to understand every line — you need to understand what the code does.

**Curator:** Over time you accumulate good prompts, good templates, good patterns. You keep the ones that work and discard the ones that do not. Your BRIEF.md and CLAUDE.md files are your curation artifacts.

---

## Programming with intent

Old model: write code step by step.
```python
words = []
for line in file:
    for word in line.split():
        words.append(word.lower())
counts = {}
for word in words:
    ...
```

New model: express the outcome you want.
```
"Read this text file and show me the 10 words that appear most often,
 ignoring common words like 'the' and 'and'. Output as a numbered list."
```

You are not describing *how* to build it. You are describing *what* you want and *what done looks like*. The AI handles the how.

This is harder than it sounds. Precision in English is a skill. You will practice it all term.

---

## What makes a good direction?

The difference between a weak and a strong direction is specificity.

| Weak | Strong |
|---|---|
| "Make it better" | "Show the count next to each word, sorted highest to lowest" |
| "Fix the bug" | "When I run this on an empty file, it crashes. Fix it so it prints 'No words found' instead." |
| "Add a feature" | "Add a button that clears all entries. Ask the user to confirm before clearing." |
| "Make it look nicer" | "Use a two-column layout: input on the left, results on the right. Keep it minimal." |

**Concrete + specific + with an example = Claude Code gets it right the first time.**

---

## Claude Code: not a chatbot

Claude Code is different from Claude.ai or ChatGPT in one important way: it takes actions.

It can:
- Create, read, edit, and delete files on your computer
- Run terminal commands (install packages, run your app, run tests)
- Search the web
- Read documentation

This is powerful. It is also why you stay in the director role — you review what it does before it does more.

Today's lab: you will see this in action. You will give Claude Code a modification task and watch it edit the file, run the script, and report back.

---

## The CLAUDE.md file

`CLAUDE.md` is a plain-text file you put in your project folder. It tells Claude Code about your project — so you do not have to re-explain it every session.

Think of it as the briefing document you give a new contractor:
- What this project does
- What language and tools it uses
- What rules to follow (never hardcode API keys, keep functions small)
- What to watch out for

The industry standard file is `CLAUDE.md` for Claude Code, `AGENTS.md` for other agents. Same idea: a file that primes the AI before it touches your code.

You will write a simple version today. You will fill it out properly in Week 2.

---

## Demo: Claude Code modifying word_counter.py

*[Live demo — instructor walks through:]*

1. Open Claude Code in terminal (`claude`)
2. Show the starter file in VS Code
3. Run the script: `python word_counter.py sample.txt`
4. Give Claude Code a modification task
5. Watch it read the file, make the change, run the script
6. Ask Claude Code to explain what it changed
7. Show the updated file in VS Code

Key observation: Claude Code edited the actual file on disk. It ran the script to verify. It reported back with an explanation. This is the agent loop in practice.

---

## Lab overview

**What you are doing today (65 min)**

| Part | Time | What you do |
|---|---|---|
| Part 1 | 10 min | Run word_counter.py on sample.txt — make sure your setup works |
| Part 2 | 25 min | Use Claude Code to make 3 modifications; ask it to explain each one |
| Part 3 | 10 min | Run the script on a text file of your own |
| Part 4 | 20 min | Start your CLAUDE.md for the project you want to build this term |

The goal is not to memorize anything. The goal is to get the feel of directing Claude Code and to leave with a project idea in your head.

---

## Key takeaways

- Vibe coding is a real skill: clear direction, careful review, honest testing
- Claude Code is an agent, not a chatbot — it takes actions, not just answers
- Your job covers the 30% AI cannot do: judgment, vision, verification
- The director / reviewer / curator model is how you stay in control
- CLAUDE.md is how you give Claude Code memory of your project
- Programming with intent means describing outcomes, not steps

---

## Reading for next week

**Before Wednesday, January 27:**

1. *Beyond Vibe Coding* — Chapters 1 and 2 (~25 min). Available free via Stanford library → O'Reilly Learning.

2. Andrej Karpathy's original "vibe coding" thread: [x.com/karpathy/status/1886192184808149190](https://x.com/karpathy/status/1886192184808149190) (~5 min)

**Also:** Come to Week 2 with a project idea. One sentence is enough: *"A tool that does X for me."* You will turn it into a formal BRIEF.md in the lab.
