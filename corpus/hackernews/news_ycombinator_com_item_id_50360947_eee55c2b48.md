---
title: "Tell HN: Don't use Postman, they proxy your info without your permission"
url: "https://news.ycombinator.com/item?id=50360947"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-11-04T09:31:09Z"
metadata:
  score: "32"
---

# Tell HN: Don't use Postman, they proxy your info without your permission

> Source: hackernews | Category: news | 2026-11-04T09:31:09Z

Score: 32 | Comments: 1

When you send a POST request to your server, you think you&#x27;re sending the information to YOUR server, right? That was the default behaviour - as it should be. After updating the Postman client, I noticed Postman also sends the request to their internal servers, which then sends your server the actual request (proxying). I thought I was paranoid until another commenter confirmed the same (https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=50358055). It&#x27;s fucking annoying that something called POSTman does anything but that. Please don&#x27;t use Postman for anything sensitive. It&#x27;s borderline spyware, especially when you didn&#x27;t consent to this behavior.
