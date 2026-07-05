---
title: "Show HN: Osint tool that finds exposed files on domains"
url: "https://search.cerast-intelligence.com/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-05T22:11:23Z"
metadata:
  score: "14"
---

# Show HN: Osint tool that finds exposed files on domains

> Source: hackernews | Category: news | 2026-07-05T22:11:23Z

Score: 14 | Comments: 0

hey guys, wanted to show one of my side projects i just made public.<p>the idea is basically another osint tool for pentesters and bug bounty
hunters. it watches certificate transparency logs and checks newly-seen
domains for exposed stuff like .env files, open .git dirs, config files,
db dumps and so on, and puts whatever it finds into a searchable db. you
just search a domain (or part of one) and see what&#x27;s exposed.<p>it&#x27;s read-only and free. one thing i&#x27;ve been thinking about adding is a
way to register for certain keywords and get notified when something new
shows up for that search.<p>would love to hear if you have other ideas for useful features, and also
ideas for how to reduce abuse of the data, since that&#x27;s the part i&#x27;m least
sure about.<p><a href="https:&#x2F;&#x2F;search.cerast-intelligence.com&#x2F;" rel="nofollow">https:&#x2F;&#x2F;search.cerast-intelligence.com&#x2F;</a>
