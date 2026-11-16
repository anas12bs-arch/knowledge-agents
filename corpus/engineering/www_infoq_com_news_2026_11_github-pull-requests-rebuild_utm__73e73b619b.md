---
title: "[infoq] GitHub Rebuilds the Copilot App's Diff Surface to Open Million-Line Pull Requests Without Jank"
url: "https://www.infoq.com/news/2026/11/github-pull-requests-rebuild/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-11-16T17:33:20Z"
metadata:
  {}
---

# [infoq] GitHub Rebuilds the Copilot App's Diff Surface to Open Million-Line Pull Requests Without Jank

> Source: engineering | Category: engineering | 2026-11-16T17:33:20Z

GitHub Rebuilds the Copilot App's Diff Surface to Open Million-Line Pull Requests Without Jank

GitHub engineers rebuilt the diff view in the Copilot app to handle a pull request with 2,200 files, over a million changed lines and 400 inline comments. The design separates fixed-height code rows from variable-height comment blocks, which are measured in batches near the viewport. Performance is checked through CI budgets and automated app runs.   By Daniel Curtis
