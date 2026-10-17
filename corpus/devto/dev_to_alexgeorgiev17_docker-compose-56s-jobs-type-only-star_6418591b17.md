---
title: "Docker Compose 5.6's jobs type only starts through docker compose run"
url: "https://dev.to/alexgeorgiev17/docker-compose-56s-jobs-type-only-starts-through-docker-compose-run-4c1a"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-10-17T17:18:47Z"
metadata:
  tag: "devops"
---

# Docker Compose 5.6's jobs type only starts through docker compose run

> Source: devto | Category: news | 2026-10-17T17:18:47Z

Docker Compose 5.6 added a jobs: section for one-off tasks. up, create and start all refuse to touch one, a scheduled trigger makes up fail outright, and only docker compose run actually starts a job, paying about 15% more when its dependency has to start cold.

Reactions: 6
