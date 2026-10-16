---
title: "PostgreSQL 19 beta's parallel autovacuum launches workers but leaves vacuum time unchanged"
url: "https://dev.to/alexgeorgiev17/postgresql-19-betas-parallel-autovacuum-launches-workers-but-leaves-vacuum-time-unchanged-3g4j"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-10-16T11:40:43Z"
metadata:
  tag: "devops"
---

# PostgreSQL 19 beta's parallel autovacuum launches workers but leaves vacuum time unchanged

> Source: devto | Category: news | 2026-10-16T11:40:43Z

I measured PostgreSQL 19 beta4's new parallel autovacuum on a six-index, 400,000-row table: 4 workers launched every time, but wall-clock vacuum time stayed within 4% of the serial run, while dead-tuple memory doubled.

Reactions: 6
