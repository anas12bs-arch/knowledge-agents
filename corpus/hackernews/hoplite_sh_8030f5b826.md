---
title: "Launch HN: Hoplite (YC S26) – Effortlessly deploy cloud coding agents"
url: "https://hoplite.sh"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-08-03T18:05:03Z"
metadata:
  score: "18"
---

# Launch HN: Hoplite (YC S26) – Effortlessly deploy cloud coding agents

> Source: hackernews | Category: news | 2026-08-03T18:05:03Z

Score: 18 | Comments: 17

Hi HN, we’re Bence and Ryan, founders of Hoplite (<a href="https:&#x2F;&#x2F;hoplite.sh">https:&#x2F;&#x2F;hoplite.sh</a>). Hoplite lets you deploy coding agents in the cloud, with a suite of tools that makes it incredibly easy to QA features. During onboarding, we port over your local setup - sessions, memories, MCP servers, and get your projects ready to run in the cloud.<p>Here’s a demo: <a href="https:&#x2F;&#x2F;youtu.be&#x2F;bnyktZ_9pjE" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;bnyktZ_9pjE</a><p>We got here after pivoting away from the idea we applied to YC with; AI for retail investing. It ultimately wasn’t a product that we ourselves would use, nor served a customer base that we felt connected to. In reflecting on what we really wanted to do, we realised that we loved talking to founders and developers, and were really opinionated about the specific area of cloud agents. We tried out all the existing solutions, and didn’t find one that A) took good advantage of being in the cloud, and B) was performant and felt good to use.<p>We’re building a product that we feel reflects what mainstream development will look like in 6-12 months. As models improve, developers will end up reviewing less and less code, and will instead focus on reviewing the product output. That means evaluating new user flows, visually verifying that new features look good, that the API works as expected, that the CLI works on Windows, etc. And doing it while running hundreds of agents concurrently.<p>On the agent side, we’ve created a custom harness. We spent a lot of time deciding on whether we should use an off the shelf solution like Codex&#x2F;Claude Code, but ultimately wanted the independence and freedom that came with building it in house. It also means that we can test out completely new features without relying on Anthropic and OpenAI to catch up.<p>Everything is hosted on AWS, with the exception of: Temporal for durable workflows, Modal for sandboxes, and Planetscale for our database. Our infra decisions were driven by a strong belief that agents are becoming a tier 0 piece of infrastructure, and they need the reliability and security to match that.<p>You can try it now for free with the code ‘HACKERNEWS’ - we’ve included $100 in free credits, plus you can connect your Codex subscription and use OpenAI models via it. You can see some more details around our pricing at <a href="https:&#x2F;&#x2F;hoplite.sh&#x2F;pricing">https:&#x2F;&#x2F;hoplite.sh&#x2F;pricing</a>.<p>At the moment we’re focusing on optimising two key experiences: onboarding and previews, and would love to hear your feedback on them. And if you find that the agent&#x27;s performance in certain tasks doesn’t match your expectations, please let us know!
