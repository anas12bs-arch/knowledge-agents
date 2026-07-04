---
title: "Position: fixed is a paint trick, not an event boundary"
url: "https://dev.to/earthbound_misfit/position-fixed-is-a-paint-trick-not-an-event-boundary-3cgp"
source: "devto"
category: "news"
tags: ["devto", "javascript", "tech-article"]
date: "2026-07-04T20:32:46Z"
metadata:
  tag: "javascript"
---

# Position: fixed is a paint trick, not an event boundary

> Source: devto | Category: news | 2026-07-04T20:32:46Z

A crop handle that would not drag. The overlay was position:fixed, but an ancestor stole the pointer with setPointerCapture. Synthetic events never see it. Only a real mouse does.

Reactions: 1
