---
title: "Show HN: The Goal is simple, there should be an actual free editor"
url: "https://sylixide.com"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-31T19:01:43Z"
metadata:
  score: "7"
---

# Show HN: The Goal is simple, there should be an actual free editor

> Source: hackernews | Category: news | 2026-07-31T19:01:43Z

Score: 7 | Comments: 0

Hey HN, I&#x27;m Saai, one of the creators of Sylix. I made this open-minded version of Cursor where you can get all of the core features of Cursor but in a fully customizable IDE (Ctrl+K, @docs, parallel agents). We love Cursor so much, but there are so many other features we&#x27;re building, including all things like multi-edit, parallel swaps, agent indexing (but not the traditional one), parallel LSP, or maybe... we might give agents a better understanding of the codebase via multi-semantic memory instead, alongside in-search grep for your system files or workspace. Sylix will be open source once it&#x27;s stable, but it&#x27;s a fully customizable tool we&#x27;ve been wanting!<p>Sorry for the delay; well, it&#x27;s almost a year now. Well, I know developers were waiting for this.<p>The hard part: we&#x27;re building Sylix not as a traditional fork of VS Code but as a mixer of all things; Sylix is built on top of Monaco Editor along with the Monaco Editor API, backed natively in Rust. The VS Code repo helps a lot, along with its great documentation about the src&#x2F;workbench files extension, but it&#x27;s great as we got into it pretty deep. Since we leveraged the monaco-vscode-api, it was easy for us to embed it nicely into our React code. So it was a pretty decent thing for adding a new feature alongside a new UI. For Sylix, all the core systems behind all things built in Rust are done; building just a little polish over the UI is a task since we are not UI designers,s though. Now two things left: a polished UI and the marketplace for Sylix, since we already figured out how we canroute then extension core; just the UI left. One thing we&#x27;re excited about is how we make things work out after trying over and over a VS Code fork, Void fork, and VS Code 1.58; after trying all those things, it finally works. It&#x27;s like this: maybe the 6th or 7th version of Sylix works for us.<p>The other benefit is that Sylix is going to be open source once it has a stable version, so we don&#x27;t need to hide our prompts from what we built. We let you use Cursor&#x27;s core features and functions right on your machine along with any of your existing subscriptions (like Codex, Claude Code, Kimi K3, DeepSeek) while we are working on it so that you can also use OpenCode Go as a provider. Sylix supports over 120+ models via your own providers; any model you want this lets you completely control your own data, and on-prem, a hosted model.<p>There is a lot to talk about: how we build, and full disclosure, we have passed most of the early phase and currently have around 43 developers using it with their own subscription... thank you to them; we have come so far through their feedback. But we&#x27;re super excited to cover the gap alongside Cursor.<p>Let us know if there is anything you want to see Cursor-style in an actual Free Editor. Or feel free to shoot us a message.
