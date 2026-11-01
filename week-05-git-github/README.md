# Week 5: Data & Agent-Ready Repos
**TECH 85 · February 17 · Stanford Continuing Studies**

## Session Goals

- Add SQLite to an existing Streamlit app so data persists between sessions
- Design a data schema for Project 2 with Claude Code's help
- Structure your repository so Claude Code can work effectively every session

## Before Class

- Bring your Project 1 project folder with a working app
- Make sure Git is set up from Week 4 (your project should have at least one commit)
- Think about what you want to build for Project 2 — it will use SQLite and an external API. Track A is a local weather journal, Track B is a news digest saver. Come with a rough idea.

## Concepts (20 min)

- **SQLite for data persistence:** SQLite is a database that lives in a single file on your computer. No server to set up, no cloud account required. It is built into Python — no installation needed. When your Streamlit app uses SQLite, data persists between sessions: close the browser, open it tomorrow, your data is still there. This is the difference between a toy and a real tool.
- **What "full stack" means in vibe coding:** Frontend = Streamlit (what the user sees). Backend = Python logic. Database = SQLite. All three on your laptop. That is a full stack application, and you are building one.
- **Agent-ready repo structure:** Claude Code works best when your repository is clean and self-describing. That means: a CLAUDE.md at the root, sensibly named files, a clear README, and no mystery files. An agent-ready repo is one where Claude Code can read CLAUDE.md and immediately understand how to help without you re-explaining everything.
- **Schema design:** A schema is the structure of your database — which tables you have, which columns each table has, and what type of data each column holds. Claude Code can help you design a good schema if you describe your data clearly.

## Lab (65 min)

### Part 1: Add SQLite to your Project 1 app (25 min)

Your Project 1 app probably stores data in Python variables (lists, dictionaries). That means data disappears when the app restarts. Today you add a database.

1. Open your Project 1 project in VS Code and Claude Code.
2. Ask Claude Code:
   > "My app currently stores data in Python variables. Add SQLite to it so data persists between sessions. Create a `db.py` file with helper functions for the database, and update `app.py` to use them. Use the built-in `sqlite3` module — no new packages required."
3. Run the app locally. Add some data. Restart the app. Verify the data is still there.
4. Look at `starter/sqlite_starter.py` to see a reference implementation of the SQLite + Streamlit pattern.

**Common issue:** Streamlit reruns the whole script on every interaction. Make sure your database initialization (the `CREATE TABLE IF NOT EXISTS` call) only runs once, not on every rerun. Ask Claude Code: *"Make sure the database is only initialized once, not on every Streamlit rerun."*

### Part 2: Design a schema for Project 2 (20 min)

Before you write any code for Project 2, design the data model.

1. Open `starter/schema_design_prompt.md`. Follow the prompting guide.
2. Tell Claude Code what you are building and what data you need to store. Example:
   > "I'm building a weather journal. Each entry has: the city, the date, the temperature in Fahrenheit, the weather description (like 'sunny' or 'rainy'), and my personal notes about the day. Help me design a SQLite schema for this."
3. Review what Claude Code proposes. Ask follow-up questions:
   - "Should I store temperature as an integer or a float?"
   - "What index should I add to make searches fast?"
   - "How would I store multiple weather entries for the same city?"
4. Write the final agreed schema into a new file in your Project 2 folder: `schema.sql`. Ask Claude Code to generate it.

### Part 3: Make your repo agent-ready (20 min)

A repo is agent-ready when Claude Code can open it cold and know exactly what to do.

1. **Update your CLAUDE.md.** Open your Project 1 (or new Project 2) CLAUDE.md. Make sure it includes:
   - Project summary (2–3 sentences)
   - Tech stack including the database
   - File structure (what each file does)
   - Any known quirks Claude Code should know about
2. **Clean up your file names.** If you have files called `app_v2_final.py` or `test_copy.py`, ask Claude Code to help you consolidate:
   > "I have several app files. Help me figure out which is the main one and archive or delete the others."
3. **Add or update your README.md.** Ask Claude Code:
   > "Write a brief README.md for this project. Include: what it does, how to run it locally, and what Python packages are required."
4. **Commit everything:**
   ```
   git add .
   git commit -m "Make repo agent-ready: update CLAUDE.md, clean up files, add README"
   git push
   ```

## Project Milestone

**Project 2 launched.** By the end of today's class you should have:
- A Project 2 project folder with a schema.sql and a BRIEF.md
- Your Project 1 app updated to use SQLite (or Project 2 started from scratch with SQLite)
- A clean, agent-ready repo with an up-to-date CLAUDE.md

Submit your Project 2 BRIEF.md to Canvas before next class.

## Reading for Next Week

1. *Beyond Vibe Coding* — Chapter 8 (~20 min). This chapter covers external API integration and the security patterns you will use in Week 6.

2. Stanford CS146S "Agent-Ready Repos" at [themodernsoftware.dev/fall2025](https://themodernsoftware.dev/fall2025) (~10 min). This page covers the repo structure principles from today in more depth.
