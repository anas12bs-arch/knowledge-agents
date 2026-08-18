---
title: "[schneier] LLMs and Contextual Integrity"
url: "https://www.schneier.com/blog/archives/2026/08/llms-and-contextual-integrity.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "schneier"]
date: "2026-08-18T10:46:41Z"
metadata:
  {}
---

# [schneier] LLMs and Contextual Integrity

> Source: security | Category: security | 2026-08-18T10:46:41Z

LLMs and Contextual Integrity

I have been thinking a lot about AI and integrity. Part of that is contextual integrity. I recently found two papers on the topic. 
 &#8220; CIMemories: A Compositional Benchmark for Contextual Integrity of Persistent Memory in LLMs &#8220;: 
   Abstract:  Large Language Models (LLMs) increasingly use persistent memory from past interactions to enhance personalization and task performance. However, this memory introduces critical risks when sensitive information is revealed in inappropriate contexts. We present CIMemories, a benchmark for evaluating whether LLMs appropriately control information flow from memory based on task context. CIMemories uses synthetic user profiles with over 100 attributes per user, paired with diverse task contexts in which each attribute may be essential for some tasks but inappropriate for others. Our evaluation reveals that frontier models exhibit up to 69% attribute-level violations (leaking information inappropriately), with lower violation rates often coming at the cost of task utility. Violations accumulate across both tasks and runs: as usage increases from 1 to 40 tasks, GPT-5&#8217;s violations rise from 0.1% to 9.6%, reaching 25.1% when the same prompt is executed 5 times, revealing arbitrary and unstable behavior in which models leak different attributes for identical prompts. Privacy-conscious prompting does not solve this&#8212;models overgeneralize, sharing everything or nothing rather than making nuanced, context-dependent decisions. These findings reveal fundamental limitations that require contextually aware reasoning capabilities, not just better prompting or scaling...
