---
title: "Valkey 9.2's INCREX command removes the crash window between INCR and EXPIRE"
url: "https://dev.to/alexgeorgiev17/valkey-92s-increx-command-removes-the-crash-window-between-incr-and-expire-1344"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-10-07T16:21:25Z"
metadata:
  tag: "devops"
---

# Valkey 9.2's INCREX command removes the crash window between INCR and EXPIRE

> Source: devto | Category: news | 2026-10-07T16:21:25Z

Valkey 9.2.0-rc1's new INCREX command merges an atomic increment and expiry into one round trip. A simulated crash between the old INCR and EXPIRE calls left 11 of 489 keys with no TTL; INCREX left zero, and its latency edge over the old pattern shrinks from about 2x to roughly 1.1x once you pipeline it.

Reactions: 7
