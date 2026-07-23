---
title: "Show HN: Hanky – ETL style framework for loading flash cards into Anki"
url: "https://github.com/Haeata-Ash/hanky"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-23T16:21:09Z"
metadata:
  score: "5"
---

# Show HN: Hanky – ETL style framework for loading flash cards into Anki

> Source: hackernews | Category: news | 2026-07-23T16:21:09Z

Score: 5 | Comments: 0

It makes it easy to hit API&#x27;s, web scrape, do text-to-speech via online services etc in order to build rich flash cards in an automated way.<p>This has grown organically over a couple of years while learning French and German with some friends and thought some of you guys might find it useful.<p>An example pipeline I built with Hanky:<p>- Use CV to grab highlighted words and their context off of a page of printed text (extract)<p>- translate the highlighted word via an API (transform)<p>- generate audio with a tts service (transform)<p>Then load all that into anki as flash cards (load)<p>Keen to hear any feedback and hope you find it useful.
