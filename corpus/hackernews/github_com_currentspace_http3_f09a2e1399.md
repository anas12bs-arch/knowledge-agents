---
title: "Show HN: HTTP/3 and raw QUIC client/server APIs for Node.js"
url: "https://github.com/currentspace/http3"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-06-08T21:25:14Z"
metadata:
  score: "6"
---

# Show HN: HTTP/3 and raw QUIC client/server APIs for Node.js

> Source: hackernews | Category: news | 2026-06-08T21:25:14Z

Score: 6 | Comments: 0

I built this because I wanted to make outbound and accept inbound HTTP&#x2F;3 and raw QUIC connections from ordinary Node.js code, without building Node from source or putting everything behind a reverse proxy.<p>Repo: <a href="https:&#x2F;&#x2F;github.com&#x2F;currentspace&#x2F;http3" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;currentspace&#x2F;http3</a> 
npm: <a href="https:&#x2F;&#x2F;www.npmjs.com&#x2F;package&#x2F;@currentspace&#x2F;http3" rel="nofollow">https:&#x2F;&#x2F;www.npmjs.com&#x2F;package&#x2F;@currentspace&#x2F;http3</a><p>It’s a native package around Rust&#x2F;quiche. It supports both client and server APIs, I&#x27;m using it in a couple of projects: creating raw QUIC streams, datagrams, custom ALPN, session behavior, and HTTP&#x2F;3 client work from Node.<p>I&#x27;ve tried to be very safe in the native code, written in rust, with proofs around the parts I was most concerned about getting wrong. I have it hosting a couple of sites as HTTP3 endpoints and found it working well.
