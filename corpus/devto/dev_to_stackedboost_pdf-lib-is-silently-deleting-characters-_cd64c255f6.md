---
title: "pdf-lib throws on Ł. The obvious fix silently deletes your users' data"
url: "https://dev.to/stackedboost/pdf-lib-is-silently-deleting-characters-from-your-users-data-51ld"
source: "devto"
category: "news"
tags: ["devto", "javascript", "tech-article"]
date: "2026-08-30T16:41:55Z"
metadata:
  tag: "javascript"
---

# pdf-lib throws on Ł. The obvious fix silently deletes your users' data

> Source: devto | Category: news | 2026-08-30T16:41:55Z

The standard 14 PDF fonts are WinAnsi only, so pdf-lib throws on Łódź Sp. z o.o. Strip the characters to stop the exception and you quietly corrupt a name on a document your user is about to send. Here is the real fix.

Reactions: 0
