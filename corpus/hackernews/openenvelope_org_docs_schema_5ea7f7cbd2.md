---
title: "Show HN: Open Envelope – an open schema for defining AI agent teams"
url: "https://openenvelope.org/docs/schema/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-05-30T23:38:27Z"
metadata:
  score: "11"
---

# Show HN: Open Envelope – an open schema for defining AI agent teams

> Source: hackernews | Category: news | 2026-05-30T23:38:27Z

Score: 11 | Comments: 1

Built an open JSON Schema for defining AI agent teams.<p>Multi-agent systems are becoming a real deployment pattern — not single assistants, but teams with roles, handoffs, and human checkpoints. But there&#x27;s no shared way to define one that travels across frameworks. Every implementation is scattered, locked to whichever tool you picked first. Built the schema to fix that.<p>The schema lives at schema.openenvelope.org and is registered in SchemaStore, so if you drop a .envelope.json file in VS Code you get autocomplete and validation without installing anything. It&#x27;s also on npm as @openenvelope&#x2F;schema if you want to validate programmatically.<p>The spec covers: agent definitions (role, prompt, model, access policy), supervisor&#x2F;sub-agent hierarchy, human-in-the-loop gates, pipelines, schedules, and secrets&#x2F;variables that get injected at deploy time. Access policies let you declare exactly which hosts each agent can call — the runtime enforces this at the network level, not in the prompt.<p>The goal is a portable definition format — define a team once, any compatible runtime can execute it. Similar to how Dockerfiles describe a container without being tied to a specific host. There&#x27;s a managed runtime at openenvelope.org but the schema is Apache 2.0 and anyone can implement it.<p>Happy to answer questions on any part of the spec — especially interested in feedback from people who&#x27;ve built multi-agent systems and have opinions on what&#x27;s missing.
