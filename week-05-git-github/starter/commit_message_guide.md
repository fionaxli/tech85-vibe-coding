# How to Write Good Commit Messages

A commit message is a note to your future self (and anyone else reading your project) explaining what changed and why. A good message makes your history readable. A bad one makes it useless.

---

## The One-Line Rule

Most commits need only one line. Keep it under 72 characters.

**Format:** Use the imperative mood — write as if you are giving an instruction.

Think of it as completing this sentence:
> "If applied, this commit will: _______________"

---

## Good vs. Bad Examples

| Bad | Good |
|-----|------|
| `stuff` | `Fix crash when input file is missing` |
| `fix` | `Add --help flag with usage instructions` |
| `update` | `Improve CSV output: add header row` |
| `final version` | `Handle empty files without crashing` |
| `working now` | `Correct word count to exclude punctuation` |
| `asdfgh` | (no commit message is ever acceptable) |
| `WIP` | `Save progress: partially implement category totals` |
| `fixed the bug` | `Fix off-by-one in word count for apostrophes` |

---

## The Three-Part Format (for bigger changes)

When a one-liner is not enough, use this format:

```
Short summary line (under 72 characters)

Longer explanation of what changed and why. This paragraph is
optional but helpful for complex changes. Explain the reasoning,
not just what happened — the diff already shows what happened.

- Bullet points work well for listing multiple changes
- Keep each bullet focused on one change
```

Example:

```
Refactor file reading to handle encoding errors

The previous version crashed on files saved with Windows-1252
encoding. The new version tries UTF-8 first, then falls back to
latin-1 so Western European characters are preserved.

- Added encoding fallback in read_file()
- Added a test case with a non-UTF-8 sample file
```

---

## When to Commit

**Commit often.** Small commits are better than large ones because:
- Easier to undo one small change than to undo a huge batch
- Easier to understand what each change did
- Easier to find the commit that introduced a bug

**Good times to commit:**
- After getting a feature working for the first time
- Before making a risky or experimental change
- After fixing a bug
- Before leaving your computer for the day
- Anytime you think "I would hate to lose this progress"

**Avoid committing:**
- Broken code (unless on a branch specifically for that work)
- Files with secrets or passwords (use `.gitignore` and `.env`)
- Generated files or build output (they clutter the history)

---

## Quick Reference: Imperative Verbs

Use these at the start of your commit messages:

| Verb | When to use it |
|------|----------------|
| `Add` | New feature, file, or capability |
| `Fix` | Bug fix |
| `Update` | Improving or changing existing behavior |
| `Remove` | Deleting something |
| `Refactor` | Restructuring code without changing behavior |
| `Test` | Adding or fixing tests |
| `Doc` | Adding or fixing documentation / comments |
| `Handle` | Adding error handling |

---

## What NOT to Put in a Commit Message

- The date (Git records this automatically)
- Your name (Git records this from `git config`)
- The word "code" (you are always committing code — be specific)
- What you were thinking ("I hope this works")
- The diff in words ("changed line 17 from X to Y" — the diff shows this)

---

## Checking Your Own Messages

Before pushing, run `git log --oneline`. If you squint at the list and cannot tell what each commit did without opening it, your messages need work. A good history looks like:

```
a3f21bc Add --help flag with usage instructions
9d1e07a Fix crash when input file is missing
5bc4f11 Improve CSV output: add column headers
3a8d920 Initial commit: word counter and sample file
```

That tells a story. That is the goal.
