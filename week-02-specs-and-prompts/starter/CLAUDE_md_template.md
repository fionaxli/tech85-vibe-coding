# CLAUDE.md

## Project overview
[What this project does in 2–3 sentences. Write it as if you are explaining to a developer joining mid-project. Example: "A Streamlit web app for tracking daily habits. Users add habits, check them off each day, and see a streak count. Data is stored locally in a SQLite database."]

## Tech stack
- Language: Python 3.10+
- UI: Streamlit
- Data storage: [SQLite via the built-in `sqlite3` module / none / CSV]
- Key libraries: [list the main ones — e.g., streamlit, sqlite3, requests, python-dotenv]

## File structure
[Describe the main files and what each one does. Example:]
- `app.py` — main Streamlit app, all UI code lives here
- `db.py` — database helper functions (create table, insert, query, delete)
- `requirements.txt` — Python dependencies
- `.env` — API keys and secrets (never commit this file)

## Coding conventions
- Keep functions small and focused — one function, one job
- Add a one-line comment above each function explaining what it does
- Never hardcode API keys or passwords; use `.env` and `os.getenv()`
- Use descriptive variable names (`habit_name`, not `h` or `x`)
- If something is not implemented yet, use a comment: `# TODO: add streak logic`

## Known issues / things to watch out for
[Anything the AI should know before touching this code. Examples:]
- The SQLite connection must be closed after each query to avoid locking issues
- Streamlit reruns the entire script on every interaction — do not store state in module-level variables; use `st.session_state`
- [Add your own project-specific notes here]
