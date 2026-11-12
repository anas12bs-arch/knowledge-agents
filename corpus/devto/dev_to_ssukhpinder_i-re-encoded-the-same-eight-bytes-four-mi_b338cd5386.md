---
title: "I Re-Encoded the Same Eight Bytes Four Million Times"
url: "https://dev.to/ssukhpinder/i-re-encoded-the-same-eight-bytes-four-million-times-f21"
source: "devto"
category: "news"
tags: ["devto", "programming", "tech-article"]
date: "2026-11-12T19:53:49Z"
metadata:
  tag: "programming"
---

# I Re-Encoded the Same Eight Bytes Four Million Times

> Source: devto | Category: news | 2026-11-12T19:53:49Z

A server-sent-events writer was allocating a fresh byte[] for its constant framing on every record. Switching to C#'s u8 literals cut 122 MB of garbage per pass and ran about 3x faster.

Reactions: 1
