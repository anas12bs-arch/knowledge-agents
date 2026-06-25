---
title: "Show HN: OpenKnowledge – open source AI-first alternative to Obsidian/Notion"
url: "https://github.com/inkeep/open-knowledge"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-06-25T20:22:18Z"
metadata:
  score: "58"
---

# Show HN: OpenKnowledge – open source AI-first alternative to Obsidian/Notion

> Source: hackernews | Category: news | 2026-06-25T20:22:18Z

Score: 58 | Comments: 22

Hi HN, Nick here. We’re launching OpenKnowledge (<a href="https:&#x2F;&#x2F;openknowledge.ai&#x2F;" rel="nofollow">https:&#x2F;&#x2F;openknowledge.ai&#x2F;</a>), a “what you see is what you get” markdown editor that has direct integrations with Claude, Codex, and Cursor. Available as MacOS app or CLI. Fully free&#x2F;local and OSS (<a href="https:&#x2F;&#x2F;github.com&#x2F;inkeep&#x2F;open-knowledge" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;inkeep&#x2F;open-knowledge</a>).<p>We built this because we wanted a “Google docs” like experience for writing and sharing markdown files across our team. Obsidian is the best alternative we tried, but found it doesn’t have a true “what you see is what you get” UI and it didn’t integrate well with Claude&#x2F;Codex outside of community plugins.<p>So we built OpenKnowledge. It takes shape as:<p>1. A MacOS app with a file navigator, the WYSIWYG editor, and link explorer.<p>2. Integrations with the Claude, Codex, and Cursor desktop apps. The agents can open an OpenKnowledge editor within their embedded web browsers for a side-by-side experience.<p>3. Built-in mcps, skills, and RAG for LLM-wiki and “AI Second Brain” scenarios + spec writing<p>4. An embedded terminal and CLI for TUI-first users<p>OSS stack includes: Tiptap&#x2F;prosemirror, CodeMirror, yjs (CRDT), Electron (MacOS app), Orama, remark&#x2F;rehype&#x2F;micromark&#x2F;mdast, @pierre&#x2F;trees<p>On the architecture side, the interesting eng. challenges included:<p>1. A pipeline to convert ProseMirror to markdown in a bidirectional lossless way. ProseMirror uses ASTs, which are not designed to have byte-fidelity.<p>2. A dual-observer CRDT to keep the ProseMirror and markdown state in-sync.<p>The CRDT + git also power a collaborative experience that shows what Agents are doing in the markdown, have undo&#x2F;redo, and version history. The “Share” and cloud-sync functionality are geared for team collaboration. They feel “no-code” but leverage git&#x2F;GitHub under the hood, which also means data stays fully private.<p>In that spirit, we made OpenKnowledge open source for anybody who’s curious or who’d like to contribute.<p>We’re actively thinking about plugins&#x2F;extensibility and what’s next. If you have suggestions or feedback, would love to hear it.
