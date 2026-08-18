---
title: "Show HN: macOS data protection keychain for Electron apps"
url: "https://github.com/biw/keychain-store"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-08-18T18:39:56Z"
metadata:
  score: "6"
---

# Show HN: macOS data protection keychain for Electron apps

> Source: hackernews | Category: news | 2026-08-18T18:39:56Z

Score: 6 | Comments: 0

Hey HN,<p>I&#x27;ve been working on Hansel [1] (an encrypted personal data store you can query with agents), and there wasn&#x27;t a good way to use the modern macOS Data Protection Keychain.<p>Electron&#x27;s safeStorage [2] uses the legacy file-based keychain, which allows other apps&#x2F;agents to query it with the `security` CLI. Not great when you have a dozen agents running in the background! The Data Protection Keychain is nice because it limits access via code-signing access groups and lets you set access rules like Touch ID and&#x2F;or password.<p>1: <a href="https:&#x2F;&#x2F;hansel.so&#x2F;" rel="nofollow">https:&#x2F;&#x2F;hansel.so&#x2F;</a><p>2. <a href="https:&#x2F;&#x2F;www.electronjs.org&#x2F;docs&#x2F;latest&#x2F;api&#x2F;safe-storage" rel="nofollow">https:&#x2F;&#x2F;www.electronjs.org&#x2F;docs&#x2F;latest&#x2F;api&#x2F;safe-storage</a>
