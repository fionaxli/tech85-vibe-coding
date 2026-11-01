"""
Week 6 API starter: a Streamlit app that calls the OpenWeatherMap API.

This is a complete, runnable reference example. It shows:
  - Loading an API key safely from a .env file
  - Making an API call with the requests library
  - Handling errors gracefully (city not found, network down, bad key)
  - Displaying results in a clean Streamlit UI
  - Storing results in SQLite

Run it:
    pip install streamlit requests python-dotenv
    streamlit run api_starter.py

Before running, create a .env file in the same folder:
    OPENWEATHER_API_KEY=your_actual_key_here

Get a free API key at: https://openweathermap.org/api
(free tier allows 1,000 calls/day — more than enough for this course)

TODO stubs at the bottom: tasks for connecting your own API.
"""

import os
import sqlite3
from datetime import datetime

import requests
import streamlit as st
from dotenv import load_dotenv

# -----------------------------------------------------------------------
# Load secrets from .env
# This must be called before any os.getenv() calls.
# On Streamlit Cloud, secrets come from the Settings → Secrets tab instead.
# -----------------------------------------------------------------------
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

DB_FILE = "weather_log.db"
OPENWEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


# -----------------------------------------------------------------------
# Database: log every API call
# -----------------------------------------------------------------------

def initialize_database() -> None:
    """Create the weather_log table if it does not exist."""
    conn = sqlite3.connect(DB_FILE)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS weather_log (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            city       TEXT    NOT NULL,
            temp_f     REAL,
            description TEXT,
            success    INTEGER NOT NULL,  -- 1 = success, 0 = failure
            queried_at TEXT    NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def log_query(city: str, temp_f: float | None, description: str | None, success: bool) -> None:
    """Record an API call in the database."""
    conn = sqlite3.connect(DB_FILE)
    conn.execute(
        "INSERT INTO weather_log (city, temp_f, description, success, queried_at) VALUES (?, ?, ?, ?, ?)",
        (city, temp_f, description, 1 if success else 0, datetime.now().isoformat()),
    )
    conn.commit()
    conn.close()


def get_recent_queries(limit: int = 10) -> list[dict]:
    """Return the most recent API calls from the log."""
    conn = sqlite3.connect(DB_FILE)
    rows = conn.execute(
        "SELECT city, temp_f, description, success, queried_at FROM weather_log "
        "ORDER BY queried_at DESC LIMIT ?",
        (limit,),
    ).fetchall()
    conn.close()
    return [
        {"city": r[0], "temp_f": r[1], "description": r[2],
         "success": bool(r[3]), "queried_at": r[4]}
        for r in rows
    ]


# -----------------------------------------------------------------------
# API call: fetch weather from OpenWeatherMap
# -----------------------------------------------------------------------

def get_weather(city: str) -> dict | None:
    """Fetch current weather for a city.

    Returns a dictionary with temperature, description, and humidity,
    or None if the call fails.
    Errors are returned as strings in the 'error' key.
    """
    if not API_KEY:
        return {"error": "API key not found. Add OPENWEATHER_API_KEY to your .env file."}

    try:
        response = requests.get(
            OPENWEATHER_BASE_URL,
            params={"q": city, "units": "imperial", "appid": API_KEY},
            timeout=10,
        )

        # 404 means the city was not found
        if response.status_code == 404:
            return {"error": f"City '{city}' not found. Check the spelling and try again."}

        # 401 means the API key is wrong
        if response.status_code == 401:
            return {"error": "Invalid API key. Check your OPENWEATHER_API_KEY in .env."}

        # Raise an exception for any other 4xx or 5xx status
        response.raise_for_status()

        data = response.json()
        return {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temp_f": round(data["main"]["temp"], 1),
            "feels_like_f": round(data["main"]["feels_like"], 1),
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"].capitalize(),
            "icon_code": data["weather"][0]["icon"],
        }

    except requests.exceptions.ConnectionError:
        return {"error": "Could not connect. Check your internet connection."}
    except requests.exceptions.Timeout:
        return {"error": "The request timed out. Try again in a moment."}
    except Exception as e:
        return {"error": f"Something went wrong: {str(e)}"}


# -----------------------------------------------------------------------
# Streamlit UI
# -----------------------------------------------------------------------

def main() -> None:
    st.title("Weather Lookup")
    st.caption("Powered by OpenWeatherMap. API key loaded from .env.")

    initialize_database()

    # Warn if the API key is missing
    if not API_KEY:
        st.error(
            "No API key found. Create a `.env` file in this folder with: "
            "`OPENWEATHER_API_KEY=your_key_here`"
        )

    # --- Search form ---
    with st.form("weather_form"):
        city_input = st.text_input("Enter a city name", placeholder="e.g., San Francisco")
        submitted = st.form_submit_button("Get Weather", type="primary")

    if submitted and city_input.strip():
        city = city_input.strip()
        with st.spinner(f"Looking up {city}..."):
            result = get_weather(city)

        if "error" in result:
            st.error(result["error"])
            log_query(city, None, None, success=False)
        else:
            # Display the weather result
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Temperature", f"{result['temp_f']}°F")
            with col2:
                st.metric("Feels Like", f"{result['feels_like_f']}°F")
            with col3:
                st.metric("Humidity", f"{result['humidity']}%")

            st.write(f"**{result['city']}, {result['country']}** — {result['description']}")
            log_query(city, result["temp_f"], result["description"], success=True)

    # --- Recent queries log in sidebar ---
    with st.sidebar:
        st.subheader("Recent Searches")
        recent = get_recent_queries()
        if not recent:
            st.caption("No searches yet.")
        else:
            for entry in recent:
                status = "OK" if entry["success"] else "failed"
                temp_str = f"{entry['temp_f']}°F" if entry["temp_f"] else "—"
                st.caption(
                    f"{entry['queried_at'][:16]}  |  {entry['city']}  |  "
                    f"{temp_str}  |  {status}"
                )


# -----------------------------------------------------------------------
# TODO: connect your own API
#
# To adapt this starter for a different API:
#
# 1. Replace the get_weather() function with a function that calls your API.
#    The pattern is the same:
#      - Load your API key from .env with os.getenv("YOUR_API_KEY")
#      - Use requests.get(url, params={...}, timeout=10)
#      - Handle errors (404, 401, connection errors)
#      - Return a dictionary of the data you need
#
# 2. Update the database schema in initialize_database() to store the
#    fields that matter for your API.
#
# 3. Update the Streamlit UI to show the data from your API.
#
# Ask Claude Code:
# "Replace the OpenWeatherMap call with a call to [your API]. Keep the
#  same .env pattern for the API key and the same error handling structure."
# -----------------------------------------------------------------------

if __name__ == "__main__":
    main()
