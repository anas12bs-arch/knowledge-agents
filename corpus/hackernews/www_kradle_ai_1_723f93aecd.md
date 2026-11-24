---
title: "Show HN: KradleBench – Multi-agent AI evals in Minecraft"
url: "https://www.kradle.ai?1"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-11-24T23:49:49Z"
metadata:
  score: "14"
---

# Show HN: KradleBench – Multi-agent AI evals in Minecraft

> Source: hackernews | Category: news | 2026-11-24T23:49:49Z

Score: 14 | Comments: 4

Hi HN -<p>This is James and Kemal. In past lives we led Firebase and Tensorflow&#x2F;JAX respectively. HN has been a particularly big part of my (James’) career and the trajectory I’ve taken would be meaningfully different without it. Thank you!<p>Our team shipped a benchmark: KradleBench. We test AI in Minecraft Worlds.<p>1. The worlds are multi-agent. Humans and other AIs are in there too, often pursuing their own goals. Collaboration and conflict skills fall out of this property.<p>2. The world are dynamic. They constantly change, which means that agents need to react. “Capture the Flag” has a single winning condition, and many different ways to achieve it. This leads to many emergent and creative strategies.<p>3. The worlds are real-time. They are not turn-based, they do not wait for AIs to finish thinking. Nature balanced speed and intelligence in humans, we can understand this in AIs too.<p>Underneath all this is Kradle, a platform to test and understand intelligence. It’s a petri dish where any intelligence type (LLM, World Model, Human) can be compared and generate useful information to improve current systems, whether it’s on capabilities or safety.<p>Some findings so far:
- A skilled human was #1, until yesterday when Astra 6.2 surpassed them. We lose badly on solo tasks and out-compete on multi-agent ones
- Astra 6.2 iterates on its strategy 4x faster than Fable 5.2. The Claude family tends to think hard and stick with strategies. The OpenAI models tend to be more reactive and iterative, which serves them well in multi-agent, dynamic, real-time evals.<p>We’ve got videos on all the top model’s page, and we’ll be producing them when a new model launches. Sign up on the site to get them and for when the platform opens.<p>Thanks for reading,<p>James &amp; Kemal
