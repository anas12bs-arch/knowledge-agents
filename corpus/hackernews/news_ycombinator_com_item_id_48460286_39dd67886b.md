---
title: "Show HN: Atlasphere – Live Infrastructure Diagrams"
url: "https://news.ycombinator.com/item?id=48460286"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-06-10T21:21:01Z"
metadata:
  score: "8"
---

# Show HN: Atlasphere – Live Infrastructure Diagrams

> Source: hackernews | Category: news | 2026-06-10T21:21:01Z

Score: 8 | Comments: 2

Hi HN. My name is Andrey. On a regular business day, I&#x27;m a software engineer working at AWS. Outside of work hours, I spend time on my hobby - writing code.<p>I was once building a pet project that allowed customers to spin up fully synchronized blockchain nodes within just a few minutes. The backend was split into a control plane and a data plane, each with its own AWS account. Later I added two more AWS accounts. One for shared RPC nodes. One for the Analytics Service.<p>Since I love to visualize things, I used drawio to visualize the architecture.<p>With time, I noticed a pattern. I&#x27;d write some code, add a few lambda functions, update my drawio diagram, write more code, introduce a few more resources, test things, see that everything works fine and go to sleep with a smile on my face. Next week I&#x27;d check my diagram, and shockingly, it&#x27;s missing some of the resources! This kept happening for a few more weeks until I decided to fully abandon the project until my infrastructure diagrams could stay in sync with my cloud account.<p>That&#x27;s how Atlasphere.io was born. I&#x27;ve been working on it for the past 6 months and I think the product is ready for some feedback :)<p>A few notes:<p>- Atlasphere uses a ReadOnly IAM role to scan your AWS account (my account reaches your account through a trust relationship).<p>- The number of services is currently limited (WIP)<p>- It&#x27;s a macOS app<p>- It&#x27;s NOT an Electron app, i use Rust + Webview<p>What am I looking for? All I really need is for someone to try the app and tell me what they like about it and what they absolutely hate about it, haha!<p>The website is <a href="https:&#x2F;&#x2F;atlasphere.io&#x2F;" rel="nofollow">https:&#x2F;&#x2F;atlasphere.io&#x2F;</a>
