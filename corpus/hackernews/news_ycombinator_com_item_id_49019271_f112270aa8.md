---
title: "Show HN: Running PrismML's Bonsai inside DRAM by breaking DDR4 timing rules"
url: "https://news.ycombinator.com/item?id=49019271"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-27T17:54:33Z"
metadata:
  score: "8"
---

# Show HN: Running PrismML's Bonsai inside DRAM by breaking DDR4 timing rules

> Source: hackernews | Category: news | 2026-07-27T17:54:33Z

Score: 8 | Comments: 3

The excitement surrounding PrismML’s 1-bit&#x2F;ternary Bonsai models has the industry closely watching how smartphone giants, particularly Apple, will implement LLMs on edge devices.<p>Moving AI on-device is a brilliant and necessary strategy. It ensures absolute user privacy in alignment with EU regulations, fundamentally shifts the economics away from costly cloud inference, and paves the way for a significant hardware upgrade supercycle as users seek true AI-capable silicon.<p>To create a smart on-device &quot;Semantic Router,&quot; models need to reach the 27B+ parameter scale. Achieving this on a phone requires extreme quantization, such as PrismML’s ternary weights.<p>However, a critical hardware reality often overlooked by the software world is that fitting the weights in RAM is not equivalent to moving them. Running a 27B ternary model on standard LPDDR encounters a significant memory bandwidth limitation. Transferring gigabytes of data across the SoC bus for each token generation can lead to thermal throttling of the NPU and excessive battery drain.<p>This raises an important question: why are we still transferring data to the compute? Why not execute AI inference natively within the memory?<p>Frustrated with academic PIM simulations that overlook bare-metal physics, I developed CaSA, an architecture that performs ternary LLM inference directly inside COTS DRAM through charge-sharing, completely bypassing the memory bus.<p>Software quantization is a great initial step, and CaSA provides the physical hardware substrate needed to complete the bridge: <a href="https:&#x2F;&#x2F;github.com&#x2F;pcdeni&#x2F;CaSA" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;pcdeni&#x2F;CaSA</a>
