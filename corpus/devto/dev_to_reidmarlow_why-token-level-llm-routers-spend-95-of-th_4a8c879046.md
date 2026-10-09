---
title: "Why Token-Level LLM Routers Spend 95% of Their Time on Cache Bookkeeping"
url: "https://dev.to/reidmarlow/why-token-level-llm-routers-spend-95-of-their-time-on-cache-bookkeeping-5959"
source: "devto"
category: "news"
tags: ["devto", "python", "tech-article"]
date: "2026-10-09T18:50:36Z"
metadata:
  tag: "python"
---

# Why Token-Level LLM Routers Spend 95% of Their Time on Cache Bookkeeping

> Source: devto | Category: news | 2026-10-09T18:50:36Z

Routing 5% of hard tokens to a 32B model and keeping the rest on a 0.6B model looks great on paper, until standard serving engines spend 95.8% of the step redoing prefix matching. TokenRouter fixes the scheduler and hits up to 64x higher throughput.

Reactions: 5
