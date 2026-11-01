# Week 4: Testing and Debugging with AI

**Session:** Tue Feb 9, 2027, 7:00–8:30 pm PT

## Goals

By the end of this session you will be able to:

- Write simple tests that verify a function produces the right output for a given input
- Read a Python traceback and identify which line caused an error
- Guide an AI assistant through the debug loop: run → read error → ask AI → fix → repeat

---

## Key Concepts

### What is a test?

A test is a small piece of code that checks whether your tool does the right thing for a specific input. The idea is simple: you call a function with an input you know, and you check that the output matches what you expected.

```python
# Example test: checking word_counter
result_total, result_top = count_words("the cat sat on the mat")
assert result_total == 6, f"Expected 6 words, got {result_total}"
```

`assert` means: "I am asserting this is true. If it is not, stop and show me an error." That error message is your test failure — it tells you exactly what went wrong.

### What tests are for

Tests are not about finding bugs immediately. They are about confidence. When you write a test for behavior you care about, you can change the code later and run the test again to make sure you did not break it. This is especially important when using AI to make changes: the AI might fix one thing and accidentally break another.

### Reading a traceback

When Python crashes, it prints a "traceback" — a stack of function calls leading to the error. It looks frightening but always has the same structure:

```
Traceback (most recent call last):
  File "word_counter.py", line 28, in main     ← where it was when things went wrong
    total, top = count_words(text)
  File "word_counter.py", line 17, in count_words  ← where the error actually is
    words = re.findall(pattern, text.lower())
TypeError: expected string or bytes-like object  ← the actual error message
```

**Read from bottom to top.** The last line is the error. The line above it is where in the code the error occurred. That is where you start.

### The debug loop

```
1. Run the script (or the tests)
2. Read the error message — note the line number and the error type
3. Copy the error and relevant code, ask the AI:
   "I got this error on line N. Here is the code. What is wrong and how do I fix it?"
4. Apply the fix
5. Run again
6. Repeat until it passes
```

Most bugs are fixed in one or two loops. If you are on loop five and still stuck, ask the AI to explain the code from scratch — sometimes the bug is in your understanding, not the code.

---

## Lab: Tests, Bugs, and Fixes

This lab uses two starter files: `test_word_counter.py` (a test file with some tests written and some left for you) and `buggy_word_counter.py` (the word counter with three deliberate bugs). Your job is to find and fix all three bugs using the test suite and AI help.

### Part 1 — Run the existing tests (10 min)

1. Open `starter/test_word_counter.py` in VS Code.
2. Read the tests that are already written (the ones that do not say `# TODO`). For each one, answer in your head: "What input is this testing? What output am I expecting?"
3. Open a terminal. Activate your virtual environment if you have one, or just use your normal Python:
   ```bash
   cd /path/to/week-04-testing-debugging/starter
   python -m pytest test_word_counter.py -v
   ```
   If `pytest` is not installed:
   ```bash
   pip install pytest
   ```
4. Read the output. Some tests will pass (shown with a green dot or `PASSED`). Some will fail. Note which ones fail.

   **If you see `ImportError: cannot import name 'count_words'`**, make sure both files are in the same folder.

### Part 2 — Read the failures and debug (20 min)

5. For each failing test, find the corresponding line in `buggy_word_counter.py`.
6. Copy the failing test output (the full error message), the test code, and the relevant function from `buggy_word_counter.py`. Paste all three into Claude and ask:
   > "This test is failing with this error. Here is the test code and the function it is testing. What is the bug and how do I fix it?"

7. Apply the fix to `buggy_word_counter.py`. Run the tests again.
8. Repeat until all existing tests pass.

   There are three deliberate bugs. Hint: they are all in `count_words()`. You do not need to modify `main()`.

### Part 3 — Write the missing tests (10 min)

9. In `test_word_counter.py`, find all the sections marked `# TODO`. Complete each one.
10. Run the tests again after each new test you add. If a new test fails, debug it the same way as before.
11. When all tests pass (including your new ones), run the tests one final time and screenshot or copy the output showing all green.

### Part 4 — Try breaking it on purpose (5 min)

12. This step is optional but instructive. In `buggy_word_counter.py`, introduce a new bug yourself — for example, delete the `.lower()` call on one line, or change the `5` in `most_common(5)` to `0`.
13. Run the tests. Watch them fail. This is what it feels like to catch a regression — a change that broke something that used to work.
14. Undo your change (Ctrl+Z or Cmd+Z). Run the tests. They pass again. That is the power of a test suite.

---

## Expected Outputs

By the end of lab you should have:

- All existing tests in `test_word_counter.py` passing
- The three bugs in `buggy_word_counter.py` found and fixed
- At least two new tests written (the `# TODO` items)
- A terminal showing `X passed` with no failures

---

## If Something Goes Wrong

| Problem | What to do |
|---|---|
| `command not found: pytest` | Run `pip install pytest` first |
| `ImportError: cannot import name 'count_words'` | Make sure `test_word_counter.py` and `buggy_word_counter.py` are in the same folder and you ran `python -m pytest` from that folder |
| The AI's fix introduces a new failure | Paste the new failure back to the AI — that is the normal debug loop |
| You cannot figure out which line has the bug | Ask the AI: "Look at this function line by line and tell me if any line looks wrong" |
| All tests pass but the output looks wrong | Add a new test for the case that looks wrong — if there is no test for it, the test suite cannot catch it |

---

## Before Next Week

Save your fixed `buggy_word_counter.py` — renamed to something meaningful, like `word_counter_fixed.py`. In Week 5 we put code under version control, and this file is a good example of "code with a history."

Write down: what would happen if you ran your tool from Week 2 with a completely empty file? With a file full of numbers? Those are edge cases — we will test for them in a future exercise.

## Slides

See `slides.md` in this folder (also posted in Canvas).
