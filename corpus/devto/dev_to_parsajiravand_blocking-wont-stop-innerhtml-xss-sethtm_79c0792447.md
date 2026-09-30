---
title: "Blocking `<script>` Won't Stop innerHTML XSS. `setHTML()` Will."
url: "https://dev.to/parsajiravand/blocking-wont-stop-innerhtml-xss-sethtml-will-4dh2"
source: "devto"
category: "news"
tags: ["devto", "webdev", "tech-article"]
date: "2026-09-30T23:45:46Z"
metadata:
  tag: "webdev"
---

# Blocking `<script>` Won't Stop innerHTML XSS. `setHTML()` Will.

> Source: devto | Category: news | 2026-09-30T23:45:46Z

A regex that strips <script> tags misses the XSS that actually runs — an onerror attribute. Element.setHTML(), from the HTML Sanitizer API, strips it natively, and for once Firefox shipped the finished version before Chrome did.

Reactions: 6
