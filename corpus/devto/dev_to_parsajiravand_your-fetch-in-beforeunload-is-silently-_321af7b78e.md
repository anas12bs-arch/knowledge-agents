---
title: "Your fetch in beforeunload is silently killed. navigator.sendBeacon guarantees delivery."
url: "https://dev.to/parsajiravand/your-fetch-in-beforeunload-is-silently-killed-navigatorsendbeacon-guarantees-delivery-17pn"
source: "devto"
category: "news"
tags: ["devto", "webdev", "tech-article"]
date: "2026-08-22T09:33:05Z"
metadata:
  tag: "webdev"
---

# Your fetch in beforeunload is silently killed. navigator.sendBeacon guarantees delivery.

> Source: devto | Category: news | 2026-08-22T09:33:05Z

When the page unloads, the browser may cancel any in-flight fetch or XHR before it completes. navigator.sendBeacon sends a POST the browser commits to delivering, even after the document is gone.

Reactions: 3
