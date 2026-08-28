---
title: "Unicode's bold alphabet has holes in it, and every text generator falls in"
url: "https://dev.to/support_confileo_ce7442eb/unicodes-bold-alphabet-has-holes-in-it-and-every-text-generator-falls-in-1d8j"
source: "devto"
category: "news"
tags: ["devto", "javascript", "tech-article"]
date: "2026-08-28T12:19:05Z"
metadata:
  tag: "javascript"
---

# Unicode's bold alphabet has holes in it, and every text generator falls in

> Source: devto | Category: news | 2026-08-28T12:19:05Z

The Mathematical Alphanumeric Symbols block looks like a clean 26-letter run you can index into. It is not. Five of its alphabets have gaps where Unicode had already encoded the letter somewhere else, and a naive offset lands you on unassigned codepoints that render as tofu.

Reactions: 1
