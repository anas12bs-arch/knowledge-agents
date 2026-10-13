---
title: "Show HN: Parsimony – an open-source benchmark for how much code AI models add"
url: "https://parsimony.lasu.dev/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-10-13T22:00:12Z"
metadata:
  score: "14"
---

# Show HN: Parsimony – an open-source benchmark for how much code AI models add

> Source: hackernews | Category: news | 2026-10-13T22:00:12Z

Score: 14 | Comments: 1

Existing benchmarks measure solve rate and token output&#x2F;cost, but don&#x27;t punish excess code, which makes a codebase harder to work with in the long term. I wanted to measure this since it matters most for long-term projects.<p>Method: it takes the patches that benchmarks already publish (DeepSWE, SWE-bench Verified, SWE-bench Live) and counts &quot;coding units&quot;: syntax elements like statements, calls, names and literals. I didn&#x27;t use lines of code, so cramming code isn&#x27;t rewarded. Deleted code is subtracted, so it measures net units.<p>GPT-6 and Claude 5.5 have no public patches yet, so I ran them myself on 3–10 tasks on my own subscriptions (shown as faded circles, not ranked).<p>Any feedback or model contributions are welcome, especially public patch exports for newer models.<p>GitHub: <a href="https:&#x2F;&#x2F;github.com&#x2F;La5u&#x2F;Parsimony" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;La5u&#x2F;Parsimony</a><p>Not affiliated with any of the benchmarks.
