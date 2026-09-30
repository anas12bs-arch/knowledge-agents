---
title: "One long SELECT, one ALTER TABLE, and every query behind them"
url: "https://dev.to/remdore/one-long-select-one-alter-table-and-every-query-behind-them-3l6i"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-09-30T08:47:02Z"
metadata:
  tag: "devops"
---

# One long SELECT, one ALTER TABLE, and every query behind them

> Source: devto | Category: news | 2026-09-30T08:47:02Z

The same primary key lookup took 1.2 ms and 2841.2 ms, seven hundred milliseconds apart. Postgres queues lock requests in arrival order, so a blocked ALTER TABLE blocks the readers behind it.

Reactions: 6
