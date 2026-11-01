---
marp: true
theme: default
paginate: true
footer: "TECH 85 · Week 8 · Stanford Continuing Studies"
---

<!-- _class: lead -->
# Week 8: Demo Day
### TECH 85: Vibe Coding
Stanford Continuing Studies · March 10

---

## Agenda

1. The course arc: 8 weeks in review
2. What evaluation means — and why it matters
3. LLM-as-a-judge
4. AI ethics and IP: three questions
5. The golden rules of vibe coding
6. What is next
7. Eval exercise (15 min) + ethics lightning talk (5 min)
8. Capstone demos

---

## 8 weeks in review

| Week | What you learned | What you built |
|---|---|---|
| 1 | The vibe coding mindset, agent loop | Modified word_counter.py |
| 2 | Context engineering, BRIEF.md, CLAUDE.md | Project 1 scaffold |
| 3 | Review-refine-own, test checklists, deploy | Project 1 live at Streamlit Cloud |
| 4 | Claude Code as agent, Git checkpoints, debugging | Project 1 with Git history |
| 5 | SQLite, schema design, agent-ready repos | Project 2 with database |
| 6 | APIs, .env safety, security mindset | Project 2 with live API |
| 7 | Plan-first, task decomposition, MCP | Capstone launched |
| 8 | Evaluation, ethics, what is next | Capstone demo |

Three real deployed projects. From zero to full-stack in 8 weeks.

---

## What evaluation means

When you demo a tool, you pick the case that works. That is a demo, not an evaluation.

An evaluation is different: you define a set of inputs with known expected outputs, run the tool on all of them, and check the results honestly.

**A test set for a habit tracker might look like:**

| Input | Expected output | Pass? |
|---|---|---|
| Add "Read for 20 min" | Habit appears immediately | |
| Restart the app | All habits still there | |
| Delete "Meditate" | Habit removed from list | |
| Add an empty habit | Error message, no crash | |
| Check off a habit | Streak increments by 1 | |

If 4/5 pass, you know your tool is 80% reliable. That is useful information.

---

## LLM-as-a-judge

For tasks where "correct" is hard to define — summaries, recommendations, creative output — you can use an LLM to evaluate your tool's output.

**The pattern:**

```
System prompt: "You are an evaluator. Rate this response 1–5 on:
accuracy, completeness, and clarity. Explain your score."

User input: "Query: [the input]
Expected behavior: [what the app should do]
Actual output: [what the app produced]"
```

The LLM reads the output against the expected behavior and gives you a score with an explanation.

This is not perfect — LLMs have biases and can be fooled. But it is far better than "I ran it and it seemed fine."

`starter/eval_harness.py` implements a simple version of this pattern.

---

## AI ethics and IP: what the law says

**The current legal landscape (as of 2026):**

- In the United States, copyright generally requires human authorship. Purely AI-generated content without meaningful human creative input may not be protectable.
- The key phrase: "meaningful human creative input." If you directed the work, made substantive decisions, and shaped the output, you have a stronger claim.
- This area of law is actively evolving. Multiple court cases are pending that will clarify things further.

**The practical implication for you:**
If you can articulate why you made the decisions you made — what you asked for, how you refined it, what you changed — you are in a much stronger position than someone who pressed a button and shipped the result.

Being the director, not just the executor, is both a legal and an ethical posture.

---

## AI ethics and IP: what the community norms say

**Disclosure is the emerging norm.**

In software:
- "Built with Claude Code" in a README is becoming standard practice
- Job applicants who describe their AI-assisted workflow clearly are treated more favorably than those who obscure it
- Open source projects are developing norms around AI-generated contributions

**What you should do:**
- Be honest about what tools you used
- Be able to explain what you built and why you made the decisions you made
- Do not claim more than you contributed
- Do not hide less than you contributed

The community is still forming these norms. You are part of forming them.

---

## AI ethics and IP: responsible disclosure

**Three practical rules:**

1. **Disclose the tools.** Say "I built this with Claude Code" the same way you would say "I built this with React" or "I used a library for the charts."

2. **Own your code.** If you cannot explain what your code does, do not deploy it somewhere the failure could harm someone. The review-refine-own cycle is not just a learning exercise — it is an ethical practice.

3. **Respect others' data.** If your app processes other people's data (even your own colleagues' emails), apply the same standards you would want applied to your data.

None of this requires perfect knowledge. It requires honest effort and a commitment to understand what you ship.

---

## The golden rules of vibe coding

These are the principles that separate someone who builds things that work from someone who produces impressive demos that break in production.

1. **Write the BRIEF before you build.** Vague direction produces vague results.
2. **Review before you ship.** Do not deploy code you cannot explain.
3. **Commit before every big change.** Git is your safety net. Use it.
4. **Describe bugs precisely.** "When I do X, I expect Y, but I get Z."
5. **Ask for a plan on complex tasks.** Review the plan before executing.
6. **Secrets go in .env.** Never in code. Never in prompts.
7. **CLAUDE.md is your memory.** Keep it updated.
8. **Test the edge cases.** The demo case always works. The edge case is where tools fail.

---

## What is next

**Keep building.** The best way to get better is to have a project. One real thing you are building beats a hundred tutorials.

**Follow the field.** This space moves fast. The Anthropic release notes, the Claude Code changelog, and the CS146S materials at [themodernsoftware.dev/fall2025](https://themodernsoftware.dev/fall2025) are good signals.

**The skills transfer.** Context engineering, precise communication, systematic debugging, Git discipline — these matter regardless of which AI tool you use next year. The tools will change. The discipline will not.

**Share your work.** The best thing you can do with a project you are proud of is publish it and write about it. Talk about what you built, why you built it, and what Claude Code was and was not good at. This contributes to a community that is still figuring this all out.

---

## Demo format — one more time

You have 4 minutes. 3 to demo, 1 for questions.

1. Open your live URL (15 sec)
2. One sentence: what it does (20 sec)
3. Demo the core feature — make it real, show it working (90 sec)
4. One prompt you had to iterate on (30 sec)
5. One bug you fixed (25 sec)
6. Say your URL out loud (10 sec)

You are not being graded on completeness. You are being graded on honesty, clarity, and showing something real.

---

## Thank you

You came to this course with no programming background. You are leaving with three deployed applications, a repeatable workflow for building with AI, and a set of mental models that will serve you regardless of which tools exist in two years.

The field is young. The norms are still forming. The people who will shape it are the ones who are building seriously and thinking carefully — which is exactly what this course asked you to do.

Good luck. Build something real.

**Fiona Li · TECH 85 · Stanford Continuing Studies**
