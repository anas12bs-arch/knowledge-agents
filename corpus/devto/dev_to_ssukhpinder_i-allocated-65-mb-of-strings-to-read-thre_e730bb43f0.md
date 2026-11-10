---
title: "I Allocated 65 MB of Strings to Read Three Numbers"
url: "https://dev.to/ssukhpinder/i-allocated-65-mb-of-strings-to-read-three-numbers-329"
source: "devto"
category: "news"
tags: ["devto", "programming", "tech-article"]
date: "2026-11-10T17:43:51Z"
metadata:
  tag: "programming"
---

# I Allocated 65 MB of Strings to Read Three Numbers

> Source: devto | Category: news | 2026-11-10T17:43:51Z

A fixed-width parse loop was quietly allocating 65 MB of strings I read once and threw away. Swapping Substring for AsSpan and the span-based Parse overloads took it to zero.

Reactions: 1
