---
marp: true
theme: default
paginate: true
footer: "TECH 85 · Week 3 · Stanford Continuing Studies"
---

<!-- _class: lead -->
# Week 3: Reading and Running AI-Generated Code Safely
### TECH 85: Vibe Coding
Stanford Continuing Studies · Feb 2, 2027

---

## Agenda

1. Why you need to read code before running it
2. The four risky operation categories
3. Reading imports: your 30-second scan
4. Virtual environments: your safety net
5. Never run as root
6. Demo: reviewing a real script with AI help
7. Lab: complete the code review checklist

---

## You Got the Code. Now What?

Last week you built a tool from a spec. You ran it immediately.

That works when the AI is just printing text. It gets risky when code can:
- Delete or overwrite files
- Send data to the internet
- Run other programs on your computer

**You are not being paranoid.** You are being a responsible user. A 2-minute read prevents a lot of grief.

---

## The Contract Analogy

You do not read every clause of every contract. But before you sign, you scan for:
- Anything that costs you money
- Anything you can never undo
- Anything that gives away something important

**Code review works the same way.** You do not need to understand every line. You need to spot the four categories that matter.

---

## The Four Risky Categories

| Category | Signals in code | What it can do |
|---|---|---|
| **Files** | `open()`, `os.remove()`, `shutil.rmtree()` | Read, write, or delete your files |
| **Network** | `requests`, `urllib`, `httpx`, `socket` | Send data to the internet |
| **Shell** | `subprocess`, `os.system()`, `os.popen()` | Run other programs |
| **Dynamic exec** | `eval()`, `exec()` | Run invisible code |

You will use a checklist in lab. You do not need to memorize this table.

---

## Start With the Imports

The first 10–20 lines of every Python script are `import` statements.

```python
import os          # can touch files and folders
import requests    # makes network calls
import subprocess  # runs shell commands
import json        # safe — parses data
import re          # safe — text patterns
import math        # safe — arithmetic
```

**Scan the imports first.** They tell you what capabilities the script has claimed, before you see what it actually does with them.

---

## A Quick Import Scan in Practice

You see:
```python
import os
import requests
import json
```

You immediately know:
- This script **can** read or write files
- This script **can** make network calls
- It uses JSON — probably reading or writing data

Now read the rest with those questions in mind:
- *Which* files does it touch?
- *What data* does it send, and *where*?

---

## Virtual Environments: Your Safety Net

A virtual environment is a self-contained copy of Python, isolated from the rest of your computer.

**Why use one:**
- Packages installed inside it stay inside it
- If something goes wrong, delete the folder and start over
- Does not affect your system Python or other projects

**How to create one (30 seconds):**
```bash
python -m venv venv
source venv/bin/activate    # Mac/Linux
# venv\Scripts\activate     # Windows
```

You will see `(venv)` in your prompt. That means it is active.

---

## The Root Rule

> **Never run a script as root or as administrator.**

Running with elevated privileges means the script can modify system files, install software, or delete things that your operating system needs.

- Mac/Linux: Do not use `sudo python my_script.py`
- Windows: Do not right-click and "Run as administrator"

A normal user terminal limits what any script can break. Use one every time.

---

## Demo: Reviewing `review_me.py`

*Watch me review the lab script live.*

Steps I will take:
1. Read the imports — what capabilities has it claimed?
2. Paste the whole file into Claude, ask for a plain-English explanation
3. Ask specifically: "What files does this write? What data does it send?"
4. Fill in the checklist
5. Create a virtual environment and run the script

---

## The "Explain Back" Check for Code

The same technique from Week 2 applies to reviewing code you didn't write:

> "I am about to run this Python script. Explain what each section does in plain English. Focus on what files it reads or writes, what network calls it makes, and anything that cannot be undone."

This forces the AI to surface the risky parts, not just summarize what the script claims to do.

---

## What Is `review_me.py`?

The lab script is a realistic tool that:
- Reads all `.txt` files from a folder you specify
- Calls a web API to process the text
- Writes results to a CSV file

It is safe and intentionally written for this class. But it has all four operation categories — files, network, nothing dangerous, but worth reading carefully before trusting.

---

## Lab Overview (45 min)

| Time | Activity |
|------|----------|
| 0–10 min | Part 1: Read the imports, fill in checklist |
| 10–25 min | Part 2: Use AI to explain the full script |
| 25–40 min | Part 3: Create a virtual environment and run it |
| 40–45 min | Part 4: Finish the checklist, answer the final question |

Starter files in `starter/`:
- `review_me.py` — the script to review
- `safety_checklist.md` — your review form

---

## Key Takeaways

1. **Read imports first** — they tell you what a script is capable of doing
2. **Four categories to flag** — files, network, shell, dynamic eval
3. **Use "explain back"** — ask AI to describe risky parts specifically
4. **Virtual environments every time** — they contain mistakes
5. **Never run as root** — a normal terminal limits blast radius

---

## Before Next Week

- Keep `review_me.py` open — we will write tests for a similar script in Week 4
- Make sure you have your `my_tool.py` from Week 2 saved
- Optional: try the "explain back" technique on one piece of code you have run before — does anything surprise you?

**Next session:** Feb 9 — Testing and debugging with AI
