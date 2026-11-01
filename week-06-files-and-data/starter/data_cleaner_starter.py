"""Week 6 starter: survey data cleaner.

This script reads survey_responses.csv, cleans the data, and writes
a plain-text summary to an output file.

How to run:
    python data_cleaner_starter.py survey_responses.csv summary.txt

The file has several intentional data problems — find them in Part 1 of the lab,
then implement the functions below using AI help in Part 2.
"""

import csv
import sys
from collections import defaultdict


# ---------------------------------------------------------------------------
# Data cleaning functions — implement these in Part 2 of the lab
# ---------------------------------------------------------------------------

def clean_row(row: dict) -> dict | None:
    """Clean one row from the CSV.

    Rules to implement:
    - If the 'name' field is blank (empty string or only spaces), return None
      (we skip anonymous rows)
    - Strip leading/trailing whitespace from all string fields
    - Convert 'department' to title case (e.g., "marketing" → "Marketing",
      "ENGINEERING" → "Engineering")
    - Convert 'satisfaction_score' to an integer. If it cannot be converted
      (e.g., it is blank, the word "three", or a non-integer), return None
    - If 'satisfaction_score' is outside the range 1–5 (inclusive), return None
    - Leave all other fields as-is after stripping whitespace

    Returns:
        A cleaned copy of the row dict, or None if the row should be skipped.
    """
    # TODO: implement this function
    # Hint: use row.copy() to avoid modifying the original dict
    # Hint: use str.strip() to remove whitespace, str.title() for title case
    # Hint: wrap int() in a try/except block to handle non-numeric scores
    pass


def compute_stats(clean_rows: list[dict]) -> dict:
    """Compute summary statistics from a list of cleaned rows.

    Returns a dictionary with these keys:
        "total_responses": int — count of valid (cleaned) rows
        "avg_score_overall": float — average satisfaction_score across all rows,
            rounded to 2 decimal places
        "avg_score_by_dept": dict — mapping of department name →
            average satisfaction_score (float, rounded to 2 decimal places)
        "recommend_yes_pct": float — percentage of respondents who answered
            "Yes" to would_recommend, rounded to 1 decimal place
        "skipped_rows": int — this is filled in by main(), not here;
            initialize to 0

    Note: if there are no valid rows, return sensible defaults (0s and empty dicts).
    """
    # TODO: implement this function
    # Hint: use collections.defaultdict(list) to accumulate scores per department
    # Hint: compute the average of a list: sum(scores) / len(scores)
    # Hint: check would_recommend with: row["would_recommend"].strip().lower() == "yes"
    pass


def format_summary(stats: dict) -> str:
    """Format the stats dictionary as a human-readable plain-text summary.

    The output should include:
    - Total valid responses and number of skipped rows
    - Overall average satisfaction score
    - Average satisfaction score per department (sorted alphabetically)
    - Percentage who would recommend the company

    Example output (your formatting can differ):

        Survey Summary
        ==============
        Total valid responses: 45
        Rows skipped (bad data): 5

        Overall average satisfaction score: 3.62 / 5

        Average score by department:
          Engineering:  3.80
          HR:           4.20
          Marketing:    3.55
          Sales:        3.10

        Would recommend to a friend: 72.0%

    Returns:
        A single string containing the full summary text.
    """
    # TODO: implement this function
    # Hint: build the string with lines and join them with "\n"
    # Hint: use f-strings for formatting numbers, e.g., f"{score:.2f}"
    # Hint: sort departments: for dept in sorted(stats["avg_score_by_dept"]):
    pass


# ---------------------------------------------------------------------------
# Main — reads the file, runs cleaning and analysis, writes output
# (this section is complete — do not modify it)
# ---------------------------------------------------------------------------

def main() -> None:
    if len(sys.argv) != 3:
        print("Usage: python data_cleaner_starter.py <input.csv> <output.txt>")
        print("Example: python data_cleaner_starter.py survey_responses.csv summary.txt")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # Read and clean the CSV
    clean_rows = []
    skipped = 0

    try:
        with open(input_path, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                cleaned = clean_row(row)
                if cleaned is None:
                    skipped += 1
                else:
                    clean_rows.append(cleaned)
    except FileNotFoundError:
        print(f"Error: file not found: {input_path}")
        sys.exit(1)

    print(f"Read {len(clean_rows) + skipped} rows: {len(clean_rows)} valid, {skipped} skipped.")

    # Compute statistics
    if not clean_rows:
        print("No valid rows after cleaning. Check your input file.")
        sys.exit(0)

    stats = compute_stats(clean_rows)
    if stats is None:
        print("Error: compute_stats returned None. Did you implement it?")
        sys.exit(1)

    stats["skipped_rows"] = skipped

    # Format and write summary
    summary_text = format_summary(stats)
    if summary_text is None:
        print("Error: format_summary returned None. Did you implement it?")
        sys.exit(1)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(summary_text)
        f.write("\n")

    print(f"Summary written to: {output_path}")
    print()
    print(summary_text)


if __name__ == "__main__":
    main()
