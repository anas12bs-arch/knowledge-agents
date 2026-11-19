---
title: "Why 'rm -rf $D*' Bypasses Almost Every AI Guardrail (And How We Scanned 115k Lines of Production Code)"
url: "https://dev.to/jimil_joshi_4baa0947baff5/why-rm-rf-d-bypasses-almost-every-ai-guardrail-and-how-we-scanned-115k-lines-of-production-28ea"
source: "devto"
category: "news"
tags: ["devto", "javascript", "tech-article"]
date: "2026-11-19T12:28:42Z"
metadata:
  tag: "javascript"
---

# Why "rm -rf $D*" Bypasses Almost Every AI Guardrail (And How We Scanned 115k Lines of Production Code)

> Source: devto | Category: news | 2026-11-19T12:28:42Z

Traditional AI safety guardrails match text strings using regex. But operating systems execute resolved shell commands. Here is why 11 out of 11 commercial agents failed GuardFall, and the open-source AST engine we built to fix it.

Reactions: 1
