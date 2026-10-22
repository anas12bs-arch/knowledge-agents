---
title: "Show HN: Replacing CAPTCHAs with adaptive proof-of-work in WordPress"
url: "https://wordpress.org/plugins/gdpr-compliant-recaptcha-for-all-forms/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-10-22T23:32:10Z"
metadata:
  score: "6"
---

# Show HN: Replacing CAPTCHAs with adaptive proof-of-work in WordPress

> Source: hackernews | Category: news | 2026-10-22T23:32:10Z

Score: 6 | Comments: 4

When I founded my business a whistle-blowing-service for enterprises, I’ve seeked for a working solution to block spam bots on that home page. The solution was intended to comply with EU data privacy law, no cookies, no sniffing, light-weight-size, on my webserver only, beeing invisible for my site visitors and no running costs at all.<p>I came across Hashcash, a proof-of-work approach, to block spam. When I implemented it, it worked immediately and blocked 100 percent without blocking any incoming real posts.<p>I was astonished, that no solution existed in the ecosystem allready that covered all forms and was for free. Therefore I‘ve turned it into a free wordpress-plugin.<p>It is not only a technical solution, but starts with the business model of spam (mass  spamming at low cost), by producing a calculation effort for every single post, that unavoidable. And therefore is not exactly unbreakable but becomes very expensive for the spammer and therefore alows only for targeted high quality approaches that need other treatment. Up to now my own page remains spam free and users report the same.<p>Now, running since 2022 on 4000+ active installations, it is working with almost every webform and plugin combination that is running on any wordpress instance, using pattern recognition on http-post-level instead of specific proprietary integration for single specific form builders. It ships with 80+ starting patterns for the most relevant form builders and themes, but can be enhanced with any pattern by the user.<p>The plugin can be previewed  directly and immediately on wordpress.org. It ships with14 KB compressed under a GPL-2.0 license.<p>I’m looking forward to discuss about the proof-of-work approach, form detection, privacy implications, and tradeoffs.
