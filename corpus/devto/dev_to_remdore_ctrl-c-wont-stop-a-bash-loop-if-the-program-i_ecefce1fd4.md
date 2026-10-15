---
title: "Ctrl-C won't stop a bash loop if the program inside it catches the signal"
url: "https://dev.to/remdore/ctrl-c-wont-stop-a-bash-loop-if-the-program-inside-it-catches-the-signal-134i"
source: "devto"
category: "news"
tags: ["devto", "python", "tech-article"]
date: "2026-10-15T05:11:11Z"
metadata:
  tag: "python"
---

# Ctrl-C won't stop a bash loop if the program inside it catches the signal

> Source: devto | Category: news | 2026-10-15T05:11:11Z

A Python or Node program that handles Ctrl-C and exits cleanly makes bash carry on with the next loop iteration. dash, zsh, busybox ash and mksh quit instead. Here is the code in bash that decides.

Reactions: 5
