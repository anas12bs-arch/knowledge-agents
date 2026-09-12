---
title: "Bun 1.4's Rust rewrite cuts script startup time from 10.5ms to 4.2ms"
url: "https://dev.to/alexgeorgiev17/bun-14s-rust-rewrite-cuts-script-startup-time-from-105ms-to-42ms-2je0"
source: "devto"
category: "news"
tags: ["devto", "javascript", "tech-article"]
date: "2026-09-12T11:35:11Z"
metadata:
  tag: "javascript"
---

# Bun 1.4's Rust rewrite cuts script startup time from 10.5ms to 4.2ms

> Source: devto | Category: news | 2026-09-12T11:35:11Z

I measured Bun 1.4's Rust runtime against 1.3.14: startup dropped 60%, idle memory 46%, but idle CPU only fell 2.5x against a claimed 5x, and invoking Bun as a node symlink silently stops loading .env files.

Reactions: 5
