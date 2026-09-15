---
title: "Redis 8.10's compact hashes need HIMPORT or a restart to kick in"
url: "https://dev.to/alexgeorgiev17/redis-810s-compact-hashes-need-himport-or-a-restart-to-kick-in-hj8"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-09-15T10:03:01Z"
metadata:
  tag: "devops"
---

# Redis 8.10's compact hashes need HIMPORT or a restart to kick in

> Source: devto | Category: news | 2026-09-15T10:03:01Z

I measured Redis 8.10's compact hash templates: 20% memory savings on a typical user-profile schema, 68% on a field-name-heavy one, but plain HSET gets none of it until you restart the server.

Reactions: 5
