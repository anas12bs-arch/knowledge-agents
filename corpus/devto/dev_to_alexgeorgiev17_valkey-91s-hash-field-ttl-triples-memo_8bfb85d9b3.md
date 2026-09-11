---
title: "Valkey 9.1's hash field TTL triples memory use for the pattern its own docs show"
url: "https://dev.to/alexgeorgiev17/valkey-91s-hash-field-ttl-triples-memory-use-for-the-pattern-its-own-docs-show-22k8"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-09-11T09:49:43Z"
metadata:
  tag: "devops"
---

# Valkey 9.1's hash field TTL triples memory use for the pattern its own docs show

> Source: devto | Category: news | 2026-09-11T09:49:43Z

I measured Valkey 9.1's HSETEX/HEXPIRE hash field TTLs: the documented per-user-hash pattern costs 261 bytes/key against 87 for a plain string with EXPIRE, a 3x regression, while the intended one-hash-many-fields pattern only adds ~23 bytes per field.

Reactions: 5
