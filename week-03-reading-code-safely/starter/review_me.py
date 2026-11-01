"""Week 3 lab script: review this before running it.

What this script claims to do:
    Read every .txt file in a folder, send each file's text to a free
    public summarization API (api.sampleapis.com — used here as a stand-in),
    and write the results to a CSV file called "summaries.csv".

How to run it:
    1. Activate your virtual environment: source venv/bin/activate
    2. Install the one required library: pip install requests
    3. Run: python review_me.py <folder_of_txt_files>

Example:
    python review_me.py ../week-01-first-tool/starter

Lab task:
    Do NOT run this script yet.
    First, work through safety_checklist.md with your AI assistant.
    Then come back to Part 3 of the lab and run it here.
"""

import csv
import os
import sys
import requests


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# The API endpoint. In a real tool this would be something like the OpenAI
# or Anthropic API. Here we use a harmless public API as a placeholder
# so the script exercises network code without requiring an API key.
API_URL = "https://api.sampleapis.com/coffee/hot"

# The output file that this script will create (or overwrite if it exists).
OUTPUT_FILE = "summaries.csv"

# Maximum number of characters to read from each file.
MAX_CHARS = 2000


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def find_text_files(folder: str) -> list[str]:
    """Return a sorted list of .txt file paths inside folder."""
    if not os.path.isdir(folder):
        print(f"Error: '{folder}' is not a folder or does not exist.")
        sys.exit(1)

    paths = []
    for entry in os.scandir(folder):
        if entry.is_file() and entry.name.endswith(".txt"):
            paths.append(entry.path)
    return sorted(paths)


def read_file(path: str) -> str:
    """Read up to MAX_CHARS characters from a text file."""
    try:
        with open(path, encoding="utf-8") as f:
            return f.read(MAX_CHARS)
    except OSError as exc:
        print(f"Warning: could not read {path}: {exc}")
        return ""


def call_api(text: str) -> dict:
    """Make a GET request to API_URL.

    NOTE: In this demo script the 'text' argument is not actually sent to
    the API — the placeholder API does not accept a body. In a real tool
    you would POST the text. This function is here to show students what
    a network call looks like and to exercise the 'requests' import.
    """
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
        # Return just the first item from the response as a stand-in "result".
        if isinstance(data, list) and len(data) > 0:
            return data[0]
        return {}
    except requests.exceptions.ConnectionError:
        print("Warning: could not reach the API. Are you connected to the internet?")
        return {}
    except requests.exceptions.Timeout:
        print("Warning: the API request timed out.")
        return {}
    except requests.exceptions.HTTPError as exc:
        print(f"Warning: API returned an error: {exc}")
        return {}


def write_results(results: list[dict], output_path: str) -> None:
    """Write a list of result dicts to a CSV file."""
    if not results:
        print("No results to write.")
        return

    fieldnames = ["filename", "char_count", "api_result_title", "api_result_id"]
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print(f"Saved results to {output_path} ({len(results)} rows).")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python review_me.py <folder>")
        print("Example: python review_me.py ../week-01-first-tool/starter")
        sys.exit(1)

    folder = sys.argv[1]
    txt_files = find_text_files(folder)

    if not txt_files:
        print(f"No .txt files found in: {folder}")
        sys.exit(0)

    print(f"Found {len(txt_files)} .txt file(s). Processing...")

    results = []
    for path in txt_files:
        text = read_file(path)
        if not text:
            continue

        print(f"  Processing: {os.path.basename(path)} ({len(text)} chars)...")
        api_data = call_api(text)

        results.append({
            "filename": os.path.basename(path),
            "char_count": len(text),
            "api_result_title": api_data.get("title", ""),
            "api_result_id": api_data.get("id", ""),
        })

    write_results(results, OUTPUT_FILE)


if __name__ == "__main__":
    main()
