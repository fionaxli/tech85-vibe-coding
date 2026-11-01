# Bug Report

Use this template when you need Claude Code to fix a bug. The more specific you are, the faster and more accurately Claude Code will fix the problem.

**How to use:** fill out each section, then paste the whole thing into Claude Code:
> "Here is a bug in my app. Please fix it: [paste this document]"

---

## What I was trying to do
[Describe the action you took or the feature you were trying to use. Be specific about what you clicked, typed, or did.]

Example: "I clicked the Delete button next to the habit named 'Read for 20 minutes'."

---

## What I expected to happen
[Describe the behavior you expected. What should the app have done?]

Example: "The habit should have been removed from the list immediately."

---

## What actually happened
[Describe what went wrong. If there is an error message, paste the entire thing — do not paraphrase it. Error messages are precise; summaries of error messages are not.]

Example:
```
Traceback (most recent call last):
  File "app.py", line 47, in delete_habit
    habits.remove(habit_id)
IndexError: list index out of range
```

---

## Steps to reproduce
[List the exact steps someone would take to trigger this bug. "It doesn't always happen" is useful information — if so, describe when it does and does not happen.]

1.
2.
3.

Example:
1. Open the app at localhost:8501
2. Add two habits: "Meditate" and "Read"
3. Delete "Read" (the second habit)
4. Try to delete "Meditate" (the first habit) — the app crashes

---

## Relevant code
[Ask Claude Code to identify the relevant section: "What part of my code is responsible for [the thing that broke]?" Then paste that function or section here.]

```python
# paste the relevant function here
```

---

## What I already tried
[Optional but helpful. If you already made a change that did not fix it, say so. This prevents Claude Code from suggesting the same thing again.]

Example: "I tried changing line 47 to use `habits.pop(index)` but got the same error."
