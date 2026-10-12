---
title: "Traefik 3.7's service middlewares target one branch of a weighted service"
url: "https://dev.to/alexgeorgiev17/traefik-37s-service-middlewares-target-one-branch-of-a-weighted-service-3i3h"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-10-12T22:48:29Z"
metadata:
  tag: "devops"
---

# Traefik 3.7's service middlewares target one branch of a weighted service

> Source: devto | Category: news | 2026-10-12T22:48:29Z

I tested Traefik 3.7's new service-level middlewares on a 90/10 weighted canary service: 20 of 200 requests landed on the canary branch and all 20 carried the canary-only header, with zero leaks across 500 concurrent requests. Traefik's own announcement blog shows YAML that doesn't parse on the real software.

Reactions: 9
