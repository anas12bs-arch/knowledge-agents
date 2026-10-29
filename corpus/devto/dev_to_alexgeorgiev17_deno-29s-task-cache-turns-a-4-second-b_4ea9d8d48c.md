---
title: "Deno 2.9's task cache turns a 4-second build into a 10-millisecond skip"
url: "https://dev.to/alexgeorgiev17/deno-29s-task-cache-turns-a-4-second-build-into-a-10-millisecond-skip-43bn"
source: "devto"
category: "news"
tags: ["devto", "javascript", "tech-article"]
date: "2026-10-29T15:34:56Z"
metadata:
  tag: "javascript"
---

# Deno 2.9's task cache turns a 4-second build into a 10-millisecond skip

> Source: devto | Category: news | 2026-10-29T15:34:56Z

I measured Deno's new deno task caching: 3.9s cold against 9ms warm on a real build step, but a 3000-file input tree made the cache check itself about 4x slower than running an untracked task.

Reactions: 9
