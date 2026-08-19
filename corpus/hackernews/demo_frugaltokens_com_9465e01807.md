---
title: "Show HN: Frugal Tokens – explore costs and usage across coding agents"
url: "https://demo.frugaltokens.com/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-08-19T17:37:28Z"
metadata:
  score: "9"
---

# Show HN: Frugal Tokens – explore costs and usage across coding agents

> Source: hackernews | Category: news | 2026-08-19T17:37:28Z

Score: 9 | Comments: 1

I wanted to share a project I’ve been working on called Frugal Tokens. I originally built it because I was curious to see how much all of my sessions cost and how much cache misses affected that spend. I’d noticed people had widely different spend profiles and wanted to better understand what might contribute to that.<p>As I’ve worked on this, the tool has grown to show more usage patterns across all of your sessions. It shows overall usage, estimated working time and overlapping sessions, and where your spend is coming from across models and cache misses. I also have a few session level metrics with percentile breakdowns, along with a list of your sessions and high level info.<p>Clicking into a session opens an explorer where you can see individual model calls and tool inputs and outputs. You can also jump directly to where a cache miss happened. There’s also a rough cost comparison that shows what the recorded session would have cost with another model’s pricing, or for Anthropic, with 5m vs 1h caching.<p>In the future, I’d love to collect more information to see which patterns might make people’s workflows more expensive, e.g. long sessions, high context usage, many turns, etc.<p>The tool requires deno, but is just one command to run once that is installed. The demo provided has some of the data scrubbed, but helps to show what it looks like before running it.<p>Would appreciate any thoughts or ideas<p><a href="https:&#x2F;&#x2F;github.com&#x2F;dpclark4&#x2F;frugal-tokens" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;dpclark4&#x2F;frugal-tokens</a>
