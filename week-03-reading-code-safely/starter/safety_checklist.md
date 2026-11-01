# Code Safety Checklist

**Script under review:** `review_me.py`
**Reviewer:** [Your name]
**Date:** [Today's date]

---

## Step 1: First impression (before reading the code)

What does the script *claim* to do, based on the comment at the top?

> Your answer:

---

## Step 2: Import scan

Read only the `import` lines at the top of the script. For each import below, check whether it appears and add a note about what it gives the script permission to do.

| Import | Present? | What it can do | Your notes |
|---|---|---|---|
| `os` | Yes / No | Read/write files, list folders, delete files | |
| `sys` | Yes / No | Read command-line arguments, exit the program | |
| `requests` | Yes / No | Make HTTP calls to the internet | |
| `subprocess` | Yes / No | Run shell commands or other programs | |
| `csv` | Yes / No | Read and write CSV files | |
| `json` | Yes / No | Parse JSON data (safe — no side effects) | |
| `eval` or `exec` | Yes / No | Execute arbitrary code at runtime | |
| Other imports you see: | | | |

**After reading the imports, what do you predict this script does?**

> Your one-sentence prediction:

---

## Step 3: File operations

Search the script for: `open(`, `os.remove(`, `os.unlink(`, `shutil.rmtree(`, `os.rename(`

| Question | Your answer |
|---|---|
| Does the script open any files for reading? | |
| Does the script write or create any files? | |
| If yes — what is the output filename? | |
| Does it overwrite files without asking? | |
| Could it accidentally delete your files? | |

---

## Step 4: Network operations

Search the script for: `requests.`, `urllib`, `httpx`, `socket`, `http.client`

| Question | Your answer |
|---|---|
| Does the script make any network calls? | |
| If yes — what URL does it contact? | |
| Does it send any of your data in the request body? | |
| Is the URL hardcoded or could it be changed by user input? | |

---

## Step 5: Subprocess / shell operations

Search the script for: `subprocess`, `os.system(`, `os.popen(`, `Popen`

| Question | Your answer |
|---|---|
| Does the script run any shell commands? | |
| If yes — what command? | |
| Could a user-supplied value be injected into the command? | |

---

## Step 6: Dynamic execution

Search the script for: `eval(`, `exec(`, `compile(`

| Question | Your answer |
|---|---|
| Does the script use `eval`, `exec`, or `compile`? | |
| If yes — where, and what is being executed? | |

---

## Step 7: AI-assisted explanation

Paste the full script into Claude and ask:

> "I am reviewing this Python script before running it. Explain what each section does in plain English, focusing on what files it reads or writes, what network calls it makes, and whether it does anything that cannot be undone."

Then ask these two follow-up questions and paste the answers below:

**Q1: "Does this script write or overwrite any files on my computer? If yes, which ones?"**

> AI answer:

**Q2: "Does this script send any of my data to an external server? If yes, what data and where?"**

> AI answer:

---

## Step 8: Risk summary

Based on your review, complete this table:

| Risk | Low / Medium / High | Your reasoning |
|---|---|---|
| Could delete or corrupt my files | | |
| Could expose my private data | | |
| Could install software without my knowledge | | |
| Could run commands I did not authorize | | |
| Depends on an external service being available | | |

---

## Step 9: Virtual environment

Before running, confirm you have:

- [ ] Created a virtual environment (`python -m venv venv`)
- [ ] Activated it (`(venv)` shows in my terminal prompt)
- [ ] Installed required packages inside it (`pip install requests`)
- [ ] Confirmed I am NOT running as root/administrator

---

## Step 10: Final judgment

**Would you run this script on a computer you care about?**

> Circle one: **YES** / **NO** / **YES, WITH MODIFICATIONS**

**Explain your reasoning (2–3 sentences):**

>

---

## Bonus question

Find the line in `review_me.py` that writes a file. Paste it here:

```python
# paste the line(s) here
```

Ask the AI: "How would I change this so the script asks the user for permission before writing any file?"

Paste the AI's suggested change here:

```python
# paste suggested code here
```
