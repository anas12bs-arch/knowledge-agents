---
title: "[schneier] More on the OpenAI Agent’s Attack on Hugging Face"
url: "https://www.schneier.com/blog/archives/2026/08/more-on-the-openai-agents-attack-on-hugging-face.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "schneier"]
date: "2026-08-03T18:05:03Z"
metadata:
  {}
---

# [schneier] More on the OpenAI Agent’s Attack on Hugging Face

> Source: security | Category: security | 2026-08-03T18:05:03Z

More on the OpenAI Agent’s Attack on Hugging Face

Hugging Face has  published  a detailed timeline of the attack. From the summary: 
  The agent was running an internal OpenAI cyber-capability evaluation based on the ExploitGym benchmark, which tasks an AI agent with finding and exploiting software vulnerabilities. OpenAI ran this on its own infrastructure, and the ExploitGym maintainers and their infrastructure had no involvement in the deployment or operation of that evaluation environment. As far as we were able to infer, across the course of being evaluated on this benchmark, the agent inferred that Hugging Face may host that benchmark&#8217;s models, datasets, and reference solutions. We believe the entire intrusion was, from the agent&#8217;s point of view, an attempt to cheat the evaluation: reach our production systems and steal the test solutions rather than solve the challenge on its own...
