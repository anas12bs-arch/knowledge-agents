---
title: "[infoq] Presentation: Scaling LLM-Based Ranking Systems for Latency-Critical Search & Recommendation Workloads"
url: "https://www.infoq.com/presentations/scale-llm-ranking-systems-linkedin/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-11-17T17:57:14Z"
metadata:
  {}
---

# [infoq] Presentation: Scaling LLM-Based Ranking Systems for Latency-Critical Search & Recommendation Workloads

> Source: engineering | Category: engineering | 2026-11-17T17:57:14Z

Presentation: Scaling LLM-Based Ranking Systems for Latency-Critical Search & Recommendation Workloads

Sundara Raman Ramachandran shares how LinkedIn productionizes LLM ranking under strict P99 latency SLAs. He discusses distilling a 7B model down to 400M parameters, compressing job contexts into single-token embeddings for a 10x throughput leap, and eliminating hidden system bottlenecks - from custom flash attention masks to Python GIL workarounds, gc.freeze, and non-blocking CUDA memory copies.   By Sundara Raman Ramachandran
