---
title: "HN Hiring (Ask HN: Who is hiring? (October 2026))"
url: "https://news.ycombinator.com/item?id=49922850"
source: "hn-hiring"
category: "job-skills"
tags: ["hiring", "tech-stack", "skills", "market-demand"]
date: "2026-10-01T16:27:05Z"
metadata:
  {}
---

# HN Hiring (Ask HN: Who is hiring? (October 2026))

> Source: hn-hiring | Category: job-skills | 2026-10-01T16:27:05Z

Thunder Compute (YC S24) | C++ Systems, Infrastructure, BizOps | San Francisco (Onsite) | Full-time | <a href="https:&#x2F;&#x2F;www.thundercompute.com">https:&#x2F;&#x2F;www.thundercompute.com</a><p>We&#x27;re building the VMware for GPUs. Most GPUs in the cloud sit idle a lot of the time because they&#x27;re bolted to one machine over PCIe. We decouple them.<p>Our virtualization layer is a userspace shim, loaded through LD_PRELOAD, that intercepts CUDA calls and ships them over the network to a host with a physical GPU somewhere else in the data center. Workloads run unchanged. When a process goes idle, the GPU detaches and gets reassigned, and reattaches in tens of milliseconds when it&#x27;s needed again. Think Ceph for GPUs: the GPU becomes a network resource a cluster-wide scheduler can pool and pack.<p>The hard part is making that fast. We&#x27;re within ~10% of native on most AI workloads, and it lets us serve ~1.8x more users on the same fleet. We run it in production as our own GPU cloud and sell it to enterprises with underutilized fleets.<p>Team is from Citadel Securities, Aquatic, Old Mission, AWS, and Bain. Series A, $17.5M raised from Matrix and Y Combinator.<p>Open roles:<p>- Software Engineer, C++ Systems ($215K-$325K + meaningful equity). Low-level, latency-sensitive work on the virtualization layer. Quant dev &#x2F; HFT background preferred: <a href="https:&#x2F;&#x2F;jobs.ashbyhq.com&#x2F;thundercompute&#x2F;2efae53b-817c-43e7-9da3-72694813f608" rel="nofollow">https:&#x2F;&#x2F;jobs.ashbyhq.com&#x2F;thundercompute&#x2F;2efae53b-817c-43e7-9...</a><p>- Software Engineer, Infrastructure ($150K-$250K + meaningful equity). Go, Kubernetes, reliable systems at scale: <a href="https:&#x2F;&#x2F;jobs.ashbyhq.com&#x2F;thundercompute&#x2F;927a922b-c607-4b0e-a6f2-451571a537f4" rel="nofollow">https:&#x2F;&#x2F;jobs.ashbyhq.com&#x2F;thundercompute&#x2F;927a922b-c607-4b0e-a...</a><p>- Business Operations Lead ($150K-$225K + meaningful equity): <a href="https:&#x2F;&#x2F;jobs.ashbyhq.com&#x2F;thundercompute&#x2F;4f28e418-b77b-446e-a30e-6b5bed36c093" rel="nofollow">https:&#x2F;&#x2F;jobs.ashbyhq.com&#x2F;thundercompute&#x2F;4f28e418-b77b-446e-a...</a><p>If you&#x27;re cracked at building systems software and want to do something more meaningful than creating liquidity, reach out.<p>Email me at carl@thundercompute.com and mention HN. I read every email.
