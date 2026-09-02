---
title: "Show HN: OwnTime – a chess clock for your day's priorities"
url: "https://owntime.app/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-09-02T22:25:26Z"
metadata:
  score: "11"
---

# Show HN: OwnTime – a chess clock for your day's priorities

> Source: hackernews | Category: news | 2026-09-02T22:25:26Z

Score: 11 | Comments: 1

I made OwnTime to balance between competing priorities in my life. The idea is based on two main influences: the concept of &quot;roles&quot; from &quot;The 5 Choices&quot; (2015), and my repeated failure to effectively implement time blocking due to the necessary flexibility in my role.<p>The app allows you to define time budgets, which are not much more than a few mutually exclusive countdown timers. The UX is essentially that of a chess clock for an arbitrary number of players with configurable time.<p>The whole point of the app is to kick you out of the running role&#x2F;priority when its time is up. One feature that was essential for me was AlarmKit alarms, which only became possible last year (&gt;= iOS 26.1). Another was watchOS support, as a natural surface for time-related matters.<p>The current version is strictly focussed. The timers track time allocation during one day. All timers are reset at midnight. I didn&#x27;t build any statistics - you can export the raw internal SQLite store and make any evaluation or dashboard you want from there.<p>I don&#x27;t plan to extend the app nor to convert it into a service. All data stays local on your devices (synced between phone and watch locally) and fully open to you. No need for an account or subscription. Thus, I ask for a small one-time fee of $1.99.<p>The website has a short video and rendered preview: <a href="https:&#x2F;&#x2F;owntime.app" rel="nofollow">https:&#x2F;&#x2F;owntime.app</a><p>If you want to go straight to the App Store: <a href="https:&#x2F;&#x2F;apps.apple.com&#x2F;app&#x2F;id6770125662">https:&#x2F;&#x2F;apps.apple.com&#x2F;app&#x2F;id6770125662</a><p>I look forward to your comments and feedback.
