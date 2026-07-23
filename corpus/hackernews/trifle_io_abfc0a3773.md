---
title: "Show HN: Trifle – Open-source analytics that stores answers, not events"
url: "https://trifle.io/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-23T20:04:25Z"
metadata:
  score: "14"
---

# Show HN: Trifle – Open-source analytics that stores answers, not events

> Source: hackernews | Category: news | 2026-07-23T20:04:25Z

Score: 14 | Comments: 0

Trifle is an open-source time-series analytics library that aggregates nested counters instead of storing raw events. All in the database you already have. After rebuilding it twice over 10 years, it now tracks ~1B events a day at my day job.<p>It started in 2015 as my own Rails APM. I plugged into ActiveSupport::Notifications, got a few small users, and one bigger one whose scraping app broke everything. That sparked the core idea: aggregate counters into pre-defined time buckets, so a single write increments multiple buckets at once. The APM eventually faded away without much traction.<p>Later in 2021 I needed analytics at my day job. Instead of going for something out there I revised the idea of Trifle as a more generic analytics library, borrowing some data warehouse ideas. First used Redis, then Postgres, eventually MongoDB. Hence why Trifle::Stats comes with multiple drivers that keep the DSL unified while storage layer changes with your needs. In our case (huge write volume, some reads) PG read faster but slowed on large writes.<p>The nested values are the whole trick here. Single:<p><pre><code>  Trifle::Stats.track(
    key: &#x27;requests::aws::s3_uploads&#x27;,
    values: {
      count: 1,
      status: { request.response_code =&gt; 1 },
      size: payload.bytes,
      duration: { sum: request.duration, count: 1 }
    }
  )
  </code></pre>
builds up counts for requests, success rate, result status codes, duration for multiple time buckets at once. Single bucket from 2am then looks like:<p><pre><code>  { count: 14, status: { 200: 12, 500: 2 }, size: 5628341, duration: { sum: 43, count: 14 } }
</code></pre>
If request.duration is in seconds, then sum stored under duration would be in seconds as well.<p>Success rate is never stored, but it is calculated by dividing 200s over total number of requests. Same with average duration: sum over count. You ask for a metrics key, granularity and timeframe and you get back aggregated values at each point. Ready for charts or to answer &quot;Average response time over last 30 days&quot;.<p>There&#x27;s a Series wrapper for aggregating and formatting values for charts in a simple call. And as building dashboards is not as much fun for other devs as I thought, I built Trifle App - a visual layer with dashboards, scheduled digests and alerts. It&#x27;s written in Elixir, so I ported the library to Elixir too. And later to Go for a CLI. All three are compatible, write in one and read in another.<p>Today we track activity from over 100M background jobs a day which turns into about 1B events. It runs surprisingly cheap when you&#x27;re willing to trade some safety away (turn off journaling and write concerns in Mongo). 3-node Hetzner MongoDB cluster where the primary does 20% utilization costs us around $1k&#x2F;month.<p>It has its limitations. Payloads can&#x27;t hold tens of thousands of keys. Documents becomes too large to update efficiently. Some planning ahead is needed. And then there are no dimensions. Sometimes you can nest them (country - there are only so many countries), sometimes it&#x27;s better to have dedicated metrics key per dimension (customer - growing forever). That multiplies tracked events, hence 1B events from 100M jobs.<p>The libraries are MIT. The App is source-available under ELv2 - free to self-host and paid cloud if you want it managed. I build this on the side with no investor money to burn on a free service.<p>Happy to answer anything about architecture, storage models, my failures or why I didn&#x27;t give up on this yet.
