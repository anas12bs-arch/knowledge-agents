---
title: "Marking a container unhealthy didn't stop it from taking traffic"
url: "https://dev.to/alexgeorgiev17/marking-a-container-unhealthy-didnt-stop-it-from-taking-traffic-54lf"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-11-20T17:55:17Z"
metadata:
  tag: "devops"
---

# Marking a container unhealthy didn't stop it from taking traffic

> Source: devto | Category: news | 2026-11-20T17:55:17Z

I broke a container on purpose and watched Docker mark it unhealthy for 35 seconds while nginx kept sending it a third of all traffic. The actual cause: a missing http_500 in proxy_next_upstream.

Reactions: 10
