---
title: "[schneier] Hiding Capabilities in AI Models"
url: "https://www.schneier.com/blog/archives/2026/10/hiding-capabilities-in-ai-models.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "schneier"]
date: "2026-10-27T12:45:58Z"
metadata:
  {}
---

# [schneier] Hiding Capabilities in AI Models

> Source: security | Category: security | 2026-10-27T12:45:58Z

Hiding Capabilities in AI Models

Interesting research: &#8220; AI Models Can Provably Hide Arbitrary Capabilities &#8221; 
   Abstract:  Capability evaluations aim to surface dangerous model behaviors before deployment, but their reliability depends on the assumption that hidden capabilities can be elicited. We show this assumption does not hold under adversarial conditions by constructing backdoor attacks that embed encrypted neural networks within host model weights, decrypting and executing them only upon receiving a secret trigger. Using digital lockers, these hidden circuits remain provably hard to elicit and interpret under cryptographic assumptions, even given full access to model weights, extending prior work from hiding fixed strings to arbitrary computations. We implement our proof of concept constructions in PyTorch and evaluate elicitation through fine-tuning, weight noising, gradient-based trigger search, and latent adversarial training, using a small chemical reaction prediction task as a proxy for CBRN-relevant capabilities. Our results demonstrate resistance to these methods and, together with our cryptographic guarantees, reveal a limit of elicitation-based capability audits. We release our models to support the improvement of defenses...
