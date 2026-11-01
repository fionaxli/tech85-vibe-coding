"""
Week 7 research agent starter: demonstrates the plan-first pattern.

This script shows how to structure a multi-step agent task:
  1. Ask for a plan before writing code
  2. Execute the plan step by step
  3. Save results to SQLite

The example here: a simple research tool that fetches quotes on a topic,
extracts the key ideas, and saves them to a database for review.

This is a simplified version of a real research agent. The important
thing is the STRUCTURE — not the specific task.

Run it:
    pip install streamlit requests
    streamlit run research_agent_starter.py

--- HOW THE PLAN-FIRST PATTERN IS SHOWN IN THIS FILE ---

Look for comments marked with [PLAN STEP N] throughout the code.
Each section corresponds to one step of a plan that Claude Code
would have written before building this file.

The plan was:
  Step 1: Define the database schema and create the table
  Step 2: Write a function to fetch data from a public API
  Step 3: Write a function to extract the key idea from a result
  Step 4: Write a function to save results to the database
  Step 5: Build the Streamlit UI that ties it all together
  Step 6: Test each step in isolation before connecting them

Notice: each step is a separate function with a clear, testable contract.
"""

import sqlite3
import requests
import streamlit as st
from datetime import datetime

DB_FILE = "research.db"


# -----------------------------------------------------------------------
# [PLAN STEP 1] Database: schema and initialization
#
# Plan note: "Create a research_results table. Each row stores:
# the search query, the source URL, a key idea extracted from the result,
# and the timestamp. The id is auto-assigned."
# -----------------------------------------------------------------------

def initialize_database() -> None:
    """Create the research_results table if it does not already exist."""
    conn = sqlite3.connect(DB_FILE)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS research_results (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            query       TEXT    NOT NULL,
            source      TEXT    NOT NULL,
            key_idea    TEXT    NOT NULL,
            saved_at    TEXT    NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def save_result(query: str, source: str, key_idea: str) -> None:
    """Save one research result to the database."""
    conn = sqlite3.connect(DB_FILE)
    conn.execute(
        "INSERT INTO research_results (query, source, key_idea, saved_at) VALUES (?, ?, ?, ?)",
        (query, source, key_idea, datetime.now().isoformat()),
    )
    conn.commit()
    conn.close()


def get_saved_results(limit: int = 20) -> list[dict]:
    """Return the most recent saved results."""
    conn = sqlite3.connect(DB_FILE)
    rows = conn.execute(
        "SELECT query, source, key_idea, saved_at FROM research_results "
        "ORDER BY saved_at DESC LIMIT ?",
        (limit,),
    ).fetchall()
    conn.close()
    return [{"query": r[0], "source": r[1], "key_idea": r[2], "saved_at": r[3]} for r in rows]


# -----------------------------------------------------------------------
# [PLAN STEP 2] Fetch data from a public API
#
# Plan note: "Use the ZenQuotes API (free, no key required) to fetch
# quotes on a topic. Return a list of (quote, author) tuples.
# Handle network errors gracefully."
# -----------------------------------------------------------------------

def fetch_quotes(topic: str) -> list[dict]:
    """Fetch quotes that may be relevant to the given topic.

    Note: ZenQuotes does not support topic filtering in the free tier —
    this returns random quotes as a stand-in for a real search API.
    For a real research agent, replace this function with a call to
    a search API (e.g., DuckDuckGo, Brave Search, or a news API).
    """
    try:
        # Fetch a set of quotes to simulate search results
        response = requests.get("https://zenquotes.io/api/quotes", timeout=10)
        response.raise_for_status()
        data = response.json()
        # Return the first 5 as our "search results"
        return [{"text": item["q"], "author": item["a"], "url": "zenquotes.io"} for item in data[:5]]
    except requests.exceptions.ConnectionError:
        return []
    except Exception:
        return []


# -----------------------------------------------------------------------
# [PLAN STEP 3] Extract the key idea from a result
#
# Plan note: "Write a function that takes a result (quote + author)
# and formats it as a key idea. In a real agent, this would call
# Claude to summarize. Here we format it directly."
#
# TODO: for your Capstone, replace this with a real summarization call.
# You could call Claude API here:
# "Summarize this result in one sentence: [paste result text]"
# -----------------------------------------------------------------------

def extract_key_idea(result: dict, query: str) -> str:
    """Format a result as a key idea sentence.

    In a production agent, this function would call an LLM to summarize
    the result in the context of the query. For this starter, we format
    the quote directly.

    TODO: replace with a real summarization call for your Capstone.
    """
    return f'"{result["text"]}" — {result["author"]}'


# -----------------------------------------------------------------------
# [PLAN STEP 4] The agent function: orchestrate steps 2 and 3
#
# Plan note: "Create a run_research() function that:
# 1. Calls fetch_quotes()
# 2. For each result, calls extract_key_idea()
# 3. Returns a list of (source, key_idea) tuples"
# -----------------------------------------------------------------------

def run_research(query: str) -> list[dict]:
    """Run the research pipeline for a query.

    This is the orchestration layer: it calls the fetch and extract
    functions in the right order and assembles the results.
    """
    raw_results = fetch_quotes(query)
    if not raw_results:
        return []

    processed = []
    for result in raw_results:
        key_idea = extract_key_idea(result, query)
        processed.append({
            "source": result["url"],
            "key_idea": key_idea,
        })
    return processed


# -----------------------------------------------------------------------
# [PLAN STEP 5] Streamlit UI
#
# Plan note: "Build a two-panel UI:
# - Left panel (sidebar): run a new research query
# - Main panel: show saved results with search/filter"
# -----------------------------------------------------------------------

def main() -> None:
    st.title("Research Agent")
    st.caption(
        "A plan-first example: fetch information, extract key ideas, save to database. "
        "See the code comments for how this maps to the plan-first pattern."
    )

    initialize_database()

    # --- Sidebar: run research ---
    with st.sidebar:
        st.header("New Research")
        query = st.text_input("Topic or question", placeholder="e.g., resilience, creativity")
        if st.button("Run Research", type="primary"):
            if query.strip():
                with st.spinner("Researching..."):
                    results = run_research(query.strip())
                if results:
                    for r in results:
                        save_result(query.strip(), r["source"], r["key_idea"])
                    st.success(f"Saved {len(results)} results.")
                    st.rerun()
                else:
                    st.warning("No results found. Check your internet connection.")
            else:
                st.warning("Enter a topic to research.")

    # --- Main panel: saved results ---
    st.subheader("Saved Research")
    saved = get_saved_results()
    if not saved:
        st.info("No research saved yet. Run a query in the sidebar.")
    else:
        for item in saved:
            with st.container(border=True):
                st.write(item["key_idea"])
                st.caption(f"Query: {item['query']}  |  {item['saved_at'][:16]}")


# -----------------------------------------------------------------------
# [PLAN STEP 6] How to extend this with the plan-first pattern
#
# To add a real search API (instead of random quotes), ask Claude Code:
#
#   "I want to replace the fetch_quotes() function with a call to the
#    DuckDuckGo Instant Answer API. Before you write any code, write a
#    numbered plan of what needs to change. Include: which files change,
#    which functions are affected, and what could go wrong."
#
# Review the plan. Edit it. Then say: "Execute this plan, one step at a
# time. Pause after each step and tell me what you did."
# -----------------------------------------------------------------------

if __name__ == "__main__":
    main()
