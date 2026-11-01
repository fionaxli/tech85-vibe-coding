"""Week 1 starter: a tiny tool built from a plain-language request.

The request given to the AI assistant was:
    "Write a Python script that takes a text file and tells me how many
     words it has, and the five words I use most often, ignoring
     common words like 'the' and 'and'."

Run it:
    python word_counter.py sample.txt

Lab: ask your AI assistant to change one thing about this tool
(for example, ignore more words, or show the top 10), then run it again.
"""

import re
import sys
from collections import Counter

COMMON_WORDS = {
    "the", "and", "a", "an", "of", "to", "in", "is", "it", "that",
    "for", "on", "with", "as", "was", "are", "be", "this", "i", "you",
}


def count_words(text: str) -> tuple[int, list[tuple[str, int]]]:
    """Return the total word count and the five most common non-trivial words."""
    words = re.findall(r"[a-zA-Z']+", text.lower())
    meaningful = [w for w in words if w not in COMMON_WORDS]
    return len(words), Counter(meaningful).most_common(5)


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python word_counter.py <file.txt>")
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
