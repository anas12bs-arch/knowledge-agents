---
title: "A New JsonSerializerOptions Every Call Cost Me 120x"
url: "https://dev.to/ssukhpinder/a-new-jsonserializeroptions-every-call-cost-me-120x-299f"
source: "devto"
category: "news"
tags: ["devto", "programming", "tech-article"]
date: "2026-11-07T07:50:22Z"
metadata:
  tag: "programming"
---

# A New JsonSerializerOptions Every Call Cost Me 120x

> Source: devto | Category: news | 2026-11-07T07:50:22Z

A tiny endpoint was allocating like crazy. The culprit was a fresh JsonSerializerOptions built inside the handler on every request. Here's the measured cost and the one-line fix.

Reactions: 0
