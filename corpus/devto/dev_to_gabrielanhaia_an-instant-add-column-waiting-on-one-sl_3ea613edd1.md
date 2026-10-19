---
title: "An Instant ADD COLUMN Waiting on One Slow SELECT Blocks Every Query Behind It"
url: "https://dev.to/gabrielanhaia/an-instant-add-column-waiting-on-one-slow-select-blocks-every-query-behind-it-367h"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-10-19T19:29:36Z"
metadata:
  tag: "devops"
---

# An Instant ADD COLUMN Waiting on One Slow SELECT Blocks Every Query Behind It

> Source: devto | Category: news | 2026-10-19T19:29:36Z

ADD COLUMN is instant, but it still needs an ACCESS EXCLUSIVE lock. Queue it behind one slow SELECT and every query waits. Reproduce it, then fix it.

Reactions: 1
