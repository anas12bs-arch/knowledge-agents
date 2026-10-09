---
title: "Django 6.1's PBKDF2 default change rewrites existing password hashes on next login"
url: "https://dev.to/alexgeorgiev17/django-61s-pbkdf2-default-change-rewrites-existing-password-hashes-on-next-login-311m"
source: "devto"
category: "news"
tags: ["devto", "python", "tech-article"]
date: "2026-10-09T18:50:36Z"
metadata:
  tag: "python"
---

# Django 6.1's PBKDF2 default change rewrites existing password hashes on next login

> Source: devto | Category: news | 2026-10-09T18:50:36Z

Django 6.1 raised the default PBKDF2 iteration count from 1,200,000 to 1,500,000. I measured the extra cost per login, then found it rewrites every hash on next login, including ones an admin had deliberately hardened above the new default.

Reactions: 12
