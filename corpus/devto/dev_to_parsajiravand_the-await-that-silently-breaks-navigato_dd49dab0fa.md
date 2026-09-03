---
title: "The await That Silently Breaks navigator.clipboard.writeText()"
url: "https://dev.to/parsajiravand/the-await-that-silently-breaks-navigatorclipboardwritetext-10oe"
source: "devto"
category: "news"
tags: ["devto", "webdev", "tech-article"]
date: "2026-09-03T19:49:14Z"
metadata:
  tag: "webdev"
---

# The await That Silently Breaks navigator.clipboard.writeText()

> Source: devto | Category: news | 2026-09-03T19:49:14Z

navigator.clipboard.writeText() only works while the document is focused and the user gesture is still fresh. Any await before the call can let both expire, so a copy button fails with an uncaught NotAllowedError and nobody ever sees why.

Reactions: 6
