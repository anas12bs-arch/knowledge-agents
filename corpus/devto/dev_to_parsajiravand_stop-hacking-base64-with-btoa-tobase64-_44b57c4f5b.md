---
title: "Stop Hacking Base64 With btoa(). toBase64() Fixes It Natively."
url: "https://dev.to/parsajiravand/stop-hacking-base64-with-btoa-tobase64-fixes-it-natively-2kkm"
source: "devto"
category: "news"
tags: ["devto", "webdev", "tech-article"]
date: "2026-11-05T17:44:37Z"
metadata:
  tag: "webdev"
---

# Stop Hacking Base64 With btoa(). toBase64() Fixes It Natively.

> Source: devto | Category: news | 2026-11-05T17:44:37Z

btoa() throws on emoji, and the classic String.fromCharCode(...bytes) workaround crashes on large files. toBase64() and fromBase64() on Uint8Array fix both — no string round trip, no library.

Reactions: 7
