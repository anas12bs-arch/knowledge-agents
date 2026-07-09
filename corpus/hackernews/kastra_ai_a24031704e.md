---
title: "Show HN: Policy enforcement for Claude Code, Cursor, and Codex"
url: "https://kastra.ai/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-09T20:12:02Z"
metadata:
  score: "4"
---

# Show HN: Policy enforcement for Claude Code, Cursor, and Codex

> Source: hackernews | Category: news | 2026-07-09T20:12:02Z

Score: 4 | Comments: 0

Show HN: Runtime authorization for Claude Code, Cursor, and Codex<p>Hi HN, Fernando and I built Kastra. Kastra intercepts AI agent tool calls and evaluates them against deterministic policies before they execute. This is aimed at developers using coding agents like Claude Code, Codex, Cursor, and OpenClaw.<p>We built Kastra after one of our Cursor agents almost executed DELETE FROM customers WHERE status=&#x27;test&#x27; against a production database. We caught it before it ran, but it made us realize that nothing in our stack actually decided what the agent was allowed to do. What mattered for us wasn&#x27;t the mistake; it was realizing nothing in our setup would have stopped it if we weren&#x27;t actively on top of it. LLMs are probabilistic, and prompts influence behavior, but they don&#x27;t deterministically decide what an agent is allowed to do. Without a deterministic policy system, nothing could have decided what it was allowed to do.<p>Kastra pushes an allow, hold, and deny decision before the action runs. You can build these policies in plain English from the web app. The interception engine evaluates the tools, targets, and parameters of every action. We also shipped many policy packs covering common high-risk scenarios, and every decision is recorded in an immutable audit trail. The desktop app, CLI, dashboard, and Recon scan are free to use for developers.<p>If you often use Claude, Codex, Openclaw, and Cursor, Kastra can run a scan command on which risky actions your agents have already taken and automatically build rules to avoid them from happening again. Recon is a feature of Kastra that scans your local agent history. In order to run this scan, execute the commands below in your coding agent.<p>brew install kastra-labs&#x2F;tap&#x2F;kastra-edge<p>kastra-edge scan<p>The scan reads your local agent session history, and it shows all the risky actions your agent has already taken before, the secrets written to tracked files, production databases touched, force pushes, curl-to-shell, and more. This runs on your machine, and secrets never leave. In our own use cases, we kept finding things we&#x27;d forgotten or didnt know agents had done.<p>Each finding can be converted into a runtime policy, letting you delegate more work to AI without trusting the model itself. Kastra intercepts all workloads at runtime and makes sure these policy evaluations typically complete in under a millisecond. Instead of trusting the model, you trust the deterministic rules that govern its actions.<p>One problem we are still working on to improve the stack is how to manage teams of agents with conflicting policies. We would love feedback from anyone building multi-agent systems. Fernando and I will be reviewing the comments. We are super curious what your first scan finds. Please post results below so we can see what the most common patterns are and adjust policy packs for our users based on your feedback.<p>Documentation: 
<a href="https:&#x2F;&#x2F;kastra.ai&#x2F;docs" rel="nofollow">https:&#x2F;&#x2F;kastra.ai&#x2F;docs</a><p>Download for MacOS Kastra Edge: 
<a href="https:&#x2F;&#x2F;kastra.ai&#x2F;edge&#x2F;download.html" rel="nofollow">https:&#x2F;&#x2F;kastra.ai&#x2F;edge&#x2F;download.html</a><p>Check Kastra in action today:
<a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=6TUETu5lb3Q&amp;feature=youtu.be" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=6TUETu5lb3Q&amp;feature=youtu.be</a>
