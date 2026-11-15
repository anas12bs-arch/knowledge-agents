---
title: "uv 0.13's tar-codec backend installs a 6,000-file sdist in 2.5 seconds instead of 3.8"
url: "https://dev.to/alexgeorgiev17/uv-013s-tar-codec-backend-installs-a-6000-file-sdist-in-25-seconds-instead-of-38-2ijc"
source: "devto"
category: "news"
tags: ["devto", "python", "tech-article"]
date: "2026-11-15T16:41:49Z"
metadata:
  tag: "python"
---

# uv 0.13's tar-codec backend installs a 6,000-file sdist in 2.5 seconds instead of 3.8

> Source: devto | Category: news | 2026-11-15T16:41:49Z

I measured uv 0.13's new tar-codec extraction backend against the old one: a 6,000-file source distribution installed in a 2.5-second median instead of 3.8, and a device-file entry the old backend silently dropped now fails with a clear error.

Reactions: 1
