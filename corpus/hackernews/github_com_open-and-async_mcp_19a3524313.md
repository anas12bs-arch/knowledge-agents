---
title: "Show HN: An MCP server that turns async-work practices into tools"
url: "https://github.com/open-and-async/mcp"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-22T03:30:55Z"
metadata:
  score: "14"
---

# Show HN: An MCP server that turns async-work practices into tools

> Source: hackernews | Category: news | 2026-07-22T03:30:55Z

Score: 14 | Comments: 4

More than a decade ago, I adopted the self-imposed rule, if I answer a question more than once, the third time I need to be able to answer with a URL. Today, I published one very large URL - a book distilling what I learned from helping people work remotely at GitHub, and I wanted to rethink my rule for the age of AI.<p>What if, instead of a URL, I could create an interactive experience that could tailor the guidance to your particular situation?<p>What I ended up building was an Open and Async Advisor MCP server. To install (in claude or any other AI):<p>&gt; claude mcp add open-async -- npx -y @open-and-async&#x2F;mcp<p>Transparently, yes, it&#x27;s from a book I wrote which launched today, but the MCP server is open source and free to use. No purchase required. It knows the key principles of the book, and has specialized tools like `draft_decision_doc`, `convert_meeting_to_async`, `score_status_update`, `triage_sync_vs_async`.<p>This is an experiment for me, and I&#x27;m genuinely curious if it&#x27;s helpful for others.
