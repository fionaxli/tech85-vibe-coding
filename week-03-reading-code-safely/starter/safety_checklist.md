# Code Safety Checklist

Use this checklist to review any AI-generated code before you run it or deploy it.

You do not need to understand every line. You need to understand what each section *does*.

**How to use this with Claude Code:**
Open your `app.py` and this file side by side. Then ask Claude Code:
> "Read app.py and answer each question in safety_checklist.md. Keep your answers to one sentence each. Flag anything I should look at more carefully."

---

## Section 1: What does this code do overall?

- [ ] I can describe what this app does in one sentence.
- [ ] I know what the main file is (usually `app.py`) and where the code starts running.
- [ ] I know what data goes in (user input? a file? an API?) and what comes out (a display? a file? a database write?).

---

## Section 2: File operations

File operations can create, modify, or delete files on your computer. Look for:
- `open(filename, 'w')` or `open(filename, 'a')` — writes to a file
- `os.remove()` or `shutil.rmtree()` — deletes files or folders
- `json.dump()`, `csv.writer` — writes structured data to a file

**Questions:**
- [ ] Does this code write or delete any files? If yes, which ones?
- [ ] Are those file paths relative (like `"data/notes.db"`) or absolute (like `"/Users/me/notes.db"`)? Relative paths are safer.
- [ ] Could any file operation overwrite something important by accident?

---

## Section 3: Network requests

Network requests send data to or receive data from the internet. Look for:
- `requests.get(url)` or `requests.post(url)` — HTTP requests
- `urllib.request.urlopen()` — another way to make web requests
- Any URL that starts with `http://` or `https://`

**Questions:**
- [ ] Does this code make any network requests? If yes, to which URLs?
- [ ] Is any personal data or user input being sent in those requests?
- [ ] If the network is unavailable, does the code fail gracefully (show an error message) or crash?

---

## Section 4: Secrets and API keys

Secrets are values like API keys, passwords, and database credentials. They should never appear in your code as plain text. Look for:
- `os.getenv("KEY_NAME")` — the safe way to read a secret
- `load_dotenv()` — loads secrets from a `.env` file
- Any string that looks like a long random code (`"sk-proj-abc123..."`) — this should NOT be in your code

**Questions:**
- [ ] Does this code use any API keys or passwords?
- [ ] Are they loaded from environment variables (safe) or hardcoded in the file (not safe)?
- [ ] Is `.env` listed in your `.gitignore`? (It should be — this prevents secrets from being uploaded to GitHub.)

---

## Section 5: Database operations

Database operations read from or write to a local database file. Look for:
- `sqlite3.connect()` — opens a SQLite database
- `.execute()` — runs a database query
- `conn.commit()` — saves changes to the database
- `conn.close()` — closes the connection

**Questions:**
- [ ] Does this code use a database? If yes, what file is it stored in?
- [ ] Is the connection closed after each operation? (Leaving connections open can cause "database is locked" errors.)
- [ ] Does any SQL query include user input directly? (It should use `?` placeholders, not string formatting, to prevent SQL injection.)

---

## Section 6: External subprocess calls

Subprocess calls run system commands directly on your computer. These are rare in Streamlit apps but worth checking. Look for:
- `subprocess.run()`, `subprocess.Popen()`
- `os.system()`

**Questions:**
- [ ] Does this code run any system commands? If yes, what commands?
- [ ] Is any user input passed directly to a system command? (This is a significant security risk.)

---

## Section 7: Overall assessment

After working through the sections above with Claude Code's help:

- [ ] I understand what every major section of this code does.
- [ ] I am comfortable with all the files it might write or read.
- [ ] I am comfortable with all the network requests it makes.
- [ ] All secrets are in `.env`, not in the code file.
- [ ] I have run the code and confirmed it does what I expect.

**If any checkbox above is unchecked:** Ask Claude Code to explain or fix that item before deploying.
