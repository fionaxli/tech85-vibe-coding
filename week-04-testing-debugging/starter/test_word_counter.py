"""
Week 4: Manual test cases for the word counter.

These are not automated pytest tests — they are plain-English assertions
you verify by running the script and checking the output yourself.

This is the human checklist approach from Week 3, applied to a command-line script.

How to use:
1. Run each test below by hand (copy the command, paste it in your terminal)
2. Compare the output to the expected result
3. If it does not match, use bug_description_template.md to describe the bug
4. Ask Claude Code to fix it

After Week 4 you can optionally ask Claude Code to convert these into real pytest tests:
    "Convert these manual test cases into pytest functions."
"""

# ============================================================
# Test cases for buggy_word_counter.py
# ============================================================

# Test 1: Basic word count
# Command: python buggy_word_counter.py sample.txt
# Expected: Total words matches the number of space-separated words in sample.txt
# How to verify: count the words in sample.txt manually (it is short enough)

# Test 2: Sentence counting with mixed punctuation
# Create a file test_sentences.txt with this content:
#   Hello world. How are you? I am great! Nice to meet you.
# Command: python buggy_word_counter.py test_sentences.txt
# Expected: Total sentences: 4
# Actual (buggy): Total sentences: 2  (only counts periods, not ? and !)

# Test 3: Top-N ordering
# Command: python buggy_word_counter.py sample.txt --top 5
# Expected: the MOST common words appear first (highest count at the top)
# Actual (buggy): the LEAST common words appear first (output is reversed)

# Test 4: Invalid --top argument
# Command: python buggy_word_counter.py sample.txt --top 0
# Expected: a clear error message: "Please specify a positive number for --top"
# Actual (buggy): either returns all words or an empty list with no explanation

# Test 5: File not found
# Command: python buggy_word_counter.py nonexistent.txt
# Expected: "Could not find the file: nonexistent.txt" and exit
# This one should already work — verify it

# Test 6: Empty file
# Create empty.txt (an empty file)
# Command: python buggy_word_counter.py empty.txt
# Expected: "Total words: 0" and "No words found" (or similar)
# Check whether the script handles this gracefully

# ============================================================
# How to create test files from the terminal
# ============================================================
#
# Create test_sentences.txt:
#   echo "Hello world. How are you? I am great! Nice to meet you." > test_sentences.txt
#
# Create empty.txt:
#   touch empty.txt   (Mac/Linux)
#   type nul > empty.txt   (Windows)
#
# ============================================================
# Turning these into real automated tests (optional, Week 4+)
# ============================================================
#
# After you fix the bugs, ask Claude Code:
# "Convert the manual test cases in test_word_counter.py into real pytest functions
#  that I can run with: pytest test_word_counter.py"
#
# Real pytest tests look like this:
#
# def test_sentence_count_mixed_punctuation():
#     text = "Hello world. How are you? I am great! Nice to meet you."
#     assert count_sentences(text) == 4
#
# pytest will run them all and tell you which pass and which fail.
