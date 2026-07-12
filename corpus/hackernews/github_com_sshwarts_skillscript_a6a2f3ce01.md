---
title: "Show HN: Skillscript – A declarative, sandboxed language for tool orchestration"
url: "https://github.com/sshwarts/skillscript"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-12T16:12:52Z"
metadata:
  score: "5"
---

# Show HN: Skillscript – A declarative, sandboxed language for tool orchestration

> Source: hackernews | Category: news | 2026-07-12T16:12:52Z

Score: 5 | Comments: 1

Hi HN — I&#x27;m Scott. Skillscript is a small language I built to write what I want my local agent to actually do, in a form I can read and version, instead of hoping the model gets it right each time.<p>The itch started with something small. I wanted my NanoClaw agent to run my morning brief the same way every day. Check overnight tickets, summarize the deploy pipeline, flag anything urgent. Every session, it would re-figure out how to do this from scratch, drift a little, and cost tokens for what&#x27;s basically a fixed procedure. I could put it in a system prompt or an MD skill file, but those are still instructions the model reads and reasons about every time. And I wanted it to run autonomously and then hand it to the model to reason over the data.<p>The second thing that pushed me: I wanted to use small local models for the cheap stuff. They&#x27;re capable, but if you just hand them the wheel, they wander. What I wanted was a way for the frontier model (or me) to write a specific procedure and hand it to the local model to execute, not interpret. The skillscript is the program; the model is the runtime.<p>Skillscript is that. A skillscript is a text file with named steps, variables, conditions, and calls out to tools (MCP connectors, a local model, and shell commands from an operator allowlist). It&#x27;s deliberately minimal — no eval, no arbitrary imports, no subprocess, no unbounded loops. Bounded language, limited potential for damage. Everything a skillscript can do is in the file. You read it and know.<p>Where it is: pre-1.0 (0.30), MCP-native, self-hosted. Rough edges I know about: first-run setup takes more steps than it should, some of the grammar is still moving, and the local model integration currently assumes Ollama. It works well enough that I use it every day, but I wouldn&#x27;t necessarily call it production-ready.<p>- Repo: [<a href="https:&#x2F;&#x2F;github.com&#x2F;sshwarts&#x2F;skillscript" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;sshwarts&#x2F;skillscript</a>](<a href="https:&#x2F;&#x2F;github.com&#x2F;sshwarts&#x2F;skillscript" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;sshwarts&#x2F;skillscript</a>)<p>- Site: [<a href="https:&#x2F;&#x2F;skillscript.ai" rel="nofollow">https:&#x2F;&#x2F;skillscript.ai</a>](<a href="https:&#x2F;&#x2F;skillscript.ai" rel="nofollow">https:&#x2F;&#x2F;skillscript.ai</a>)<p>- Docs: [<a href="https:&#x2F;&#x2F;skillscript.mintlify.app&#x2F;docs" rel="nofollow">https:&#x2F;&#x2F;skillscript.mintlify.app&#x2F;docs</a>](<a href="https:&#x2F;&#x2F;skillscript.mintlify.app&#x2F;docs" rel="nofollow">https:&#x2F;&#x2F;skillscript.mintlify.app&#x2F;docs</a>)<p>- npm: `skillscript-runtime`<p>I&#x27;d welcome critique on two things especially: the language design (is it too small? too big? wrong shape?) and the trust model around agent-authored skills. What would you want to see before you trusted this on your own machine?
