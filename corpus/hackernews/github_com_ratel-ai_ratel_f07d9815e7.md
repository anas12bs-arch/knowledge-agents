---
title: "Show HN: Ratel, give agents unlimited tools and skills without context bloat"
url: "https://github.com/ratel-ai/ratel"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-16T17:57:45Z"
metadata:
  score: "16"
---

# Show HN: Ratel, give agents unlimited tools and skills without context bloat

> Source: hackernews | Category: news | 2026-07-16T17:57:45Z

Score: 16 | Comments: 14

Hi HN! We&#x27;re Giacomo and Roberto, authors of Ratel (<a href="https:&#x2F;&#x2F;github.com&#x2F;ratel-ai&#x2F;ratel" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;ratel-ai&#x2F;ratel</a>)<p>We used to help SaaS companies build agents on top of their products. Whenever we wanted to expand the agents’ complexity&#x2F;scope, by adding more and more tools and instructions, we always run in the same issue: context bloat, with frequent hallucinations and sky high token bills. So we started constantly engineering the agents, dynamically loading tools, splitting them into subagents, inventing our own way to support skills<p>And that&#x27;s exactly when we started building Ratel: a library to let your agent keep its full catalog of tools and skills, but progressively disclosing only the few that actually matter for each turn. Now you can grow your agent&#x27;s capabilities without breaking it or taking out a loan for it<p>People are already using it in production, with a user cutting their token cost up to 81% in the first month without compromising the accuracy<p>We support both keyword and semantic retrieval, all in-process and without any additional infra. Open source, framework-agnostic, exposes OpenTelemetry metrics, available for Typescript and Python<p>Benchmarks: <a href="https:&#x2F;&#x2F;benchmark.ratel.sh" rel="nofollow">https:&#x2F;&#x2F;benchmark.ratel.sh</a><p>Some cool things we did with this:<p>•    One team&#x27;s agent had up to 300+ tools dynamically loaded into context. Ratel cut their token cost 81% in month one.
•    Another team split into several subagents instead, one agent per task. It worked, until the swarm got slow and expensive. We fixed this with our skills.<p>We&#x27;re both here all day. Tear it apart, especially if you&#x27;re an AI or SWE running agents in production
