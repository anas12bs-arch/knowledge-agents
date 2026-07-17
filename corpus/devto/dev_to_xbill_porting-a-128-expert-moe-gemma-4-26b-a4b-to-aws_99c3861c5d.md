---
title: "Porting a 128-expert MoE (Gemma-4 26B-A4B) to AWS Inferentia2 — where every rank weighted the wrong experts"
url: "https://dev.to/xbill/porting-a-128-expert-moe-gemma-4-26b-a4b-to-aws-inferentia2-where-every-rank-weighted-the-wrong-2ege"
source: "devto"
category: "news"
tags: ["devto", "python", "tech-article"]
date: "2026-07-17T14:17:17Z"
metadata:
  tag: "python"
---

# Porting a 128-expert MoE (Gemma-4 26B-A4B) to AWS Inferentia2 — where every rank weighted the wrong experts

> Source: devto | Category: news | 2026-07-17T14:17:17Z

The MoE was the hard one: a dual-path FFN, a sparse expert loop that won't trace, and a bug where the device output was empty while the CPU reference was perfect and every unit test passed.

Reactions: 1
