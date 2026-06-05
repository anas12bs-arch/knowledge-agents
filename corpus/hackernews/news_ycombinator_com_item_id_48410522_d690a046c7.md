---
title: "Ask HN: Is Azure capacity this constraind or am I doing it wrong?"
url: "https://news.ycombinator.com/item?id=48410522"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-06-05T11:39:49Z"
metadata:
  score: "4"
---

# Ask HN: Is Azure capacity this constraind or am I doing it wrong?

> Source: hackernews | Category: news | 2026-06-05T11:39:49Z

Score: 4 | Comments: 3

I&#x27;m working with AWS for many years, and currently I&#x27;m working in product with suppose to be cloud agnostic.<p>I started with AWS and now it&#x27;s time to spin up it into Azure (because many enterprises using azure for some reason).<p>I started in US EAST region in azure and at beginning I had an issue with Postgres Flexible, raised a support ticket, and in the result they recommended me to move to another region. The overall conversation to say this takes about 1 day.<p>I&#x27;ve moved to US EAST 2, and after AKS deployment I stuck with vCPU (Standard Dasv7 Family vCPUs) quote (100) and here we go again... They send me the same message template as they do for previous ticket...<p>&gt; ...
&gt; Your ask for quota has been reviewed and backlogged at this time. It will be reviewed again when additional capacity becomes available. We do not have an ETA for when your request can be fulfilled but please be assured that we will continue working on it and update you as soon as we have more details to share and&#x2F;or process the request. 
&gt; ...<p>I&#x27;m already waiting for more then 1 day, and there is no responses from their support.<p>Long Story Short: Because I don&#x27;t want to wait for days, weeks and months to be able to test infrastructure on Azure. If it will be my decision I just stop and forget about this nightmare. Please suggest the regions and instance types with which I will not have issues.
