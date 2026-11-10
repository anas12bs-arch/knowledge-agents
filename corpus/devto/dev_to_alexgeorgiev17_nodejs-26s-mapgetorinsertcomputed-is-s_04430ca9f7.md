---
title: "Node.js 26's Map.getOrInsertComputed is slower than the get-and-set it replaces"
url: "https://dev.to/alexgeorgiev17/nodejs-26s-mapgetorinsertcomputed-is-slower-than-the-get-and-set-it-replaces-2i35"
source: "devto"
category: "news"
tags: ["devto", "webdev", "tech-article"]
date: "2026-11-10T17:43:52Z"
metadata:
  tag: "webdev"
---

# Node.js 26's Map.getOrInsertComputed is slower than the get-and-set it replaces

> Source: devto | Category: news | 2026-11-10T17:43:52Z

I benchmarked Node 26.13's new Map.prototype.getOrInsertComputed: 13-18% slower than plain get-then-set on a cold map, about 40% slower on a warm one, but it collapses three concurrent async fetches for the same key into one call, and caches a rejected promise forever.

Reactions: 6
