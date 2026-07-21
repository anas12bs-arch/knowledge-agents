---
title: "Show HN: Browser Tools SDK – an optimal browser harness for agents"
url: "https://libretto.sh/browser-tools"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-21T23:06:52Z"
metadata:
  score: "7"
---

# Show HN: Browser Tools SDK – an optimal browser harness for agents

> Source: hackernews | Category: news | 2026-07-21T23:06:52Z

Score: 7 | Comments: 1

We’re open-sourcing Browser Tools SDK: a small TypeScript package to give any AI agent a reliable way to control a real browser. With just a few lines of code, you can give any agent a production-ready browser harness<p><pre><code>  import { createAiSdkBrowserTools } from &quot;libretto-browser-tools&#x2F;ai-sdk&quot;;
  import { LocalBrowserProvider } from &quot;libretto-browser-tools&quot;;

  const { tools } = createAiSdkBrowserTools(new LocalBrowserProvider());

  const result = await generateText({
    model: anthropic(&quot;claude-sonnet-4-5&quot;),
    tools,
    prompt: &quot;Go to Hacker News and tell me the top story&quot;,
  });
</code></pre>
We built the Browser Tools SDK because access to a browser is one of the most important tools of a productive agent, but we found many of the existing tools lacking. Using the insights we gained building Libretto, we were able to build the SDK so that it’s significantly more context and cost-efficient than other tools:<p>We compared Browser Tools SDK against agent-browser, playwright-cli, and dev-browser on 26 live-site tasks with GPT 5.6 Sol (best results from 3 runs). Browser Tools tied for the best pass rate at 24&#x2F;26 and came in about 55% cheaper per successful task than the next alternative ($0.106 vs $0.235) while also using far fewer tokens (1.45M vs 2.29M+). Benchmark methodology is in the repo.<p>The Browser Tools SDK only exposes 6 tools, of which only 2 are really important: `browser_snapshot` and `browser_exec`. The snapshot tool was designed from the ground up to be extremely context-efficient and provide agents the overview they need to know what to try next. The exec tool takes and executes raw Playwright code, of which the models have been trained on heaps of, and know how to use without much direction.<p>Works with AI SDK and Pi out of the box, plus a custom path for anything else. More frameworks are coming soon. You can also use any browser infra provider (Libretto Cloud, Kernel, Browserbase, etc.) or use `LocalBrowserProvider` to run Chromium locally (although that will have less anti-bot protections).<p>MIT licensed. Check out the docs: <a href="https:&#x2F;&#x2F;libretto.sh&#x2F;docs&#x2F;browser-tools&#x2F;quickstart">https:&#x2F;&#x2F;libretto.sh&#x2F;docs&#x2F;browser-tools&#x2F;quickstart</a> and join the Discord: <a href="https:&#x2F;&#x2F;discord.gg&#x2F;NYrG56hVDt" rel="nofollow">https:&#x2F;&#x2F;discord.gg&#x2F;NYrG56hVDt</a>.<p>We’d love any and all feedback.
