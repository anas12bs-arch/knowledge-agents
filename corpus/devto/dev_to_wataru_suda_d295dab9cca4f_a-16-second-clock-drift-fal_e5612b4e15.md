---
title: "A 16-second clock drift falsely tripped my trading bot's kill switch. A postmortem."
url: "https://dev.to/wataru_suda_d295dab9cca4f/a-16-second-clock-drift-falsely-tripped-my-trading-bots-kill-switch-a-postmortem-4k2f"
source: "devto"
category: "news"
tags: ["devto", "python", "tech-article"]
date: "2026-09-21T01:22:40Z"
metadata:
  tag: "python"
---

# A 16-second clock drift falsely tripped my trading bot's kill switch. A postmortem.

> Source: devto | Category: news | 2026-09-21T01:22:40Z

My PC clock ran 16 seconds ahead of the exchange. Signature validation failed, a "helpful" fallback computed equity from a paper balance, and the bot declared a 58% drawdown. No orders were sent. Here is the chain of events and the two fixes.

Reactions: 0
