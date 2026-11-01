---
title: "SQLite 3.54 stops rewriting an expression index when the indexed value hasn't changed"
url: "https://dev.to/alexgeorgiev17/sqlite-354-stops-rewriting-an-expression-index-when-the-indexed-value-hasnt-changed-56bb"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-11-01T20:33:41Z"
metadata:
  tag: "devops"
---

# SQLite 3.54 stops rewriting an expression index when the indexed value hasn't changed

> Source: devto | Category: news | 2026-11-01T20:33:41Z

SQLite 3.54.1 cut a 50,000-row no-op UPDATE from 2,143 WAL pages to 511, exactly matching a table with no expression index at all. Once the indexed value actually changes, the saving disappears entirely.

Reactions: 2
