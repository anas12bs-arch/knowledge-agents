---
title: "Too fast is wrong"
url: "https://dev.to/arcker/too-fast-is-wrong-kn5"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-09-27T15:28:49Z"
metadata:
  tag: "devops"
---

# Too fast is wrong

> Source: devto | Category: news | 2026-09-27T15:28:49Z

probatum is a test-oriented check runner I build in Rust. One issue waited forty-two days: there was no way to fail a response that came back too fast. For a login endpoint verifying an Argon2 hash, that is the only assertion that matters — swap the hash for a string compare and every test stays green while the endpoint gets a hundred times faster. Four releases in three days closed it, and along the way fixed a runner that only read the first 100,000 lines of what it was checking.

Reactions: 0
