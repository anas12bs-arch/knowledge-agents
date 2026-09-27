---
title: "containerd 2.2's mount manager panics on a one-mount mkfs chain"
url: "https://dev.to/alexgeorgiev17/containerd-22s-mount-manager-panics-on-a-one-mount-mkfs-chain-545n"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-09-27T15:28:49Z"
metadata:
  tag: "devops"
---

# containerd 2.2's mount manager panics on a one-mount mkfs chain

> Source: devto | Category: news | 2026-09-27T15:28:49Z

I measured containerd 2.2's new mount manager against doing the same loopback ext4 setup by hand: 24ms manual versus 30-47ms through the API, then found a reproducible index-out-of-range panic and a raw BoltDB error leaking through it.

Reactions: 6
