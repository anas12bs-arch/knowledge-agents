---
title: "Show HN: Justif – Knuth-Plass justification and microtypography for the web"
url: "https://justif.lyall.co/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-21T21:00:38Z"
metadata:
  score: "12"
---

# Show HN: Justif – Knuth-Plass justification and microtypography for the web

> Source: hackernews | Category: news | 2026-07-21T21:00:38Z

Score: 12 | Comments: 2

Justif is a drop-in JavaScript library that progressively enhances web pages to TeX-level text justification. Installation is a single &lt;script&gt; line, standard text and accessibility affordances are unchanged, and users with JS disabled get native browser rendering.<p>I made justif because I&#x27;ve long been a fan of justified text. I think it looks clean and elegant, and makes reading more enjoyable. But bad justification is the opposite, with gaping spaces that distract me to the point of making the text near unreadable.<p>Browsers have got better recently at handling justified text [0][1], but still use suboptimal greedy algorithms for the most part, and are not near that TeX&#x2F;InDesign level of quality that I crave. `text-wrap: pretty` exists but is far from a panacea, as you can see for yourself in the demo.<p>Justif also has the benefit of providing more consistent text layout across browsers. Blink (Chrome), Gecko (Firefox) and WebKit (Safari) all justify text differently, so normally what the user sees depends on what browser they use.<p>Take a look at the demo, play around with it, see if you can break anything. I&#x27;m open to improvements of the API design as well, so please let me know your thoughts.<p>For more details, see the README: <a href="https:&#x2F;&#x2F;github.com&#x2F;lyallcooper&#x2F;justif" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;lyallcooper&#x2F;justif</a><p>0: <a href="https:&#x2F;&#x2F;cloudfour.com&#x2F;thinks&#x2F;justified-text-better-than-expected&#x2F;" rel="nofollow">https:&#x2F;&#x2F;cloudfour.com&#x2F;thinks&#x2F;justified-text-better-than-expe...</a><p>1: <a href="https:&#x2F;&#x2F;owickstrom.github.io&#x2F;the-proportional-web&#x2F;" rel="nofollow">https:&#x2F;&#x2F;owickstrom.github.io&#x2F;the-proportional-web&#x2F;</a>
