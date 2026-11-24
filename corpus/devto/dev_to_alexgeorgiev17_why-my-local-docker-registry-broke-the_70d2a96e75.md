---
title: "Why my local Docker registry broke the day I upgraded"
url: "https://dev.to/alexgeorgiev17/why-my-local-docker-registry-broke-the-day-i-upgraded-3olg"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-11-24T04:26:32Z"
metadata:
  tag: "devops"
---

# Why my local Docker registry broke the day I upgraded

> Source: devto | Category: news | 2026-11-24T04:26:32Z

Docker Engine 29.10 quietly stopped trusting 127.0.0.1 registries once any other insecure registry is configured. I measured exactly when it breaks, which fix only covers one port, and which one doesn't need a daemon restart.

Reactions: 10
