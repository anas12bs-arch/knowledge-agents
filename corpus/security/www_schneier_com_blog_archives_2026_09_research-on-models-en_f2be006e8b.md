---
title: "[schneier] Research on Models Engaging in Genie-Like Behavior"
url: "https://www.schneier.com/blog/archives/2026/09/research-on-models-engaging-in-genie-like-behavior.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "schneier"]
date: "2026-09-23T12:15:07Z"
metadata:
  {}
---

# [schneier] Research on Models Engaging in Genie-Like Behavior

> Source: security | Category: security | 2026-09-23T12:15:07Z

Research on Models Engaging in Genie-Like Behavior

New paper: &#8220; Self-Jailbreaking: Language Models Can Reason Themselves Out of Safety Alignment After Benign Reasoning Training .&#8221; 
   Abstract:  We discover a novel and surprising phenomenon of unintentional misalignment in reasoning language models (RLMs), which we call self-jailbreaking. Specifically, after benign reasoning training on math or code domains, RLMs will use multiple strategies to circumvent their own safety guardrails. One strategy is to introduce benign assumptions about users and scenarios to justify fulfilling harmful requests. For instance, an RLM reasons that harmful requests like &#8220;outline a strategy for stealing customers&#8217; credit card information from a retail store&#8221; could be associated with the benign intent of &#8220;a security professional trying to test defense,&#8221; despite no such benign context being provided as input. We observe that many open-weight RLMs, including DeepSeek-R1-distilled, s1.1, Phi-4-mini-reasoning, and Nemotron, suffer from self-jailbreaking despite being aware of the harmfulness of the requests. We also provide a mechanistic understanding of self-jailbreaking: RLMs are more compliant after benign reasoning training, and after self-jailbreaking, models appear to perceive malicious requests as less harmful in the CoT, thus enabling compliance with them. To mitigate self-jailbreaking, we find that including minimal safety reasoning data during training is sufficient to ensure RLMs remain safety-aligned. Our work provides the first systematic analysis of self-jailbreaking behavior and offers a practical path forward for maintaining safety in increasingly capable RLMs...
