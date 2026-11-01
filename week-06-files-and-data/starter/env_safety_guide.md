# API Key Safety Guide

Five steps to handle API keys safely in your Streamlit project.

Work through this checklist before every deployment.

---

## Step 1: Create a .env file

In your project folder, create a file named exactly `.env` (note the leading dot — that is part of the name).

Add your keys in this format:
```
OPENWEATHER_API_KEY=abc123yourkeyhere
NEWS_API_KEY=def456anotherkeyhere
```

Rules for the .env file:
- One key per line
- No spaces around the `=`
- No quotes around the value (unless the value itself contains spaces)
- Never commit this file to GitHub (see Step 2)

---

## Step 2: Add .env to .gitignore

Open your `.gitignore` file (or create one if it does not exist). Make sure it includes:
```
.env
```

To verify: run `git status` in your terminal. If `.env` appears in the output under "Untracked files" or "Changes to be committed," it is NOT being ignored. Fix your `.gitignore` before committing anything.

Ask Claude Code to check:
> "Read my .gitignore and confirm that .env is excluded. If it is not, add it."

---

## Step 3: Load the key in your Python code

At the top of your `app.py` (or wherever you use the key), add:

```python
import os
from dotenv import load_dotenv

load_dotenv()  # reads .env and loads the values into the environment

# Then use the key anywhere you need it:
api_key = os.getenv("OPENWEATHER_API_KEY")
```

If `api_key` is `None`, the `.env` file was not found or the variable name does not match.

---

## Step 4: Use the key — never expose it

When you use the key in an API call:

```python
# Right: pass the key as a parameter
response = requests.get(url, params={"appid": api_key, "q": city})

# Wrong: put the key directly in the URL string
response = requests.get(f"https://api.example.com?key={api_key}&q={city}")
```

Both work — but the first form does not expose the key in browser developer tools, server logs, or error messages as easily. Prefer the params dictionary.

Also: never print or display the key value, even for debugging. If you need to verify the key loaded, check that it is not None:

```python
if not api_key:
    print("Warning: API key not found")
else:
    print("API key loaded successfully")  # Don't print the actual value
```

---

## Step 5: Adding secrets to Streamlit Cloud

Your `.env` file lives on your laptop. When you deploy to Streamlit Cloud, you cannot push your `.env` file — and you should not.

Streamlit Cloud has a built-in secrets manager:

1. Open [share.streamlit.io](https://share.streamlit.io)
2. Click on your deployed app
3. Click the three-dot menu → **Settings** → **Secrets**
4. Add your secrets in TOML format:
   ```toml
   OPENWEATHER_API_KEY = "your_actual_key_here"
   NEWS_API_KEY = "your_other_key_here"
   ```
5. Click **Save**. Your app will restart and the secrets will be available.

Your Python code does not change — `os.getenv("OPENWEATHER_API_KEY")` works both locally (reads from `.env`) and on Streamlit Cloud (reads from the secrets manager).

---

## Safety checklist

Before every push to GitHub, verify:

- [ ] My `.env` file exists locally and has my API key
- [ ] `.env` is in my `.gitignore`
- [ ] Running `git status` does NOT show `.env` in the output
- [ ] My Python code uses `os.getenv()` to read the key, not a hardcoded string
- [ ] I have not pasted my API key into any Claude Code prompt
- [ ] I have added the key to Streamlit Cloud Secrets (if deploying)

---

## What to do if your key gets exposed

If you accidentally commit a key to GitHub:

1. **Revoke the key immediately.** Go to the API provider's dashboard and delete or regenerate the key. Do not wait.
2. **Add a new key.** Get a new API key and add it to your `.env`.
3. **Remove the key from your Git history.** Ask Claude Code: *"I accidentally committed a file containing an API key. What is the safest way to remove it from my Git history?"*

Revoking the key is the most important step. GitHub scans repositories and notifies API providers when keys are exposed; some providers (like GitHub itself and some cloud services) revoke them automatically.
