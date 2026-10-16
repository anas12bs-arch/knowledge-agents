---
title: "[schneier] Backdooring Open-Weight AI Models"
url: "https://www.schneier.com/blog/archives/2026/10/backdooring-open-weight-ai-models.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "schneier"]
date: "2026-10-16T11:40:33Z"
metadata:
  {}
---

# [schneier] Backdooring Open-Weight AI Models

> Source: security | Category: security | 2026-10-16T11:40:33Z

Backdooring Open-Weight AI Models

This  is a problem: 
  Any open model whose weights have been edited can carry a backdoor, whether it&#8217;s a task-specific fine-tune, a merged adapter or an abliterated build. We have abliterated models in the title because it&#8217;s the most popular reason people download modified weights without verifying what&#8217;s inside. Abliteration is a cheap fine-tune that takes away a model&#8217;s ability to refuse. You find the direction in the weights that carries &#8220;no&#8221; and subtract it. The model then answers things a safety-tuned version would turn down. It began as a research trick and it&#8217;s now routine before people upload a model to Hugging Face, where you&#8217;ll find abliterated builds of most of the popular open weights: Qwen, Llama, even OpenAI&#8217;s gpt-oss...
