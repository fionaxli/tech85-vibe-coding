# Writing Good Commit Messages

A commit message is a short note to your future self explaining what changed and why.

When you look at your commit history six weeks from now, you want to understand what each commit did — not just "update code" or "fix stuff."

This matters even more when you use AI-generated code, because the changes can be large and fast. A good commit message is the only record of what you intended.

---

## The formula

```
[type]: [what changed, in past tense]
```

**Types:**
- `Add:` — added a new feature or file
- `Fix:` — fixed a bug
- `Update:` — modified an existing feature (not a bug fix)
- `Remove:` — deleted something
- `Refactor:` — changed how the code is organized without changing what it does
- `Checkpoint:` — saved state before a risky change

---

## Examples

**Weak messages:**
```
updated stuff
fixed it
changes
v2
WIP
```

**Strong messages:**
```
Add: SQLite database for habit persistence
Fix: delete button crashes when list is empty
Update: show streak count next to each habit
Add: search bar filters notes by content
Remove: unused test_copy.py file
Checkpoint: before adding API integration
Fix: app crashes on empty file — show "no words found" instead
```

---

## How long should it be?

One line, under 72 characters. That is it.

If you need to explain more — for example, why you made a non-obvious decision — add a blank line after the first line and then write more:

```
Fix: handle empty input in habit form

Previously, submitting an empty habit name caused the app to add a blank
entry to the database. Now the form validates before saving and shows
a warning message if the name is empty.
```

For a course project, one line is almost always enough.

---

## Asking Claude Code to write commit messages

If you are not sure what to write, ask Claude Code:
> "I just made these changes: [describe what you did or paste `git diff`]. Write a commit message for me."

Claude Code is good at this. Review it before you use it — make sure the message actually describes what changed.
