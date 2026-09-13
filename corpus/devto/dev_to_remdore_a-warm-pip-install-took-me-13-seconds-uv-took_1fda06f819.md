---
title: "A warm pip install took me 13 seconds. uv took 56 milliseconds."
url: "https://dev.to/remdore/a-warm-pip-install-took-me-13-seconds-uv-took-56-milliseconds-3ehp"
source: "devto"
category: "news"
tags: ["devto", "python", "tech-article"]
date: "2026-09-13T17:39:42Z"
metadata:
  tag: "python"
---

# A warm pip install took me 13 seconds. uv took 56 milliseconds.

> Source: devto | Category: news | 2026-09-13T17:39:42Z

Benchmarked uv from Astral against pip on a real 63-package backend. Cold, uv is ~5x faster; warm, 13s becomes 56ms because uv hard-links from a shared cache instead of copying. Even forced to copy it stays ~40x ahead.

Reactions: 5
