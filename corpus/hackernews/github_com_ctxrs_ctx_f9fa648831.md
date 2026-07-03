---
title: "Show HN: ctx – Search the coding agent history already on your machine"
url: "https://github.com/ctxrs/ctx"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-03T01:15:15Z"
metadata:
  score: "24"
---

# Show HN: ctx – Search the coding agent history already on your machine

> Source: hackernews | Category: news | 2026-07-03T01:15:15Z

Score: 24 | Comments: 7

Coding agents don&#x27;t have long-term memory.<p>But you do have months of full-fidelity agent transcripts stored on your machine.<p>A simple solution that goes a long way: ingest those transcripts and logs into a structured SQLite database, then search them with ranked text match. Everything is fully local and doesn&#x27;t require anything fancy like a graph database or hosted memory service.<p>This is the idea behind ctx, a Rust CLI that handles the ingestion and searching.<p>We give our agents a skill that tells them to reference past sessions before working in an area. Usually we do this through an &quot;Agent History Research Subagent&quot; whose job is just to prepare a short brief covering any relevant history before the task begins.<p>A real example: sometimes our test suite runs would fail because disk was full on the runner. The correct approach was to run the cleanup runbook, but the root cause of the failure was not clear to the agents, so they would think it was a test regression and go down the wrong rabbit hole debugging. When the agent searched history, it realized this failure had been encountered before and found the right workaround immediately. That got the agent onto the right cleanup path, and later we improved the log output so the same failure would be clearer next time. It&#x27;s a boring story, but it&#x27;s real agent productivity.<p>Another nice use case is quickly generating session transcripts for sharing. You can exclude the noisy intermediate messages, so the transcript shows the important parts of the session more cleanly. Try attaching a session transcript to your next PR so your teammate and their agent can review the provenance and prompting behind the change.<p>If you&#x27;re up for an additional challenge, ask your agent to &quot;exhaustively review all agent history in this repo and find where the SDLC is struggling or isn&#x27;t agent-native&quot;. Using past sessions to recursively improve the agentic SDLC is a loop that we&#x27;re using a lot today.<p>If you try it out, please let us know what you think!
