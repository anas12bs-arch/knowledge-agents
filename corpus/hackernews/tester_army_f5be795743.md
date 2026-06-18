---
title: "Launch HN: TesterArmy (YC P26) – Agents that test web and mobile apps"
url: "https://tester.army"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-06-18T19:58:14Z"
metadata:
  score: "72"
---

# Launch HN: TesterArmy (YC P26) – Agents that test web and mobile apps

> Source: hackernews | Category: news | 2026-06-18T19:58:14Z

Score: 72 | Comments: 33

Hey HN - we’re Oskar, Szymon, and Piotr, and we’re building TesterArmy (<a href="https:&#x2F;&#x2F;tester.army">https:&#x2F;&#x2F;tester.army</a>). TesterArmy is an agentic testing platform that runs end-to-end checks before deployment and in production. Instead of wasting hours on manual testing or maintaining static scripts, we let you specify your tests in natural language and handle everything in between. We&#x27;ve built the platform fully around agents. Our agent will reliably execute the tests, but your coding agent can manage everything in our platform, from defining tests in natural language to running them on your behalf.<p>Check out our demo video: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=291IkUbPrlk" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=291IkUbPrlk</a>.<p>We started TesterArmy because testing is still far too painful. AI coding tools have made it dramatically faster to write and ship code, but testing is still a bottleneck. Traditional E2E tests are slow to set up and expensive to maintain. Managing auth and test users is painful. Setting up staging environments is painful. Running tests reliably is painful.<p>We think most teams do not actually want to spend their time writing selectors or maintaining test infrastructure. They just want confidence that their core flows work. With TesterArmy, an engineer can sign up, give an agent our CLI, and let it handle creating tests and running them on schedule or on GitHub.<p>When something breaks, TesterArmy alerts your team through Slack or Discord.<p>Over the past few months, we scaled from 0 to 30+ teams using our product every day. We caught bugs in critical flows, including onboarding, checkout, and AI chat. We&#x27;ve got many of our customers migrating from already established competitors to us because of the quality and reliability of our agents.<p>Here are a few of the recent bugs that our agent found (there were quite a lot of them!):<p>1) Timezone bug that affected the booking flow in one of our clients&#x27; apps, the dashboard was very complex and hard to catch by a human. 
2) Regression in agent orchestration that caused a sandboxed environment to be stuck on loading, thanks to TesterArmy, the team was able to resolve it before it hit production.
3) Incorrectly counting the order amount in a complex dashboard flow with checkout, thanks to TesterArmy, the team was able to resolve it before it affected revenue
4) Catching a regression in an AI chat flow that would result in a user not being able to retrieve their data due to broken tool calling.<p>And many more, mostly related to some incorrect API calls, 404s, unhandled errors, etc.<p>If this sounds useful, we would love your feedback at <a href="https:&#x2F;&#x2F;tester.army">https:&#x2F;&#x2F;tester.army</a>. We have a bunch of free test runs for you to try. And don’t worry, we won’t make you do sales calls, and we don’t have long onboarding or annoying setup. Our goal is an it-just-works experience.<p>If you&#x27;re looking for an end-to-end testing solution, we&#x27;d love to hear your feedback!
