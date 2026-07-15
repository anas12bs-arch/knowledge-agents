---
title: "Show HN: Fast NF4 dequantization Triton kernel (1.41x faster than bitsandbytes)"
url: "https://github.com/Griffith-7/nf4-triton-kernel"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-15T15:56:49Z"
metadata:
  score: "3"
---

# Show HN: Fast NF4 dequantization Triton kernel (1.41x faster than bitsandbytes)

> Source: hackernews | Category: news | 2026-07-15T15:56:49Z

Score: 3 | Comments: 0

&quot;I wanted to see if I could optimize the dequantization bottleneck during 4-bit LLM inference. By writing a custom kernel in Triton to optimize memory access patterns, I managed to get up to a 1.41x speedup over the standard bitsandbytes implementation. Check out the source code and benchmarks, feedback is highly appreciated!&quot;
