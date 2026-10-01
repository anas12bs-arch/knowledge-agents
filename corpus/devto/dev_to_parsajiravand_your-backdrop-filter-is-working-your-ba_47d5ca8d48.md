---
title: "Your `backdrop-filter` Is Working. Your Background Is Hiding It."
url: "https://dev.to/parsajiravand/your-backdrop-filter-is-working-your-background-is-hiding-it-2k51"
source: "devto"
category: "news"
tags: ["devto", "webdev", "tech-article"]
date: "2026-10-01T09:13:41Z"
metadata:
  tag: "webdev"
---

# Your `backdrop-filter` Is Working. Your Background Is Hiding It.

> Source: devto | Category: news | 2026-10-01T09:13:41Z

backdrop-filter looks like a one-line copy from a Codepen: blur(20px), ship the frosted navbar. Half the time it renders as a plain flat panel instead — because backdrop-filter blurs whatever is BEHIND an element, and that only shows up if the element itself is see-through. Here's the transparency rule, the stacking-context trap it quietly sets, and why it's one of the priciest effects you can scroll past.

Reactions: 7
