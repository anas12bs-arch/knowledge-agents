---
title: "[infoq] OpenAI Details GPT-Live’s Architecture for Continuous Stateful Voice Interaction"
url: "https://www.infoq.com/news/2026/09/openai-gpt-live/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-09-02T13:57:22Z"
metadata:
  {}
---

# [infoq] OpenAI Details GPT-Live’s Architecture for Continuous Stateful Voice Interaction

> Source: engineering | Category: engineering | 2026-09-02T13:57:22Z

OpenAI Details GPT-Live’s Architecture for Continuous Stateful Voice Interaction

OpenAI recently published an engineering account of GPT-Live. It described how they designed the system to maintain continuous voice interaction while separating latency-sensitive media processing from broader application work. The live path contains the media pipeline and inference loop, while delegation, tool use, persistence, and other application logic run behind an asynchronous RPC boundary.   By Eran Stiller
