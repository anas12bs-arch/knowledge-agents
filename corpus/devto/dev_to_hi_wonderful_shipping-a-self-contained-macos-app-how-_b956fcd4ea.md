---
title: "Shipping a Self-Contained macOS App: How 24 Absolute Library Paths Broke My DeepSeek Harness Installer"
url: "https://dev.to/hi_wonderful/shipping-a-self-contained-macos-app-how-24-homebrew-dylibs-broke-my-deepseek-harness-installer-4i8b"
source: "devto"
category: "news"
tags: ["devto", "opensource", "tech-article"]
date: "2026-09-16T16:40:38Z"
metadata:
  tag: "opensource"
---

# Shipping a Self-Contained macOS App: How 24 Absolute Library Paths Broke My DeepSeek Harness Installer

> Source: devto | Category: news | 2026-09-16T16:40:38Z

I packaged DeepSeek Harness (dsh) into a double-clickable macOS installer for Apple Silicon. It worked on my machine — then died instantly on a clean Mac. Here's the otool -L investigation that found 24 absolute library paths baked into the runtime, and how to bundle them properly.

Reactions: 0
