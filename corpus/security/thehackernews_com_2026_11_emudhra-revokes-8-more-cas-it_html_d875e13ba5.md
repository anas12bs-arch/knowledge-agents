---
title: "[hacker-news-sec] eMudhra Revokes 8 More CAs It Previously Declared Unaffected by Key Compromise"
url: "https://thehackernews.com/2026/11/emudhra-revokes-8-more-cas-it.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-11-11T17:11:31Z"
metadata:
  {}
---

# [hacker-news-sec] eMudhra Revokes 8 More CAs It Previously Declared Unaffected by Key Compromise

> Source: security | Category: security | 2026-11-11T17:11:31Z

eMudhra Revokes 8 More CAs It Previously Declared Unaffected by Key Compromise

The in-house Python script behind eMudhra's October key compromise has now cost the company 8 more of its intermediate certificate authorities (CAs), even though it did not weaken their keys.

Each intermediate CA has its own private key, which the company uses to sign the certificates it issues. The 8 intermediate CAs compromised in October had a different problem: a single line in the script
