---
title: "Porting Gemma-4 12B (the encoder-free multimodal one) to AWS Inferentia2"
url: "https://dev.to/xbill/porting-gemma-4-12b-the-encoder-free-multimodal-one-to-aws-inferentia2-5f19"
source: "devto"
category: "news"
tags: ["devto", "python", "tech-article"]
date: "2026-07-17T14:17:17Z"
metadata:
  tag: "python"
---

# Porting Gemma-4 12B (the encoder-free multimodal one) to AWS Inferentia2

> Source: devto | Category: news | 2026-07-17T14:17:17Z

The 12B ships as a multimodal class with no encoder loaded, and its sliding-window attention overflows Neuron's fused-attention SBUF. Three surgical fixes and it serves Paris at ~15 tok/s on one inf2.8xlarge.

Reactions: 1
