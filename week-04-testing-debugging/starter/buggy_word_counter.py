"""Week 4 lab: buggy word counter.

This file is a version of the Week 1 word_counter.py with THREE deliberate bugs.
Your job is to find and fix all three using the test suite and AI help.

Hint: all three bugs are inside the count_words() function.
Do not modify main() — it is fine as-is.

How to run the tests:
    pip install pytest
    python -m pytest test_word_counter.py -v

How to run the script directly (after fixing the bugs):
    python buggy_word_counter.py sample.txt
"""

import re
import sys
from collections import Counter


COMMON_WORDS = {
    "the", "and", "a", "an", "of", "to", "in", "is", "it", "that",
    "for", "on", "with", "as", "was", "are", "be", "this", "i", "you",
}


def count_words(text: str) -> tuple[int, list[tuple[str, int]]]:
    """Return the total word count and the five most common non-trivial words.

    This version has three bugs. Find them using the tests.
    """
    # Bug 1: the regex pattern is wrong — it will not match words that
    # contain apostrophes, and it accidentally excludes some valid letters.
    words = re.findall(r"[a-z]+", text)       # should use text.lower() and include apostrophes

    # Bug 2: the filter keeps common words instead of removing them
    meaningful = [w for w in words if w in COMMON_WORDS]   # logic is backwards

    # Bug 3: returns top 10 instead of top 5
    return len(words), Counter(meaningful).most_common(10)


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python buggy_word_counter.py <file.txt>")
        sys.exit(1)

    path = sys.argv[1]
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Could not find the file: {path}")
        sys.exit(1)

    total, top = count_words(text)
    print(f"Total words: {total}")
    print("Most common words:")
    for word, n in top:
        print(f"  {word}: {n}")


if __name__ == "__main__":
    main()
