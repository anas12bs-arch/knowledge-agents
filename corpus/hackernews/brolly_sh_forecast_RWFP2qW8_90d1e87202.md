---
title: "Show HN: Brolly, a plain-text weather forecast site"
url: "https://brolly.sh/forecast/RWFP2qW8"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-25T19:23:21Z"
metadata:
  score: "3"
---

# Show HN: Brolly, a plain-text weather forecast site

> Source: hackernews | Category: news | 2026-07-25T19:23:21Z

Score: 3 | Comments: 0

The UK MET office recently redesigned their site, adding a lot of additional whitespace, scrolling, and animations. This significantly reduced its usability for me, and left me wanting an ‘at a glance’ weather site.<p>I made <a href="https:&#x2F;&#x2F;brolly.sh" rel="nofollow">https:&#x2F;&#x2F;brolly.sh</a>, a minimalist, plain text weather forecasting site. You can use it to view weather from around the world, with: 7 day forecast; Previous day log (so you can confirm it definitely was cooler &#x2F; hotter &#x2F; wetter &#x2F; drier yesterday!); Hourly rain, wind, temperature, conditions; Hourly UV, air quality and pollen, including pollen type specific forecasts within the EU &#x2F; UK; Location search and last 5 locations; Location specific units.<p>I mostly made the site for myself, if anyone else also benefits from it that’s an added advantage.<p>You can check out the weather in York, UK at <a href="https:&#x2F;&#x2F;brolly.sh&#x2F;forecast&#x2F;RWFP2qW8" rel="nofollow">https:&#x2F;&#x2F;brolly.sh&#x2F;forecast&#x2F;RWFP2qW8</a>, or search for a location at <a href="https:&#x2F;&#x2F;brolly.sh" rel="nofollow">https:&#x2F;&#x2F;brolly.sh</a><p>The site is deliberately styled as a single long scrollable column, to work on mobile phones. You can view it on desktop too, there&#x27;s just a lot of horizontal padding. I naturally took a lot of inspiration from plaintextsports.com. Despite not being a sports fan, I love its aesthetic. But, you&#x27;ll hopefully see that this site isn&#x27;t a rip off, and has its own deliberate look and feel.<p>Visualisations are really important to showing information at a glance. I spent a lot of time designing the different visualisations and making them work with only characters. My favourite is the hourly heat map used for pollen count.<p>It&#x27;s also frustrating to have an interactive site, where you can&#x27;t share a page with a friend and have them see what you&#x27;re seeing. To solve this, all page state (i.e. location, selected day, expanded &#x2F; collapsed sections), is stored in the URL. You can share or bookmark the specific view, and know that you&#x27;ll always be able to come back to it.<p>The site uses PocketBase. It’s written in Go and plain HTML&#x2F;JavaScript&#x2F;CSS. All pages are backend rendered, with light JavaScript to handle re-loading content without page jumps when using interactive features like next &#x2F; previous day navigation. Weather forecasts are fetched from open-meteo.com, which has a very generous free tier. However, I also built a custom LRU cache on top of PocketBase’s SQLite DB to cache forecasts for 5 minutes, and avoid putting unnecessary pressure on the open-meteo API.
