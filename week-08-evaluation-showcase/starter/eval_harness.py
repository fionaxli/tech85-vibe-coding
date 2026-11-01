"""
Week 8 evaluation harness: run a test set against any function.

This harness works with any Python function that takes a string input
and returns a string output. It runs each test case, compares the
result to the expected output, and prints a pass/fail report.

HOW TO ADAPT IT TO YOUR CAPSTONE:
1. Replace the example test cases at the bottom with your own.
2. Replace the example_function() with a function from your project.
3. (Optional) Enable the LLM-as-a-judge section to get AI-scored evaluation.

Run it:
    python eval_harness.py

To use the LLM-as-a-judge feature, you need an Anthropic API key in your .env:
    ANTHROPIC_API_KEY=your_key_here
"""

import os
import json
from dataclasses import dataclass, field
from typing import Callable

# -----------------------------------------------------------------------
# Test case definition
# -----------------------------------------------------------------------

@dataclass
class TestCase:
    """A single test case: an input, an expected output, and an optional description."""
    input: str
    expected: str
    description: str = ""
    # Pass criteria: "exact" (string match) or "contains" (expected is substring of actual)
    match_type: str = "contains"


@dataclass
class TestResult:
    """The result of running one test case."""
    test: TestCase
    actual_output: str
    passed: bool
    judge_score: int | None = None       # 1–5 if LLM-as-a-judge was used
    judge_explanation: str = ""


# -----------------------------------------------------------------------
# Core evaluation engine
# -----------------------------------------------------------------------

def run_test(test: TestCase, fn: Callable[[str], str]) -> TestResult:
    """Run one test case against a function and return the result."""
    try:
        actual = fn(test.input)
    except Exception as e:
        actual = f"ERROR: {str(e)}"

    if test.match_type == "exact":
        passed = actual.strip() == test.expected.strip()
    else:  # "contains"
        passed = test.expected.lower() in actual.lower()

    return TestResult(test=test, actual_output=actual, passed=passed)


def run_test_suite(
    test_cases: list[TestCase],
    fn: Callable[[str], str],
    use_llm_judge: bool = False,
) -> list[TestResult]:
    """Run all test cases and return results."""
    results = []
    for i, test in enumerate(test_cases, 1):
        print(f"Running test {i}/{len(test_cases)}: {test.description or test.input[:40]}...")
        result = run_test(test, fn)
        if use_llm_judge:
            result = add_llm_judgment(result)
        results.append(result)
    return results


# -----------------------------------------------------------------------
# LLM-as-a-judge (optional)
#
# Requires the anthropic package and an API key in .env.
# pip install anthropic
# -----------------------------------------------------------------------

def add_llm_judgment(result: TestResult) -> TestResult:
    """Use Claude to score a test result 1–5 and explain the score."""
    try:
        import anthropic
        from dotenv import load_dotenv
        load_dotenv()

        client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

        prompt = f"""You are evaluating a software tool's output against an expected behavior.

Input: {result.test.input}
Expected behavior: {result.test.expected}
Actual output: {result.actual_output}

Rate the actual output 1–5:
  5 = Exactly correct
  4 = Correct with minor issues
  3 = Partially correct
  2 = Wrong but related to the expected behavior
  1 = Completely wrong or error

Respond with JSON only:
{{"score": <1-5>, "explanation": "<one sentence>"}}"""

        message = client.messages.create(
            model="claude-3-5-haiku-20241022",
            max_tokens=200,
            messages=[{"role": "user", "content": prompt}],
        )
        response_text = message.content[0].text.strip()
        data = json.loads(response_text)
        result.judge_score = data["score"]
        result.judge_explanation = data["explanation"]
    except ImportError:
        result.judge_explanation = "anthropic package not installed. Run: pip install anthropic"
    except Exception as e:
        result.judge_explanation = f"LLM judge failed: {str(e)}"

    return result


# -----------------------------------------------------------------------
# Report generation
# -----------------------------------------------------------------------

def print_report(results: list[TestResult]) -> None:
    """Print a formatted test report."""
    passed = sum(1 for r in results if r.passed)
    total = len(results)

    print("\n" + "=" * 60)
    print(f"EVALUATION REPORT — {passed}/{total} tests passed")
    print("=" * 60)

    for i, result in enumerate(results, 1):
        status = "PASS" if result.passed else "FAIL"
        description = result.test.description or f"Test {i}"
        print(f"\n[{status}] {description}")
        print(f"  Input:    {result.test.input[:60]}")
        print(f"  Expected: {result.test.expected[:60]}")
        print(f"  Actual:   {result.actual_output[:60]}")

        if result.judge_score is not None:
            print(f"  LLM judge score: {result.judge_score}/5 — {result.judge_explanation}")

    print("\n" + "=" * 60)
    if passed == total:
        print("All tests passed.")
    else:
        print(f"{total - passed} test(s) failed. See details above.")
    print("=" * 60 + "\n")


# -----------------------------------------------------------------------
# Example: adapt this section for your Capstone
#
# Replace example_function() with a function from your own project.
# Replace the test cases with inputs and expected outputs that match
# your Capstone's core behavior.
#
# Tips:
# - "contains" match type is more forgiving — use it for outputs where
#   the exact wording may vary but the key information should be present.
# - "exact" match type is strict — use it for things like counts, IDs,
#   or formatted outputs that should always be exactly the same.
# - Write at least 5 test cases: the happy path, an edge case,
#   an invalid input, a boundary condition, and one you are not sure about.
# -----------------------------------------------------------------------

def example_function(text: str) -> str:
    """An example function to evaluate: counts words in a string.

    Replace this with a function from your Capstone.
    For a Streamlit app, you may need to extract the core logic
    into a testable function that does not require the Streamlit UI.

    Ask Claude Code:
    "Extract the core logic from my app.py into a separate function
     that takes [input type] and returns [output type], so I can
     test it without running the Streamlit UI."
    """
    words = text.split()
    count = len(words)
    if count == 0:
        return "No words found."
    elif count == 1:
        return f"1 word found."
    else:
        return f"{count} words found."


# Replace these test cases with your own
EXAMPLE_TEST_CASES = [
    TestCase(
        input="Hello world this is a test",
        expected="6 words",
        description="Normal sentence — should count 6 words",
        match_type="contains",
    ),
    TestCase(
        input="",
        expected="No words found",
        description="Empty input — should handle gracefully",
        match_type="contains",
    ),
    TestCase(
        input="OneWord",
        expected="1 word",
        description="Single word — should use singular form",
        match_type="contains",
    ),
    TestCase(
        input="   spaces   between   words   ",
        expected="3 words",
        description="Extra whitespace — should still count correctly",
        match_type="contains",
    ),
    TestCase(
        input="The quick brown fox jumps over the lazy dog",
        expected="9 words",
        description="Classic 9-word sentence",
        match_type="contains",
    ),
]


# -----------------------------------------------------------------------
# Main entry point
# -----------------------------------------------------------------------

if __name__ == "__main__":
    print("Running evaluation harness...")
    print("(To use your own function and test cases, edit the EXAMPLE sections above.)\n")

    # Set use_llm_judge=True to enable LLM scoring (requires ANTHROPIC_API_KEY in .env)
    results = run_test_suite(
        test_cases=EXAMPLE_TEST_CASES,
        fn=example_function,
        use_llm_judge=False,
    )

    print_report(results)
