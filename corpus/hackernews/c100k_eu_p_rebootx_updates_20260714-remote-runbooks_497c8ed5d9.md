---
title: "Show HN: Running server scripts from smartphone via SSH"
url: "https://c100k.eu/p/rebootx/updates/20260714-remote-runbooks"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-15T15:56:49Z"
metadata:
  score: "3"
---

# Show HN: Running server scripts from smartphone via SSH

> Source: hackernews | Category: news | 2026-07-15T15:56:49Z

Score: 3 | Comments: 0

I&#x27;ve added Remote Runbooks to RebootX, a mobile app for managing cloud and on-prem infrastructure, available on iOS and Android (freemium).<p>The idea is simple: when PagerDuty wakes you up, many incidents boil down to executing the same sequence of SSH commands or operational steps. Instead of opening a laptop, you can execute a predefined runbook directly from your phone.<p>Very usefyl when you&#x27;re on the go.<p>The scripts are retrieved from the server at `&#x2F;usr&#x2F;local&#x2F;sbin&#x2F;rebootx&#x2F;runbooks`, also via SSH. If a script is prefixed with `__` (2 underscores), it&#x27;s considered dangerous and the app warns you about it and ask for confirmation before executing it.<p>Some will argue that with the perfect infra, you don&#x27;t have to do all of this. By experience, none of us have the perfect infra so SSH-ing into the server (e.g VPS) is often required.<p>Happy to hear about your feedback or ideas of improvement.
