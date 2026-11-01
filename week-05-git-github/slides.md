---
marp: true
theme: default
paginate: true
footer: "TECH 85 · Week 5 · Stanford Continuing Studies"
---

<!-- _class: lead -->
# Week 5: Data & Agent-Ready Repos
### TECH 85: Vibe Coding
Stanford Continuing Studies · February 17

---

## Agenda

1. Recap: Week 4 with Steve — key takeaways
2. What "full stack" means in vibe coding
3. SQLite in 60 seconds
4. Schema design with AI
5. What makes a repo agent-ready
6. Lab overview + Project 2 launch

---

## Recap: last week with Steve

Steve shared how AI tools fit into real software development. A few themes that came up:

- AI is excellent at the predictable parts; humans are still essential for judgment calls
- The size of an AI-generated change is a risk factor — smaller, more targeted prompts produce safer results
- Commit messages matter: future you (and future Claude Code) will thank you for specific ones

Today we apply those ideas to data persistence — which is where most beginner projects get stuck.

---

## The problem with variables

Your Project 1 app probably stores data like this:

```python
habits = []  # a Python list

def add_habit(name):
    habits.append(name)
```

This works while the app is running. Stop the app — data is gone. Restart — empty list.

This is fine for a demo. Not fine for a tool you use every day.

**The fix: a database.**

---

## What "full stack" means

Your apps now have three layers:

```
┌─────────────────────────────┐
│   Streamlit (frontend)      │  ← what the user sees and clicks
├─────────────────────────────┤
│   Python logic (backend)    │  ← functions that process data
├─────────────────────────────┤
│   SQLite (database)         │  ← where data lives between sessions
└─────────────────────────────┘
```

All three layers run on your laptop — or on Streamlit Cloud.

No cloud database subscription. No separate server. One Python file and one `.db` file. That is a full stack application.

---

## SQLite in 60 seconds

SQLite is a database that lives in a single file. Built into Python — no installation needed.

```python
import sqlite3

# Open (or create) the database file
conn = sqlite3.connect("myapp.db")

# Create a table
conn.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id         INTEGER PRIMARY KEY AUTOINCREMENT,
        content    TEXT NOT NULL,
        created_at TEXT NOT NULL
    )
""")
conn.commit()

# Insert a row
conn.execute("INSERT INTO notes (content, created_at) VALUES (?, ?)",
             ("My first note", "2026-02-17"))
conn.commit()

# Read all rows
rows = conn.execute("SELECT * FROM notes").fetchall()
conn.close()
```

That is it. No account. No configuration. Data persists as long as the `.db` file exists.

---

## The three SQL operations you actually need

**Insert:** add a row
```sql
INSERT INTO notes (content, created_at) VALUES (?, ?)
```

**Select:** read rows
```sql
SELECT id, content, created_at FROM notes ORDER BY created_at DESC
```

**Delete:** remove a row
```sql
DELETE FROM notes WHERE id = ?
```

You do not need to memorize these. Claude Code knows them. You need to know what they do.

The `?` placeholders are important — never build SQL by concatenating strings with user input.

---

## Schema design with AI

A schema is the blueprint for your database: which tables, which columns, which types.

Getting it right before you build saves a lot of refactoring.

The prompt formula:
> "I'm building [project]. I need to store [describe your data]. Help me design a SQLite schema. Show me the CREATE TABLE statements."

Then iterate:
- "Should the temperature be INTEGER or REAL?"
- "How do I handle the case where a user has multiple entries for the same date?"
- "What index should I add to make search fast?"

Claude Code is very good at schema design. Give it specific data — it will give you a clean schema.

---

## Schema design example

**Prompt:**
> "I'm building a weather journal. Each entry has: city name, date, temperature in Fahrenheit, a weather description, and my personal notes. Help me design a SQLite schema."

**Claude Code's response:**
```sql
CREATE TABLE IF NOT EXISTS weather_entries (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    city        TEXT    NOT NULL,
    entry_date  TEXT    NOT NULL,
    temp_f      REAL    NOT NULL,
    description TEXT    NOT NULL,
    notes       TEXT    DEFAULT '',
    created_at  TEXT    NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_city_date
    ON weather_entries (city, entry_date);
```

Follow-up: "What's the index for?" → "It makes queries that filter by city or date fast — without it, SQLite reads every row."

---

## What makes a repo agent-ready

An agent-ready repo is one where Claude Code can open it cold and immediately know what to do.

**Four things that make a repo agent-ready:**

1. **CLAUDE.md at the root** — project summary, tech stack, file structure, conventions
2. **Clear file names** — `app.py`, `db.py`, `schema.sql` not `app_v3_final_FINAL.py`
3. **A README.md** that explains what the project does and how to run it
4. **No mystery files** — if a file is not needed, delete or archive it

When Claude Code opens an agent-ready repo, it reads CLAUDE.md first. Everything in that file shapes every decision it makes for the rest of the session.

---

## The cost of an un-ready repo

When your repo is messy:
- Claude Code reads the wrong file and modifies something you did not mean to change
- It makes assumptions about how things are structured — sometimes wrong ones
- You spend the first 10 minutes of every session re-explaining what the project does

When your repo is clean:
- Claude Code reads CLAUDE.md, understands the project, starts working
- You can say "add a delete button" and it knows exactly which file to edit
- Coming back after two weeks away is not a mystery

Clean repos are faster to develop. They are also much easier for other people (or future you) to understand.

---

## Project 2: launched today

**Track A — Local Weather Journal**
Log daily weather with notes. Pull current conditions from OpenWeatherMap. Store entries in SQLite. Search by city or date.

**Track B — News Digest Saver**
Fetch today's top headlines from NewsAPI for topics you care about. Save articles to SQLite. Mark ones you have read.

**Track C — Bring your own**
Your Project 2 must use SQLite and at least one external API. Come with a BRIEF.md.

By end of class: Project 2 BRIEF.md written and schema.sql designed.

---

## Lab overview

**What you are doing today (65 min)**

| Part | Time | What you do |
|---|---|---|
| Part 1 | 25 min | Add SQLite to your Project 1 app (or start Project 2 with SQLite) |
| Part 2 | 20 min | Design a schema for Project 2 with Claude Code |
| Part 3 | 20 min | Make your repo agent-ready: CLAUDE.md, clean names, README, commit |

Reference files in `starter/`: `sqlite_starter.py`, `schema_design_prompt.md`, `git_cheatsheet.md`

---

## Key takeaways

- SQLite is a database in a file — no server, no account, built into Python
- The three SQL operations you need: INSERT, SELECT, DELETE
- Schema design is a collaboration: describe your data to Claude Code, iterate on the result
- An agent-ready repo has: CLAUDE.md, clear file names, a README, no mystery files
- Full stack = Streamlit + Python + SQLite. All on your laptop.

---

## Reading for next week

**Before Wednesday, February 24:**

1. *Beyond Vibe Coding* — Chapter 8 (~20 min). Covers API integration and security patterns for Week 6.

2. Stanford CS146S "Agent-Ready Repos" at [themodernsoftware.dev/fall2025](https://themodernsoftware.dev/fall2025) (~10 min)

**Also:** Make progress on Project 2 this week. The API integration lab in Week 6 will go faster if you already have the basic app structure in place.
