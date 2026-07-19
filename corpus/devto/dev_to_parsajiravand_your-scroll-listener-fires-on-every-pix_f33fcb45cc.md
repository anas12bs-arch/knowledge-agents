---
title: "Your scroll listener fires on every pixel. `IntersectionObserver` fires when visibility actually changes."
url: "https://dev.to/parsajiravand/your-scroll-listener-fires-on-every-pixel-intersectionobserver-fires-when-visibility-actually-460c"
source: "devto"
category: "news"
tags: ["devto", "webdev", "tech-article"]
date: "2026-07-19T10:54:48Z"
metadata:
  tag: "webdev"
---

# Your scroll listener fires on every pixel. `IntersectionObserver` fires when visibility actually changes.

> Source: devto | Category: news | 2026-07-19T10:54:48Z

Detecting whether an element is in the viewport by listening to scroll events runs an expensive layout calculation on every frame. `IntersectionObserver` is the browser-native alternative — it fires only when visibility changes, off the main thread, with no scroll handler involved.

Reactions: 1
