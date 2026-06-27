---
title: "Show HN: Hacker News on a train station-style flip board"
url: "https://popflame.quickish.space/hn-flipboard/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-06-27T04:16:56Z"
metadata:
  score: "32"
---

# Show HN: Hacker News on a train station-style flip board

> Source: hackernews | Category: news | 2026-06-27T04:16:56Z

Score: 32 | Comments: 4

Although the page itself is more just fun to have made and look at (I like the flip sound), the fun part is how I made it to verify the (and I hate to say it) vibe host service I&#x27;ve been working on. The recent flip board back and forth&#x27;s on Twitter (X) are what inspired me.<p>The idea here is that people (like me or you) can create something neat like this, and others can remix it, change it and publish their own version. This is that all in action and it worked great. I wrote a blog about it (the blog is dogfooding, it&#x27;s just an app hosted on quickish that uses the built in db lib).<p>For the HN version of this flip board I use their firebase api via the built in quickish server functions that make use of the fact that the front-end can get realtime updates (now that you mention firebase) from cloud function db updates. Of course that&#x27;s over-kill but I wanted to show something fun. You can remix and host your own version for free, just need a google oauth login that&#x27;s it.<p>OG flip board I built (Portland Based - Current Weather): <a href="https:&#x2F;&#x2F;popflame.quickish.space&#x2F;flipboard-preview" rel="nofollow">https:&#x2F;&#x2F;popflame.quickish.space&#x2F;flipboard-preview</a><p>Blog post that dives a tiny bit deeper: <a href="https:&#x2F;&#x2F;popflame.quickish.space&#x2F;blog&#x2F;hacker-news-on-a-split-flap-board&#x2F;" rel="nofollow">https:&#x2F;&#x2F;popflame.quickish.space&#x2F;blog&#x2F;hacker-news-on-a-split-...</a>
