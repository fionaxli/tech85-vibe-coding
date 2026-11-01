---
marp: true
theme: default
paginate: true
footer: "TECH 85 · Week 7 · Stanford Continuing Studies"
---

<!-- _class: lead -->
# Week 7: Agent Workflows & MCP
### TECH 85: Vibe Coding
Stanford Continuing Studies · March 3

---

## Agenda

1. Recap: Project 2 and security
2. Prompt-first vs. plan-first
3. Task decomposition in practice
4. The agent loop revisited — what changed
5. What MCP is and why it matters
6. Skills vs. MCP: a decision tree
7. Lab Part 1: plan-first exercise
8. Guest Speaker: Sai
9. Capstone launch

---

## Recap: six weeks in

Look at what you have built:

- **Project 1:** A personal Streamlit tool deployed at a real public URL
- **Project 2:** A data-connected app with SQLite and an external API

You understand the agent loop. You write CLAUDE.md files. You use Git checkpoints. You handle API keys safely.

This week: you use everything you have learned on your most ambitious project yet.

But first: a better way to give Claude Code complex tasks.

---

## The problem with big prompts

You have probably run into this.

You give Claude Code a large, complex task. It builds something. It runs. But it is 80% right and 20% wrong in ways that are hard to fix because the problem is spread across many files.

Why this happens: Claude Code is executing step by step. When it gets to step 4, it has already made assumptions in steps 1–3 that constrain what is possible. Without a plan, those assumptions go unreviewed.

The fix: **ask for the plan before asking for the code.**

---

## Plan-first: the difference in practice

**Prompt-first:**
> "Build a research assistant that searches the web, summarizes results, and saves them to my database."

Claude Code starts building. Maybe it gets it right. Often it builds the wrong thing and you cannot easily tell why.

**Plan-first:**
> "I want to build a research assistant that searches the web, summarizes results, and saves them to my database. Before you write any code, write a numbered plan. Include: what files you will create or modify, what each function will do, and what could go wrong at each step."

You read the plan. You catch the wrong assumption in step 2 before any code is written. You edit the plan. Then you execute.

One plan review saves hours of debugging.

---

## What a good plan looks like

When you ask Claude Code for a plan, you want to see:

1. A numbered list of steps in the right order
2. For each step: which file is being changed and what the change is
3. A "what could go wrong" note on any step that touches external services or complex logic
4. A list of new functions that will be added
5. How the steps connect — what each step depends on

A plan that is too short (3 steps for a complex feature) means Claude Code has not thought it through. Ask: *"This seems too simple for what I described. Add more detail for steps 2 and 3."*

A plan that is too long may be over-engineering. Ask: *"Can we simplify this? I want the simplest possible version that works."*

---

## Task decomposition in practice

"Build a research assistant" is not a task. It is a project. Break it down.

**Level 1 (too big):**
> "Build a research assistant that searches the web, summarizes, and saves."

**Level 2 (three tasks):**
1. "Add a web search function using the DuckDuckGo API. Test it with three search queries."
2. "Add a summarization function that takes a list of search results and returns a 3-sentence summary. Test it with sample data."
3. "Add a `research_log` table to SQLite and save each search + summary. Test that entries persist."

**Each task is a commit.** One commit per working step. Roll back is easy. Progress is visible.

---

## The agent loop revisited

In Week 1 you learned the basic loop:
```
Model → Harness → Tools → Result → Repeat
```

By Week 7, you understand the nuances:

- The **model** reasons better when it has a plan to follow
- The **harness** (Claude Code) maintains context across steps — but that context has limits
- The **tools** are only as useful as your instructions about when to use them
- The **result** needs to be reviewed before the next step

The big change: you are not just giving tasks. You are collaborating on a plan, then supervising an execution. That is the professional workflow.

---

## What MCP is

**MCP = Model Context Protocol**

A standard from Anthropic that defines how AI agents connect to external tools and data sources.

