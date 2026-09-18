---
title: "Show HN: Ax-check.com – Can agents use your product?"
url: "https://www.ax-check.com/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-09-18T20:56:01Z"
metadata:
  score: "23"
---

# Show HN: Ax-check.com – Can agents use your product?

> Source: hackernews | Category: news | 2026-09-18T20:56:01Z

Score: 23 | Comments: 22

I&#x27;m the co-founder of Gauge, and I built ax-check.com to quickly test how well coding agents can onboard to your product.<p>You&#x27;ll get a scorecard, specific suggested fixes, and three full coding sessions that show how agents read your site and use your product.<p>I built this because similar checks were too noisy. Most suggested obscure technical changes that don&#x27;t actually make a difference in agent experience (or AX, hence ax-check.com).<p>This check starts by using DeepSeek 4.1 Flash to try to find key information about your product, starting from the homepage. In actual agent traffic data, we&#x27;ve seen that the key pages are the homepage, llms.txt, pricing, and the docs site (by traffic volume, and by influence), so we focus on those and ignore the rest. We also find that content negotiation for Markdown is legitimately helpful for agents to complete tasks faster and find what they&#x27;re looking for, so the scan tests that your key pages can serve Markdown.<p>The other key piece is that we run actual coding agents in sandboxes, and have them try to onboard to your product. You can see the full trace and watch it happen live (we kick it off fresh when you enter a new site). We surface interesting findings like hallucinated URLs, inaccurate docs instructions, or product confusion.<p>It also detects whether the agents could complete a fully working onboarding autonomously, without being blocked by a login wall. This is still controversial, but I think finding ways to let agents safely onboard autonomously is going to be table stakes within a year for developer tools in particular.<p>The whole site is agent-friendly itself! You can generally just talk to your coding agent about ax-check.com and it can do the rest. Would really appreciate any feedback to make this useful.
