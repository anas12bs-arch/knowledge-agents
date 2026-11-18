---
title: "Show HN: Unref – A Python dead code finder built on Ruff's parser"
url: "https://github.com/Apakottur/unref"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-11-18T07:10:56Z"
metadata:
  score: "9"
---

# Show HN: Unref – A Python dead code finder built on Ruff's parser

> Source: hackernews | Category: news | 2026-11-18T07:10:56Z

Score: 9 | Comments: 1

I wanted a good Python dead code finder that just works, with minimal config, until Ruff adds support for that (<a href="https:&#x2F;&#x2F;github.com&#x2F;astral-sh&#x2F;ruff&#x2F;issues&#x2F;872" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;astral-sh&#x2F;ruff&#x2F;issues&#x2F;872</a>).<p>None of the newer alternatives to Vulture worked out of the box on my codebases, so I decided to build one.<p>The first version was in Python, then I switched to Rust for speed and to reuse Ruff&#x27;s parser. It checks all of CPython in under a second.<p>It found lots of interesting dead code in my team&#x27;s codebases, and it&#x27;s the first time in years we&#x27;ve had a Python dead code finder in our CI.<p>Feedback is very welcome, especially dead code it misses.
