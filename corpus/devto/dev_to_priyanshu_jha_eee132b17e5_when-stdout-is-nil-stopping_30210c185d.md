---
title: "When stdout is nil: stopping a WinRM panic in GitLab Fleeting"
url: "https://dev.to/priyanshu_jha_eee132b17e5/when-stdout-is-nil-stopping-a-winrm-panic-in-gitlab-fleeting-3o5l"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-11-14T01:37:09Z"
metadata:
  tag: "devops"
---

# When stdout is nil: stopping a WinRM panic in GitLab Fleeting

> Source: devto | Category: news | 2026-11-14T01:37:09Z

How I reproduced a nil-pointer panic in GitLab Fleeting's WinRM connector with a fake SOAP transport, defaulted a nil stdout writer to io.Discard, and got the fix merged during the October 2026 Hackathon.

Reactions: 1
