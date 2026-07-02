---
title: "HN Hiring (Ask HN: Who is hiring? (July 2026))"
url: "https://news.ycombinator.com/item?id=48762916"
source: "hn-hiring"
category: "job-skills"
tags: ["hiring", "tech-stack", "skills", "market-demand"]
date: "2026-07-02T15:27:33Z"
metadata:
  {}
---

# HN Hiring (Ask HN: Who is hiring? (July 2026))

> Source: hn-hiring | Category: job-skills | 2026-07-02T15:27:33Z

Kog (<a href="https:&#x2F;&#x2F;kog.ai" rel="nofollow">https:&#x2F;&#x2F;kog.ai</a>) | GPU Engineer | Paris, France | REMOTE within a Europe-compatible timezone, one week per month onsite in Paris<p>We are hiring a GPU Engineer to work on the fastest LLM inference engine on standard datacenter GPUs.<p>You would own low-level kernel work in CUDA&#x2F;PTX or HIP&#x2F;CDNA ISA, the monokernel pipeline, profiling infrastructure inside it, scaling to the frontier MoE models that run in production, and building our own agents that optimize kernels and inference autonomously.<p>We generate 3,000 tokens&#x2F;s per request on 8x AMD MI300X and 2,100 on 8x NVIDIA H200, at batch size 1, FP16, no speculative decoding.<p>At batch size 1, the decode is GEMV, so it is memory bandwidth bound, and MBU is what counts.<p>We rewrote the whole hot path ourselves, from the assembly on the chip up to the Transformer we designed around it, with the full decode running as a single persistent GPU kernel.<p>Try it at <a href="https:&#x2F;&#x2F;playground.kog.ai" rel="nofollow">https:&#x2F;&#x2F;playground.kog.ai</a><p>Showing your code is part of the process.<p>If you are outside a Europe-compatible timezone, relocation to one is required.<p>Apply: <a href="https:&#x2F;&#x2F;jobs.ashbyhq.com&#x2F;kog&#x2F;e3950334-a2a6-43cc-a744-df6c38683166" rel="nofollow">https:&#x2F;&#x2F;jobs.ashbyhq.com&#x2F;kog&#x2F;e3950334-a2a6-43cc-a744-df6c386...</a><p>Questions, email me at nicolas.constant@kog.ai
