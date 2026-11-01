---
marp: true
theme: default
paginate: true
footer: "TECH 85 · Week 4 · Stanford Continuing Studies"
---

<!-- _class: lead -->
# Week 4: Testing and Debugging with AI
### TECH 85: Vibe Coding
Stanford Continuing Studies · Feb 9, 2027

---

## Agenda

1. What a test actually is
2. Why tests matter when using AI
3. Reading a traceback without panicking
4. The debug loop
5. Demo: catching a bug with a test
6. Lab: find and fix three deliberate bugs

---

## The Problem with "Looks Right"

You run your tool. It does not crash. The output looks reasonable.

Are you done?

**Not quite.**

What if:
- The word count is off by one in some edge case?
- The tool silently skips files with special characters?
- An AI edit last week accidentally changed the behavior?

"Looks right" is not the same as "is correct." Tests give you certainty.

---

## What Is a Test?

A test is a small piece of code that asks: **"If I give this function input X, do I get output Y?"**

```python
total, top_words = count_words("the cat sat on the mat")

assert total == 6
assert top_words[0][0] == "cat"  # most common non-trivial word
```

`assert` means: "I am asserting this is true. If it is not, crash loudly and tell me."

That crash is good news — it caught a bug before you ran the tool on your real data.

---

## Why Tests Matter *Especially* with AI

Every time you ask the AI to change your code, you take a small risk: the change might fix one thing and silently break another.

Without tests: you find out when the tool gives wrong results on real data — possibly too late.

With tests: you find out in 3 seconds, on your laptop, before anything matters.

**Tests are your regression net.** They catch the AI making something worse while trying to make something better.

---

## Three Kinds of Tests You Will Write

**1. Normal case** — does it work on typical input?
```python
total, top = count_words("hello world hello")
assert total == 3
```

**2. Edge case** — what about unusual input?
```python
total, top = count_words("")        # empty string
assert total == 0
```

**3. Known-wrong case** — does it reject bad input gracefully?
```python
# What if the file doesn't exist?
# The program should print an error, not crash with a traceback
```

---

## Reading a Traceback

Python tracebacks look scary. They are not.

```
Traceback (most recent call last):
  File "word_counter.py", line 28, in main
    total, top = count_words(text)
  File "word_counter.py", line 17, in count_words
    words = re.findall(pattern, text.lower())
TypeError: expected string or bytes-like object
```

**Read from the bottom:**
1. Last line = the error type and message
2. Line above it = the exact file and line number where it broke
3. Lines above that = how you got there (usually less important)

The fix is almost always on the line Python points to.

---

## The Debug Loop

```
Run the code (or tests)
       ↓
Read the error — note file name, line number, error type
       ↓
Copy: the error message + the relevant function + the test
       ↓
Paste to AI: "I got this error. Here is the code. What is wrong?"
       ↓
Apply the fix
       ↓
Run again
       ↓
Repeat (usually 1–3 loops)
```

If you are still stuck after 5 loops, ask the AI to explain the function from scratch — sometimes the bug is in your mental model.

---

## What to Send the AI When Debugging

**Don't send:** "It doesn't work."

**Do send:**

> "I got this error when running my tests:
>
> ```
> TypeError: expected string or bytes-like object
>   File "word_counter.py", line 17, in count_words
> ```
>
> Here is the `count_words` function:
> ```python
> [paste the function]
> ```
>
> What is wrong and how do I fix it?"

More context = faster fix. The AI cannot see your screen.

---

## Demo: Catching a Bug with a Test

*Watch me work through one bug in `buggy_word_counter.py` live.*

Steps:
1. Run `python -m pytest test_word_counter.py -v`
2. Read the first failure carefully
3. Find the relevant line in `buggy_word_counter.py`
4. Ask the AI what is wrong
5. Apply the fix
6. Run tests again

---

## `pytest` in 60 Seconds

`pytest` is a tool that automatically finds and runs all your tests.

```bash
pip install pytest                        # install once
python -m pytest test_word_counter.py -v  # run tests, verbose output
```

Output you want to see:
```
test_word_counter.py::test_total_count PASSED
test_word_counter.py::test_top_words   PASSED
2 passed in 0.04s
```

Output you want to investigate:
```
test_word_counter.py::test_empty_string FAILED
```

Green = good. Red = a bug (or a wrong test). Both are useful.

---

## Lab Overview (45 min)

| Time | Activity |
|------|----------|
| 0–10 min | Part 1: Run existing tests, read failures |
| 10–30 min | Part 2: Debug the three bugs with AI help |
| 30–40 min | Part 3: Write the missing tests (# TODO sections) |
| 40–45 min | Part 4: Break it on purpose, watch tests catch it |

Starter files in `starter/`:
- `buggy_word_counter.py` — has 3 deliberate bugs (all in `count_words`)
- `test_word_counter.py` — tests to run, plus TODOs for you to complete

---

## Key Takeaways

1. **Tests = inputs + expected outputs** — simple assertions, not magic
2. **Tests catch AI regressions** — every time you change code, run the tests
3. **Read tracebacks bottom-up** — last line is the error, the line above it is where
4. **Give the AI context** — error message + relevant function = fast fix
5. **The debug loop is normal** — 2–3 cycles is typical, not a sign of failure

---

## Before Next Week

- Save your fixed `word_counter.py` somewhere easy to find
- Think about your tool from Week 2: what are two inputs that might break it?
- Install `git` if you have not already (instructions in Week 5 README)

**Next session:** Feb 16 — Version control with Git and GitHub
