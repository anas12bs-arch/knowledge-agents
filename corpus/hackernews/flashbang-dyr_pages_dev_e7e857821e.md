---
title: "Show HN: Flashbang – DuckDuckGo bangs resolved locally with a Service Worker"
url: "https://flashbang-dyr.pages.dev"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-14T23:08:38Z"
metadata:
  score: "6"
---

# Show HN: Flashbang – DuckDuckGo bangs resolved locally with a Service Worker

> Source: hackernews | Category: news | 2026-07-14T23:08:38Z

Score: 6 | Comments: 0

I like to use DuckDuckGo-style bangs and snaps, they are fast and efficient shortcuts.<p>However, neither Kagi nor DuckDuckGo resolves them as quickly as I would like and subjectively Google has better search results than DuckDuckGo.<p>After trying a few local alternatives eg. unduck, unduckified, I wasn&#x27;t satisfied, the ones I tried briefly loaded a page before redirecting causing visible page flickering, still took time to resolve the actual redirect and lacked advanced features (address-bar autocomplete). Flashbang avoids that by handling the redirect in a Service Worker, before the browser renders anything. On my machine, the added ove rhead is around 0.14ms.<p>It has 14,470 bangs, custom shortcuts, address-bar suggestions, and works offline once installed (except for suggestions). No runtime dependencies.<p>Try it: <a href="https:&#x2F;&#x2F;flashbang-dyr.pages.dev" rel="nofollow">https:&#x2F;&#x2F;flashbang-dyr.pages.dev</a>
Code: <a href="https:&#x2F;&#x2F;github.com&#x2F;ph1losof&#x2F;flashbang" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;ph1losof&#x2F;flashbang</a>
