---
title: "Show HN: I built a smart proxy so your coding agent can run loose"
url: "https://trollbridge.dev/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-15T14:24:38Z"
metadata:
  score: "7"
---

# Show HN: I built a smart proxy so your coding agent can run loose

> Source: hackernews | Category: news | 2026-07-15T14:24:38Z

Score: 7 | Comments: 5

The only way to go fast is full YOLO mode in your coding agent. I&#x27;ve got the local sandbox figured out (pro tip: Incus VMs work great) but I wanted to keep my agents from doing things like inadvertently blowing up my cloud services or chasing a prompt to POST to some random website. I struggle most with this on my side projects where my permission model isn&#x27;t quite as robust as it is at the office.<p>I started with a firewall on the Incus container but every time the agent needed access to something new, I was poking more holes in it - and it didn&#x27;t differentiate between HTTP verbs.<p>I&#x27;ve been using Claude Code auto mode too but I wanted to be able to guide the LLM, not just hand over control completely. I also want some flat allow and deny rules.<p>So, I built Trollbridge: an HTTP&#x2F;S proxy that runs in front of your coding agent and lets you set up allow or deny lists, realtime approve or deny in the TUI, or wire up an LLM that makes calls based on your prior decisions.<p>Would love to hear what you think - give it a shot, leave a comment, file a bug. Thanks!<p>Website: <a href="https:&#x2F;&#x2F;trollbridge.dev" rel="nofollow">https:&#x2F;&#x2F;trollbridge.dev</a>
Github: <a href="https:&#x2F;&#x2F;github.com&#x2F;dandriscoll&#x2F;trollbridge" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;dandriscoll&#x2F;trollbridge</a>
