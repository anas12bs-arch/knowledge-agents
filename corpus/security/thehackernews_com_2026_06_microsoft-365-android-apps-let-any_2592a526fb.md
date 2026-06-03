---
title: "[hacker-news-sec] Microsoft 365 Android Apps Let Any App Steal Account Tokens via Leftover Debug Flag"
url: "https://thehackernews.com/2026/06/microsoft-365-android-apps-let-any-app.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-06-03T23:15:18Z"
metadata:
  {}
---

# [hacker-news-sec] Microsoft 365 Android Apps Let Any App Steal Account Tokens via Leftover Debug Flag

> Source: security | Category: security | 2026-06-03T23:15:18Z

Microsoft 365 Android Apps Let Any App Steal Account Tokens via Leftover Debug Flag

A development flag left switched on in production builds of several Microsoft 365 Android apps disabled the check that limits account-token sharing to trusted Microsoft apps.

Any other app on the same phone could ask for the signed-in user's token and get it, then read email, open files, browse the calendar, and send messages as that user. No password, no login screen, no permission prompt.
