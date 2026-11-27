---
title: "Show HN: bouncemarket – a live prediction market game for a bouncing ball"
url: "https://bouncemarket.minhanhday.com/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-11-27T19:30:17Z"
metadata:
  score: "264"
---

# Show HN: bouncemarket – a live prediction market game for a bouncing ball

> Source: hackernews | Category: news | 2026-11-27T19:30:17Z

Score: 264 | Comments: 79

a ball will fall. trade on where it lands.<p>I made this game! Some technical details:<p>The entire drop of the ball is simulated server-side, then streamed to each client as server-sent events with a small buffer. Every drop is deterministic from its starting position, so rounds can be replayed exactly for later analysis, but tiny variations in starting position can change the ultimate outcome.<p>There&#x27;s some AI traders to keep the market moving, but they drop out in any round that has more than five people. They operate using a naive set of rules that I wrote for them, so they&#x27;re not too hard to beat -- it&#x27;s when the market is full of real people that it gets tricky.<p>Curious to get feedback on anything you would change, and especially whether the mechanics were clear right away or not.
