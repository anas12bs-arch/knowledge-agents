---
title: "Caddy 2.11's default post-quantum key exchange sends six times more handshake bytes"
url: "https://dev.to/alexgeorgiev17/caddy-211s-default-post-quantum-key-exchange-sends-six-times-more-handshake-bytes-38g3"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-09-19T09:27:10Z"
metadata:
  tag: "devops"
---

# Caddy 2.11's default post-quantum key exchange sends six times more handshake bytes

> Source: devto | Category: news | 2026-09-19T09:27:10Z

I measured Caddy's new default X25519MLKEM768 key exchange against classical X25519: ClientHello grows from 318 to 1494 bytes, ServerHello from 122 to 1210, but the raw crypto costs under 65 microseconds and old clients still connect fine.

Reactions: 6
