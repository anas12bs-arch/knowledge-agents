---
title: "My credential rule reported 842 secrets in vercel/ai. The real count was 0."
url: "https://dev.to/ofri-peretz/my-credential-rule-reported-842-secrets-in-vercelai-the-real-count-was-0-249p"
source: "devto"
category: "news"
tags: ["devto", "ai", "tech-article"]
date: "2026-07-04T16:11:25Z"
metadata:
  tag: "ai"
---

# My credential rule reported 842 secrets in vercel/ai. The real count was 0.

> Source: devto | Category: news | 2026-07-04T16:11:25Z

Our no-hardcoded-credentials rule fired 842 times on vercel/ai. The peer plugin fired 380. I assumed we had better recall — until I sampled. 807 of the 'extra' findings were TypeScript union-type literals, error class names, and the string 'test'. The real number of hardcoded credentials was zero. Here's how a context-blind regex becomes a context-aware detector — and why AI assistants keep regenerating the exact strings that fool it.

Reactions: 2
