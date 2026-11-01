---
marp: true
theme: default
paginate: true
footer: "TECH 85 · Week 8 · Stanford Continuing Studies"
---

<!-- _class: lead -->
# Week 8: Evaluating AI-Built Software, and Final Showcase
### TECH 85: Vibe Coding
Stanford Continuing Studies · Mar 9, 2027

---

## Agenda

1. What evaluation means (and what it doesn't)
2. Building a test set
3. The LLM-as-a-judge pattern
4. What "good enough" looks like in practice
5. Demo: running the eval harness live
6. Lab: evaluate your tool, fill in the scorecard
7. Final showcase — 3-minute demos

---

## We Have Been Here Before

Week 4: you wrote tests to check specific inputs and outputs.

That is the beginning of evaluation. Today we go further:

- **Larger test sets** — more cases, more coverage
- **Graded outputs** — not just pass/fail, but a quality score
- **LLM-as-a-judge** — use Claude to grade outputs that have no single right answer

The goal: not "does it work?" but "how well does it work, and where does it fail?"

---

## Evaluation Has Three Parts

**1. A test set**
A collection of inputs and what a good output looks like for each.

**2. A way to run them**
A script that feeds inputs to your tool and records outputs automatically.

**3. A way to grade them**
Compare outputs to expectations — by hand for small sets, or with AI for larger ones.

You can do all three with what you already know. The eval harness in today's starter files does parts 2 and 3 for you.

---

## Building a Good Test Set

You do not need 1000 test cases. For a personal tool, 10–20 well-chosen cases are enough.

**Cover four types of input:**

| Type | Example |
|------|---------|
| Happy path | Typical input the tool is designed for |
| Edge case | Empty input, very long input, unusual characters |
| Known failure | Input you already know causes a problem |
| Boundary case | Input right at the limit of what is expected to work |

**Rule:** if you have used your tool on a real input and something looked odd — add that input to your test set.

---

## LLM-as-a-Judge

For text outputs, there is no single "correct" answer. Two good summaries can look completely different.

Solution: use Claude as a grader.

```
Prompt:
"I am evaluating a text summarization tool.

Input: {input}
Expected output: {expected}
Actual output: {actual}

Rate the actual output on a scale of 1–5 for:
- Accuracy (does it get the facts right?)
- Completeness (does it cover the key points?)
- Conciseness (is it appropriately brief?)

Give a single overall score from 1–5 and explain your rating in one sentence."
```

---

## LLM-as-a-Judge: What to Watch For

**It is useful because:**
- Fast — grades dozens of outputs in seconds
- Understands nuance that `assert output == expected` cannot
- Can explain why something scored poorly

**It is imperfect because:**
- Scores vary slightly between runs
- It can be fooled by confident-sounding wrong answers
- It reflects Claude's biases

**Rule of thumb:** use LLM-as-a-judge for initial triage. For anything important, have a human look at low-scoring outputs.

---

## What "Good Enough" Looks Like

You do not need a perfect tool. You need an *honest assessment* of your tool.

A useful evaluation says:

> "My tool handles the 8 standard test cases with an average judge score of 4.2/5. It fails on inputs that contain only numbers (known limitation). It crashes on empty input — I would fix this next."

This is more valuable than saying "it works" — and more credible to anyone you show it to.

---

## Demo: Running the Eval Harness

*Watch me run `eval_harness.py` against the word counter.*

1. Show the test cases defined in the file
2. Run the harness: `python eval_harness.py`
3. Read the output table
4. Find the lowest-scoring case — look at why
5. Fill in one row of the scorecard from the output

---

## Today's Lab Files

| File | What it does |
|---|---|
| `eval_harness.py` | Runs test cases, grades with Claude, saves results |
| `eval_scorecard.md` | Template for your honest assessment |
| `presentation_template.md` | Guide for your 3-minute demo |

The harness is already working. Your job:
1. Add 5+ more test cases to the `TEST_CASES` list
2. Run it and read the results
3. Fill in the scorecard completely
4. Fill in the presentation template

---

## Lab Overview (30 min evaluation + 15 min demo prep)

| Time | Activity |
|------|----------|
| 0–10 min | Part 1a: Add test cases to eval_harness.py |
| 10–20 min | Part 1b: Run the harness, read results |
| 20–30 min | Part 1c: Fill in eval_scorecard.md |
| 30–45 min | Part 2: Fill in presentation_template.md, practice once |

Then: **Final showcase — everyone demos their tool**

---

## Your 3-Minute Demo

**Structure:**
- 30 sec — what the tool does and who it is for
- 90 sec — live demo (show it running on a real input)
- 60 sec — one thing that works well, one limitation, what you'd do next

**Tips:**
- Run your tool once before the demo to make sure it works
- Pick an input that shows the tool at its best
- Do not apologize for limitations — just name them clearly

No grade. Just share what you built.

---

## What You Have Built Over 8 Weeks

- Week 1: First AI-built tool, command-line Python script
- Week 2: Spec-first prompting, iterative refinement
- Week 3: Code review, virtual environments, safety checklist
- Week 4: Tests, tracebacks, the debug loop
- Week 5: Git, branches, GitHub
- Week 6: CSV/JSON, data cleaning, summaries
- Week 7: APIs, Anthropic SDK, multi-step agent
- Week 8: Evaluation, LLM-as-a-judge, demo

---

## Key Takeaways

1. **Evaluation is not the same as testing** — it measures quality across many inputs, not just correct/incorrect
2. **Build a test set from real inputs** — the cases that matter are ones you have actually encountered
3. **LLM-as-a-judge is fast but imperfect** — useful for triage; human judgment still matters
4. **"Good enough" is honest** — knowing your tool's limitations is more useful than pretending they do not exist
5. **Vibe coding is a skill** — you are better at it than you were 8 weeks ago; keep building

---

<!-- _class: lead -->
## Thank You

### TECH 85: Vibe Coding
**Instructor:** Fiona Li
**Stanford Continuing Studies · Winter 2027**

Keep building. The best way to get better is to make one more tool.
