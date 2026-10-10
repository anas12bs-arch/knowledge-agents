---
title: "Node.js 26's default Temporal API fixes a one-hour DST drift that Date still has"
url: "https://dev.to/alexgeorgiev17/nodejs-26s-default-temporal-api-fixes-a-one-hour-dst-drift-that-date-still-has-16ad"
source: "devto"
category: "news"
tags: ["devto", "webdev", "tech-article"]
date: "2026-10-10T14:27:56Z"
metadata:
  tag: "webdev"
---

# Node.js 26's default Temporal API fixes a one-hour DST drift that Date still has

> Source: devto | Category: news | 2026-10-10T14:27:56Z

Node.js 26 enables the Temporal API with no flag. I found it fixes a real one-hour DST drift in naive Date arithmetic, but costs about 19 times more than Date per operation, and its default overflow mode doesn't throw where I expected it to.

Reactions: 9
