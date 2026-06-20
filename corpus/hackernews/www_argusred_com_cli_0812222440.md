---
title: "Show HN: We post-trained a model that pen tests instead of refusing"
url: "https://www.argusred.com/cli"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-06-20T20:51:13Z"
metadata:
  score: "49"
---

# Show HN: We post-trained a model that pen tests instead of refusing

> Source: hackernews | Category: news | 2026-06-20T20:51:13Z

Score: 49 | Comments: 20

Anthropic and OpenAI&#x27;s publicly available models are explicitly guard-railed so that they refuse offensive tasks. And their cyber-focussed models are gated for enterprises. This leaves SMEs and mid market open to major vulnerabilities.<p>AI can be used as both an adversarial and defensive tool in the world of cyber. A worst case outcome is if only the adversaries have access.<p>Meanwhile, most existing AI cyber tools are just wrappers. The problem is that they still have all the guardrails on from the foundation model where they will inherit its refusals.<p>For this project we&#x27;ve post-trained a specific model on a decade of capture-the-flag contests. This won&#x27;t be made available to anyone and everyone, but we do believe that responsible SMEs and midmarket companies also need access to these tools in order to identify key vulnerabilities in their systems; not just enterprises.<p>We have developed two modes that run over a CLI:<p>• Security scan: a read-only audit of your local codebase for vulnerabilities. It only reports what it can tie to a specific file and line, so you&#x27;re not wading through vibes-based findings.<p>• Pen test: an active adversarial mode that will try to break a live system in a sandboxed environment. It proves each vulnerability by running the exploit and showing the request it sent and the response your code gave back, not a confidence score. Currently gated.<p>To show what the scan does, we pointed it at Bank of Anthos and it found an integer overflow in the transfer path: amount is an int, and amount + fee can overflow negative, so the balance check passes and you move funds you don&#x27;t have. Plus the usual auth and secrets issues. (Bank of Anthos is Google&#x27;s open-source bank. It&#x27;s a known app and some of it is intentionally weak, which is the point: you can clone it and re-run the scan yourself instead of trusting a screenshot)<p>The base model is a Kimi K2.6 (open weights). We didn&#x27;t pretrain from scratch. We post-trained it ourselves, SFT on CTF writeups, then RL with verifiable rewards against actual exploit checks.<p>How the harness works:<p>Along with the model we built the harness to support this. The harness runs on a multi-agent swarm: an orchestrator splits the job across subagents running in parallel, each owning a slice, then synthesising one report.<p>The CLI is a local binary (brew&#x2F;curl). It reads your code locally, then sends context to our inference API over TLS tcpdump it and you&#x27;ll see exactly what leaves and where. Install is free; and you can run a scan for free up to 2m tokens, then need to pay for tokens beyond this.<p>For full disclosure this is a product part of Cosine (YC W23)<p>Up for debate: tool safety, e.g. domain verification is one method that proves control but not necessarily permission. How would you gate a pen-test tool given that?
