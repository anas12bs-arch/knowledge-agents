---
title: "I Replaced pytest-xdist With 60 Lines of subprocess.Popen. Here's Why."
url: "https://dev.to/chenyuan20509/i-replaced-pytest-xdist-with-60-lines-of-subprocesspopen-heres-why-pfo"
source: "devto"
category: "news"
tags: ["devto", "python", "tech-article"]
date: "2026-07-26T08:43:36Z"
metadata:
  tag: "python"
---

# I Replaced pytest-xdist With 60 Lines of subprocess.Popen. Here's Why.

> Source: devto | Category: news | 2026-07-26T08:43:36Z

Our test suite kept flaking from cross-file state leakage. xdist's persistent workers were the cause, not the cure. Here's the per-file subprocess runner that fixed it.

Reactions: 0
