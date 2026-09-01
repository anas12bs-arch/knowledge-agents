---
title: "[martin-fowler] Fragments: September  1"
url: "https://martinfowler.com/fragments/2026-09-01.html"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "martin-fowler"]
date: "2026-09-01T21:24:13Z"
metadata:
  {}
---

# [martin-fowler] Fragments: September  1

> Source: engineering | Category: engineering | 2026-09-01T21:24:13Z

Fragments: September  1

Like many readers, I’m wary of AI generated prose. Simon Wilison has written an  LLM cliché highlighter  - paste in some text, or a URL, and it will flag various patterns common to LLMs. It references a  wikipedia page of signs of AI writing . That page points out that: 

 
   Humans are notoriously bad at distinguishing human and LLM-generated text. While research on humans’ abilities to detect AI-generated text is still limited, a 2025 study has shown that human ability to distinguish LLM text from human is no better than random chance. Another 2025 study on German theses has shown that humans managed a “recognition rate of 57% for AI texts and 64% for human-generated texts”.[ 
 

 Not just do I find myself repelled by prose with an LLM-voice, I also wonder how accurate my reaction is. I’m old enough to see all sorts of new tic-phrases appear, and in the past would just chalk it up to youngsters or airport business books. (Not to mention Americanisms, which I’ll get used to momentarily.) 

  ❄                ❄                ❄                ❄                ❄ 

 NVIDIA’s technical blog reports on an  Architecture for Long-Horizon Autonomous Agents . Their research group used a combination of Claude Opus 5 and a harness called AVO, and used it first to do GPU kernel optimization and then a broader reasoning benchmark (ARC-AGI-3). Both of these were long-term tasks, for the kernel optimization the agent ran for seven days. 

 
   AVO is designed to preserve progress beyond a single model context. Two mechanisms are particularly important: persistent memory and supervision. 

   Persistent memory carries forward prior implementations, evaluation results, compiler and profiler outputs, and accumulated reasoning, allowing the agent to resume from the current state rather than repeatedly reconstructing the search. 

   The supervisor monitors the broader trajectory for stagnation or repeated unproductive cycles and can redirect the main agent toward alternative strate
