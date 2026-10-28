---
title: "440 MB of Closures on Pure Cache Hits"
url: "https://dev.to/ssukhpinder/440-mb-of-closures-on-pure-cache-hits-35l"
source: "devto"
category: "news"
tags: ["devto", "programming", "tech-article"]
date: "2026-10-28T19:12:22Z"
metadata:
  tag: "programming"
---

# 440 MB of Closures on Pure Cache Hits

> Source: devto | Category: news | 2026-10-28T19:12:22Z

My ConcurrentDictionary cache was all hits, yet it churned the GC. The GetOrAdd factory closed over a loop-local, so it allocated a closure on every call even though the factory never ran. The state-arg overload does the same work at zero bytes.

Reactions: 1
