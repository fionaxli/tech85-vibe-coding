"""Week 4 lab: tests for the word counter.

Run these with:
    python -m pytest test_word_counter.py -v

Some tests are already written for you.
Find all sections marked # TODO and complete them.

Import note: we import from buggy_word_counter so your fixes happen there.
Once all bugs are fixed, this import should work without errors.
"""

import pytest
from buggy_word_counter import count_words


# ---------------------------------------------------------------------------
# Tests that are already written — run these first to see what fails
# ---------------------------------------------------------------------------

def test_total_word_count_simple():
    """count_words should count all words in the input."""
    total, _ = count_words("hello world foo bar")
    assert total == 4, f"Expected 4 total words, got {total}"


def test_total_word_count_with_common_words():
    """Common words (like 'the', 'and') count toward total but not top words."""
    total, _ = count_words("the cat and the dog")
    assert total == 5, f"Expected 5 total words, got {total}"


def test_common_words_excluded_from_top():
    """Words like 'the', 'and', 'a' should NOT appear in the top-words list."""
    _, top = count_words("the the the cat")
    top_words = [word for word, _ in top]
    assert "the" not in top_words, "'the' should be excluded from top words"
    assert "cat" in top_words, "'cat' should appear in top words"


def test_most_common_word_is_first():
    """The word that appears most often should be first in the results."""
    _, top = count_words("apple apple apple banana banana cherry")
    assert top[0][0] == "apple", f"Expected 'apple' to be first, got '{top[0][0]}'"
    assert top[0][1] == 3, f"Expected count 3 for 'apple', got {top[0][1]}"


def test_returns_at_most_five_results():
    """count_words should return at most 5 top words, even if there are more."""
    # This string has 10 distinct meaningful words, each appearing twice
    text = (
        "apple apple banana banana cherry cherry "
        "delta delta echo echo foxtrot foxtrot "
        "golf golf hotel hotel india india"
    )
    _, top = count_words(text)
    assert len(top) <= 5, f"Expected at most 5 results, got {len(top)}"


def test_case_insensitive():
    """'Hello' and 'hello' should be counted as the same word."""
    _, top = count_words("Hello hello HELLO world")
    top_words_with_counts = {word: count for word, count in top}
    # After lowercasing, 'hello' should appear 3 times
    assert "hello" in top_words_with_counts, "'hello' not found in top words"
    assert top_words_with_counts["hello"] == 3, (
        f"Expected 'hello' count to be 3, got {top_words_with_counts.get('hello')}"
    )


# ---------------------------------------------------------------------------
# TODO: Complete these tests
# ---------------------------------------------------------------------------

def test_empty_string():
    """count_words on an empty string should return 0 total and an empty list."""
    # TODO: call count_words("") and assert:
    #   - total == 0
    #   - top is an empty list
    pass  # replace this line with your assertions


def test_string_with_only_common_words():
    """If all words are common words, the top-words list should be empty."""
    # TODO: call count_words with a string containing only words from COMMON_WORDS
    # (e.g., "the and a of to in") and assert that top is an empty list
    pass  # replace this line with your assertions


def test_single_word():
    """A single non-common word should appear in the results with count 1."""
    # TODO: call count_words("python") and assert:
    #   - total == 1
    #   - top contains ("python", 1)
    pass  # replace this line with your assertions


def test_words_with_apostrophes():
    """Words like "don't" and "it's" should be counted as single words."""
    # TODO: call count_words("don't stop won't stop") and assert:
    #   - total == 4
    #   - either "don't" or "stop" appears in top (your choice which to check)
    # Hint: if this test fails, it is related to Bug 1
    pass  # replace this line with your assertions


def test_punctuation_does_not_affect_count():
    """Punctuation marks should not be counted as words or affect word counts."""
    # TODO: these two inputs should produce the same total word count:
    #   "hello, world." and "hello world"
    # Call count_words on both and assert their totals are equal
    pass  # replace this line with your assertions
