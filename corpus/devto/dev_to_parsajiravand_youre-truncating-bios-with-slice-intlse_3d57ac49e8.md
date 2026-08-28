---
title: "You're truncating bios with `.slice()`. `Intl.Segmenter` knows where the emoji actually end."
url: "https://dev.to/parsajiravand/youre-truncating-bios-with-slice-intlsegmenter-knows-where-the-emoji-actually-end-36eo"
source: "devto"
category: "news"
tags: ["devto", "webdev", "tech-article"]
date: "2026-08-28T00:53:16Z"
metadata:
  tag: "webdev"
---

# You're truncating bios with `.slice()`. `Intl.Segmenter` knows where the emoji actually end.

> Source: devto | Category: news | 2026-08-28T00:53:16Z

A 30-character bio limit that cuts off mid-emoji isn't a rendering bug — it's .length counting UTF-16 code units instead of what's on screen. Intl.Segmenter counts graphemes, words, and sentences the way a reader actually sees them, and every major browser supports it now.

Reactions: 8
