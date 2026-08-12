---
title: "I benchmarked my language's native Postgres ORM against SQLAlchemy: ~8 faster reads, 5.7 less memory — and where it ties"
url: "https://dev.to/martin_palopoli/i-benchmarked-my-languages-native-postgres-orm-against-sqlalchemy-8x-faster-reads-57x-less-4ogn"
source: "devto"
category: "news"
tags: ["devto", "opensource", "tech-article"]
date: "2026-08-12T21:01:52Z"
metadata:
  tag: "opensource"
---

# I benchmarked my language's native Postgres ORM against SQLAlchemy: ~8 faster reads, 5.7 less memory — and where it ties

> Source: devto | Category: news | 2026-08-12T21:01:52Z

"Zero overhead" is the easiest claim to make and the hardest to prove. So the Fitz repo ships a reproducible head-to-head between two identical boilerplates — same Postgres, same endpoints, same docker compose — one on Fitz's native ORM, one on Python + SQLAlchemy. Here are the honest numbers (median of 3), why Fitz wins the reads, why it ties on writes, and the Nagle bug that once made Fitz 30% slower than Python.

Reactions: 0
