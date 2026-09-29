---
title: "Your 'Save' Button Makes Copies. The File System Access API Doesn't."
url: "https://dev.to/parsajiravand/your-save-button-makes-copies-the-file-system-access-api-doesnt-2d7h"
source: "devto"
category: "news"
tags: ["devto", "javascript", "tech-article"]
date: "2026-09-29T20:16:25Z"
metadata:
  tag: "javascript"
---

# Your 'Save' Button Makes Copies. The File System Access API Doesn't.

> Source: devto | Category: news | 2026-09-29T20:16:25Z

The classic web 'save' — a Blob and an <a download> link — doesn't overwrite a file, it manufactures a new one every time, leaving notes.md, notes (1).md, notes (2).md scattered in Downloads. The File System Access API fixes this with real, permissioned read-write access to a file on disk. Here's the difference, and why it's Chromium-only progressive enhancement, not a drop-in replacement.

Reactions: 3
