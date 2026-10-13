---
title: "Show HN: Stream live open data in two commands"
url: "https://docs.hypermass.io/docs/cli/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-10-13T22:00:15Z"
metadata:
  score: "8"
---

# Show HN: Stream live open data in two commands

> Source: hackernews | Category: news | 2026-10-13T22:00:15Z

Score: 8 | Comments: 1

A service and open source tool to get open data streams in two commands. No sign up needed for subscribing.<p>Streams to try:<p>- <a href="https:&#x2F;&#x2F;hypermass.io&#x2F;stream&#x2F;_J0fm450s" rel="nofollow">https:&#x2F;&#x2F;hypermass.io&#x2F;stream&#x2F;_J0fm450s</a> - extreme UV images of the sun from SOHO - visual data<p>- <a href="https:&#x2F;&#x2F;hypermass.io&#x2F;stream&#x2F;_ATtCoEK" rel="nofollow">https:&#x2F;&#x2F;hypermass.io&#x2F;stream&#x2F;_ATtCoEK</a> - GDACS live disaster data (filtered to just the ongoing items)<p>The CLI (Apache 2.0, <a href="https:&#x2F;&#x2F;github.com&#x2F;hypermass-io&#x2F;hypermass-cli" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;hypermass-io&#x2F;hypermass-cli</a>) tool allows you to subscribe to multiple live streams of files, with the files arriving in a local folder. The filenames are ULIDs so they can be easily sorted into time order in scripts and code. Publishing works similarly - drop files into a folder and they get read, published and deleted locally. The idea is that by being highly opinionated about the shape of the data (files, delivered in sequence, in real time) a bunch of the logic and edge cases get handled well in one place (things like ordering, retries, hash verification, reconnection, etc) - rather than requiring every subscriber to implement it themselves for every source.<p>A high-speed version for things like departure boards, train positions is in the pipeline.<p>Background: About 10 years ago, I worked for a few years supporting and developing some of the UK Rail Open Data systems. As a developer I was frustrated at how fragmented the open data space was, and how every open data system was designed as a blank-page exercise. I realised that a lot of data falls into an odd middle ground, too infrequent to economically poll on a large scale, too large for messaging protocols, but in some sense still real time. For example transport schedules, periodic solar imagery, disaster alerts - real-time but infrequent.<p>Fairly often I just wanted a &quot;just give me the data&quot; option when the solutions I found were static catalogues with no nod towards real-time use, bespoke APIs, analytics systems and other things I didn&#x27;t need. I couldn&#x27;t find a simple approach that leaned into what I saw as the data&#x27;s strengths (simple files, delivered in order, as&#x2F;when they are published) - so I built it.<p>About me: Solo founder based in the UK, full time for just over a year.<p>Sustainability: Initially a &quot;heavy users pay for more data allowance&quot; model with a decent free tier. Ideally we later shift to institutional publishers pay to keep their streams free to download. Possibly a paid data marketplace to support costs, but the main focus would always be the free and open data.<p>What I&#x27;d like to know:<p>- Does the CLI approach solve any real problems for you?<p>- Is the technical approach sane?<p>- Would you use a service like this to publish data?<p>- Recommendations to bootstrap users (particularly publishers)?
