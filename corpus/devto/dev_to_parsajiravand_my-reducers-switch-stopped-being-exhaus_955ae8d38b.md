---
title: "My Reducer's Switch Stopped Being Exhaustive. `as const` Fixed It."
url: "https://dev.to/parsajiravand/my-reducers-switch-stopped-being-exhaustive-as-const-fixed-it-4aa4"
source: "devto"
category: "news"
tags: ["devto", "programming", "tech-article"]
date: "2026-10-25T23:14:00Z"
metadata:
  tag: "programming"
---

# My Reducer's Switch Stopped Being Exhaustive. `as const` Fixed It.

> Source: devto | Category: news | 2026-10-25T23:14:00Z

Object and array literals widen to `string` and `number` the moment you write them, which quietly breaks discriminated unions and exhaustive switch checks. `as const` keeps the literal types — but it also freezes the value, which bites in its own way.

Reactions: 5
