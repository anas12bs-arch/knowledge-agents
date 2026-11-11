---
title: "[infoq] Article: The iOS Crash We Could Not Reproduce"
url: "https://www.infoq.com/articles/ios-crash-sigbus-debugging-experiment/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-11-11T09:18:26Z"
metadata:
  {}
---

# [infoq] Article: The iOS Crash We Could Not Reproduce

> Source: engineering | Category: engineering | 2026-11-11T09:18:26Z

Article: The iOS Crash We Could Not Reproduce

This article describes the investigation to find the root cause of a production crash in a large-scale iOS consumer app that had no clean stack trace. The crash occurred intermittently and resisted every local reproduction attempt. The final code change was small, but identifying the root cause required turning a vague SIGBUS report into a controlled set of experiments.   By Abhishek Gang Deb
