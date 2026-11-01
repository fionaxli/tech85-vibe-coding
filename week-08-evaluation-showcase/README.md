# Week 8: Demo Day
**TECH 85 · March 10 · Stanford Continuing Studies**

## Session Goals

- Evaluate your Capstone project against a test set you define
- Understand the basics of LLM-as-a-judge evaluation
- Demo your Capstone to the class in a 3-minute presentation

## Before Class

- Your Capstone must be deployed and accessible at a Streamlit Cloud URL
- If something is broken, deploy what works — a partial app you understand is better than a complete app you cannot explain
- Have your demo ready: you will open your live URL in front of the class and walk through it in exactly 3 minutes. Practice once.
- Come having read the ICSE 2026 paper: "Vibe Coding in Practice: Motivations, Challenges, and a Future"

## Session Structure

| Time | What happens |
|---|---|
| 7:00–7:15 PM | Eval exercise: run eval_harness.py and fill out eval_scorecard.md |
| 7:15–7:20 PM | Ethics / IP lightning talk (5 min) |
| 7:20–8:25 PM | Capstone demos (3 min each + 1 min Q&A) |
| 8:25–8:30 PM | Closing remarks |

## Concepts (in the first 20 min)

- **Evaluation:** A test set is a small collection of inputs with known correct outputs. You run your app on each input and check whether the output matches. This is how you know your tool is reliable, not just impressive in a demo.
- **LLM-as-a-judge:** For tasks where "correct" is hard to define (summaries, recommendations, creative output), you can ask an LLM to evaluate the output. You give it the input, the output, and a rubric. It scores the output 1–5 and explains the score. This is called LLM-as-a-judge.
- **AI ethics and IP:** When Claude Code generates code, who owns it? The short answer: you do. The longer answer depends on jurisdiction and the specific license terms of the tool you used. The general principle: if you directed the work, made meaningful decisions, and could explain it to a court, you have the stronger claim. The community norm: disclose that you used AI. The practical rule: if you cannot explain what the code does, you cannot defend it.
- **The golden rules of vibe coding:** The distillation of 8 weeks of practice. See the slides.
- **What is next:** Resources, community, and what this course was actually preparing you for.

## Lab (15 min before demos)

### Run the evaluation harness

1. Open `starter/eval_harness.py`. Read the comments — they explain how to adapt it to your Capstone.
2. Define 5 test cases for your Capstone. Each test case is:
   - An input (what the user does or types)
   - An expected output (what the app should return or show)
   - A pass/fail criterion (how you know it worked)
3. Run the harness against your Capstone.
4. Fill out `starter/eval_scorecard.md`.

You do not need to pass all 5 tests. You need to have run them and know the results.

### Ethics lightning talk (5 min)

The instructor will cover three questions:
1. What does the law currently say about AI-generated code? (short version: complicated, jurisdiction-dependent, evolving)
2. What does the community norm say? (disclose; be honest about what you built vs. what Claude built)
3. What should you do? (build in public, be honest about the tools you use, keep learning)

## Demo Format

Each student has exactly 4 minutes: 3 minutes to demo, 1 minute for one question.

**Your 3 minutes:**

1. **Open your live URL** (15 sec) — go to your Streamlit Cloud URL in the browser
2. **Tell us what it does** (20 sec) — one sentence, like you are describing it to a friend
3. **Demo the core feature** (90 sec) — do the thing. Show the AI working. Show data persisting. Show the thing you are most proud of.
4. **Tell us about one prompt you iterated on** (30 sec) — pick one place where you had to refine your direction to Claude Code. What did you ask? What went wrong? How did you fix it?
5. **Tell us about one major bug you fixed** (25 sec) — the bug, the error, how you described it to Claude Code
6. **Share the URL** (10 sec) — say your URL out loud and put it in the Canvas thread

**The Q&A minute:** one question from the class or instructor. Answer honestly — "I don't know" is a fine answer.

## What to Submit

Submit to Canvas after class:
1. Your live Capstone URL
2. Your GitHub repository link
3. Your completed eval_scorecard.md
4. Three sentences: what you built, what you would add next, what surprised you most about this course

## Reading for After the Course

1. *Beyond Vibe Coding* — any chapters you have not yet read (~ongoing reference)

2. Anthropic Claude Code documentation at [docs.anthropic.com/claude-code](https://docs.anthropic.com/claude-code) — the official reference; now that you know the tool, the docs are much more useful

3. Stanford CS146S at [themodernsoftware.dev/fall2025](https://themodernsoftware.dev/fall2025) — the reference materials from a university course using similar tools

4. GitHub's Copilot Labs and Claude Code release notes — this space moves fast; follow the official changelogs to know what is new
