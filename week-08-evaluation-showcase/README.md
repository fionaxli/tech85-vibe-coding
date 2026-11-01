# Week 8: Evaluating AI-Built Software, and Final Showcase

**Session:** Tue Mar 9, 2027, 7:00–8:30 pm PT

## Goals

By the end of this session you will be able to:

- Explain what evaluation means for an AI-built tool
- Build a small test set and run it through your tool automatically
- Use the "LLM-as-a-judge" pattern to grade your tool's outputs with Claude
- Give a 3-minute demo of the tool you built during this course

---

## Key Concepts

### What evaluation means

Building a tool is not the same as knowing whether the tool is good. Evaluation answers the question: "For the inputs I care about, does my tool produce outputs that are correct and useful?"

Evaluation has three parts:
1. **A test set** — a collection of inputs and the correct answers for them
2. **A way to run them** — a script that feeds each input to your tool and records the output
3. **A way to grade them** — comparing outputs to expected answers, either by hand or with AI

### Building a test set

A test set does not need to be large. For a personal tool, 10–20 well-chosen test cases tell you a lot. Good test cases cover:

- **Happy path** — typical inputs that should work
- **Edge cases** — empty input, very long input, inputs with special characters
- **Known failures** — inputs you already know cause problems (from Weeks 3–4)

Your test set is just a list of input/expected-output pairs. You can store them in a Python list, a CSV, or a JSON file.

### LLM-as-a-judge

For some outputs — especially text summaries or open-ended answers — there is no single "correct" answer. Two summaries can both be good. You need a grader that understands nuance.

The "LLM-as-a-judge" pattern uses Claude to grade your tool's outputs by giving it a rubric:

```
Prompt to Claude:
"I am evaluating a summarization tool. Here is the input, the expected output,
and the tool's actual output. On a scale of 1–5, rate the actual output on:
accuracy, completeness, and conciseness. Explain your rating briefly."
```

This is not a perfect evaluation method. But it is useful, fast, and good enough for assessing a personal tool.

### What "good enough" looks like

You do not need a 100% pass rate. You need to understand where your tool works well and where it struggles. A useful evaluation report says:

- "My tool handles the 8 standard test cases correctly."
- "It fails on inputs with special characters — I know about this and it is a known limitation."
- "The LLM judge rated its summaries an average of 4.1/5 on accuracy."

This is more valuable than vague confidence that "the tool works."

---

## Lab: Evaluate Your Tool and Prepare Your Demo

This lab has two parts: evaluation (30 min) and demo prep (15 min).

### Part 1 — Run the evaluation harness (30 min)

You will run a mini-evaluation on the word counter from Week 1/4, or on your own tool from Week 2.

#### 1a. Build a test set (10 min)

1. Open `starter/eval_scorecard.md` and read the rubric.
2. In `starter/eval_harness.py`, find the `TEST_CASES` list. It has 5 examples already — add at least 5 more based on inputs you have actually tried with your tool.
   - If using the word counter: add test cases with edge-case inputs (empty string, all common words, very long text, text with numbers)
   - If using your own tool: add inputs that cover your tool's range

3. For each test case, fill in the `expected` field. This is what you would want the output to look like for a good tool. It does not have to be exact — for text outputs, write a description of what a good answer looks like.

#### 1b. Run the harness (10 min)

4. Make sure your Anthropic API key is set (from Week 7 setup).
5. Run the eval harness:
   ```bash
   python eval_harness.py
   ```
6. The harness will run each test case through the function and use Claude to grade each output. A summary table will be printed and saved to `eval_results.txt`.

7. Read the output. For any test case graded below 3/5, look at the input and output and ask: "What went wrong?"

#### 1c. Fill in the scorecard (10 min)

8. Open `starter/eval_scorecard.md` and complete every section. Use the eval harness results plus your own judgment.
9. In the "What I would do next" section, write at least one concrete improvement you would make if you had more time.

### Part 2 — Prepare your demo (15 min)

Your demo should be exactly 3 minutes. Use `starter/presentation_template.md` as your guide.

10. Open `presentation_template.md`. Fill in each section.
11. Practice out loud once (yes, really — it makes a difference).
12. Make sure your tool runs on your laptop without errors. Run it once right now to confirm.

**Demo format:**
- 30 seconds: what the tool does and who it is for
- 90 seconds: live demo — show it running on a real input
- 60 seconds: what works well, one limitation, what you would do next

There is no grade on the demo. The goal is to share what you built.

---

## Expected Outputs

By the end of lab you should have:

- A completed `eval_scorecard.md` with honest ratings
- `eval_results.txt` showing output from the harness run
- A filled-in `presentation_template.md` you can use to guide your demo
- A live demo that runs without errors

---

## If Something Goes Wrong

| Problem | What to do |
|---|---|
| `eval_harness.py` crashes on import | Make sure the function you are testing is importable. Check the `FUNCTION_TO_TEST` variable at the top of the file. |
| Claude's grades seem inconsistent | LLM-as-a-judge is not perfectly consistent — that is expected. Look at the reasoning, not just the number. |
| Your tool crashes on one of the test inputs | Note it in your scorecard as a known failure and describe the input. Crashing on edge cases is normal at this stage. |
| You have not finished your Week 2 tool | Use the word counter from Week 1 for the evaluation. Your demo can describe what you planned to build. |
| You are nervous about the demo | That is also normal. Everyone in the room is in the same position. Focus on showing something real that works. |

---

## Congratulations

You have reached the end of TECH 85: Vibe Coding.

Over eight weeks you have:
- Built your first AI-assisted tool
- Learned to write clear specs and prompts
- Reviewed and run code safely
- Written tests and debugged failures
- Used version control with Git and GitHub
- Worked with real-world data files
- Built a web-connected agent
- Evaluated your own tool's reliability

These skills compound. Each project you build from here will be faster, cleaner, and more intentional than the last.

## Slides

See `slides.md` in this folder (also posted in Canvas).
