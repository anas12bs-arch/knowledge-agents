---
title: "Math.random() Is Not Secure. I Found It Generating API Keys in a 44K-Star Repo."
url: "https://dev.to/ofri-peretz/mathrandom-is-not-random-enough-i-found-it-building-api-keys-in-a-57k-star-repo-2pl1"
source: "devto"
category: "news"
tags: ["devto", "javascript", "tech-article"]
date: "2026-05-30T23:38:34Z"
metadata:
  tag: "javascript"
---

# Math.random() Is Not Secure. I Found It Generating API Keys in a 44K-Star Repo.

> Source: devto | Category: news | 2026-05-30T23:38:34Z

Math.random() is a PRNG, not a CSPRNG — its outputs are predictable once an attacker recovers the internal state. I found this pattern in a 44K-star open-source codebase generating integration API keys. Here is the attack class, the ESLint rule that catches it, and the one-line fix.

Reactions: 3
