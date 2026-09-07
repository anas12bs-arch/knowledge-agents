---
title: "Apparently CodePen 2.0 sends data to their servers as you type"
url: "https://news.ycombinator.com/item?id=49596976"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-09-07T16:01:52Z"
metadata:
  score: "78"
---

# Apparently CodePen 2.0 sends data to their servers as you type

> Source: hackernews | Category: news | 2026-09-07T16:01:52Z

Score: 78 | Comments: 37

They send all typed into editor input to codepen.dev almost immediately (you would see in 1-2 sec after you typed your secret that it appears in respective Network&#x2F;Response tab) even before one saved it. I tested this with a unique marker: after typing it into index.html, CodePen ran a build with &quot;save:false&quot;, and the marker then appeared verbatim in the HTML served from the generated &quot;*.codepen.dev preview&quot;. Thus, if you ever entered some secrets in there by mistake consider them compromized even if you did not publish&#x2F;save the pen
