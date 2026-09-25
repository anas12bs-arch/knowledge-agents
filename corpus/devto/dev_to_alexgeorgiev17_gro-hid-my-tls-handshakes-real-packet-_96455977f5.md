---
title: "GRO Hid My TLS Handshake's Real Packet Split, Even Over a Real Network"
url: "https://dev.to/alexgeorgiev17/gro-hid-my-tls-handshakes-real-packet-split-even-over-a-real-network-2eec"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-09-25T15:20:27Z"
metadata:
  tag: "devops"
---

# GRO Hid My TLS Handshake's Real Packet Split, Even Over a Real Network

> Source: devto | Category: news | 2026-09-25T15:20:27Z

Docker couldn't show me whether a post-quantum TLS handshake really splits across two TCP segments, same-host GSO hides it. Testing over a real external network wasn't enough either, until I found and disabled GRO, a default on basically any Linux cloud VM.

Reactions: 5
