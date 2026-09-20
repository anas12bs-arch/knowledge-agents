---
title: "[infoq] Cloudflare Measures Origin TLS Preferences, Cutting Handshake Retries from 52% to 3.7%"
url: "https://www.infoq.com/news/2026/09/cloudflare-automatic-key-exchang/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-09-20T09:47:09Z"
metadata:
  {}
---

# [infoq] Cloudflare Measures Origin TLS Preferences, Cutting Handshake Retries from 52% to 3.7%

> Source: engineering | Category: engineering | 2026-09-20T09:47:09Z

Cloudflare Measures Origin TLS Preferences, Cutting Handshake Retries from 52% to 3.7%

Cloudflare has replaced its static X25519 guess for origin TLS handshakes with per-origin measurement. HelloRetryRequests on scanned origins fell from roughly 52% to 3.7%, removing over 150 ms from p90 latency. Post-quantum connections completing in one round trip rose from 0% to 99.2%, though only 12.8% of origins support it.   By Steef-Jan Wiggers
