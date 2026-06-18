---
title: "Ask HN: Am I being advertised an ARG via user agent logs?"
url: "https://news.ycombinator.com/item?id=48582005"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-06-18T19:58:17Z"
metadata:
  score: "7"
---

# Ask HN: Am I being advertised an ARG via user agent logs?

> Source: hackernews | Category: news | 2026-06-18T19:58:17Z

Score: 7 | Comments: 5

I&#x27;m here looking through logs on my unnamed reverse proxy and CDN service. The crawler bot swarm has been hitting my PHP application like I&#x27;ve upset them so I&#x27;m seeing which weird user agent strings are being allowed to connect. There&#x27;s &quot;Sogou&quot; and &quot;meta-webindexer&quot; and a small number of requests from &quot;SleepBot&#x2F;1.0&quot;<p>What&#x27;s SleepBot?<p>The ASN is Google and the UA string is: &quot;Mozilla&#x2F;5.0 AppleWebKit&#x2F;537.36 (KHTML, like Gecko; compatible; SleepBot&#x2F;1.0; +http &#x2F;&#x2F;sleepbot com&#x2F;) Chrome&#x2F;131.0.0.0 Safari&#x2F;537.36&quot; [edited to make link non-clickable]<p>So I visit the site. And it looks like the homepage of an interesting tech and ambient music guy who is still running a Shoutcast online radio stream but otherwise hasn&#x27;t been seen online in 5 years. The Wayback Machine shows few changes in over a decade. But the resume link brings up a GitHub account with a different URL and username which reported 1 issue in March of this year. It goes deeper.<p>What&#x27;s going on? Is a Google or adjacent employee running a personal scraper or just custom UA string while browsing the web? Did someone make a typo? Or is it some kind of weird security game &#x2F; ARG (&quot;Alternate Reality Game&quot;) and I&#x27;m the sap who&#x27;s taken the bait?
