# Tool Spec: Meeting Note Formatter

**Author:** Fiona Li (example)
**Date:** Jan 26, 2027

---

## Goal

A script that reads a plain-text file of raw meeting notes, removes action items and meta-lines, and saves a clean summary to a new file.

---

## Inputs

- A single `.txt` file path, given on the command line (e.g., `notes_jan26.txt`)
- The output filename is optional; if not given, default to `summary.txt` in the same folder

---

## Outputs

- A new text file (`summary.txt` by default) containing only the content lines — no lines that start with "Action:", "TODO:", or "---"
- A short message printed to the screen: "Saved summary to summary.txt (12 lines kept, 5 removed)"

---

## Steps

1. Read the file path from the command line
2. Open the file and read all lines
3. For each line, skip it if it starts with "Action:", "TODO:", or contains only dashes ("---")
4. Also skip blank lines (lines with only spaces or nothing)
5. Write the kept lines to the output file
6. Print a summary message showing how many lines were kept and how many removed

---

## Edge Cases

- If the input file does not exist, print: "Error: file not found: [path]" and exit without crashing
- If the file is empty, print: "The file is empty — nothing to format" and exit
- If all lines are removed (e.g., the file only contains action items), print a warning: "Warning: all lines were removed. Check your input file."
- If the output file already exists, overwrite it (do not ask for confirmation — keep it simple)

---

## Nice-to-haves (optional)

- A `--dry-run` flag that prints the output to the screen without saving a file
- Support for multiple input files at once: `python formatter.py notes1.txt notes2.txt`

---

## Notes for the AI

- Use only Python's built-in standard library (no pip installs)
- Keep the script in a single file
- Add a comment block at the top showing the exact command to run it with a real example
- The line-matching should be case-insensitive: "action:" and "Action:" and "ACTION:" should all be removed
- Do NOT delete the original input file under any circumstances

---

## Example input file (`notes_jan26.txt`)

```
Weekly sync — Jan 26
---
Discussed Q1 roadmap priorities.
Revenue target confirmed at $2.4M for the quarter.
Action: Fiona to send updated deck by Friday
Marketing campaign launches Feb 3.
TODO: Book venue for offsite
Design review scheduled for Feb 10.
---
Next meeting: Feb 2
```

## Expected output file (`summary.txt`)

```
Weekly sync — Jan 26
Discussed Q1 roadmap priorities.
Revenue target confirmed at $2.4M for the quarter.
Marketing campaign launches Feb 3.
Design review scheduled for Feb 10.
Next meeting: Feb 2
```

## Expected console output

```
Saved summary to summary.txt (6 lines kept, 5 removed)
```
