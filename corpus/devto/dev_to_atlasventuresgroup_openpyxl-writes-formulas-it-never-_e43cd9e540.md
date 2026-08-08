---
title: "openpyxl writes formulas. It never evaluates them — so your generated spreadsheet can be silently wrong."
url: "https://dev.to/atlasventuresgroup/openpyxl-writes-formulas-it-never-evaluates-them-so-your-generated-spreadsheet-can-be-silently-106e"
source: "devto"
category: "news"
tags: ["devto", "python", "tech-article"]
date: "2026-08-08T13:27:12Z"
metadata:
  tag: "python"
---

# openpyxl writes formulas. It never evaluates them — so your generated spreadsheet can be silently wrong.

> Source: devto | Category: news | 2026-08-08T13:27:12Z

Your test asserts the cell equals "=AVERAGE(B2:B13)" and passes. The customer opens the file and reads 1.6% where the truth is 3.25%. Here is why the usual test suite can't see it, why data_only=True doesn't save you, and what to assert instead.

Reactions: 0
