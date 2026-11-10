---
title: "Postmortem (hypothetical): our health check was so thorough it took every instance out of the load balancer at once"
url: "https://dev.to/upordownonline/postmortem-hypothetical-our-health-check-was-so-thorough-it-took-every-instance-out-of-the-load-158m"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-11-10T17:43:53Z"
metadata:
  tag: "devops"
---

# Postmortem (hypothetical): our health check was so thorough it took every instance out of the load balancer at once

> Source: devto | Category: news | 2026-11-10T17:43:53Z

A health check that tested the database seemed responsible. When the database slowed down, every instance failed it together, and a partial slowdown became a full outage. A hypothetical, blameless writeup.

Reactions: 1
