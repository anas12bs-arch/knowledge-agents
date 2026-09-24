---
title: "Show HN: AgentRun: DSL to turn agents into workflows"
url: "https://github.com/Parcha-ai/agentrun"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-09-24T19:12:44Z"
metadata:
  score: "18"
---

# Show HN: AgentRun: DSL to turn agents into workflows

> Source: hackernews | Category: news | 2026-09-24T19:12:44Z

Score: 18 | Comments: 1

Hi HN,<p>I just open sourced the DSL that our harness in grep.ai uses to turn repeatable parts of agent work into workflows. You can combine tool calls, code, Jev-powered system one decisions for things like routing and screening evidence, and agents when a step needs more investigation.<p>Our harness uses the traces and retro notes agents leave behind when doing a job to figure out which parts can become a workflow. The idea is to make the work easier to understand and avoid paying for a full agent loop where one isn’t needed.
For example, a research workflow can split a question into subquestions, send agents to research them in parallel, use Jev to screen the evidence, and have another agent write the report. You can inspect the steps, evaluate the evidence screening separately, or change one agent without rebuilding everything.<p>The DSL and examples are in our GitHub. There’s a scripted demo you can run without API keys: <a href="https:&#x2F;&#x2F;github.com&#x2F;Parcha-ai&#x2F;agentrun" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;Parcha-ai&#x2F;agentrun</a><p>You can also use it as a Pi extension to build, inspect, and run workflows: <a href="https:&#x2F;&#x2F;github.com&#x2F;Parcha-ai&#x2F;agentrun#use-it-in-pi" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;Parcha-ai&#x2F;agentrun#use-it-in-pi</a><p>I would love to hear if this is useful to others.<p>More background on how AgentRun works in this video: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=vOVhtGjtwpg" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=vOVhtGjtwpg</a>. Or read about our use cases in this article: <a href="https:&#x2F;&#x2F;x.com&#x2F;MiguelriosEN&#x2F;status&#x2F;2101029313906987422" rel="nofollow">https:&#x2F;&#x2F;x.com&#x2F;MiguelriosEN&#x2F;status&#x2F;2101029313906987422</a>.
