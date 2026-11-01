"""Week 8: evaluation harness.

This script runs a set of test cases through a function, then uses Claude to
grade each output against an expected result. It prints a summary table and
saves the results to eval_results.txt.

How to run:
    python eval_harness.py

Setup:
    pip install anthropic
    export ANTHROPIC_API_KEY="sk-ant-yourkey"   (Mac/Linux)
    set ANTHROPIC_API_KEY=sk-ant-yourkey        (Windows)

Customizing:
    1. Change FUNCTION_TO_TEST to point to the function you want to evaluate.
    2. Add more entries to TEST_CASES — at least 5 more for the lab.
    3. The harness handles the rest.
"""

import os
import sys
from datetime import datetime

# Load .env file if present
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

try:
    import anthropic
except ImportError:
    print("Error: install the anthropic library first: pip install anthropic")
    sys.exit(1)

# ---------------------------------------------------------------------------
# Import the function to test
# ---------------------------------------------------------------------------
# By default this tests count_words from the Week 1 / Week 4 word counter.
# To test your own tool, change this import and update TEST_CASES below.
#
# Example for your own tool:
#   import sys, os
#   sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../week-02-specs-and-prompts/starter"))
#   from my_tool import my_function
#   FUNCTION_TO_TEST = my_function

import sys, os
sys.path.insert(
    0,
    os.path.join(os.path.dirname(__file__), "../../week-01-first-tool/starter")
)
try:
    from word_counter import count_words

    def FUNCTION_TO_TEST(text: str) -> str:
        """Wrapper so count_words fits the harness interface (input → string output)."""
        total, top = count_words(text)
        top_str = ", ".join(f"{w}({n})" for w, n in top)
        return f"total={total}, top=[{top_str}]"

except ImportError:
    print("Could not import word_counter from Week 1.")
    print("Update the import at the top of this file to point to your own tool.")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Test cases
# ---------------------------------------------------------------------------
# Each test case is a dict with:
#   "input"    — the string to pass to FUNCTION_TO_TEST
#   "expected" — a description of what a GOOD output looks like
#                (does not have to be exact; Claude uses it as a rubric)
#   "label"    — a short name for this test case

TEST_CASES = [
    {
        "label": "basic sentence",
        "input": "the quick brown fox jumps over the lazy dog",
        "expected": "total=9, top words are fox, quick, brown, jumps, lazy (each count 1); 'the' excluded as common word",
    },
    {
        "label": "repeated word",
        "input": "apple apple apple banana banana",
        "expected": "total=5, top word is apple with count 3, then banana with count 2",
    },
    {
        "label": "only common words",
        "input": "the and a of to in is it that for",
        "expected": "total=10, top words list is empty because all words are common words",
    },
    {
        "label": "mixed case",
        "input": "Hello hello HELLO world World",
        "expected": "total=5, hello appears 3 times (case insensitive), world appears 2 times",
    },
    {
        "label": "empty string",
        "input": "",
        "expected": "total=0, top words list is empty",
    },
    # -----------------------------------------------------------------------
    # TODO: Add at least 5 more test cases below this line.
    #
    # Ideas:
    #   - A very long piece of text (paste a paragraph from any article)
    #   - Text with punctuation (commas, periods, exclamation marks)
    #   - Text with apostrophes (don't, it's, won't)
    #   - Text with numbers mixed in ("I have 3 cats")
    #   - A single word
    #   - Text with lots of the same word to verify the count
    # -----------------------------------------------------------------------
]


# ---------------------------------------------------------------------------
# LLM judge
# ---------------------------------------------------------------------------

JUDGE_MODEL = "claude-opus-4-5"

JUDGE_PROMPT_TEMPLATE = """\
I am evaluating a text-processing tool. Here is one test case:

INPUT:
{input}

EXPECTED OUTPUT (description of what a good output looks like):
{expected}

ACTUAL OUTPUT (what the tool produced):
{actual}

Please rate the actual output on a scale of 1 to 5 where:
  5 = Exactly correct or clearly matches what was expected
  4 = Mostly correct, minor differences that do not affect usefulness
  3 = Partially correct — some right, some wrong
  2 = Mostly wrong, but there is one correct element
  1 = Completely wrong or the tool crashed

Reply with:
SCORE: [1-5]
REASON: [one sentence explaining your rating]
"""


