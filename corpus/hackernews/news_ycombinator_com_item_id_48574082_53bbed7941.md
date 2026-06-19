---
title: "Ask HN: How do you separate intentional test boilerplate from real duplication?"
url: "https://news.ycombinator.com/item?id=48574082"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-06-19T22:12:38Z"
metadata:
  score: "7"
---

# Ask HN: How do you separate intentional test boilerplate from real duplication?

> Source: hackernews | Category: news | 2026-06-19T22:12:38Z

Score: 7 | Comments: 5

I am maintaining an open-source project (deterministic open source duplicate-code detector) and a user asked for a feature which I don’t have a clear answer on how to implement.<p>This seems a very hard problem to solve:<p>-Tests repeat the same scenario. For a structural detector, this flags as repetition (duplication). However, tests are not something people want to delete from the codebases.<p>-The repetitions from tests (on purpose) end up looking like undesired code duplication and the tools canno tell which is which.<p>-One way to solve this would be something like a human in the loop (kind of how linters allow user to accept something once, while keeping the default first run zero-config).<p>Wonder how you have seen this handle and if anyone have any ideas.<p>Here is the the repo: https:&#x2F;&#x2F;github.com&#x2F;Rafaelpta&#x2F;dupehound<p>And here is the issue with more detail: https:&#x2F;&#x2F;github.com&#x2F;Rafaelpta&#x2F;dupehound&#x2F;issues&#x2F;23
