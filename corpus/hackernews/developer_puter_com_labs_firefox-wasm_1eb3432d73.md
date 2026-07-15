---
title: "Show HN: Firefox in WebAssembly"
url: "https://developer.puter.com/labs/firefox-wasm/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-15T21:34:41Z"
metadata:
  score: "7"
---

# Show HN: Firefox in WebAssembly

> Source: hackernews | Category: news | 2026-07-15T21:34:41Z

Score: 7 | Comments: 2

This is the entire Firefox browser rendering to a &lt;canvas&gt; element. Gecko, all UI components, and the Spidermonkey JS engine are all compiled and running in WebAssembly.<p>Here are a few things you might find interesting:<p>- This is fully end to end encrypted! We use the WISP protocol for TCP-over-websockets.<p>- There is a novel WASM-&gt;JS JIT for experimental site speedup<p>- This port cost over 25k in opus&#x2F;fable tokens for debugging and JIT research<p>This was just a fun experiment to push the boundaries of WebAssembly. For a more usable &quot;browser in browser&quot; experience, we also built <a href="https:&#x2F;&#x2F;github.com&#x2F;HeyPuter&#x2F;browser.js" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;HeyPuter&#x2F;browser.js</a> that eats a bit less RAM.
