---
title: "Show HN: Recurse – Develop and deploy specialist agents faster"
url: "https://recurse.run"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-09-26T00:44:51Z"
metadata:
  score: "4"
---

# Show HN: Recurse – Develop and deploy specialist agents faster

> Source: hackernews | Category: news | 2026-09-26T00:44:51Z

Score: 4 | Comments: 0

Hi HN! We are looking to gather some feedback on our serverless agent harness. The admittedly not-so-specific use case is to accelerate agent development and deployment. After building several custom&#x2F;special-purpose agents for a few customers, we built this to accelerate our workflow at first, and now we are trying to understand whether it could be useful to others.<p>Our driver use case was development of specialist agents with a request&#x2F;response lifecycle. Think of agents that have a well established input&#x2F;output contract where they are expected to produce high-quality output (artifacts, responses etc.). Especially when the problem is in some verifiable domain and the LLM can iteratively refine a result to a final value that satisfies constraints or optimizes some goal.<p>The product is a coding agent skill + a serverless execution runtime with a harness that takes in a system prompt + Python functions as tools. The coding agent takes in the requirements from the user, and tries agent variants by executing prompt&#x2F;tool variants it creates.<p>It works best for cases where you can think of how you can evaluate a candidate agent - when you describe this information to your coding agent, it often does a decent job at building candidate prompts, tools and even benchmarks.<p>Prompts and Python tools that the coding agent creates integrate with a harness that implements an FSM that is tuned to drive an iterative refinement process for verifiable domains. This tuning enables one to use small models like Luna to produce high quality results while keeping costs at a manageable level.<p>Our website is not 100% complete yet (some examples are missing write-ups, not all use cases we tried are there etc.), but the system is operational and docs are there.<p>Thanks!
