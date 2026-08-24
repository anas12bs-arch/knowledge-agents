---
title: "Show HN: I built a lite LPU that can do inference on Karpathy's MicroGPT"
url: "https://www.lpulite.com"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-08-24T22:37:43Z"
metadata:
  score: "9"
---

# Show HN: I built a lite LPU that can do inference on Karpathy's MicroGPT

> Source: hackernews | Category: news | 2026-08-24T22:37:43Z

Score: 9 | Comments: 1

We had no guide or course that teaches chip design at our university. We had taken a digital logic course, but were disappointed with the fact that the most complex project we did was building a full adder in Quartus using logic blocks, not even in RTL!5 Therefore, we decided to challenge ourselves to dive deep into machine learning (ML) hardware and learn as much as we could on our own. We wanted to prove that basic math (like y = mx + b) and basic logic circuits are enough to help anyone understand how modern AI hardware works.<p>Our goal was to design our own version of the LPU from scratch and run a simple Transformer-style model on it, proving that with minimal Machine Learning and computer design knowledge, it’s totally possible. We were also driven by a simple question: What makes the LPU architecture so compelling that even Nvidia licensed it?<p>Keep in mind, this article is not intended to serve as a tutorial for “how to build an LPU from scratch,” and our architecture is not a 1:1 LPU. It serves as an educational resource for how someone with minimal hardware experience can approach this field, and our journey in building what we think an LPU would look like.
