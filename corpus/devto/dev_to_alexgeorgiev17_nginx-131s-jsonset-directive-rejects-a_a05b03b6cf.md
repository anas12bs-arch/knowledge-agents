---
title: "nginx 1.31's json_set directive rejects a bad webhook payload about 13 times faster than forwarding it"
url: "https://dev.to/alexgeorgiev17/nginx-131s-jsonset-directive-rejects-a-bad-webhook-payload-about-13-times-faster-than-forwarding-3b00"
source: "devto"
category: "news"
tags: ["devto", "webdev", "tech-article"]
date: "2026-11-14T14:46:06Z"
metadata:
  tag: "webdev"
---

# nginx 1.31's json_set directive rejects a bad webhook payload about 13 times faster than forwarding it

> Source: devto | Category: news | 2026-11-14T14:46:06Z

I measured nginx 1.31's new native JSON parser against a Python backend doing the same validation: roughly 13x faster per-request rejection at low concurrency, half a backend's request count removed outright in a 50/50 mix, and no measurable overhead when nothing gets rejected at all.

Reactions: 6
