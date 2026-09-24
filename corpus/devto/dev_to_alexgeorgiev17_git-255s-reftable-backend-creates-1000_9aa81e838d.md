---
title: "Git 2.55's reftable backend creates 10,000 refs in 40ms instead of 650ms"
url: "https://dev.to/alexgeorgiev17/git-255s-reftable-backend-creates-10000-refs-in-40ms-instead-of-650ms-inn"
source: "devto"
category: "news"
tags: ["devto", "opensource", "tech-article"]
date: "2026-09-24T10:22:39Z"
metadata:
  tag: "opensource"
---

# Git 2.55's reftable backend creates 10,000 refs in 40ms instead of 650ms

> Source: devto | Category: news | 2026-09-24T10:22:39Z

Git's reftable ref backend cut a 10,000-branch bulk write from up to 650ms to about 40ms and shrank the ref store from 40MB to 272KB. Push 150 concurrent writers at it and roughly 40% failed outright with the default lock timeout.

Reactions: 1
