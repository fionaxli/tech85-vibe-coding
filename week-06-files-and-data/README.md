# Week 6: Working with Files and Data

**Session:** Tue Feb 23, 2027, 7:00–8:30 pm PT

## Goals

By the end of this session you will be able to:

- Read a CSV file into Python and inspect its contents
- Identify and clean common data quality problems (blanks, inconsistent capitalization, stray spaces)
- Write a summary of cleaned data to an output file
- Ask AI to handle data transformation tasks from a plain-language description

---

## Key Concepts

### Three common data formats

**CSV (Comma-Separated Values)** — a plain text file where each row is a record and columns are separated by commas. Excel can open and save CSV files. Python reads them with the built-in `csv` module or the `pandas` library.

```
name,score,department
Alice,87,Engineering
Bob,92,Marketing
,78,Engineering         ← blank name — messy data
carol,85,marketing      ← lowercase, inconsistent with other rows
```

**JSON (JavaScript Object Notation)** — structured data as text, common in web APIs and configuration files.

```json
{"name": "Alice", "score": 87, "department": "Engineering"}
```

**Excel (.xlsx)** — a binary format that requires the `openpyxl` library. Often easier to convert to CSV first.

### What "cleaning" means

Real-world data is almost never clean. Common problems:

| Problem | Example | Fix |
|---|---|---|
| Blank cells | Name is empty | Skip or flag the row |
| Inconsistent capitalization | `"marketing"` vs `"Marketing"` | Normalize with `.title()` or `.lower()` |
| Extra whitespace | `"  Alice  "` | Strip with `.strip()` |
| Inconsistent values | `"yes"`, `"Yes"`, `"Y"`, `"TRUE"` | Map to a standard value |
| Out-of-range numbers | Score of `999` | Filter or flag as invalid |

Cleaning is not about perfection. It is about making data consistent enough for your summary to be meaningful.

### Reading a CSV with Python

```python
import csv

with open("survey_responses.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)      # reads each row as a dictionary
    for row in reader:
        print(row["name"], row["score"])
```

`csv.DictReader` uses the first row (the header) as column names. Each subsequent row becomes a dictionary: `{"name": "Alice", "score": "87", ...}`.

**Note:** CSV stores everything as strings. If you want to do math on a number, you need to convert it first: `int(row["score"])` or `float(row["score"])`.

---

## Lab: Build a Survey Summarizer

This lab uses the file `starter/survey_responses.csv` — 50 rows of fake survey data about a fictional company wellness program. The data has several intentional quality problems for you to find and fix.

### Part 1 — Explore the data (10 min)

1. Open `starter/survey_responses.csv` in VS Code. If VS Code offers to preview it as a table, do that — it is easier to read.
2. Scroll through all 50 rows. Answer these questions in your notes:
   - How many columns are there? What are their names?
   - Can you spot at least three rows with data problems? Describe what is wrong with each.
   - What kind of summary would be useful? (Example: average satisfaction score per department)

3. Open `starter/data_cleaner_starter.py`. Read the function stubs at the top. Understand what each function is supposed to do before writing any code.

### Part 2 — Ask AI to help implement the cleaning functions (20 min)

4. Open Claude. Describe what you found in step 2 and paste the contents of `data_cleaner_starter.py`. Ask:
   > "Here is a Python script with function stubs for cleaning a CSV file. Please implement the functions based on their docstrings. The CSV has these problems I found: [describe what you found]. Use only Python's built-in csv module — no pandas."

5. Copy the completed code into `data_cleaner_starter.py`, replacing the stubs.

6. Run the script:
   ```bash
   python data_cleaner_starter.py survey_responses.csv summary.txt
   ```

7. Open `summary.txt`. Does the output look right? Check: does it handle the messy rows you found in step 2?

### Part 3 — Refine the output (10 min)

8. Look at your `summary.txt`. Pick one thing to improve. Some ideas:
   - Add the number of rows that were skipped due to bad data
   - Show the distribution of satisfaction scores (how many gave each rating)
   - Group the results by department

9. Ask the AI to make that one improvement:
   > "Here is my current data cleaning script and the output it produces. I would like to also show [your improvement]. Here is the code: [paste code]. Here is the current output: [paste output]."

10. Replace the code, run again, check the output.

### Part 4 — Try your own data (5 min, if time allows)

11. If you brought a CSV file from your own work, open it in VS Code and look at it. What cleaning problems do you see? Ask the AI: "I have a CSV with these columns and these problems. How would I clean it?" You do not need to implement anything — just get the AI's assessment.

---

## Expected Outputs

By the end of lab you should have:

- `data_cleaner_starter.py` with all function stubs implemented
- A `summary.txt` showing cleaned statistics from the survey data
- At least one round of refinement to the output format

---

## If Something Goes Wrong

| Problem | What to do |
|---|---|
| `UnicodeDecodeError` | Add `encoding="utf-8"` to the `open()` call, or try `encoding="latin-1"` |
| `KeyError: 'column_name'` | The column name in your code does not exactly match the header in the CSV. Print `row.keys()` to see the actual names. |
| `ValueError: invalid literal for int()` | A cell that should be a number contains text or is blank. Add a check: `if row["score"].strip(): int(row["score"])` |
| The summary looks wrong | Print a few rows before and after cleaning to verify the transformation is working |
| The AI generates code using `pandas` | Say: "Please rewrite this using only Python's built-in csv module, without pandas." |

---

## Before Next Week

Week 7 is about web services and agents — we will use the Anthropic API to have Claude analyze data as part of a pipeline. You will need an Anthropic API key.

**Get your API key now:**
1. Go to [console.anthropic.com](https://console.anthropic.com) and sign up for a free account
2. Go to "API keys" and create a new key
3. Copy it somewhere safe (you can only see it once)
4. Set it as an environment variable (instructions in the Week 7 README)

Do NOT paste your API key into any code file or share it publicly.

## Slides

See `slides.md` in this folder (also posted in Canvas).
