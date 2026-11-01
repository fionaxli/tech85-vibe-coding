# Week 7: Agent Workflows & MCP
**TECH 85 · March 3 · Stanford Continuing Studies**

## Session Goals

- Use the plan-first workflow to give Claude Code complex multi-step tasks
- Understand what MCP (Model Context Protocol) is and when it matters
- Launch your Capstone project with a complete BRIEF.md and CLAUDE.md

## Before Class

- Bring your Project 2 app — we will reference it when discussing agent workflows
- Come with a Capstone idea. It can be ambitious. The prompt: "What is the most useful thing I could build?" The Capstone is your most significant project and should be something you are proud to show publicly.
- Review the Week 6 reading (Chapters 9–10 of *Beyond Vibe Coding*) before class

## Concepts (20 min)

- **Plan-first vs. prompt-first:** Prompt-first means throwing a big task at Claude Code and hoping it figures it out. It sometimes works for small tasks. For complex ones — "build me a multi-step tool that does X, Y, and Z" — it usually produces something partially wrong that is hard to untangle. Plan-first means asking Claude Code to write a plan first, before writing any code. You review the plan, edit it, and only then ask Claude Code to execute. This dramatically improves the output on complex tasks.
- **Task decomposition:** Large tasks succeed when they are broken into small, well-defined pieces. "Build a research assistant that searches the web, summarizes the results, and saves them to a database" is three distinct tasks. Each one should be its own prompt, its own commit, its own verification step.
- **MCP (Model Context Protocol):** A standard developed by Anthropic that lets AI agents connect to external tools and data sources. With MCP, Claude Code can access a database, search a specific corpus of documents, call a private API, or control a browser — not just the files in your project folder. You will not build an MCP server in this course, but you should understand what it is and when it applies.
- **Skills vs. MCP:** In Claude Code's architecture, a "skill" is a reusable prompt or workflow pattern that the user defines. MCP is a protocol for giving agents access to external tools and data. Skills are about what you ask; MCP is about what Claude Code can access. When your project needs Claude Code to reach outside your files — to a database, an API, or a running service — that is an MCP use case.

## Lab (65 min)

### Part 1: Plan-first exercise (20 min)

Before our guest arrives, you will practice the plan-first workflow on a complex task.

1. Think of a complex feature you want to add to your project — something that would require three or more changes to different parts of your codebase.
2. Give this task to Claude Code, but ask for a plan first, not code:
   > "I want to [describe the complex feature]. Before you write any code, write a numbered plan of the steps you would take. Include: what files you will change, what new functions you will add, and what could go wrong. Do not write any code yet."
3. Read the plan. Edit it if you see something wrong or missing. Add a step for error handling if it is not there.
4. Then say: "Execute this plan, one step at a time. After each step, pause and tell me what you did before continuing."
5. Compare the result to what you would have gotten from a single big prompt.

See `starter/research_agent_starter.py` for a complete example of the plan-first pattern applied to a research tool.

---

### Guest: Sai (~45 min)

Sai works on agent systems in production. Tonight he will share:
- How agents are actually used in real products — not demos, real usage
- What the failure modes are (and they are different from what people expect)
- Where he sees the field going in the next 12–18 months

Come with questions. Specific ones tend to get better answers than general ones.

---

### Part 2: Launch your Capstone (25 min)

Your Capstone is your most ambitious project. The best Capstones from previous terms have been:
- Personal productivity agents that automate a repetitive task
- Data dashboards with live feeds that aggregate information from multiple sources
- Domain-specific tools (for a field the student knows well) that a real person would actually use

**Step 1:** Fill out `starter/capstone_BRIEF_template.md`. Take it seriously — your Capstone BRIEF should be more detailed than your Project 1 or 2 BRIEF. Include the "What makes this portfolio-worthy?" section.

**Step 2:** Give your completed Capstone BRIEF to Claude Code and ask it to scaffold the project:
> "Read this BRIEF.md and create a project structure for my Capstone. Include: app.py, db.py (if needed), requirements.txt, a CLAUDE.md, and a schema.sql (if there is a database). Do not build the full app yet — just the skeleton with placeholder functions and comments."

**Step 3:** Review the scaffold. Make sure it matches your vision. Ask Claude Code to explain anything that surprises you.

**Step 4:** Commit the scaffold with a clear message:
```
git commit -m "Capstone launch: scaffold from BRIEF.md"
```

## Project Milestone

**Capstone launched.** Submit to Canvas:
1. Your completed Capstone BRIEF.md
2. A link to your Capstone GitHub repository (even if it is just a scaffold)
3. One sentence: what makes this your most ambitious project so far

## Reading for Next Week

1. "Vibe Coding in Practice: Motivations, Challenges, and a Future" — ICSE 2026. Posted on Canvas. (~20 min). We will discuss this paper in Week 8's ethics segment. Note: this paper is academic but readable. Read for the main arguments, not the statistics.

2. Anthropic's Claude Code documentation on MCP at [docs.anthropic.com/claude-code](https://docs.anthropic.com/claude-code) (~10 min). Skim the MCP section. You now have enough context to understand what the docs are describing.
