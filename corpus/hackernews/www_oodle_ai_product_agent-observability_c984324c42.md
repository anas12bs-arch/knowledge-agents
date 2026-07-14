---
title: "Show HN: Oodle.ai – $10 per million agent traces"
url: "https://www.oodle.ai/product/agent-observability"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-14T16:51:18Z"
metadata:
  score: "17"
---

# Show HN: Oodle.ai – $10 per million agent traces

> Source: hackernews | Category: news | 2026-07-14T16:51:18Z

Score: 17 | Comments: 6

Hi HN, we&#x27;re Kiran and Vijay!<p>Over the past two years, we have built a columnar storage engine for observability: logs, metrics, and traces. Today, it&#x27;s exciting for us to show what we&#x27;ve built on top of that foundation: LLM Agent Observability.<p>Given how non-deterministic agents are, storing all traces without sampling was critical for us. But these traces tend to be in the MBs, sometimes GBs - we needed to store them inexpensively. We also needed the queries and analyses to be fast. To meet both these goals, we store them in S3 in our own parquet-like file format, and query them using AWS Lambda.<p>Since we process each span of every trace, instead of running LLM-based evals on each, we first analyze them using deterministic techniques. We detect tool failures, retries, loops, abnormal token usage, latency regressions, schema violations, sentiment, and other production signals. We&#x27;ve written more about the approach here: <a href="https:&#x2F;&#x2F;blog.oodle.ai&#x2F;you-cant-sample-your-way-to-reliable-agents&#x2F;" rel="nofollow">https:&#x2F;&#x2F;blog.oodle.ai&#x2F;you-cant-sample-your-way-to-reliable-a...</a><p>The combination of our own engine, no sampling, and deterministic processing before LLM-for-evals allows us to price at $10 per million traces, provide sub-second p99 query latency, and have healthy margins. Before building this, we used Langfuse for our own agent observability, which was 6x more expensive.<p>Still super early, and rough around some edges, we would love your questions and feedback!
