---
title: "Launch HN: General Instinct (YC P26) – Frontier models on edge devices"
url: "https://news.ycombinator.com/item?id=48414869"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-06-05T18:26:40Z"
metadata:
  score: "17"
---

# Launch HN: General Instinct (YC P26) – Frontier models on edge devices

> Source: hackernews | Category: news | 2026-06-05T18:26:40Z

Score: 17 | Comments: 8

Hey HN, Guanming and Bill here from General Instinct (<a href="https:&#x2F;&#x2F;general-instinct.com&#x2F;">https:&#x2F;&#x2F;general-instinct.com&#x2F;</a>).<p>After years of working in robotics, we kept running into the same problem: the best models never fit the hardware we actually had available.<p>The models that performed best were usually designed around datacenter assumptions: large GPUs, lots of memory bandwidth, and reliable network access. But most physical systems have the opposite constraints.<p>That led us down the path of figuring out how much of a frontier model could be preserved while still making it practical to run on edge hardware.<p>As part of that work, we recently open sourced InstinctRazor (<a href="https:&#x2F;&#x2F;github.com&#x2F;General-Instinct&#x2F;InstinctRazor" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;General-Instinct&#x2F;InstinctRazor</a>)<p>One result we&#x27;re excited about is compressing Qwen3.5-122B-A10B, a roughly 245 GB BF16 MoE model, into a 48 GiB GGUF. The resulting model is actually smaller than Gemma-4-26B-A4B while outperforming it on benchmarks like MMLU-Pro and GPQA-D etc. we preserve the parts that are always active (router, norms, Gated-DeltaNet&#x2F;SSM layers, vision pathway, etc.) and quantize the routed experts much more aggressively. We then use on-policy distillation to recover capability lost during quantization.<p>The model can also run in a &quot;small GPU&quot; configuration where experts are streamed from system RAM. With an 8k context window, peak VRAM usage is around 7.6–8 GB.<p>If you&#x27;re interested in the technical details, we wrote up the approach here (<a href="https:&#x2F;&#x2F;general-instinct.com&#x2F;blog&#x2F;frontier-moe-sub-4-bit">https:&#x2F;&#x2F;general-instinct.com&#x2F;blog&#x2F;frontier-moe-sub-4-bit</a>)<p>We&#x27;re especially interested in hearing from people deploying models onto robots or other edge devices. What models are you trying to run locally today? What has been the biggest bottleneck in getting them into production?
