"""
Week 3 review exercise: a realistic Streamlit app with file I/O, an API call,
and data processing. This is the kind of code Claude Code might generate for you.

Your job: read it with the safety_checklist.md and explain what each section does.
You do not need to understand every line — you need to understand what it does.

Run it:
    pip install streamlit requests
    streamlit run review_me.py
"""

import json
import os
import sqlite3
import requests
import streamlit as st
from datetime import datetime

# -----------------------------------------------------------------------
# Database setup
# Creates the SQLite database and the notes table if they do not exist yet.
# The database file is stored in the same folder as this script.
# -----------------------------------------------------------------------

DB_PATH = "notes.db"


def get_connection():
    """Open a connection to the SQLite database."""
    return sqlite3.connect(DB_PATH)


def initialize_database():
    """Create the notes table if it does not already exist."""
    conn = get_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS notes (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            title     TEXT    NOT NULL,
            content   TEXT    NOT NULL,
            tag       TEXT    DEFAULT '',
            created_at TEXT   NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


# -----------------------------------------------------------------------
# Database helpers: the four CRUD operations
# CRUD = Create, Read, Update, Delete
# -----------------------------------------------------------------------

def add_note(title: str, content: str, tag: str) -> None:
    """Insert a new note into the database."""
    conn = get_connection()
    conn.execute(
        "INSERT INTO notes (title, content, tag, created_at) VALUES (?, ?, ?, ?)",
        (title, content, tag, datetime.now().isoformat()),
    )
    conn.commit()
    conn.close()


def get_all_notes() -> list[dict]:
    """Return all notes from the database, newest first."""
    conn = get_connection()
    cursor = conn.execute(
        "SELECT id, title, content, tag, created_at FROM notes ORDER BY created_at DESC"
    )
    rows = cursor.fetchall()
    conn.close()
    # Convert each row (a tuple) into a dictionary so it is easier to work with
    return [
        {"id": r[0], "title": r[1], "content": r[2], "tag": r[3], "created_at": r[4]}
        for r in rows
    ]


def delete_note(note_id: int) -> None:
    """Delete a note by its ID."""
    conn = get_connection()
    conn.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    conn.close()


def search_notes(query: str) -> list[dict]:
    """Return notes whose title or content contains the search query."""
    conn = get_connection()
    cursor = conn.execute(
        "SELECT id, title, content, tag, created_at FROM notes "
        "WHERE title LIKE ? OR content LIKE ? "
        "ORDER BY created_at DESC",
        (f"%{query}%", f"%{query}%"),
    )
    rows = cursor.fetchall()
    conn.close()
    return [
        {"id": r[0], "title": r[1], "content": r[2], "tag": r[3], "created_at": r[4]}
        for r in rows
    ]


# -----------------------------------------------------------------------
# API call: fetch a random motivational quote
# This function makes a network request to an external service.
# NOTE: this is a place to review when using safety_checklist.md.
# -----------------------------------------------------------------------

def fetch_quote() -> str:
    """Fetch a random quote from the ZenQuotes API. Returns a fallback string on failure."""
    try:
        # This makes an HTTP GET request to an external URL
        response = requests.get("https://zenquotes.io/api/random", timeout=5)
        response.raise_for_status()
        data = response.json()
        return f'"{data[0]["q"]}" — {data[0]["a"]}'
    except Exception:
        # If the API is unavailable, return a hardcoded fallback
        return '"Write it down. Written goals have a way of transforming themselves into action." — Unknown'


# -----------------------------------------------------------------------
# Export helper: write notes to a JSON file
# NOTE: this writes a file to disk — another item for safety_checklist.md.
# -----------------------------------------------------------------------

def export_notes_to_json(notes: list[dict]) -> str:
    """Write all notes to a JSON file and return the file path."""
    export_path = "notes_export.json"
    with open(export_path, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=2)
    return export_path


# -----------------------------------------------------------------------
# Streamlit UI
# Everything below is the user interface. Streamlit reruns this entire
# script on every user interaction, so all state must go in st.session_state.
# -----------------------------------------------------------------------

def main():
    st.title("My Notes App")
    st.caption("A simple note-taking tool with search, tags, and export.")

    # Initialize the database on first run
    initialize_database()

    # --- Sidebar: add a new note ---
    with st.sidebar:
        st.header("Add a Note")
        new_title = st.text_input("Title")
        new_content = st.text_area("Content", height=120)
        new_tag = st.selectbox("Tag", ["", "work", "personal", "idea", "todo"])
        if st.button("Save Note", type="primary"):
            if new_title.strip() and new_content.strip():
                add_note(new_title.strip(), new_content.strip(), new_tag)
                st.success("Note saved.")
                st.rerun()
            else:
                st.error("Please fill in both the title and content.")

        st.divider()

        # Export button: writes a file to disk
        if st.button("Export All Notes to JSON"):
            all_notes = get_all_notes()
            if all_notes:
                path = export_notes_to_json(all_notes)
                st.success(f"Exported {len(all_notes)} notes to {path}")
            else:
                st.info("No notes to export yet.")

    # --- Main area: search and display notes ---
    search_query = st.text_input("Search notes", placeholder="Type to search by title or content...")

    if search_query:
        notes = search_notes(search_query)
    else:
        notes = get_all_notes()

    # --- Quote of the day ---
    with st.expander("Quote of the Day"):
        if st.button("Fetch a new quote"):
            st.session_state["quote"] = fetch_quote()
        if "quote" not in st.session_state:
            st.session_state["quote"] = fetch_quote()
        st.write(st.session_state["quote"])

    st.divider()

    # --- Display notes ---
    if not notes:
        st.info("No notes yet. Add one using the sidebar.")
    else:
        st.write(f"{len(notes)} note(s) found.")
        for note in notes:
            with st.expander(f"{note['title']}  {'#' + note['tag'] if note['tag'] else ''}"):
                st.write(note["content"])
                st.caption(f"Saved: {note['created_at'][:10]}")
                if st.button("Delete", key=f"delete_{note['id']}"):
                    delete_note(note["id"])
                    st.rerun()


if __name__ == "__main__":
    main()
