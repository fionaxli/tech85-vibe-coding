# Week 6: APIs, Auth & Security
**TECH 85 · February 24 · Stanford Continuing Studies**

## Session Goals

- Connect your Project 2 app to an external API using Claude Code
- Move all secrets to a `.env` file and verify nothing sensitive is in your code
- Add a basic usage log to your app using SQLite

## Before Class

- Bring your Project 2 project with the SQLite database working from Week 5
- If you want to use OpenWeatherMap (Track A): create a free account at [openweathermap.org](https://openweathermap.org/api) and get a free API key. It takes about 2 minutes.
- If you want to use NewsAPI (Track B): create a free account at [newsapi.org](https://newsapi.org) and get a free API key.
- If you are doing Track C, choose a free public API. Good starting point: [public-apis.io](https://public-apis.io)

## Concepts (20 min)

- **What an API is:** An API (Application Programming Interface) is how software talks to other software over the internet. Think of a restaurant: you do not go into the kitchen — you tell the waiter what you want, and the kitchen prepares it. The waiter is the API. You send a request; you get back data. You never see the code that runs on the other side.
- **How `requests` works:** Python's `requests` library makes HTTP calls. In five lines you can ask OpenWeatherMap for the current weather, get back a JSON response, and extract the temperature. That is all an API integration is.
- **API key safety — the rule:** An API key is a password. Treat it like one. Never paste it into your code. Never include it in a prompt to Claude Code (describe what you need, not the key value). Store it in a `.env` file. The `.env` file should be in your `.gitignore` so it never gets uploaded to GitHub.
- **Basic auth patterns:** Full OAuth (the "Sign in with Google" flow) is complex. For your projects, you need something simpler: either no auth (personal tool, you are the only user) or a session-based pattern (user logs in once, gets a token that lives in their browser session). Week 7 goes deeper on agents and auth; today you learn the basics.
- **Security mindset:** What are the worst things that could happen if your app were public? Could a user see data that is not theirs? Could someone extract your API key from the browser? Could a malicious input crash your database? Thinking through these questions — even for a class project — builds a habit that matters when you build for real.

## Lab (65 min)

### Part 1: Add an external API to your Project 2 app (25 min)

1. Open your Project 2 folder with Claude Code.
2. Create a `.env` file (do not commit this):
   ```
   OPENWEATHER_API_KEY=your_actual_key_here
   ```
3. Ask Claude Code to add the API integration:
   > "Add an OpenWeatherMap API integration to my app. When the user enters a city name and clicks Search, fetch the current weather (temperature in Fahrenheit, description, humidity) and display it. Load the API key from a .env file using python-dotenv. Handle errors gracefully — if the city is not found, show a friendly message instead of crashing."
4. Run the app locally and test it with a real city name.
5. Test the error case: enter a city name that does not exist. Does it fail gracefully?

See `starter/api_starter.py` for a complete working reference example.

### Part 2: Move all secrets to .env and audit your code (15 min)

1. Ask Claude Code to audit your code for any hardcoded secrets:
   > "Read all my Python files. Look for any API keys, passwords, or hardcoded credentials. If you find any, move them to .env and update the code to use os.getenv() instead."
2. Check your `.gitignore`. It should include `.env`. Ask Claude Code to verify:
   > "Read my .gitignore and make sure .env is listed. If it is not, add it."
3. Open `starter/env_safety_guide.md` and work through the checklist.
4. Run `git status` — make sure `.env` does not appear in the list of files to commit.

**The rule, restated:** If a value would be a problem if it appeared on GitHub, it belongs in `.env`, not in your code.

### Part 3: Add a simple usage log (15 min)

A usage log records what your app does — which searches were run, when. This is useful for debugging and for understanding how the app is used.

Ask Claude Code:
> "Add a `usage_log` table to my SQLite database. Each time the user makes an API call, insert a row recording: the query (e.g., the city name), the timestamp, and whether the call succeeded. Add a simple log viewer in the sidebar that shows the last 10 entries."

Run the app, make a few API calls, then check the log to confirm entries are being recorded.

### Part 4: 3-minute Project 2 demo (10 min)

Same format as Week 3:
1. Show your live app at its Streamlit Cloud URL (make sure you have deployed this week's changes)
2. Demonstrate the API integration working with a real example
3. Show one thing you added this week that you are proud of
4. Share one thing you would add if you had more time

## Project Milestone

**Project 2 complete.** Submit to Canvas:
1. Your live Streamlit Cloud URL (updated with this week's API integration)
2. A link to your GitHub repository
3. Two sentences: what the API adds to your app and what you learned about security

## Reading for Next Week

1. *Beyond Vibe Coding* — Chapters 9 and 10 (~25 min). These chapters cover agent workflows and the plan-first pattern you will use in Week 7.

2. OWASP Top 10 for beginners at [owasp.org/Top10](https://owasp.org/Top10) (~5 min). Skim the list — you do not need to understand every item, but recognize that the issues you thought about today (hardcoded keys, unchecked input) appear on this list. Security thinking is not a separate skill; it is part of building anything.
