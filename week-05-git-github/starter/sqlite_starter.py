"""
Week 5 SQLite + Streamlit starter: a simple notes app.

This is a complete, runnable example of the full SQLite + Streamlit pattern.
It demonstrates all four CRUD operations (Create, Read, Update, Delete)
in a clean Streamlit UI.

Use this as a reference when adding a database to your own project.

Run it:
    pip install streamlit
    streamlit run sqlite_starter.py

TODO section at the bottom: tasks for students to extend this example.
"""

import sqlite3
import streamlit as st
from datetime import datetime

# -----------------------------------------------------------------------
# Configuration
# Change this to match your project's database file name.
# -----------------------------------------------------------------------
DB_FILE = "notes.db"


# -----------------------------------------------------------------------
# Database layer
# All database code lives here — separated from the UI code below.
# This separation keeps app.py readable and makes it easy to swap
# the database implementation later.
# -----------------------------------------------------------------------

def get_connection() -> sqlite3.Connection:
    """Open a connection to the SQLite database file."""
    return sqlite3.connect(DB_FILE)


def initialize_database() -> None:
    """Create the notes table if it does not already exist.

    Called once at startup. The IF NOT EXISTS clause means this is safe
    to call multiple times — it will not overwrite existing data.
    """
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            content    TEXT    NOT NULL,
            created_at TEXT    NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def add_note(content: str) -> None:
    """Insert a new note into the database."""
    conn = get_connection()
    conn.execute(
        "INSERT INTO notes (content, created_at) VALUES (?, ?)",
        (content, datetime.now().isoformat()),
    )
    conn.commit()
    conn.close()


def get_all_notes() -> list[dict]:
    """Return all notes, newest first."""
    conn = get_connection()
    rows = conn.execute(
        "SELECT id, content, created_at FROM notes ORDER BY created_at DESC"
    ).fetchall()
    conn.close()
    # Convert tuples to dictionaries for easier access in the UI layer
    return [{"id": r[0], "content": r[1], "created_at": r[2]} for r in rows]


def delete_note(note_id: int) -> None:
    """Delete a note by its ID."""
    conn = get_connection()
    conn.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    conn.close()


# -----------------------------------------------------------------------
# Streamlit UI
# All user-interface code lives here. The database functions above
# are called from here, but the UI layer does not know or care how
# the database works — it just calls functions and displays results.
# -----------------------------------------------------------------------

def main() -> None:
    st.title("My Notes")
    st.caption("A simple app to add, view, and delete notes. Data is stored in SQLite.")

    # Initialize the database on the very first run
    initialize_database()

    # --- Add a new note ---
    st.subheader("Add a Note")
    new_note = st.text_area("What do you want to save?", height=100, key="new_note_input")
    if st.button("Save Note", type="primary"):
        if new_note.strip():
            add_note(new_note.strip())
            st.success("Note saved.")
            st.rerun()  # Refresh the page so the new note appears in the list below
        else:
            st.warning("Please type something before saving.")

    st.divider()

    # --- Show all notes ---
    st.subheader("Your Notes")
    notes = get_all_notes()

    if not notes:
        st.info("No notes yet. Add one above.")
    else:
        st.caption(f"{len(notes)} note(s) saved.")
        for note in notes:
            # Display each note in a bordered container
            with st.container(border=True):
                col1, col2 = st.columns([5, 1])
                with col1:
                    st.write(note["content"])
                    st.caption(f"Saved: {note['created_at'][:16].replace('T', ' ')}")
                with col2:
                    # Each delete button needs a unique key to avoid Streamlit conflicts
                    if st.button("Delete", key=f"del_{note['id']}"):
                        delete_note(note["id"])
                        st.rerun()


# -----------------------------------------------------------------------
# TODO: extend this example
#
# Here are tasks for you to try with Claude Code's help:
#
# 1. Add a "title" field to each note (a short label, separate from the content)
#    Ask Claude Code: "Add a title column to the notes table and update the UI
#    to show a text input for the title."
#
# 2. Add a search bar that filters notes by content
#    Ask Claude Code: "Add a search box at the top. When the user types,
#    only show notes whose content contains the search term."
#
# 3. Add a second table for your Project 2 data
#    Ask Claude Code: "I'm building a [describe your project]. Add a new
#    table called [your table name] with columns [describe your columns].
#    Add CRUD functions for it."
#
# 4. Add tags to notes (work, personal, idea)
#    Ask Claude Code: "Add a tag field to each note. Let the user pick
#    from: work, personal, idea. Show the tag as a colored badge next to
#    each note in the list."
# -----------------------------------------------------------------------

if __name__ == "__main__":
    main()
