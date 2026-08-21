---
title: "Show HN: Proliferate- open-source, self-hostable Codex for any coding agent"
url: "https://github.com/proliferate-ai/proliferate"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-08-21T17:40:03Z"
metadata:
  score: "7"
---

# Show HN: Proliferate- open-source, self-hostable Codex for any coding agent

> Source: hackernews | Category: news | 2026-08-21T17:40:03Z

Score: 7 | Comments: 1

Hi HN- I&#x27;m Pablo, the founder of Proliferate!<p>Proliferate (<a href="https:&#x2F;&#x2F;github.com&#x2F;proliferate-ai&#x2F;proliferate" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;proliferate-ai&#x2F;proliferate</a>) is an open-source, self-hostable AI IDE that lets you work and automate tasks with Claude Code, Codex, OpenCode, Cursor, and Grok in one place.<p>Here&#x27;s a quick 2m demo of how we use Proliferate to build Proliferate: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=tGNX0oaWmBY" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=tGNX0oaWmBY</a><p>I started building Proliferate after my team onboarded to OpenAI Codex. Within days, we were using it for everything: using computer use instead of navigating websites ourselves, having Codex coordinate other agents, and setting up automations for recurring work. We really never needed to leave the desktop app to get work done.<p>If my team’s experience is anything close to representative, a Codex-like app (a horizontal agent with a beautiful UI) is the main interface every company is going to use to get work done. That is perfectly in line with OpenAI’s mission to make Codex the everything app (see: <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=47796469">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=47796469</a>).<p>But as we started automating work closer to the core of the business, I wanted to work with agents from all the labs, including open-weight models, without becoming increasingly dependent on OpenAI.<p>And that’s what Proliferate is for! It&#x27;s the open-source, self-hostable Codex that preserves your optionality across agents and model providers while building toward Codex’s breadth.<p>Today Proliferate supports:<p>* Working with Claude Code, Codex, OpenCode, Cursor, and Grok with their native inference and configuration options, including Bedrock, Azure, and self hosted inference.  
* Inter-agent communication and management: a parent agent can spawn and communicate with another supported agent as a subagent (I personally like to have Fable delegate to Codex, with OpenCode models reviewing PRs).  
* Building workflows- one of the features I&#x27;m most excited about. These are re-usable chains of agent sessions and human approval gates, with the harness and model chosen per step and documents passed between them. I use this to automate code review, QA, and my PR construction process.<p>All of Proliferate is 100% open source under AGPL-3.0. There are still definitely some rough spots, but we’re building fast and I’d really love any feedback!
