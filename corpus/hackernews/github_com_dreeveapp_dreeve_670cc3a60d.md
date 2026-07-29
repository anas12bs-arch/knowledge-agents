---
title: "Show HN: Dreeve, a self-hosted dashboard for your sports and fitness data"
url: "https://github.com/dreeveapp/dreeve"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-29T21:14:01Z"
metadata:
  score: "4"
---

# Show HN: Dreeve, a self-hosted dashboard for your sports and fitness data

> Source: hackernews | Category: news | 2026-07-29T21:14:01Z

Score: 4 | Comments: 0

I&#x27;ve been building this for a few years under the name &quot;Statistics for Strava&quot; but I renamed it to Dreeve recently because of Strava&#x27;s recently changed API usage terms. They paywalled their API.<p>You point it at your activity files (FIT&#x2F;TCX&#x2F;GPX) or connect a Strava account, and it gives you a dashboard with segment efforts, gear and maintenance tracking, a heatmap, monthly calendar view, milestones and a year-in-review. It runs as a Docker container, stores everything in SQLite, and nothing leaves your machine.<p>Stack is PHP 8.5 + Symfony, SQLite, Docker Compose. Simple, straightforward and fast.<p>Caveats: it&#x27;s built around a single user, so there&#x27;s no multi-tenant story. The AI workout assistant is optional and off unless you configure it. Segment data still comes from Strava if you want it, which is the one dependency I haven&#x27;t been able to remove.<p>Docs at <a href="https:&#x2F;&#x2F;docs.dreeve.app" rel="nofollow">https:&#x2F;&#x2F;docs.dreeve.app</a>. Happy to answer any questions you have
