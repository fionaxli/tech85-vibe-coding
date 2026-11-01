# Week 3: Reading and Running AI-Generated Code Safely

**Session:** Tue Feb 2, 2027, 7:00–8:30 pm PT

## Goals

By the end of this session you will be able to:

- Read an AI-generated Python script at a high level without understanding every line
- Spot the four categories of risky operations (file, network, subprocess, eval)
- Use a safety checklist before running any code you did not write yourself
- Run code inside a virtual environment to keep your computer safe

---

## Key Concepts

### Why reading matters

You do not need to understand every line of AI-generated code. But you do need to understand *what it does at a high level* before you run it. A script that looks helpful might also delete files, send your data to a server, or do something irreversible.

Think of it like checking a contract before signing. You do not read every clause in detail, but you do look for anything that mentions money, liability, or things you can never undo.

### The four risky categories

When you scan a new script, look for these four patterns:

| Category | What to look for | Why it matters |
|---|---|---|
| **File operations** | `open(...)`, `os.remove()`, `shutil.rmtree()`, `os.rename()` | The script can read, write, or delete your files |
| **Network operations** | `requests`, `urllib`, `httpx`, `socket` | The script can send data to the internet |
| **Subprocess / shell** | `subprocess`, `os.system()`, `os.popen()` | The script can run other programs on your computer |
| **Dynamic execution** | `eval(...)`, `exec(...)` | The script can run code that was not visible when you read it |

You do not need to memorize these. The safety checklist in `starter/safety_checklist.md` has them.

### Reading imports first

The first 10–20 lines of any Python script are the `import` statements. These tell you which capabilities the script is using. Start here every time.

```python
import os        # can read/write/delete files and folders
import requests  # can make network calls
import subprocess  # can run shell commands
import json      # safe — just parses data format
import re        # safe — just works with text patterns
```

Some imports are neutral (like `json`, `re`, `math`). Some are powerful and worth examining more closely.

### Virtual environments

A virtual environment is a contained copy of Python that is isolated from the rest of your computer. If something goes wrong inside a virtual environment, it is easy to delete and start fresh without affecting your other projects or system files.

Creating one takes 30 seconds. You should use one for every project.

```bash
# Create a virtual environment named "venv" in the current folder
python -m venv venv

# Activate it (Mac/Linux)
source venv/bin/activate

# Activate it (Windows)
venv\Scripts\activate

# You will see (venv) in your terminal prompt — that means it is active
# Install packages inside it safely
pip install requests

# Deactivate when done
deactivate
```

### Never run as root or administrator

Running a script with elevated privileges (as `root` on Mac/Linux, or "Run as Administrator" on Windows) gives that script permission to modify system files. A script that has a bug could damage your operating system. Only ever run scripts in a normal user terminal.

---

## Lab: The Code Review

This lab takes about 45 minutes. You will review a realistic but safe Python script (`starter/review_me.py`) using the safety checklist.

### Part 1 — Read the imports (10 min)

1. Open `starter/review_me.py` in VS Code.
2. Read only the first 20 lines (do not scroll further yet).
3. Open `starter/safety_checklist.md`. For each import you see, check the corresponding box.
4. Ask yourself: "Based on these imports alone, what is this script probably going to do?"
5. Write your answer (one sentence) as a comment at the very top of the checklist file.

### Part 2 — Use AI to explain the script (15 min)

6. Go back to `review_me.py` and now read the whole file. Do not worry if most of it is unfamiliar.
7. Open Claude. Paste the entire contents of `review_me.py` and ask:
   > "I am reviewing this Python script before running it. Please explain what each section does in plain English. Focus especially on: what files it reads or writes, what network calls it makes, and whether it does anything that cannot be undone."

8. Read the AI's explanation carefully. Go back to the checklist and fill in the "Notes" column for each item.

9. Ask the AI two follow-up questions:
   > "Does this script write or overwrite any files on my computer? If yes, which ones?"

   > "Does this script send any data to an external server? If yes, what data and where?"

### Part 3 — Run the script safely (15 min)

10. Open a terminal in VS Code. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

11. Activate it:
    ```bash
    # Mac / Linux:
    source venv/bin/activate
    # Windows:
    venv\Scripts\activate
    ```
    You should see `(venv)` appear at the start of your terminal prompt.

12. Install the one required library:
    ```bash
    pip install requests
    ```

13. Look at the top of `review_me.py` — it has a comment block showing how to run it. Follow those instructions. The script needs a folder of text files; use `../week-01-first-tool/starter/` as the input folder.

14. Read the output. Does it match what the AI's explanation said it would do?

### Part 4 — Complete the checklist (5 min)

15. Finish filling in `safety_checklist.md`. For the final question — "Would you run this script on a computer you care about?" — answer honestly and explain why.

16. **Bonus:** Find the line in `review_me.py` that writes a file. Ask the AI: "How would I change this script so it asks me for permission before writing any file?"

---

## Expected Outputs

By the end of lab you should have:

- A completed `safety_checklist.md` with notes for every section
- A terminal showing successful output from `review_me.py`
- Answers to both follow-up AI questions (what files it writes, what data it sends)

---

## If Something Goes Wrong

| Problem | What to do |
|---|---|
| `ModuleNotFoundError: No module named 'requests'` | Make sure the virtual environment is activated (`(venv)` should show in your prompt), then run `pip install requests` |
| `(venv)` is not showing in the prompt | Run the activate command again. On Windows, check that you typed `venv\Scripts\activate` (backslash, not forward slash) |
| Script crashes with a permission error | Do not run as administrator. Close the terminal, open a new normal terminal, and try again |
| The AI explanation mentions something alarming | Ask it to show you the specific line. Then ask: "Is this dangerous? What would it take for this to cause harm?" |
| VS Code says it cannot find Python | Click the Python version in the bottom-left of VS Code and select the `venv` interpreter |

---

## Before Next Week

Keep your copy of `review_me.py` open. In Week 4 we will write tests for a similar script — understanding what a script *does* is the first step to knowing how to test it.

Also: make sure your `my_tool.py` from Week 2 is saved somewhere you can find it. We will use it in Week 4.

## Slides

See `slides.md` in this folder (also posted in Canvas).
