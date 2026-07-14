---
title: "Show HN: Hackney – Compare Uber, Lyft, Waymo, and Robotaxi Prices"
url: "https://hackney.app/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-14T00:05:17Z"
metadata:
  score: "8"
---

# Show HN: Hackney – Compare Uber, Lyft, Waymo, and Robotaxi Prices

> Source: hackernews | Category: news | 2026-07-14T00:05:17Z

Score: 8 | Comments: 10

I created an app that compares real-time prices and wait times across Uber, Lyft, Waymo, Tesla Robotaxi, Curb, and Empower. It shows you all ride options in one list, then once you’re ready to book, it deeplinks you to the provider’s app with the route pre-filled.<p>I reverse-engineered ride-hailing mobile apps to understand how they fetch prices from their servers. You sign in to my app with your ride-hailing accounts, and then my app requests live prices from the same APIs that ride-hailing apps use. Importantly, my app is built using an on-device approach: the app on your phone stores authentication tokens locally and sends network requests directly to each ride-hailing company’s servers. This keeps your accounts private. I wrote a blog post showing network requests sent by my app, which you can verify yourself: <a href="https:&#x2F;&#x2F;blog.hackney.app&#x2F;p&#x2F;how-hackney-works" rel="nofollow">https:&#x2F;&#x2F;blog.hackney.app&#x2F;p&#x2F;how-hackney-works</a><p>This seems like an obvious app. Why doesn’t it already exist? That’s because most ride-hailing companies don’t offer public APIs for prices and wait times. Uber does offer one, but they prohibit using it for price comparison. When someone built a comparison app using the official API, Uber terminated their API access (<a href="https:&#x2F;&#x2F;www.benedelman.org&#x2F;news-053116" rel="nofollow">https:&#x2F;&#x2F;www.benedelman.org&#x2F;news-053116</a>). There are apps today that don’t use official APIs, but they run your account tokens through their servers and send price requests server-side.<p>To integrate a ride-hailing provider, my app sends network requests for sign-in, token refresh, ride prices, and ride history (to power a feature that shows you unified ride history across apps and how much you’ve saved on each ride). Some ride-hailing apps implement certificate pinning to prevent you from viewing their network requests, and some communicate with their server using Protobuf, a data format that doesn’t include the original field names. Building an app using this approach is technically complex, but it makes possible all sorts of useful products that couldn’t otherwise exist.<p>The app is completely free. In the future, I may monetize through a subscription or partnerships with ride-hailing companies. I’d love to hear your feedback. You can download it today.<p>iOS: <a href="https:&#x2F;&#x2F;apps.apple.com&#x2F;us&#x2F;app&#x2F;hackney-compare-rideshares&#x2F;id6754620049">https:&#x2F;&#x2F;apps.apple.com&#x2F;us&#x2F;app&#x2F;hackney-compare-rideshares&#x2F;id6...</a><p>Android: <a href="https:&#x2F;&#x2F;play.google.com&#x2F;store&#x2F;apps&#x2F;details?id=app.hackney">https:&#x2F;&#x2F;play.google.com&#x2F;store&#x2F;apps&#x2F;details?id=app.hackney</a>
