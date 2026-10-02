---
title: "Redis says the key is gone. The memory comes back 22 seconds later."
url: "https://dev.to/remdore/redis-says-the-key-is-gone-the-memory-comes-back-22-seconds-later-5ap5"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-10-02T21:52:27Z"
metadata:
  tag: "devops"
---

# Redis says the key is gone. The memory comes back 22 seconds later.

> Source: devto | Category: news | 2026-10-02T21:52:27Z

Five million keys expiring on the same second held 810 MB for 22.8 seconds after every client agreed they were gone. A busy Redis reclaims four times faster than an idle one, which is backwards from what I assumed.

Reactions: 5
