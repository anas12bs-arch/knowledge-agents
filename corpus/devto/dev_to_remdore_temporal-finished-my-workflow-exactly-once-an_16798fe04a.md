---
title: "Temporal finished my workflow exactly once and ran its first step four times"
url: "https://dev.to/remdore/temporal-finished-my-workflow-exactly-once-and-ran-its-first-step-four-times-59dh"
source: "devto"
category: "news"
tags: ["devto", "python", "tech-article"]
date: "2026-10-10T14:27:57Z"
metadata:
  tag: "python"
---

# Temporal finished my workflow exactly once and ran its first step four times

> Source: devto | Category: news | 2026-10-10T14:27:57Z

I killed a Temporal worker eight times during a ten-step workflow. It completed once, and one side effect ran four times. Heartbeating made the duplicates worse, an idempotency key fixed them, and the determinism check turned out to compare shape, not arguments.

Reactions: 1
