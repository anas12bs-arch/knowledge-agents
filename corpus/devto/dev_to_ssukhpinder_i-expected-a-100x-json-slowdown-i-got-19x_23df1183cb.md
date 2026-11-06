---
title: "I Expected a 100x JSON Slowdown. I Got 1.9x."
url: "https://dev.to/ssukhpinder/i-expected-a-100x-json-slowdown-i-got-19x-3d6n"
source: "devto"
category: "news"
tags: ["devto", "programming", "tech-article"]
date: "2026-11-06T10:01:06Z"
metadata:
  tag: "programming"
---

# I Expected a 100x JSON Slowdown. I Got 1.9x.

> Source: devto | Category: news | 2026-11-06T10:01:06Z

I benchmarked the old 'never build a new JsonSerializerOptions per call' rule on .NET 10, expecting the famous 100x penalty. I got 1.9x. Here's why the runtime now rescues you, and the one case where it still doesn't.

Reactions: 0
