---
title: "Tigris marks every read with the region and cache layer that actually served it"
url: "https://dev.to/alexgeorgiev17/tigris-marks-every-read-with-the-region-and-cache-layer-that-actually-served-it-28p"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-09-15T14:44:02Z"
metadata:
  tag: "devops"
---

# Tigris marks every read with the region and cache layer that actually served it

> Source: devto | Category: news | 2026-09-15T14:44:02Z

Every GET on a Tigris bucket returns X-Tigris-Served-From and X-Tigris-Read-Source headers naming the exact region and cache layer that answered it. I tested that, region pinning, and what happens when you try to enable S3 versioning.

Reactions: 5
