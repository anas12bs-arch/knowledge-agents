---
title: "Stop Trusting npm Scans: Run Untrusted Packages in an Isolated AWS Sandbox"
url: "https://dev.to/aws-builders/stop-trusting-npm-scans-run-untrusted-packages-in-an-isolated-aws-sandbox-cmm"
source: "devto"
category: "news"
tags: ["devto", "ai", "tech-article"]
date: "2026-11-11T02:09:58Z"
metadata:
  tag: "ai"
---

# Stop Trusting npm Scans: Run Untrusted Packages in an Isolated AWS Sandbox

> Source: devto | Category: news | 2026-11-11T02:09:58Z

Static scanners read npm packages without running them, so they miss the postinstall that only fires at install time. I gave my AI agent one tool that runs the install in a disposable AWS CodeBuild sandbox and catches the curl | bash from the real build log.

Reactions: 5
