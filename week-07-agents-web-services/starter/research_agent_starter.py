"""Week 7 starter: research helper agent.

This agent takes a question from the command line, searches Wikipedia for
relevant information, then asks Claude to summarize an answer based on
what it found.

How to run:
    python research_agent_starter.py "What is machine learning?"
    python research_agent_starter.py "Who invented the telephone?"

Setup:
    pip install anthropic requests python-dotenv

    Set your Anthropic API key in a .env file in this folder:
        ANTHROPIC_API_KEY=sk-ant-your-key-here

    OR set it as an environment variable:
        export ANTHROPIC_API_KEY=sk-ant-your-key-here   (Mac/Linux)
        set ANTHROPIC_API_KEY=sk-ant-your-key-here      (Windows)

Lab task:
    Three sections are marked TODO. Implement each one using AI help.
    See the README for step-by-step instructions.
"""

import os
import sys
import urllib.parse

import requests

# Load .env file if it exists (sets ANTHROPIC_API_KEY from .env)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # python-dotenv not installed; assume env var is set another way

try:
    import anthropic
except ImportError:
    print("Error: the 'anthropic' library is not installed.")
    print("Run: pip install anthropic")
    sys.exit(1)


# ---------------------------------------------------------------------------
# TODO 1: Implement the Wikipedia search function
# ---------------------------------------------------------------------------

def search_wikipedia(query: str) -> str:
    """Search Wikipedia and return a plain-text summary of the most relevant article.

    Uses the Wikipedia REST API:
        https://en.wikipedia.org/api/rest_v1/page/summary/{title}

    Steps to implement:
    1. URL-encode the query so spaces and special characters work in a URL.
       Use: urllib.parse.quote(query)
    2. Make a GET request to the Wikipedia summary endpoint with that title.
       Set a timeout of 10 seconds.
    3. If the response status code is 200, return the "extract" field from
       the JSON response (this is the plain-English article summary).
    4. If the status code is 404 (article not found), return this string:
       "No Wikipedia article found for: {query}"
    5. If any other error occurs (network error, timeout, etc.), return:
       "Wikipedia search failed: {error message}"

    Args:
        query: a search term, e.g., "photosynthesis" or "Alan Turing"

    Returns:
        A string containing the Wikipedia article summary, or an error message.
    """
    # TODO 1: implement this function
    # Remove the line below and replace with your implementation
    raise NotImplementedError("TODO 1: implement search_wikipedia")


# ---------------------------------------------------------------------------
# TODO 2: Implement the Claude summarizer function
# ---------------------------------------------------------------------------

def summarize_with_claude(question: str, context: str) -> str:
    """Use the Anthropic API to answer a question based on provided context.

    Steps to implement:
    1. Create an Anthropic client: client = anthropic.Anthropic()
       It will automatically read ANTHROPIC_API_KEY from environment variables.
    2. Build a prompt that:
       - Provides the context (Wikipedia text) to Claude
       - Asks Claude to answer the question using only the provided context
       - Asks for a concise answer in 2-3 sentences
       - Tells Claude to say "I don't have enough information" if the context
         doesn't contain the answer
    3. Call client.messages.create() with:
       - model="claude-opus-4-5"
       - max_tokens=512
       - messages=[{"role": "user", "content": your_prompt}]
    4. Return the text of the first content block:
       message.content[0].text
    5. If an AuthenticationError occurs, return a helpful message telling the
       user their API key is missing or incorrect.
    6. If any other error occurs, return: "Claude summarization failed: {error}"

    Args:
        question: the user's original question
        context: text retrieved from Wikipedia (or an error message)

    Returns:
        A string containing Claude's answer.
    """
    # TODO 2: implement this function
    # Remove the line below and replace with your implementation
    raise NotImplementedError("TODO 2: implement summarize_with_claude")


# ---------------------------------------------------------------------------
# TODO 3: Add one improvement of your choice
# ---------------------------------------------------------------------------

def apply_improvement(question: str, answer: str, context: str) -> None:
    """Apply one improvement to the research helper output.

    This function is called after the main answer is printed.
    Choose ONE of these to implement (or propose your own):

    Option A — Show the source:
        Print the Wikipedia article title and URL so the user can read more.
        The Wikipedia URL for a title is: https://en.wikipedia.org/wiki/{url_encoded_title}

    Option B — Save to log file:
        Append the question, answer, and timestamp to a file called
        "research_log.txt" so users can review past queries.
        Use: from datetime import datetime; datetime.now().isoformat()

    Option C — Interactive loop:
        This function doesn't directly support it, but you can modify main()
        to keep asking for questions until the user types "quit".

    Option D — Confidence check:
        Ask Claude a second question: "On a scale of 1-10, how confident are
        you in the answer you just gave, and why?" Print the confidence rating.

    Args:
        question: the user's original question
        answer: the answer Claude produced
        context: the Wikipedia context that was used
    """
    # TODO 3: implement one improvement
    # If you choose Option C, modify main() instead of this function
    pass  # replace this with your implementation


# ---------------------------------------------------------------------------
# Main — reads question from command line, runs the agent loop
# (structure is complete; do not modify until you have finished TODO 1 and 2)
# ---------------------------------------------------------------------------

def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python research_agent_starter.py \"your question here\"")
        print("Example: python research_agent_starter.py \"What is photosynthesis?\"")
        sys.exit(1)

    question = " ".join(sys.argv[1:])

    print(f"Question: {question}")
    print("Searching Wikipedia...")

    context = search_wikipedia(question)

    if not context:
        context = "No information was found."

    print("Asking Claude to summarize...")

    answer = summarize_with_claude(question, context)

    print()
    print("Answer:")
    print(answer)
    print()

    # Call the improvement function (TODO 3)
    apply_improvement(question, answer, context)


if __name__ == "__main__":
    main()
