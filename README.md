# TECH 85: Vibe Coding

**Stanford Continuing Studies · Winter 2026**

| | |
|---|---|
| **Instructor** | Fiona Li |
| **Sessions** | Wednesdays, 7:00–8:30 PM PT |
| **Dates** | January 20 – March 10, 2026 |
| **Location** | Stanford Campus (room posted on Canvas) |
| **Units** | 1 continuing studies unit (optional) |

---

## What makes this course different

Most coding courses teach you to write code. This course teaches you to **direct** an AI that writes code for you — then read, test, and own what it builds.

You will leave with three real, deployed projects and a mental model that transfers to every tool that comes next. The skill you are developing is not Python syntax. It is **context engineering**: knowing how to give an AI coding agent the right information at the right time, so it builds exactly what you have in mind.

This course uses **Claude Code** exclusively. One tool, learned deeply, from Week 1 through Demo Day.

---

## What you will be able to do

By the end of this course, you will be able to:

1. Launch Claude Code and direct it to build a working web application from a plain-language description
2. Write a BRIEF.md specification that gives an AI coding agent everything it needs to get started
3. Read AI-generated code confidently — enough to catch errors, ask good follow-up questions, and make informed decisions
4. Connect your app to a database (SQLite) and an external API, without managing a server
5. Use Git to checkpoint your work before risky changes, and roll back when something breaks
6. Describe bugs precisely enough that Claude Code can diagnose and fix them
7. Deploy a working app to a public URL and walk someone through it in three minutes

---

## The three projects

Every student ships three real projects during the course. Each project has three track options — pick one or bring your own.

| Project | Weeks | What you build | Track A | Track B | Track C |
|---|---|---|---|---|---|
| **Project 1** | 2–3 | A personal tool deployed as a Streamlit web app with a real public URL | Daily habit tracker | Reading list manager | Bring your own idea |
| **Project 2** | 5–6 | A data-connected app using SQLite and an external API | Local weather journal (OpenWeatherMap) | News digest saver (NewsAPI) | Bring your own idea |
| **Capstone** | 7–8 | Your most ambitious project — an agent, a multi-step tool, or a polished product you are proud to show publicly | Personal productivity agent | Data dashboard with live feeds | Bring your own idea |

**Track C** (bring your own) is encouraged for anyone with a clear use case. Come to Week 2 with an idea and the class will help you scope it.

---

## Weekly schedule

| Week | Date | Title | Project milestone | Guest |
|---|---|---|---|---|
| 1 | Jan 20 | The Vibe Coding Mindset | — | — |
| 2 | Jan 27 | Context Engineering & Your BRIEF | Launch Project 1 | — |
| 3 | Feb 3 | Read, Test & Ship | Project 1 demo (3 min each) | — |
| 4 | Feb 10 | Claude Code + Git | — | Steve (~45 min) |
| 5 | Feb 17 | Data & Agent-Ready Repos | Launch Project 2 | — |
| 6 | Feb 24 | APIs, Auth & Security | Project 2 demo (3 min each) | — |
| 7 | Mar 3 | Agent Workflows & MCP | Launch Capstone | Sai (~45 min) |
| 8 | Mar 10 | Demo Day | Capstone demo (3 min each) | — |

---

## Tools

You need these installed before Week 1. Setup guides are linked in the Week 1 README.

| Tool | What it is | Cost |
|---|---|---|
| **Claude Code** | The AI coding agent used throughout the course. Runs in your terminal. | ~$20/month (Anthropic Pro or Max plan) |
| **Python 3.10+** | The programming language Claude Code will write. You will not type Python yourself — but it needs to be installed. | Free |
| **VS Code** | A code editor. You will read code here, not write it. | Free |
| **Git + GitHub** | Version control. Git saves checkpoints locally; GitHub stores them in the cloud. | Free |
| **Streamlit Cloud** | Deploys your app to a real public URL. One click from GitHub. | Free |

**Important:** Claude Code requires an Anthropic account. The course uses the API or a Pro/Max subscription. Check current pricing at anthropic.com. Stanford does not provide API credits.

---

## Required readings

All readings are free to access.

**Primary text:** *Beyond Vibe Coding* by Addy Osmani (O'Reilly, 2025). Available free via O'Reilly Learning through the Stanford library (library.stanford.edu → Databases → O'Reilly).

**Reference materials:** Stanford CS146S public course materials at [themodernsoftware.dev/fall2025](https://themodernsoftware.dev/fall2025)

**Paper (Week 8):** "Vibe Coding in Practice: Motivations, Challenges, and a Future" — ICSE 2026 proceedings

Specific chapters and links are assigned at the bottom of each week's README. Total reading per week: 30 minutes maximum.

---

## Guest speakers

| Week | Guest | Topic |
|---|---|---|
| **Week 4 (Feb 10)** | **Steve** | How AI fits into real software projects — practical tips from someone who builds with these tools every day. Steve will speak for approximately 45 minutes, followed by a lab on Claude Code + Git. |
| **Week 7 (Mar 3)** | **Sai** | How agents are used in real products — what works in practice, what the failure modes are, and where the field is heading. Sai will speak for approximately 45 minutes, followed by the Capstone launch. |

---

## FAQ

**"I have never written a line of code. Will I be lost?"**
No. This course is designed from the ground up for non-programmers. The first thing you will do in Week 1 is run a Python script — and you will not have written a single line of it. The skills that matter here are clear thinking, good communication, and curiosity. You have all of those.

**"I already know how to code. Is this too basic?"**
Probably not. The interesting challenge in this course is not writing code — it is directing an AI to write code well. Experienced programmers often find they need to unlearn the habit of writing everything themselves. The context engineering and agent workflow skills in Weeks 5–7 are useful regardless of prior experience.

**"What if my project is not done by the demo week?"**
You demo what you have. A partially working app you understand is better than a complete app you cannot explain. Demos are 3 minutes; the goal is to show something real and explain one decision you made.

**"Can I use these projects in a portfolio?"**
Yes. Everything you build is yours. The course uses an MIT License on the starter code, which means you can use, modify, and publish your projects freely. Including AI-generated code in a portfolio is increasingly normal; Week 8 covers how to discuss it honestly.

**"How much time should I expect to spend outside of class?"**
About 1–2 hours per week: 30 minutes of reading and 30–90 minutes working on your project. Project weeks (2–3, 5–6, 7–8) require more time. The workload is manageable if you keep up week to week.

---

## Repository structure

```
week-01-first-tool/        Week 1 lab guide and starter files
week-02-specs-and-prompts/ Week 2 lab guide and templates
week-03-reading-code-safely/
week-04-testing-debugging/
week-05-git-github/
week-06-files-and-data/
week-07-agents-web-services/
week-08-evaluation-showcase/
```

Each week folder contains:
- `README.md` — the lab guide for that session
- `slides.md` — lecture slides in Marp format
- `starter/` — runnable starter files for the lab

---

## Getting the materials

**Without a GitHub account:** click the green **Code** button at the top of this page, then **Download ZIP**.

**With Git:** `git clone <repository URL>` (covered in Week 4).

---

## License

Code and written materials in this repository are released under the [MIT License](LICENSE).
