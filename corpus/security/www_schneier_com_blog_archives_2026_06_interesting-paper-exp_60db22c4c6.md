---
title: "[schneier] Interesting Paper Exploring Prompt Injection"
url: "https://www.schneier.com/blog/archives/2026/06/interesting-paper-exploring-prompt-injection.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "schneier"]
date: "2026-06-25T13:29:04Z"
metadata:
  {}
---

# [schneier] Interesting Paper Exploring Prompt Injection

> Source: security | Category: security | 2026-06-25T13:29:04Z

Interesting Paper Exploring Prompt Injection

This  is a fascinating explotation of how LLMs fall for prompt injection attacks. It turns out that they learn to recognize the style of text in different role/instruction blocks, and not just the tags. 
 Their conclusion: 
  Role tags were a formatting trick that became the security architecture and the cognitive scaffolding of modern LLMs. We&#8217;ve shown that this architecture doesn&#8217;t survive into the model&#8217;s actual representations, and that such role confusion is linked to prompt injection. 
 Unless LLMs achieve genuine role perception, we think injection defense will remain a perpetual whack-a-mole game. And the continuous nature of role boundaries opens the threat of injections designed to subtly shift LLM states through seemingly innocuous text, legally and at scale...
