# Week 7: Small Agents and Web Services

**Session:** Tue Mar 2, 2027, 7:00–8:30 pm PT

## Goals

By the end of this session you will be able to:

- Explain what an API is and make a simple HTTP request with Python
- Use the Anthropic API to call Claude programmatically (from code, not the browser)
- Build a small "research helper" agent that retrieves information from the web and asks Claude to summarize it

---

## Key Concepts

### What is an API?

API stands for "Application Programming Interface." It is a way for your code to talk to another program — often one running on someone else's server.

Think of it like a restaurant menu. You do not go into the kitchen and cook yourself. You look at the menu (the API documentation), place an order (send a request), and get back a meal (receive a response). You do not need to know how the kitchen works.

Almost every web service you use has an API: Google Maps, Spotify, Twitter, Wikipedia — they all let you request data with a simple HTTP call.

### HTTP requests in Python

```python
import requests

response = requests.get("https://en.wikipedia.org/api/rest_v1/page/summary/Python")
data = response.json()
print(data["extract"])   # prints a plain-English summary of the Python article
```

Two things to check after any request:
- `response.status_code` — 200 means success; 404 means not found; 500 means server error
- `response.json()` — the response body, parsed as a Python dictionary

### The Anthropic API

So far you have used Claude through the website. You can also call Claude from your own code. This is how AI-powered tools work.

```python
import anthropic

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from environment

message = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Explain photosynthesis in two sentences."}
    ]
)
print(message.content[0].text)
```

Your API key authenticates you. **Never put your API key in code.** Put it in an environment variable.

### Environment variables and `.env` files

An environment variable is a named value that lives outside your code, in your shell. Programs read it without it appearing in any file you might accidentally share.

```bash
# Set it in your terminal (lasts until you close the terminal)
export ANTHROPIC_API_KEY="sk-ant-..."   # Mac/Linux
set ANTHROPIC_API_KEY=sk-ant-...       # Windows

# Or save it permanently in a .env file and load it with python-dotenv
```

Your `.env` file:
```
ANTHROPIC_API_KEY=sk-ant-yourkey
```

Then in your Python code:
```python
from dotenv import load_dotenv
load_dotenv()   # reads .env and sets environment variables
```

**Never commit `.env` to Git.** The `.gitignore` in this repo already excludes it.

### What is an agent?

An agent is a program that uses an AI model to decide what to do next, then takes an action, then looks at the result, and repeats. A simple agent loop:

```
User gives a question
    ↓
Agent searches Wikipedia for relevant content
    ↓
Agent sends the Wikipedia content + the question to Claude
    ↓
Claude generates a summary answer
    ↓
Agent returns the answer to the user
```

Today's lab builds exactly this loop.

---

## Setup Before Lab

You need an Anthropic API key (from Week 6's "before next week" task).

1. Set your API key as an environment variable:
   ```bash
   export ANTHROPIC_API_KEY="sk-ant-yourkey"  # Mac/Linux
   set ANTHROPIC_API_KEY=sk-ant-yourkey       # Windows
   ```
   Or create a `.env` file in the starter folder:
   ```
   ANTHROPIC_API_KEY=sk-ant-yourkey
   ```

2. Install required libraries:
   ```bash
   pip install anthropic requests python-dotenv
   ```

3. Test your key:
   ```python
   import anthropic
   client = anthropic.Anthropic()
   print(client.messages.create(
       model="claude-opus-4-5",
       max_tokens=50,
       messages=[{"role": "user", "content": "Say hello in one word."}]
   ).content[0].text)
   ```
   If you see a one-word response, your key works.

---

## Lab: Build the Research Helper Agent

This lab uses `starter/research_agent_starter.py`. It has the structure and imports in place; your job is to fill in the three TODO sections.

### Part 1 — Understand the structure (5 min)

1. Open `starter/research_agent_starter.py` in VS Code.
2. Read the file top to bottom — do not worry about parts you do not understand. Answer:
   - What are the three functions?
   - What does each function's docstring say it should do?
   - Which function calls the Wikipedia API? Which calls the Anthropic API?

### Part 2 — Implement the Wikipedia search (15 min)

3. Find `# TODO 1` in the file. You need to implement `search_wikipedia(query)`.

4. Ask Claude to help you:
   > "I need to implement a Python function that takes a search query string and uses the Wikipedia REST API to return a plain-text summary of the most relevant article. The API endpoint is: `https://en.wikipedia.org/api/rest_v1/page/summary/{title}` where {title} is the URL-encoded search term. The function should return the 'extract' field from the JSON response, or a default message if nothing is found. Use the requests library."

5. Paste the implementation into the TODO 1 section.

6. Test it in isolation:
   ```python
   # Add this temporarily at the bottom of the file to test
   print(search_wikipedia("photosynthesis"))
   print(search_wikipedia("quantum computing"))
   ```
   Run the file: `python research_agent_starter.py`.
   You should see Wikipedia summaries. Remove the test lines when done.

### Part 3 — Implement the Claude summarizer (15 min)

7. Find `# TODO 2`. Implement `summarize_with_claude(question, context)`.

8. Ask Claude to help:
   > "I need a Python function that takes a question string and a context string (text from Wikipedia), and uses the Anthropic API to return a concise answer. The function should send a message to claude-opus-4-5 asking it to answer the question using only the provided context, in 2-3 sentences. Use the anthropic library. Assume ANTHROPIC_API_KEY is set as an environment variable."

9. Paste the implementation into the TODO 2 section.

10. Test the full agent by running:
    ```bash
    python research_agent_starter.py "What is machine learning?"
    python research_agent_starter.py "Who invented the telephone?"
    ```
    You should get short, accurate answers.

### Part 4 — Add one improvement (10 min)

11. Find `# TODO 3`. Add one feature of your choice. Ideas:
    - Print the Wikipedia article title and URL along with the answer
    - Let the user ask follow-up questions in a loop (keep asking until they type "quit")
    - Save the question and answer to a log file with a timestamp

12. Ask the AI to implement your chosen feature, then test it.

---

## Expected Outputs

By the end of lab you should have:

- A working `research_agent_starter.py` that answers questions using Wikipedia + Claude
- At least two successful queries demonstrated in your terminal
- One additional feature implemented (TODO 3)

---

## If Something Goes Wrong

| Problem | What to do |
|---|---|
| `AuthenticationError` | Your API key is wrong or not set. Run `echo $ANTHROPIC_API_KEY` (Mac) or `echo %ANTHROPIC_API_KEY%` (Windows) to check. |
| `ModuleNotFoundError: No module named 'anthropic'` | Run `pip install anthropic` inside your virtual environment |
| Wikipedia returns empty or unhelpful content | The search title needs to match Wikipedia's article naming. Try more specific or differently-phrased queries |
| Claude gives a very short or unhelpful answer | The context might be too short. Print `len(context)` and check if Wikipedia returned anything useful |
| `RateLimitError` | You have made too many API calls. Wait 30 seconds and try again |

---

## Before Next Week — Final Session

Week 8 is the last session: evaluation and project showcase.

**Prepare a 3-minute demo of your project.** You can show any tool you built or improved during this course. Plan to:
1. State in one sentence what your tool does
2. Show it running on a real input
3. Describe one thing that works well and one thing you would improve

There is no grade — just a chance to show what you built.

Also: make sure your project is working and committed to GitHub before class.

## Slides

See `slides.md` in this folder (also posted in Canvas).
