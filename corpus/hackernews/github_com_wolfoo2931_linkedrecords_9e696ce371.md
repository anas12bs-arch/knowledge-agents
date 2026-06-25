---
title: "Show HN: Write SaaS apps where users control where their data is stored"
url: "https://github.com/wolfoo2931/linkedrecords/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-06-25T05:37:25Z"
metadata:
  score: "29"
---

# Show HN: Write SaaS apps where users control where their data is stored

> Source: hackernews | Category: news | 2026-06-25T05:37:25Z

Score: 29 | Comments: 3

Hello HN,<p>I would like to share with you linkedrecords.com - an open source backend as a service I&#x27;m working on since some time now. You can think of it as an firebase&#x2F;convex alternative with an interesting twist.<p>In 2018 I needed to write large software requirements&#x2F;architecture documents in Google Docs. While I was annoyed by the limitations of Google Docs back then (no captions on figures, no automatic heading numbering, slow when docs are bigger,...) I was still fascinated by the real time collaboration features of it. So I&#x27;ve started a quest to understand how it works and I begun to implement an alternative to Google Docs.<p>I was convinced that this kind of real time collaboration is the future so I&#x27;ve given it much thought how I could make this as generic as possible so I could use it in all future tools I would build.<p>In the same time I was playing around with firebase (surprisingly you can not build a google docs alternative with firebase that easy as their real time collaboration does not provide merging text but rather just JSON). And back then I was also convinced that backend as a service is the right way to go. I was thinking that one of the most important reason we were still writing custom backend code is because of authorization.<p>I also was faced with another problem when trying to make the backend as generic as possible: relations between entities are also domain specific. E.g. A Documents can have many comments.<p>Luckily I was intrigued by another concept back in 2018 it was called web 3.0. Back in 2018 this had nothing to do with crypto. It was used as a term to refer to the semantic web and the resource description framework as one of its standards. There are also some RDF implementations which I could have reused but they are all XML and mostly Java based. I needed something light. Instead of implementing my own RDF product I took the idea of the RDF triplestore and came up with my own interpretation of it.<p>Using concepts like: triplestores and schema-on-read, I came up with a system that does not has any business logic in its backend and while working on my Google Docs alternative I felt in love with it as I&#x27;ve discovered some properties I did not anticipated from the get go:<p>- Dealing with global state in react is very easy. It feels like you use an SQL client in your browser and all queries are reactive and always up to date. When writing a query you do not have to think about authorization it&#x27;s all backed in.
- Because the backend is 100% free of domain specific code you can point your single page app to any linkedrecords deployment.
- You never have to write backend code
- Its quite efficient when using AI agents<p>The best way to experience it, is to follow this little tutorial: <a href="https:&#x2F;&#x2F;linkedrecords.com&#x2F;getting-started&#x2F;" rel="nofollow">https:&#x2F;&#x2F;linkedrecords.com&#x2F;getting-started&#x2F;</a><p>It takes a while to get a hang of it so you have to have an open mind.<p>I would love to read your feedback on this.
