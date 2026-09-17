---
title: "I had a model translate my locale file. The bug it introduced was correct Japanese."
url: "https://dev.to/remdore/i-had-a-model-translate-my-locale-file-the-bug-it-introduced-was-correct-japanese-58nk"
source: "devto"
category: "news"
tags: ["devto", "webdev", "tech-article"]
date: "2026-09-17T14:53:07Z"
metadata:
  tag: "webdev"
---

# I had a model translate my locale file. The bug it introduced was correct Japanese.

> Source: devto | Category: news | 2026-09-17T14:53:07Z

430 strings, four models, four languages. Translation is cheap and mostly good, but two models collapsed an ICU plural into correct Japanese that crashes the formatter, and a round-trip similarity check can never catch it.

Reactions: 7
