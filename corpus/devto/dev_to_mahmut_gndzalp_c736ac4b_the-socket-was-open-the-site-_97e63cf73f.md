---
title: "The Socket Was Open. The Site Was Dead for Fourteen Hours."
url: "https://dev.to/mahmut_gndzalp_c736ac4b/the-socket-was-open-the-site-was-dead-for-fourteen-hours-aie"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-09-07T10:33:15Z"
metadata:
  tag: "devops"
---

# The Socket Was Open. The Site Was Dead for Fourteen Hours.

> Source: devto | Category: news | 2026-09-07T10:33:15Z

DNS resolved, port 443 accepted, TLS handshake succeeded against a valid certificate - and every request returned 503 for fourteen hours. One PHP pool child had outlived its parent, gone to sleep inside a timer, and kept holding the socket and the pid file. The supervisor saw a live PID and refused to spawn a real pool. Here is how to spot a process that exists but does not work.

Reactions: 0
