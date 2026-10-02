---
title: "Show HN: Rhun, an open-source code editor written in assembly"
url: "https://rhun.app/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-10-02T00:45:34Z"
metadata:
  score: "30"
---

# Show HN: Rhun, an open-source code editor written in assembly

> Source: hackernews | Category: news | 2026-10-02T00:45:34Z

Score: 30 | Comments: 11

I found that I&#x27;m not using even 1&#x2F;3 of vim&#x2F;vscode features anymore.<p>That&#x27;s wht I&#x27;m building rhun - a small code editor for Linux, Windows and Apple silicon Macs. It obviously has Vim mode, a terminal, Git diffs and a panel for Claude Code or Codex sessions.<p>The editor and pixel renderer share an x86-64 assembly core. For Apple silicon, a build-time translator converts that core to AArch64, with separate platform adapters around it.
The latest release can draft commit messages using a local Ollama model or an existing Claude Code or Codex subscription.<p>It&#x27;s a solo project, MIT licensed and still early.
