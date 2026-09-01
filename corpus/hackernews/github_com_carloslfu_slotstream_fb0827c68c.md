---
title: "Show HN: Running 104GB Qwen3.8-Flash-Next on 48GB Mac with at ~12 tok/s"
url: "https://github.com/carloslfu/slotstream"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-09-01T18:48:04Z"
metadata:
  score: "52"
---

# Show HN: Running 104GB Qwen3.8-Flash-Next on 48GB Mac with at ~12 tok/s

> Source: hackernews | Category: news | 2026-09-01T18:48:04Z

Score: 52 | Comments: 49

I built slotstream, a way to run Qwen3.8-Flash-Next 4-bit on a low-memory mac starting from 16GB, a 125B parameter model that would need 100GB+ memory&#x2F;RAM, thanks to expert-offloading&#x2F;ssd-streaming. Easy to install&#x2F;update, and mac-native using MLX and Swift.<p>It ships with auto-mode, which makes a good tradeoff between memory usage and speed. I&#x27;ll be implementing and porting the MTP module for speculative decoding next
