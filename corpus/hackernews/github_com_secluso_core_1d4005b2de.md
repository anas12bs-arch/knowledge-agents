---
title: "Show HN: Open-source private home security camera system (end-to-end encryption)"
url: "https://github.com/secluso/core"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-05-30T14:30:01Z"
metadata:
  score: "92"
---

# Show HN: Open-source private home security camera system (end-to-end encryption)

> Source: hackernews | Category: news | 2026-05-30T14:30:01Z

Score: 92 | Comments: 21

Hey everyone,<p>I previously introduced an open source private home security camera in 2024, which uses OpenMLS for end-to-end encryption: <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=42284412">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=42284412</a>.<p>It was called Privastead then and it&#x27;s now renamed to Secluso.<p>John Kaczman found my project from here and has been working on it with me over the last year and half. We&#x27;ve made a lot of improvements to the software, which we would like to share with you:<p>- You can now set this up on your Raspberry Pi in less than 5 minutes with no technical expertise using our easy-to-use GUI deploy tool. We&#x27;ve put together a comprehensive build-your-own guide that walks you through the required steps (you can find a link at the top of the repository README).<p>- We use a customized, minimal OS based on the Yocto project for the camera.<p>- Every part of our stack except for the iOS app has reproducible builds. This includes our Android app, camera&#x2F;server binaries, deploy tool, and the aforementioned OS.<p>- We&#x27;ve re-designed our mobile app, which is now on the iOS App Store and Google Play store.<p>- We now support UnifiedPush for more privacy-preserving push notifications.<p>Looking forward to seeing what you all think!
