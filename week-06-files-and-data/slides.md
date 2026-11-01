---
marp: true
theme: default
paginate: true
footer: "TECH 85 · Week 6 · Stanford Continuing Studies"
---

<!-- _class: lead -->
# Week 6: APIs, Auth & Security
### TECH 85: Vibe Coding
Stanford Continuing Studies · February 24

---

## Agenda

1. Recap: Project 2 and data persistence
2. What an API is — the restaurant analogy
3. How `requests` works in 5 lines
4. API key safety: the one rule
5. The `.env` pattern
6. Auth basics: what session tokens are
7. The security mindset
8. Lab + Project 2 demo format

---

## Recap: where we are

You now have:
- A Streamlit app with a SQLite database
- Data that persists between sessions
- A clean, agent-ready repo

Today you add the third layer: **external data**.

APIs let your app talk to the internet — get current weather, fetch news headlines, look up stock prices, translate text. Your app stops being a local tool and starts being connected.

With that connection comes responsibility: **API keys are passwords**.

---

## What an API is

**The restaurant analogy:**

You walk into a restaurant. You do not go into the kitchen, you do not see the recipes, and you do not cook the food yourself.

You tell the waiter what you want. The waiter goes to the kitchen. The kitchen prepares it. The waiter brings it back to you.

The waiter is the API.

You send a **request** (what you want).
You get back a **response** (the data).
You never see the code that runs on the other side.

OpenWeatherMap, NewsAPI, Google Maps, Stripe — they are all kitchens you talk to through a waiter.

---

## How `requests` works in 5 lines

```python
import requests

# 1. Build the URL with your parameters
url = "https://api.openweathermap.org/data/2.5/weather"
params = {"q": "San Francisco", "units": "imperial", "appid": api_key}

# 2. Make the request
response = requests.get(url, params=params, timeout=10)

# 3. Check that it worked (raises an error if status is 4xx or 5xx)
response.raise_for_status()

# 4. Get the data as a Python dictionary
data = response.json()

# 5. Extract what you need
temperature = data["main"]["temp"]
description = data["weather"][0]["description"]
```

That is an API integration. Five lines to get real-time weather data.

---

## The structure of an HTTP response

When you call `response.json()`, you get back a Python dictionary. For OpenWeatherMap it looks like:

```python
{
  "name": "San Francisco",
  "main": {
    "temp": 58.3,         # temperature in Fahrenheit (with units=imperial)
    "humidity": 72,
    "feels_like": 55.1
  },
  "weather": [
    {
      "description": "overcast clouds",
      "icon": "04d"
    }
  ]
}
```

You navigate this like any dictionary: `data["main"]["temp"]`, `data["weather"][0]["description"]`.

Ask Claude Code: *"Show me the structure of the JSON response for [API name] and how to extract [what you need]."*

---

## API key safety: the one rule

**An API key is a password. Treat it like one.**

If your API key gets onto GitHub:
- Bots scan GitHub continuously for exposed keys
- Within minutes, someone can run up charges on your account
- Many free-tier APIs will deactivate your key

The rule: **never put an API key in a code file.**

Wrong:
```python
api_key = "sk-proj-abc123def456"  # DO NOT DO THIS
```

Right:
```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")  # reads from .env file
```

---

## The `.env` pattern

A `.env` file is a plain text file that lives in your project folder. It holds your secrets.

**Your `.env` file:**
```
OPENWEATHER_API_KEY=abc123yourkeyhere
NEWS_API_KEY=def456anotherkeyhere
```

**Your `.gitignore` file must include:**
```
.env
```

This prevents the `.env` file from ever being uploaded to GitHub.

**Your Python code:**
```python
from dotenv import load_dotenv
import os

load_dotenv()  # reads .env and puts values into the environment
api_key = os.getenv("OPENWEATHER_API_KEY")
```

On Streamlit Cloud: add secrets in the app's Settings → Secrets tab instead.

---

## Never paste your key into a prompt

When you ask Claude Code to add an API integration, describe what you need — not the key itself.

**Wrong:**
> "Add OpenWeatherMap. My API key is sk-abc123def456."

**Right:**
> "Add OpenWeatherMap. Load the API key from a .env file using `os.getenv('OPENWEATHER_API_KEY')`. I will add the key to .env myself."

The prompt goes to an AI service. You do not know where it is logged. Treat API keys in prompts the same way you treat them in code: never put them there.

---

## Auth basics: what you actually need

Full OAuth (the "Sign in with Google" flow) is complex and overkill for personal projects.

Here are the two patterns that cover 95% of class projects:

**Pattern 1: No auth (personal tool)**
You are the only user. No login needed. The `.env` file is on your laptop; no one else can access your API key. Simpler is better.

**Pattern 2: Simple session token**
The user enters a password on a login page. Your app checks it against a stored hash. If it matches, store a flag in `st.session_state["logged_in"] = True`. Every page checks that flag.

This is not production-grade security — but it is appropriate for a class project that is not handling sensitive data.

Ask Claude Code: *"Add a simple password-protected login to my app. Store the password as a hash in my .env file, not in the code."*

---

## The security mindset

Before you deploy any app, ask yourself three questions:

**1. What is the worst thing a random person could do with this app?**
Can they see data that is not theirs? Can they trigger expensive API calls? Can they delete data?

**2. What happens if my API key is exposed?**
Is there a usage limit? Can someone run up charges? Does the API provider let you revoke and replace keys?

**3. What user input goes into my database or API calls?**
If a user types something malicious into a text field and your code passes it directly to a SQL query or API call, that is a vulnerability. Use parameterized queries (`?` placeholders) for SQL. Validate input before passing it to APIs.

You are not building a bank. But thinking through these questions now builds habits that matter later.

---

## Demo: API integration with .env safety

*[Live demo — instructor walks through:]*

1. Show a Project 2 app with no API yet
2. Create `.env` file with a key (show the file, blur the value)
3. Show `.gitignore` includes `.env`
4. Ask Claude Code to add the API call
5. Run the app — show real API data appearing
6. Enter a bad city name — show graceful error handling
7. Run `git status` — confirm `.env` is not staged

---

## Lab overview

**What you are doing today (65 min)**

| Part | Time | What you do |
|---|---|---|
| Part 1 | 25 min | Add an external API to your Project 2 app |
| Part 2 | 15 min | Audit for hardcoded secrets; update .gitignore; work through env_safety_guide.md |
| Part 3 | 15 min | Add a usage_log table to SQLite |
| Part 4 | 10 min | 3-minute Project 2 demo |

Reference files in `starter/`: `api_starter.py`, `env_safety_guide.md`

---

## Key takeaways

- An API is a waiter: you send a request, you get back data, you never see the kitchen
- `requests.get()` + `response.json()` is all you need for most API calls
- API keys are passwords: never in code, never in prompts, always in `.env`
- `.env` must be in `.gitignore` — verify this before every push
- Security mindset: what is the worst that could happen? Think it through.

---

## Reading for next week

**Before Wednesday, March 3:**

1. *Beyond Vibe Coding* — Chapters 9 and 10 (~25 min). These chapters cover the agent workflows and plan-first approach you will use in Week 7.

2. OWASP Top 10 at [owasp.org/Top10](https://owasp.org/Top10) (~5 min). Skim the list. You do not need to understand every item — just recognize that the issues you thought about today appear on a well-known security reference list.

**Also:** Come to Week 7 with a Capstone idea. The more ambitious the better. You will write the BRIEF.md in class.
