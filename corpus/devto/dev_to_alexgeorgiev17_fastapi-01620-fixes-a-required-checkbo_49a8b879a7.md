---
title: "FastAPI 0.162.0 fixes a required checkbox that was never actually required"
url: "https://dev.to/alexgeorgiev17/fastapi-01620-fixes-a-required-checkbox-that-was-never-actually-required-5boc"
source: "devto"
category: "news"
tags: ["devto", "webdev", "tech-article"]
date: "2026-11-04T02:24:42Z"
metadata:
  tag: "webdev"
---

# FastAPI 0.162.0 fixes a required checkbox that was never actually required

> Source: devto | Category: news | 2026-11-04T02:24:42Z

FastAPI 0.162.0 stopped silently turning every omitted boolean form field into False, including ones declared Form(...) as required. I measured the before and after on four field shapes, and found an unrelated sibling-parameter break that shipped the same week.

Reactions: 12
