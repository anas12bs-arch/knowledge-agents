---
title: "`beforeunload` Can Still Kill Your bfcache. Mount It Only When Dirty."
url: "https://dev.to/parsajiravand/beforeunload-can-still-kill-your-bfcache-mount-it-only-when-dirty-50jp"
source: "devto"
category: "news"
tags: ["devto", "javascript", "tech-article"]
date: "2026-10-05T12:46:42Z"
metadata:
  tag: "javascript"
---

# `beforeunload` Can Still Kill Your bfcache. Mount It Only When Dirty.

> Source: devto | Category: news | 2026-10-05T12:46:42Z

A `beforeunload` listener you left mounted forever can still quietly cost you bfcache eligibility — and an `unload` listener reliably will. Here's the pagehide/pageshow fix, and why 'mount it only when there's something to lose' is the durable rule.

Reactions: 3
