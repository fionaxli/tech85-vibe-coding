---
marp: true
theme: default
paginate: true
footer: "TECH 85 · Week 2 · Stanford Continuing Studies"
---

<!-- _class: lead -->
# Week 2: Turning an Idea into Clear Instructions
### TECH 85: Vibe Coding
Stanford Continuing Studies · Jan 26, 2027

---

## Agenda

1. Why specs matter before you start coding
2. What makes a prompt weak vs. strong
3. The iterative refinement loop
4. The "explain back" technique
5. Demo: building a tool from a spec live
6. Lab: write your spec and build your first personal tool

---

## Last Week's Takeaway

You ran the word counter and asked the AI to change something.

**What you actually did:**
- Described a desired behavior in plain English
- Let the AI translate that into code
- Ran the result

That is vibe coding. This week we make it *systematic*.

---

## The Problem with Jumping Straight In

Imagine asking a contractor to "renovate your kitchen" without a plan.

They show up Monday. You meant a new countertop. They ripped out the cabinets.

**Same thing happens with AI coding:**

- Vague request → AI makes assumptions
- You get code that does something, just not what you meant
- You spend more time correcting than building

The fix: write a one-page spec *before* you prompt.

---

## What Is a Spec?

A spec (specification) is a short written description of your tool, written before you build it.

**Five parts — one page total:**

| Part | Question it answers |
|------|-------------------|
| Goal | What does this tool do? (one sentence) |
| Inputs | What does it receive? (files, text, numbers) |
| Outputs | What does it produce or print? |
| Steps | What are the main operations? |
| Edge cases | What if something is missing or weird? |

Think of it as a recipe before you cook.

---

## Weak Prompt vs. Strong Prompt

**Weak:**
> "Make a tool that cleans up my notes."

**Strong:**
> "You are a Python developer helping a non-programmer. Write a single Python script that reads a plain-text file of meeting notes, removes any line starting with 'Action:', and saves the remaining lines to summary.txt. Use only Python's built-in standard library. Include a comment at the top showing the exact command to run it."

**The difference:** role, exact behavior, constraint (no extra libraries), output format.

---

## Anatomy of a Strong Prompt

Every good first prompt has four ingredients:

```
1. ROLE
   "You are a Python developer helping a non-programmer."

2. TASK  (paste your spec here)
   "Build a script that reads a CSV and prints totals per category."

3. CONSTRAINTS
   "One file. Use only Python's built-in standard library."

4. OUTPUT FORMAT
   "Give me the full script with a comment showing how to run it."
```

You do not have to memorize this. The spec template will remind you.

---

## The Iterative Refinement Loop

AI code is rarely perfect on try one — and that is fine.

```
Prompt
  ↓
Get first version
  ↓
Run it (or read it)
  ↓
Identify ONE thing that is wrong or missing
  ↓
Ask for that specific change
  ↓
Repeat (usually 2–3 loops)
```

**Key rule:** change one thing at a time. Asking for five changes at once produces messy code and confusing explanations.

---

## How to Ask for a Change

**Don't say:** "Fix the code."

**Do say:**

> "Right now the script prints every result on a single line.
> I would like it to print a numbered list instead, like:
>   1. first result
>   2. second result
> Here is the current code: [paste]"

Describe what **you see** and what **you want to see**. The AI figures out how.

---

## The "Explain Back" Technique

After getting code, before running it:

> "Explain what each section of this code does in plain English,
> as if I have never coded before."

**Why this helps:**
- You learn what the code actually does
- AI reasoning errors surface during the explanation
- You will catch problems like "wait, that deletes the original file?"

This is your safety check. Use it every time.

---

## Demo: Building the Meeting Note Formatter

*Watch me build the example tool from `example_spec.md` live.*

Steps I will follow:
1. Open the spec
2. Paste the framing message + spec into Claude
3. Copy the code, save to a file, run it
4. Show what happens when it fails
5. Paste the error back, get the fix
6. Use "explain back" on the final version

---

## What You Will Build Today

A personal tool based on your own idea from Week 1.

**By the end of lab you will have:**
- A filled-in one-page spec
- A working Python script that runs on a real file
- One completed refinement cycle

**Starter files in `starter/`:**
- `spec_template.md` — fill this in
- `example_spec.md` — see a completed example

---

## Lab Overview (45 min)

| Time | Activity |
|------|----------|
| 0–15 min | Part 1: Write your spec (use the template) |
| 15–35 min | Part 2: Prompt the AI, get code, run it |
| 35–45 min | Part 3: Make one refinement, use "explain back" |

No idea? Pick from the list in the README:
- Word count per file, expense totals, name reformatter, keyword finder

**Raise your hand** if you get stuck — do not wait more than 3 minutes.

---

## Key Takeaways

1. **Spec first, code second** — a one-page spec prevents most misunderstandings
2. **Four-part prompt** — role, task, constraints, output format
3. **One change at a time** — iterative refinement beats big rewrites
4. **Explain back** — always ask the AI to explain before you trust the code
5. **Errors are information** — paste error messages back; they are not failures

---

## Before Next Week

Run your tool on several different inputs. Find at least one case where it behaves unexpectedly or crashes. Write down:
- What input you gave it
- What happened
- What you expected

You will use this in Week 3 when we learn to read code safely.

**Next session:** Feb 2 — Reading and running AI-generated code safely