Without MCP: Claude Code can only see the files in your project folder. It writes code that calls APIs — but it cannot actually run those APIs itself.

With MCP: Claude Code can directly access a database, search a document corpus, call a private API, or control a browser — and get real results back in the same session.

Think of it as expanding the **Tools** part of the agent loop. Instead of just file operations and terminal commands, the agent gains access to any tool that has an MCP server.

---

## MCP in practice

You will not build an MCP server in this course. But you should know what they look like.

An MCP server is a small program that exposes a set of **tools** to an AI agent. For example:

- A SQLite MCP server lets Claude Code run SQL queries against your database directly
- A web browser MCP server lets Claude Code actually browse URLs and read content
- A Slack MCP server lets Claude Code send and read messages in your workspace

When you use Claude Code and it reads a file or runs a command, that is a built-in tool. MCP extends this to custom, domain-specific tools.

For more: [docs.anthropic.com/claude-code](https://docs.anthropic.com/claude-code) → MCP section.

---

## Skills vs. MCP: a decision tree

```
You want Claude Code to...
         |
         ├── Follow a specific workflow you define?
         │   → Use a Skill (a reusable prompt or workflow pattern)
         │
         └── Access data or tools outside your project folder?
             |
             ├── A public API (weather, news, etc.)?
             │   → Your code calls the API; Claude Code writes the code
             │
             └── A custom tool, database, or private service?
                 → MCP (define an MCP server that exposes the tool)
```

For this course: skills and direct API calls cover everything. MCP is the next step when you are building agent systems that need to reach into custom infrastructure.

---

## Demo: plan-first workflow

*[Live demo — instructor walks through:]*

1. Show a working app with a feature request
2. Give Claude Code the feature request — ask for a plan, not code
3. Read the plan with the class — find one thing to change
4. Approve the edited plan
5. Execute: "Execute this plan one step at a time. Pause after each step."
6. Watch Claude Code work through the steps
7. Commit at each step: `git commit -m "Plan step 2: add summary function"`

Key observation: the plan acts as a shared understanding. You both know what the goal is and how you are getting there.

---

## Lab overview

**What you are doing today (65 min)**

| Part | Time | What you do |
|---|---|---|
| Part 1 | 20 min | Plan-first exercise: give Claude Code a complex task, ask for a plan first |
| Guest: Sai | 45 min | Agent systems in production |
| Part 2 | 25 min | Launch Capstone: fill out capstone_BRIEF_template.md, scaffold the project |

Reference files in `starter/`: `research_agent_starter.py`, `capstone_BRIEF_template.md`

---

## Guest Speaker: Sai

Sai builds agent-powered systems for real products — not research demos, but systems that people use every day.

Tonight he will cover:
- What "agent workflow" means in a production context
- The failure modes that catch teams off guard
- How he evaluates whether an agent is reliable enough to ship
- Where he sees this field going in the next 12–18 months

Sai will speak for approximately 45 minutes, followed by the Capstone launch lab.

---

## Key takeaways

- Plan-first before complex tasks: ask for the plan, review it, then execute
- Task decomposition: large tasks succeed when broken into small, well-defined pieces with one commit per step
- MCP extends Claude Code's tool access beyond your project folder — to databases, browsers, custom services
- Skills are reusable workflow patterns; MCP is infrastructure for agent tool access
- The Capstone is your most ambitious project — write a detailed BRIEF

---

## Reading for next week

**Before Wednesday, March 10 (Demo Day):**

1. "Vibe Coding in Practice: Motivations, Challenges, and a Future" — ICSE 2026 (~20 min). Posted on Canvas. Read the abstract, introduction, and conclusion at minimum.

2. Anthropic Claude Code MCP docs at [docs.anthropic.com/claude-code](https://docs.anthropic.com/claude-code) (~10 min)

**Also:** Make significant progress on your Capstone this week. Demo Day is next Wednesday. You have 3 minutes to show something real.
