---
title: "Show HN: Watches user sessions, finds bugs that matter, and fixes them"
url: "https://github.com/opslane/opslane"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-08-28T12:19:02Z"
metadata:
  score: "26"
---

# Show HN: Watches user sessions, finds bugs that matter, and fixes them

> Source: hackernews | Category: news | 2026-08-28T12:19:02Z

Score: 26 | Comments: 4

Hey HN,<p>I’m Abhishek. I&#x27;m building Opslane, an open-source agent that identifies user-facing issues and investigates them. It only creates a PR if it can verify the fix.<p>Demo: <a href="https:&#x2F;&#x2F;youtu.be&#x2F;ccuOTYQMeYg" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;ccuOTYQMeYg</a>
Docs: <a href="https:&#x2F;&#x2F;docs.opslane.com">https:&#x2F;&#x2F;docs.opslane.com</a><p>At my last job at Robinhood, we used to do a quarterly bug bash. We would go through our Sentry backlog and try to fix as many of them as possible. We only fixed bugs we knew were reported by customers. We had hundreds of bugs, and Sentry’s default priority levels made no sense. After the bug bash, we would declare bankruptcy - select all remaining bugs and mark them as resolved.<p>This problem has only gotten worse since coding agents have become more prevalent.<p>So I started thinking: what would Sentry look like if it were built in 2026?<p>To me, error trackers have two failure modes:<p>1. False positives: They show you thousands of errors, and you can’t tell the impact on the user<p>2. False negatives: Many user-facing issues don’t throw exceptions, so they go unnoticed.<p>Opslane combines error tracking and session recording. And there is an agent that acts on both. To get started, you install the Opslane SDK. It captures everything the user did: errors, console logs, network requests, and session recordings.<p>Opslane reduces false positives by ranking issues based on how many users are facing a particular issue. It also learns about your product by reading your code and watching your session recordings.<p>False negatives are harder. Opslane reviews session recordings to spot frustration. They look for rage clicks, dead clicks, and abandoned forms.<p>This recently caught a bug in an early customer’s onboarding flow: a dropdown that closed itself when clicked. No exception, no bug report. The recordings showed users clicking it, selecting nothing, and dropping out of onboarding. Opslane flagged it and the team fixed it.<p>Three guiding principles when building Opslane:<p>1. Open Source: Self-host with one Docker Compose file.<p>2.Agent-first: I never want to open an error dashboard again. Opslane ships an MCP server, so you can ask &quot;what broke for users this week&quot; from Claude Code. You get back issues that need your attention and you drive the resolution.<p>3. It knows about your product: Opslane is continuously learning about your product. Every investigation begins with what it knows about your product.<p>It’s early. Frontend apps work end to end today.I am currently focused on improving reliability and accuracy.<p>Here is a link to our repo: <a href="https:&#x2F;&#x2F;github.com&#x2F;opslane&#x2F;opslane" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;opslane&#x2F;opslane</a><p>Would love to get feedback from folks on our approach to this problem!