def judge_output(input_text: str, expected: str, actual: str, client: anthropic.Anthropic) -> tuple[int, str]:
    """Ask Claude to rate the actual output against the expected description.

    Returns (score, reason) where score is an int 1–5.
    """
    prompt = JUDGE_PROMPT_TEMPLATE.format(
        input=input_text or "(empty string)",
        expected=expected,
        actual=actual or "(no output produced)",
    )

    try:
        message = client.messages.create(
            model=JUDGE_MODEL,
            max_tokens=200,
            messages=[{"role": "user", "content": prompt}],
        )
        response_text = message.content[0].text.strip()

        # Parse the structured response
        score = 3   # default if parsing fails
        reason = response_text

        for line in response_text.splitlines():
            if line.upper().startswith("SCORE:"):
                try:
                    score = int(line.split(":", 1)[1].strip())
                    score = max(1, min(5, score))   # clamp to 1–5
                except ValueError:
                    pass
            elif line.upper().startswith("REASON:"):
                reason = line.split(":", 1)[1].strip()

        return score, reason

    except anthropic.AuthenticationError:
        print("\nError: Anthropic API key is missing or invalid.")
        print("Set it with: export ANTHROPIC_API_KEY='sk-ant-yourkey'")
        sys.exit(1)
    except Exception as exc:
        return 0, f"Judge error: {exc}"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def run_evaluation() -> None:
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY is not set.")
        print("Set it with: export ANTHROPIC_API_KEY='sk-ant-yourkey'  (Mac/Linux)")
        print("         or: set ANTHROPIC_API_KEY=sk-ant-yourkey        (Windows)")
        sys.exit(1)

    client = anthropic.Anthropic()

    results = []
    total_score = 0

    print(f"Running {len(TEST_CASES)} test cases...\n")
    print(f"{'#':<4} {'Label':<25} {'Score':<7} Reason")
    print("-" * 80)

    for i, case in enumerate(TEST_CASES, 1):
        label = case["label"]
        input_text = case["input"]
        expected = case["expected"]

        # Run the function
        try:
            actual = FUNCTION_TO_TEST(input_text)
        except Exception as exc:
            actual = f"CRASHED: {exc}"

        # Ask Claude to grade it
        score, reason = judge_output(input_text, expected, actual, client)
        total_score += score

        results.append({
            "case_num": i,
            "label": label,
            "input": input_text,
            "expected": expected,
            "actual": actual,
            "score": score,
            "reason": reason,
        })

        score_display = f"{score}/5"
        print(f"{i:<4} {label:<25} {score_display:<7} {reason[:60]}")

    # Summary
    avg = total_score / len(TEST_CASES) if TEST_CASES else 0
    passed = sum(1 for r in results if r["score"] >= 4)
    print("-" * 80)
    print(f"Average score: {avg:.1f}/5   |   Passed (4+): {passed}/{len(TEST_CASES)}")
    print()

    # Save detailed results
    output_path = os.path.join(os.path.dirname(__file__), "eval_results.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"Evaluation Results\n")
        f.write(f"Run at: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"Function: {FUNCTION_TO_TEST.__name__}\n")
        f.write(f"Model used for judging: {JUDGE_MODEL}\n")
        f.write("=" * 60 + "\n\n")

        for r in results:
            f.write(f"Test {r['case_num']}: {r['label']}\n")
            f.write(f"  Input:    {r['input'][:80]!r}\n")
            f.write(f"  Expected: {r['expected'][:80]}\n")
            f.write(f"  Actual:   {r['actual'][:80]}\n")
            f.write(f"  Score:    {r['score']}/5\n")
            f.write(f"  Reason:   {r['reason']}\n\n")

        f.write("-" * 60 + "\n")
        f.write(f"Average score: {avg:.1f}/5\n")
        f.write(f"Passed (score >= 4): {passed}/{len(TEST_CASES)}\n")

    print(f"Detailed results saved to: {output_path}")


if __name__ == "__main__":
    run_evaluation()
