---
marp: true
theme: default
paginate: true
footer: "TECH 85 · Week 6 · Stanford Continuing Studies"
---

<!-- _class: lead -->
# Week 6: Working with Files and Data
### TECH 85: Vibe Coding
Stanford Continuing Studies · Feb 23, 2027

---

## Agenda

1. The three data formats you will encounter most
2. What "messy data" looks like (and why it is normal)
3. The clean → analyze → summarize pattern
4. Reading CSV files in Python
5. Demo: cleaning a survey dataset live
6. Lab: build the survey summarizer

---

## Why Data Skills Matter for Vibe Coders

The tools most people actually want to build involve data:

- "Summarize this spreadsheet of customer feedback"
- "Find all orders over $500 in this CSV"
- "Combine data from these three files"
- "Flag rows where the email address looks wrong"

None of these require a data science degree. They require: reading files, cleaning problems, computing summaries. You will do all three today.

---

## Three Formats You Will See

**CSV** — "Comma-Separated Values"
- Plain text, one row per line, columns separated by commas
- Excel can open and save it
- Python reads it with the built-in `csv` module

**JSON** — "JavaScript Object Notation"
- Nested key-value pairs
- Very common in web APIs and app config files
- Python reads it with the built-in `json` module

**Excel (.xlsx)**
- Binary format, requires `openpyxl` library
- Often easiest to "Save As → CSV" and work with that

---

## What Messy Data Looks Like

Real data almost always has problems. Here is a real-ish CSV:

```
name,score,department
Alice,87,Engineering
Bob,92,Marketing
,78,Engineering        ← name is blank
carol,85,marketing     ← lowercase (inconsistent)
David,999,Sales        ← score out of range
  Eve  ,90,Marketing   ← extra spaces around name
Frank,eighty,R&D       ← text instead of a number
```

Every one of these will cause your script to behave oddly — or crash — if you do not account for them.

---

## The Four Most Common Data Problems

| Problem | Example | Python fix |
|---|---|---|
| Blank cells | `""` where a value should be | Skip or flag: `if not row["name"]: ...` |
| Wrong capitalization | `"marketing"` vs `"Marketing"` | Normalize: `dept.title()` |
| Extra whitespace | `"  Alice  "` | Strip: `name.strip()` |
| Non-numeric numbers | `"eighty"` | Catch the error: `try: int(v) except: ...` |

You do not need to fix every problem. You need to handle it — either fix it, skip it, or flag it in your output.

---

## Reading a CSV in Python

```python
import csv

with open("survey_responses.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)   # each row = a dictionary
    for row in reader:
        print(row["name"], row["score"], row["department"])
```

`csv.DictReader` uses the first row as column names.

**Important:** everything in a CSV is a string. To do math:
```python
score = int(row["score"])    # convert string "87" to integer 87
```

If the cell is blank or contains text, `int()` will crash. That is why cleaning happens before math.

---

## The Clean → Analyze → Summarize Pattern

```
Read CSV
    ↓
Clean each row
 (fix capitalization, skip blanks, validate numbers)
    ↓
Analyze clean rows
 (compute averages, counts, totals)
    ↓
Write summary
 (print to screen or save to a file)
```

Your script today follows this pattern exactly. The AI will help you fill in the details, but the structure is always the same.

---

## Describing Data Work to AI

AI is excellent at data cleaning because the operations are easy to describe precisely:

Good prompt for this kind of work:

> "I have a CSV with columns: name, satisfaction_score (1–5), department.
> Write a Python function called `clean_row(row)` that:
> - Returns None if the name is blank
> - Converts the score to an integer; returns None if it is not a valid number between 1 and 5
> - Strips whitespace from all string fields
> - Converts department to title case
> Use only Python's built-in csv module."

Specific field names + specific rules = accurate code.

---

## Demo: Cleaning the Survey Data

*Watch me work through the first two parts of the lab live.*

1. Open `survey_responses.csv` — find the messy rows
2. Paste the spec into Claude, get the cleaning function
3. Add the analysis: average score per department
4. Run it and check the summary output
5. Make one refinement: add skipped-row count to the output

---

## Today's Data: `survey_responses.csv`

50 rows from a fictional company wellness survey.

**Columns:**
- `respondent_id` — unique ID per person
- `name` — respondent's name
- `department` — which team they are on
- `satisfaction_score` — 1 (very dissatisfied) to 5 (very satisfied)
- `would_recommend` — "Yes" or "No"
- `comments` — free-text feedback

**Intentional problems to find:**
- A few rows with blank names
- Inconsistent department capitalization
- One score that is out of range
- A few blank score cells

---

## Lab Overview (45 min)

| Time | Activity |
|------|----------|
| 0–10 min | Part 1: Open the CSV, find 3+ problems, read the stubs |
| 10–30 min | Part 2: Ask AI to implement cleaning + analysis |
| 30–40 min | Part 3: Refine the output format |
| 40–45 min | Part 4: Try your own CSV (if you brought one) |

Starter files in `starter/`:
- `survey_responses.csv` — 50-row survey dataset
- `data_cleaner_starter.py` — function stubs to fill in

---

## Key Takeaways

1. **Messy data is normal** — every real dataset has problems; plan for them
2. **Clean before you analyze** — computing averages on dirty data gives wrong results
3. **CSV DictReader** — each row is a dictionary; all values are strings until you convert them
4. **Describe data work precisely** — field names, rules, edge cases → AI gives working code
5. **The pattern is reusable** — read → clean → analyze → write works for almost any data task

---

## Before Next Week

- Get your Anthropic API key: [console.anthropic.com](https://console.anthropic.com)
- Copy it somewhere safe — you will need it next week
- Do NOT share it or put it in code files
- Install the `anthropic` library so we can test your setup:
  ```bash
  pip install anthropic
  ```

**Next session:** Mar 2 — Small agents and web services
