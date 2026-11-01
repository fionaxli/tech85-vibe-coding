# Deploying to Streamlit Cloud

A step-by-step guide to getting your Streamlit app live at a real public URL.

**Time required:** about 15 minutes the first time, 2 minutes for every update after that.

**What you need before you start:**
- Your app running locally (`streamlit run app.py` works without errors)
- A GitHub account (free at github.com)
- Your project folder pushed to a GitHub repository

---

## Step 1: Make sure your code is in a GitHub repository

If you have never used GitHub before, Claude Code can do this for you:

> "My project is in the folder `/path/to/my-project`. Help me create a GitHub repository and push my code to it. I have a GitHub account."

Claude Code will walk you through creating the repo, initializing Git, and pushing. You will need to enter your GitHub username and a personal access token (GitHub will guide you through creating one).

If you are already comfortable with Git:
```bash
cd my-project
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/your-repo-name.git
git push -u origin main
```

---

## Step 2: Create a requirements.txt file

Streamlit Cloud needs to know which Python packages to install. This list goes in a `requirements.txt` file in the root of your project.

Ask Claude Code to generate it:
> "Look at my project and generate a requirements.txt that lists all the Python packages it needs."

A typical `requirements.txt` for a Streamlit + SQLite project looks like this:
```
streamlit>=1.32.0
requests>=2.31.0
python-dotenv>=1.0.0
```

Make sure this file is committed and pushed to GitHub before you deploy.

---

## Step 3: Go to Streamlit Cloud and sign in

1. Open your browser and go to [share.streamlit.io](https://share.streamlit.io)
2. Click **Sign in with GitHub**
3. Authorize Streamlit to access your GitHub account (you can limit this to specific repositories if you prefer)

---

## Step 4: Create a new app

1. Click **New app** in the top right corner
2. Select your **repository** from the dropdown (it will list all your GitHub repos)
3. Select your **branch** — this is almost always `main`
4. Set the **Main file path** — this is the file Streamlit runs. Usually `app.py`. If your main file is named something else (like `streamlit_app.py`), enter that exact name.
5. (Optional) Set a custom **App URL** — your app will be available at `your-chosen-name.streamlit.app`

---

## Step 5: Click Deploy and watch the logs

After clicking Deploy, Streamlit Cloud will:
1. Clone your GitHub repository
2. Install the packages in `requirements.txt`
3. Run your app

You will see a log output. This usually takes 1–2 minutes. When it succeeds, the log will show `You can now view your Streamlit app in your browser` and your app will appear.

**If it fails:** read the error in the log. The three most common errors and their fixes are below.

---

## Step 6: Share your URL

Your app is now live at a URL like:
```
https://your-app-name.streamlit.app
```

You can share this URL with anyone. They do not need a GitHub account or Python installed — they just open the link.

**Automatic updates:** every time you push a new commit to your GitHub repo, Streamlit Cloud will automatically redeploy. Changes usually go live within 30–60 seconds.

---

## Troubleshooting the three most common errors

### Error 1: `ModuleNotFoundError: No module named 'X'`

A Python package your code imports is not listed in `requirements.txt`.

**Fix:**
1. Find the package name (it is the thing after `import` or `from` in your code — e.g., `import requests` means you need `requests`)
2. Add it to `requirements.txt`
3. Commit and push to GitHub:
   ```bash
   git add requirements.txt
   git commit -m "Add missing package to requirements"
   git push
   ```
4. Streamlit Cloud will automatically redeploy

### Error 2: `FileNotFoundError: [Errno 2] No such file or directory: 'data.csv'`

Your code references a file by a relative path, and that file either:
- Was not committed to GitHub (common with `.db` database files and data files), or
- Uses a path that works on your laptop but not on Streamlit Cloud

**Fix for database files:** SQLite creates the file automatically — make sure your code uses `sqlite3.connect("habits.db")` not `sqlite3.connect("/Users/yourname/habits.db")`. Relative paths work fine on Streamlit Cloud.

**Fix for data files (like CSV):** The file needs to be in your GitHub repository. If it contains sensitive data, ask Claude Code to generate a small sample file for the deployment version.

**Fix for files you do not want in GitHub:** Ask Claude Code: *"Rewrite any file paths in my code so they work on Streamlit Cloud."*

### Error 3: App loads but shows a blank screen or spinner that never finishes

Usually means:
- Your main file does not have any `st.` calls at the top level (the Streamlit UI code is inside a function that never gets called), or
- Your app is stuck waiting for something — like a database connection that times out, or an API call with no timeout

**Fix for missing UI calls:**
Ask Claude Code: *"My Streamlit app shows a blank screen. Check that app.py has at least one st. call at the top level and that the main() function is called."*

**Fix for stuck API calls:**
Ask Claude Code: *"Add a timeout of 5 seconds to all requests.get() and requests.post() calls in my code."*

---

## Adding secrets to Streamlit Cloud

If your app uses a `.env` file with API keys, you cannot commit that file to GitHub (and you should not). Streamlit Cloud has a built-in secrets manager.

1. In your Streamlit Cloud dashboard, click the three-dot menu on your app and select **Settings**
2. Go to the **Secrets** tab
3. Paste your secrets in TOML format:
   ```toml
   OPENWEATHER_API_KEY = "your-actual-key-here"
   ```
4. Save. Your app will restart automatically.

In your code, read the secret the same way you read environment variables:
```python
import os
api_key = os.getenv("OPENWEATHER_API_KEY")
```

This works both locally (via your `.env` file) and on Streamlit Cloud (via the secrets manager).
