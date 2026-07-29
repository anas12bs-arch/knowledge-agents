---
title: "Launch HN: Tokenless (YC S26) – Automatic model switching to save money"
url: "https://usetokenless.com/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-29T16:47:41Z"
metadata:
  score: "15"
---

# Launch HN: Tokenless (YC S26) – Automatic model switching to save money

> Source: hackernews | Category: news | 2026-07-29T16:47:41Z

Score: 15 | Comments: 15

Hi HN, Rohit here from Tokenless (<a href="https:&#x2F;&#x2F;usetokenless.com&#x2F;" rel="nofollow">https:&#x2F;&#x2F;usetokenless.com&#x2F;</a>), which I’m building alongside co-founders Andrew and Kev. We’re building an API gateway which routes agent traffic dynamically turn-by-turn between different models to save on AI spend.<p>The cost of AI tokens is top-of-mind for many. Companies like Uber and Salesforce have been complaining about blowing their yearly AI spend faster than expected.<p>Frontier models are amazing for dev work, but are so expensive. Open-source models are cheap and rapidly improving, closing the gap with frontier models, but aren’t quite there yet.<p>Tokenless gets you the best of both worlds–routing harder turns to smarter models only when needed, which keeps costs low.<p>Before Tokenless, I was doing a PhD at Princeton. While using coding&#x2F;other agents, I constantly agonized over model choice, to make sure my AI spend was going as far as possible on my academic Cursor account.<p>At the same time, I was doing LLM research, and a small technique I developed while in recovery from NeurIPS submission season seemed to hit SOTA pretty fast. I was surprised that such simple ideas could do routing well.<p>We’ve been able to develop a version of the router that matches the performance of Claude Fable 5 at half the cost. The blog post on our website explores the technical details on how we did this (<a href="https:&#x2F;&#x2F;usetokenless.com&#x2F;blog&#x2F;building-tokenless&#x2F;" rel="nofollow">https:&#x2F;&#x2F;usetokenless.com&#x2F;blog&#x2F;building-tokenless&#x2F;</a>).<p>Highlights:
- Our approach queries multiple models at once and uses their progress to make decisions (this technique is novel AFAIK, let us know if you know anyone else doing this).
- Switching models doesn’t destroy the cache if the routing algorithm is aware of when the cache is hot&#x2F;cold.<p>To come:
- Adding Kimi K3, all other GPT efforts and more to the router<p>Go ahead and sign up on usetokenless.com and try using Tokenless with your agent, you’ll get $20 of free credit. Here’s a demo on how to use it: <a href="https:&#x2F;&#x2F;youtu.be&#x2F;sjZWriclcls" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;sjZWriclcls</a><p>Tokenless provides frontier-level intelligence for cheaper, so we’d love some feedback on how it feels to use, any corner cases that the router routes incorrectly, and whether you find the routing problem interesting!
