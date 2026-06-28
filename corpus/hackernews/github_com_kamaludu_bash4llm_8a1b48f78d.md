---
title: "Show HN: Bash4LLM+ – A lightweight, dependency-free Bash wrapper for LLM APIs"
url: "https://github.com/kamaludu/bash4llm/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-06-28T21:13:30Z"
metadata:
  score: "10"
---

# Show HN: Bash4LLM+ – A lightweight, dependency-free Bash wrapper for LLM APIs

> Source: hackernews | Category: news | 2026-06-28T21:13:30Z

Score: 10 | Comments: 5

Bash4LLM is a single-file Bash wrapper for interacting with LLMs from the terminal.  I created it because I wanted something simple that worked without installing Python, Node, or any other runtime.<p>It uses only Bash, curl, and jq. You can send prompts, start a small chat, process files line by line, stream output, and save session metadata in JSON format.<p>I tried to make it safe and predictable: no use of the system &#x2F;tmp, no use of eval. Groq is supported by default, and other providers can be added with dedicated Bash scripts in the extras&#x2F;providers&#x2F; folder.<p>Example:<p><pre><code>  echo &quot;explains the command: ls -l&quot; | .&#x2F;bash4llm</code></pre>
