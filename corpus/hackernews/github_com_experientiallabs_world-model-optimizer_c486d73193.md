---
title: "Show HN: Optimize and serve models with Fable quality at half the cost"
url: "https://github.com/experientiallabs/world-model-optimizer"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-30T20:17:13Z"
metadata:
  score: "51"
---

# Show HN: Optimize and serve models with Fable quality at half the cost

> Source: hackernews | Category: news | 2026-07-30T20:17:13Z

Score: 51 | Comments: 23

Hi HN, we built world-model-optimizer, an open source tool to continually improve a specialized model for an agent.<p>It does this by simulating production tool responses through text world modeling (similar to QwenAgentWorld, summary here <a href="https:&#x2F;&#x2F;x.com&#x2F;silennai&#x2F;status&#x2F;2073887455884058814" rel="nofollow">https:&#x2F;&#x2F;x.com&#x2F;silennai&#x2F;status&#x2F;2073887455884058814</a>).<p>We can then use this to train a router for frontier, OS, and local models (use defaults or pick which ones to optimize against).<p>wmo ingests agent traces, builds the simulation, embeds the traces, runs different models you choose against the simulation scenarios, and then uses a KNN for model selection (similar to <a href="https:&#x2F;&#x2F;arxiv.org&#x2F;abs&#x2F;2505.19797" rel="nofollow">https:&#x2F;&#x2F;arxiv.org&#x2F;abs&#x2F;2505.19797</a>).<p>- Cache aware: cache is taken into account for the effective price in routing.<p>- Confidence gated: we don&#x27;t deviate from the best fit model when paired evidence over retrieved neighbors is below 0.5 standard errors or on queries unlike anything in the fit set.<p>- Optimize for cost or quality: train a balanced, cost max, or quality max router.<p>Usage<p>`wmo build` creates the simulation (or add your own benchmark)<p>`wmo optimize` tunes the router<p>`wmo serve` starts the server and can run everything fully locally. The simulation and router can update over time as more agent traces are gathered and new models are added.<p>Router results vs Fable<p>- RouterBench: -66.5% cost, -1.7% performance, -24.7% latency p50. 77.5% of traffic to Sonnet 5, 16.1% Fable 5.<p>- TauBench: -44.5% cost, +6.3% performance, -20% latency. 83% to Opus 5, 17% to Kimi-K2.6 (over K3).<p>- Terminal Bench 2: -64% cost, +8% performance, -50.6% latency. Sonnet 5 is fully along the pareto front. Training a specialized router per task isn&#x27;t cheap. In sparse data regimes the value can be &quot;here&#x27;s the best model&quot;.<p>We&#x27;re working on sample effiient continual learning for agent specific models at experientiallabs.ai&quot;
