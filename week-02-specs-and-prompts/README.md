# Week 2: Turning an Idea into Clear Instructions

**Session:** Tue Jan 26, 2027, 7:00–8:30 pm PT

## Goals

By the end of this session you will be able to:

- Write a one-page specification (spec) for your own personal tool idea
- Use proven prompting patterns to get better code from an AI assistant on the first try
- Refine AI-generated code through conversation rather than starting over

---

## Key Concepts

### What is a spec?

A spec (short for specification) is a short written description of what you want your tool to do, written *before* you start building. Think of it like a recipe: before you cook, you write down what you are making, who it is for, what ingredients you need, and what the finished dish should look like. A spec does the same thing for software.

A one-page spec has five parts:

1. **Goal** — one sentence describing what the tool does
2. **Inputs** — what data or files the tool receives
3. **Outputs** — what the tool produces or prints
4. **Steps** — the main operations in plain English
5. **Edge cases** — what happens when something is missing or unexpected

### Anatomy of a good prompt

A good first prompt to an AI coding assistant covers:

- **Role**: "You are a Python developer helping a non-programmer."
- **Task**: describe exactly what the tool should do (paste your spec here)
- **Constraints**: language, libraries, style (e.g., "one file, no external libraries")
- **Output format**: "Give me the full script, with a comment at the top showing how to run it."

**Weak prompt:** *"Make a tool that cleans up my notes."*

**Strong prompt:** *"You are a Python developer helping someone who has never coded before. Write a single Python script that reads a plain-text file of meeting notes, removes any line that starts with the word 'Action:', and saves the remaining lines to a new file called summary.txt. Use only Python's built-in standard library. Include a comment block at the top showing the exact command to run it."*

The difference: the strong prompt tells the AI the role, the exact behavior, the constraint (no extra libraries), and the output format.

### Iterative refinement

AI-generated code is rarely perfect on the first try, and that is fine. Plan for a loop:

1. Prompt → get first version
2. Run it (or read it with the AI)
3. Identify the one thing that is most wrong or missing
4. Ask the AI for *that specific change* — describe what you see, not what you think needs to change in the code
5. Repeat until the tool does what you need

Each loop is short: two or three exchanges is typical. You are not debugging; you are having a conversation.

### The "explain back" technique

After the AI generates code, ask: *"Explain what each section of this code does in plain English, as if I have never coded before."*

This has two benefits:
- You learn what the code actually does (important before running anything)
- Errors in the AI's reasoning often surface when it has to explain itself

---

## Lab: Build Your First Personal Tool

This lab takes about 45 minutes. Work at your own pace — there are extension tasks if you finish early.

### Part 1 — Write your spec (15 min)

1. Open `starter/spec_template.md` in VS Code.
2. Fill in every section for the tool idea you brainstormed at the end of Week 1.
   - If you do not have an idea yet, pick one from the suggestion list at the bottom of this section.
   - Keep it to one page. Bullet points are fine; complete sentences are not required.
3. Read `starter/example_spec.md` to see a completed example — the "Meeting Note Formatter."
4. Share your spec with the person next to you. Can they understand what the tool does without asking you any questions? If not, revise until they can.

**Tool ideas if you need one:**
- A script that takes a folder of `.txt` files and prints the word count for each file
- A script that reads a CSV of expenses and prints the total per category
- A script that reformats a list of names from "Firstname Lastname" to "Lastname, Firstname"
- A script that checks a text file for any line containing a keyword you specify, and prints those lines with their line numbers
- A script that reads a list of URLs from a text file and checks which ones are duplicates

### Part 2 — Build with AI (20 min)

5. Open Claude (claude.ai) in your browser, or use the Claude extension in VS Code.
6. Start a new conversation. Paste this framing message first, then add your spec text below it:

   ```
   You are a Python developer helping someone who has never coded before.
   I am going to give you a one-page spec for a small tool I want to build.
   Please write a single Python file that implements the spec exactly.
   Use only Python's built-in standard library (no pip installs needed).
   Add a comment block at the top of the file showing exactly how to run it
   from the command line, with a concrete example using a real filename.
   ```

7. On the next line, paste your filled-in spec.
8. Copy the Python code the AI returns. In VS Code, create a new file named `my_tool.py` inside this week's `starter/` folder and paste the code.
9. Open a terminal in VS Code (`Terminal → New Terminal`). Run the script exactly as shown in the AI's comment block at the top of the file.

   **If it runs but prints nothing**, check whether the input file exists at the path you gave it.

   **If it crashes**, copy the full error message and paste it back to the AI:
   > "I ran the script and got this error. What is wrong and how do I fix it?"
   Replace the code with the fixed version and run again.

10. Run the script on a real input — either a file of your own, or one of the sample files from `week-01-first-tool/starter/`.

### Part 3 — Refine and explain (10 min)

11. Pick one thing to improve. Examples:
    - The output format is hard to read
    - You want to save output to a file instead of just printing
    - An error message is confusing

12. Ask the AI for that one change. Be specific — describe what you currently see and what you want instead:
    > "Right now the script prints each result on its own line. I would like it to print a numbered list instead, like '1. result one'. Here is the current code: [paste code]"

13. Replace the code in `my_tool.py` with the new version and run it again.

14. Ask the AI the "explain back" question:
    > "Explain what each section of the new code does in plain English, as if I have never coded before."

    Read the explanation carefully. Put a comment in your spec noting one thing that surprised you.

### Extension tasks (if you finish early)

- Ask the AI to add a `--help` flag that prints usage instructions when you run `python my_tool.py --help`.
- Ask the AI: *"What are three ways this script could fail or produce wrong results? Show me how to handle each one."*
- Add an "Error handling" section to your spec based on what the AI tells you.

---

## Expected Outputs

By the end of lab you should have:

- A filled-in spec saved in `starter/` (or wherever you are keeping your notes)
- A working `my_tool.py` that runs without errors on a real input
- At least one completed refinement cycle (Parts 2 and 3)

---

## If Something Goes Wrong

| Problem | What to do |
|---|---|
| `python: command not found` | Try `python3` instead. If still missing, re-run the installer from Week 1. |
| `ModuleNotFoundError: No module named 'X'` | The AI used a library that requires installation. Ask it: "Rewrite this using only Python's built-in standard library." |
| Script runs but output looks wrong | Paste the actual output back to the AI and describe what you expected to see. |
| You cannot think of what to change in Part 3 | Ask the AI: "What are three small improvements you would suggest for this script?" |
| The AI keeps asking clarifying questions | Say: "Make reasonable assumptions and give me a complete working script now. I will refine it after." |

---

## Before Next Week

Run your `my_tool.py` on several different inputs. Note at least one case where the output looked wrong, unexpected, or where the script crashed. Bring that example to Week 3 — you will use it when we learn how to read and review AI-generated code safely.

## Slides

See `slides.md` in this folder (also posted in Canvas).
