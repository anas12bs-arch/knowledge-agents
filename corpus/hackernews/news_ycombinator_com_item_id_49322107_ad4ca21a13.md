---
title: "Tell HN: Cloudflare silently injects its analytics when you switch nameservers"
url: "https://news.ycombinator.com/item?id=49322107"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-08-16T19:09:09Z"
metadata:
  score: "28"
---

# Tell HN: Cloudflare silently injects its analytics when you switch nameservers

> Source: hackernews | Category: news | 2026-08-16T19:09:09Z

Score: 28 | Comments: 2

A few hours ago I switched my nameservers to Cloudflare in order to enable R2 bucket serving through my own subdomain, and I found out that it silently had injected a JS analytics snippet in my HTML-only JS-free site textlog.cc — I had to go to the Analytics dashboard, Add the site to the analytics and <i>then</i> disable the snippet. I find this approach entirely invasive, you should opt-in to features like that not have to opt-out. Just a warning out there to folks who might not be aware of this.
