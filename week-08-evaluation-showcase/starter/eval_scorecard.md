# Evaluation Scorecard

**Student:** [Your name]
**Tool evaluated:** [Name of your tool — e.g., "Word Counter", "Meeting Note Formatter"]
**Date:** [Today's date]
**Session:** TECH 85 Week 8, Mar 9, 2027

---

## Section 1: Functionality

Rate each item on a scale of 1–5. Use the definitions below.

**Scale:**
- 5 = Works perfectly, no issues
- 4 = Works for most inputs with minor issues
- 3 = Works for some inputs but has notable problems
- 2 = Barely works; most inputs produce wrong results
- 1 = Does not work or crashes consistently

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Handles typical inputs correctly | | |
| Handles edge cases without crashing | | |
| Produces output in the expected format | | |
| Error messages are clear and helpful | | |
| Runs in a reasonable time (under 5 seconds for typical input) | | |

**Section 1 average:** _____ / 5

---

## Section 2: Evaluation Harness Results

Fill this in after running `eval_harness.py`.

| Metric | Your result |
|---|---|
| Total test cases run | |
| Average LLM judge score | / 5 |
| Number of cases scoring 4 or 5 (passed) | |
| Number of cases scoring 1 or 2 (failed) | |
| Lowest-scoring test case (label) | |
| Why did that case score low? | |

---

## Section 3: Known Limitations

List every input or situation where your tool does not work correctly. Be specific.

| Input / situation | What happens | Severity (Low / Medium / High) |
|---|---|---|
| | | |
| | | |
| | | |

If your tool has no known limitations (all test cases passed perfectly), explain how you verified this.

---

## Section 4: Code Quality

| Criterion | Score (1–5) | Notes |
|---|---|---|
| Code is organized into clearly-named functions | | |
| There is at least one comment explaining a non-obvious section | | |
| The script prints a useful error message when given bad input | | |
| You could explain what every function does to a classmate | | |

**Section 4 average:** _____ / 5

---

## Section 5: Safety (from Week 3)

| Question | Answer |
|---|---|
| Does your tool write or overwrite any files? If yes, which ones? | |
| Does your tool make any network calls? If yes, to where? | |
| Have you reviewed the imports and understand what each one does? | Yes / No |
| Is your API key (if any) stored in an environment variable, not in code? | Yes / No / N/A |

---

## Section 6: Overall Assessment

**What does this tool do well?**
(Write 2–3 sentences describing the tool's strengths. Be specific — "it handles edge cases" is vague; "it correctly handles empty files and files with only whitespace" is specific.)

>

**What is the most important limitation or failure mode?**
(Describe the one problem that would most often affect a real user.)

>

**What would you do next, with one more hour of work?**
(Be specific about one concrete improvement. "Make it better" is not enough.)

>

---

## Section 7: Reflection

Answer each question in 2–4 sentences.

**Which week's concepts were most useful when building this tool?**

>

**What was the hardest part of using AI to build software?**

>

**If you were starting over, what would you do differently?**

>

---

## Overall Scores Summary

| Section | Score |
|---|---|
| Section 1: Functionality | /5 |
| Section 2: Harness results (avg LLM score) | /5 |
| Section 4: Code quality | /5 |
| **Overall average** | **/ 5** |

---

*This scorecard is for your own reflection. There is no passing grade.*
*The goal is an honest picture of what you built and what you learned.*
