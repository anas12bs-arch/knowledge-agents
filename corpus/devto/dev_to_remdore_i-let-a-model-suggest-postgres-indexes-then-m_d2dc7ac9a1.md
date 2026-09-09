---
title: "I let a model suggest Postgres indexes, then made the database mark its work"
url: "https://dev.to/remdore/i-let-a-model-suggest-postgres-indexes-then-made-the-database-mark-its-work-2a4c"
source: "devto"
category: "news"
tags: ["devto", "ai", "tech-article"]
date: "2026-09-09T13:47:26Z"
metadata:
  tag: "ai"
---

# I let a model suggest Postgres indexes, then made the database mark its work

> Source: devto | Category: news | 2026-09-09T13:47:26Z

An LLM will propose an index for any query you show it. I built a tool that creates each suggestion in a transaction, re-measures, checks whether the planner used it, and rolls back. Four in ten suggestions did not survive.

Reactions: 12
