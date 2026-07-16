---
title: "Show HN: Libretto PR agents – Automatically fix failing playwright scripts"
url: "https://libretto.sh/debug-agents"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-16T22:14:10Z"
metadata:
  score: "8"
---

# Show HN: Libretto PR agents – Automatically fix failing playwright scripts

> Source: hackernews | Category: news | 2026-07-16T22:14:10Z

Score: 8 | Comments: 0

Libretto PR agents is a free TypeScript library for maintaining Playwright browser automations. Add one line of code to your existing Playwright scripts and it lets an agent automatically open GitHub PRs fixing the script when it fails.<p>A few months ago we released Libretto, a CLI + coding-agent skill for building deterministic browser automations. The idea was that for many browser workflows, especially repetitive business workflows, you don’t need an AI agent making decisions at runtime. You want deterministic Playwright scripts that are inspectable, faster to run, and much cheaper than repeatedly calling an AI browser agent.<p>That helped us generate Playwright and network-request-based scripts, but websites can often change which breaks deterministic scripts. So maintaining a variety of scripts at scale is a headache. If you already have a bunch of functioning Playwright scripts, the last thing you want is to rewrite everything around a new runtime AI framework like browser-use or stagehand just to make maintenance easier.<p>The Libretto PR Agent pulls your code from GitHub and connects via CDP to the browser session that just failed. It has an exec tool for injecting Playwright and javascript into the page, and once its inspected the failure, it opens a PR to your repo with a proposed code fix.<p>You use it like this:<p><pre><code>  try {
    await automationLogic(page);
  } catch (error) {
    await playwrightDebugger.debugFailure(error, page);
  throw error;
  }

</code></pre>
The agent is completely free and open source, lets you bring your own LLM provider API keys, and works with any browser provider (including self hosted).<p>The source code is here: <a href="https:&#x2F;&#x2F;github.com&#x2F;saffron-health&#x2F;libretto&#x2F;tree&#x2F;main&#x2F;packages&#x2F;playwright-debugger" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;saffron-health&#x2F;libretto&#x2F;tree&#x2F;main&#x2F;package...</a><p>We think this makes browser integrations much easier to maintain, especially for teams that already have Playwright browser automation scripts in production and don’t want a full migration to get AI-assisted debugging and repair.<p>If you’re maintaining browser automations in production, would love to know what your debugging flow is currently and any feedback on this approach.
