---
title: "[infoq] AlloyDB Ships Proxy Models That Replace LLM Calls with Local Inference Inside the Database"
url: "https://www.infoq.com/news/2026/07/alloydb-ai-proxy-models/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-07-09T08:43:19Z"
metadata:
  {}
---

# [infoq] AlloyDB Ships Proxy Models That Replace LLM Calls with Local Inference Inside the Database

> Source: engineering | Category: engineering | 2026-07-09T08:43:19Z

AlloyDB Ships Proxy Models That Replace LLM Calls with Local Inference Inside the Database

Google shipped AlloyDB AI functions GA with a proxy model architecture that trains a lightweight local model from LLM outputs, then runs queries at database speed without external calls. Smart batching delivers 2,400x throughput improvement. The proxy model reaches 100,000 rows per second in preview, but benchmark numbers apply only to ai.if in internal testing.   By Steef-Jan Wiggers
