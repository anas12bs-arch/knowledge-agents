---
title: "The Array Hiding in Every params Call"
url: "https://dev.to/ssukhpinder/the-array-hiding-in-every-params-call-4hf9"
source: "devto"
category: "news"
tags: ["devto", "programming", "tech-article"]
date: "2026-11-12T12:10:13Z"
metadata:
  tag: "programming"
---

# The Array Hiding in Every params Call

> Source: devto | Category: news | 2026-11-12T12:10:13Z

A four-line display-name helper was quietly allocating an array on every call through params T[]. Switching to C# 13's params ReadOnlySpan<T> took it from 107 MB to zero, with the call sites unchanged.

Reactions: 1
