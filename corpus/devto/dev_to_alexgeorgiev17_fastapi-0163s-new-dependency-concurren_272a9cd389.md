---
title: "FastAPI 0.163's new dependency concurrency limit deadlocked two of my routes"
url: "https://dev.to/alexgeorgiev17/fastapi-0163s-new-dependency-concurrency-limit-deadlocked-two-of-my-routes-33k6"
source: "devto"
category: "news"
tags: ["devto", "python", "tech-article"]
date: "2026-11-18T16:26:15Z"
metadata:
  tag: "python"
---

# FastAPI 0.163's new dependency concurrency limit deadlocked two of my routes

> Source: devto | Category: news | 2026-11-18T16:26:15Z

FastAPI 0.163.0's Depends(max_concurrency=...) cut 20 concurrent calls to a peak of 5, but applies per Depends() object and per worker process, and two yield dependencies acquired in opposite order hung forever.

Reactions: 9
