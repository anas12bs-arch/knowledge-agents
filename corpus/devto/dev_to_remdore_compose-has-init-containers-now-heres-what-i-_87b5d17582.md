---
title: "Compose has init containers now. Here's what I deleted."
url: "https://dev.to/remdore/compose-has-init-containers-now-heres-what-i-deleted-903"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-09-08T13:39:40Z"
metadata:
  tag: "devops"
---

# Compose has init containers now. Here's what I deleted.

> Source: devto | Category: news | 2026-09-08T13:39:40Z

Docker Compose 5.3 added pre_start steps: run migrations and seeds in throwaway containers before the service starts, with no one-off services and no depends_on chain. I tested reruns, failure, scaling, and found one thing I don't like.

Reactions: 5
