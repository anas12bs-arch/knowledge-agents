---
title: "My Struct Key Boxed Itself Two Million Times"
url: "https://dev.to/ssukhpinder/my-struct-key-boxed-itself-two-million-times-1if5"
source: "devto"
category: "news"
tags: ["devto", "programming", "tech-article"]
date: "2026-11-01T20:33:39Z"
metadata:
  tag: "programming"
---

# My Struct Key Boxed Itself Two Million Times

> Source: devto | Category: news | 2026-11-01T20:33:39Z

A dictionary lookup shouldn't allocate, so why was mine showing up in the profiler? The culprit was a struct key missing one interface, boxing itself on every call.

Reactions: 0
