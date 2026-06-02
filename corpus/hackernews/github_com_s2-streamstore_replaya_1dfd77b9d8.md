---
title: "Show HN: RePlaya – self-hosted browser session replay with live tailing"
url: "https://github.com/s2-streamstore/replaya"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-06-02T22:13:31Z"
metadata:
  score: "33"
---

# Show HN: RePlaya – self-hosted browser session replay with live tailing

> Source: hackernews | Category: news | 2026-06-02T22:13:31Z

Score: 33 | Comments: 6

Hi HN, I&#x27;m one of the founders of s2.dev. RePlaya (<a href="https:&#x2F;&#x2F;github.com&#x2F;s2-streamstore&#x2F;replaya" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;s2-streamstore&#x2F;replaya</a>) is a self-hosted browser session replay tool using rrweb (<a href="https:&#x2F;&#x2F;github.com&#x2F;rrweb-io&#x2F;rrweb" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;rrweb-io&#x2F;rrweb</a>).<p>It occurred to me that a durable stream per session would be a much neater architectural foundation for much of what you&#x27;d want from such a tool. As a unique feature, it also made live tailing straightforward because the player can read from the same stream the recorder is appending to.<p>The alternative architecture is likely an ingest firehose which is then indexed, with associated complexity and latency. You&#x27;d have to string together multiple data systems like a message queue, a metadata database, and blob storage and&#x2F;or an OLAP database.<p>Here the only dependency is S2, which has an open source version you can self-host called s2-lite (<a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=46708055">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=46708055</a>).<p>How it works:<p>- one S2 stream per browser session<p>- large rrweb events (like a full snapshot) get framed across multiple binary S2 records and reassembled on read<p>- active sessions are tailed with an S2 read session, and bridged to the browser over SSE<p>- session listing relies on stream names encoding reverse timestamps, as S2 returns a lexicographic order listing<p>- relying on fencing tokens so a stopped session can&#x27;t be written to again by a late recorder<p>- retention and GC are handled via S2 stream config, so no background job needed<p>Curious to hear from folks on the tool or the stream-per-session model!
