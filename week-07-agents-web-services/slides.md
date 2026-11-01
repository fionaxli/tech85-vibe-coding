---
marp: true
theme: default
paginate: true
footer: "TECH 85 · Week 7 · Stanford Continuing Studies"
---

<!-- _class: lead -->
# Week 7: Small Agents and Web Services
### TECH 85: Vibe Coding
Stanford Continuing Studies · Mar 2, 2027

---

## Agenda

1. What an API is (and the restaurant analogy)
2. Making HTTP requests in Python
3. The Anthropic API: calling Claude from code
4. Environment variables and API key safety
5. What "agent" means
6. Demo: building the research helper live
7. Lab: fill in the three TODOs

---

## Up to Now

Everything you have built reads files from your own computer and prints results.

Today we connect to the outside world:
- Wikipedia API — fetch information from the web
- Anthropic API — call Claude from your code (not the browser)

By the end of this session you will have a tool that *goes out and gets information*, then *thinks about it*, then *gives you an answer*. That is an agent.

---

## What Is an API?

**API = Application Programming Interface**

The restaurant analogy:
- You do not go into the kitchen and cook
- You look at the menu (the documentation)
- You place an order (send a request)
- You receive the food (get a response)

Every major web service has an API: maps, weather, Wikipedia, Spotify, Google Translate, Anthropic. They all follow the same basic pattern.

---

## HTTP Requests in Plain English

Your browser makes HTTP requests all day long — every time you load a page.

Your code can do the same:

```python
import requests

# GET means "give me information"
response = requests.get("https://en.wikipedia.org/api/rest_v1/page/summary/Python")

# Check if it worked
print(response.status_code)   # 200 = success, 404 = not found

# Get the response data
data = response.json()
print(data["extract"])        # the plain-English Wikipedia summary
```

That is it. Two lines to get information from the internet.

---

## The Anthropic API

Claude lives on Anthropic's servers. Your code can talk to it.

```python
import anthropic

client = anthropic.Anthropic()   # reads API key from ANTHROPIC_API_KEY env var

message = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Explain photosynthesis in two sentences."}
    ]
)

print(message.content[0].text)
```

This is exactly what Claude.ai does under the hood — it is just a call to this same API.

---

## API Keys: The Rule

> **Never put your API key in a code file.**

If you commit it to GitHub, anyone can find it and use your account.

**The right way — environment variable:**
```bash
# Mac/Linux (in terminal)
export ANTHROPIC_API_KEY="sk-ant-your-key-here"

# Windows (in terminal)
set ANTHROPIC_API_KEY=sk-ant-your-key-here
```

**Or use a `.env` file** (already listed in `.gitignore`):
```
ANTHROPIC_API_KEY=sk-ant-your-key-here
```

```python
from dotenv import load_dotenv
load_dotenv()   # reads .env, sets env vars
```

---

## What Is an Agent?

An agent is a program that uses an AI model to take multi-step actions.

The simplest agent loop:

```
User asks a question
       ↓
Agent fetches relevant information (e.g., Wikipedia)
       ↓
Agent sends information + question to Claude
       ↓
Claude generates an answer
       ↓
Agent returns the answer to the user
```

"Agent" sounds futuristic. The reality is: it is just a loop where the AI decides what to do next based on what it sees.

---

## Today's Agent: The Research Helper

```python
def research_helper(question: str) -> str:
    # Step 1: search Wikipedia
    context = search_wikipedia(question)

    # Step 2: ask Claude to answer using that context
    answer = summarize_with_claude(question, context)

    return answer
```

Three functions:
1. `search_wikipedia(query)` — hit the Wikipedia API, return the summary text
2. `summarize_with_claude(question, context)` — call the Anthropic API, get a clean answer
3. `main()` — read the question from command line, call the above, print the result

You implement functions 1 and 2 in the lab.

---

## Demo: Building It Live

*Watch me fill in TODO 1 and TODO 2 in `research_agent_starter.py`.*

1. Open the starter file — read the structure
2. Ask Claude to implement `search_wikipedia`
3. Test it: `python research_agent_starter.py "photosynthesis"`
4. Ask Claude to implement `summarize_with_claude`
5. Test the full pipeline: `python research_agent_starter.py "Who invented the internet?"`
6. Add one small feature (TODO 3)

---

## Lab Overview (45 min)

| Time | Activity |
|------|----------|
| 0–5 min | Part 1: Read the starter file structure |
| 5–20 min | Part 2: Implement Wikipedia search (TODO 1) |
| 20–35 min | Part 3: Implement Claude summarizer (TODO 2) |
| 35–45 min | Part 4: Add one improvement (TODO 3) |

Setup needed before starting:
```bash
pip install anthropic requests python-dotenv
export ANTHROPIC_API_KEY="your-key-here"
```

---

## Key Takeaways

1. **APIs are just HTTP requests** — send a request, receive data, parse JSON
2. **The Anthropic API is Claude** — calling it from code is exactly like using claude.ai, but automated
3. **Environment variables keep keys safe** — never hardcode API keys in files you might share
4. **Agent = LLM + action loop** — fetch context, send to model, return answer
5. **This pattern scales** — swap Wikipedia for any data source; swap the task for any question

---

## Before Next Week (Final Session!)

Week 8 is the last session: evaluation and showcase.

**Prepare a 3-minute demo of your best work from this course.** Plan:
1. One sentence: what does your tool do?
2. Live demo: show it running on a real input
3. One thing that works well, one thing you would do next

Bring your laptop, make sure the tool runs.

**Next session:** Mar 9 — Evaluating AI-built software and final showcase
