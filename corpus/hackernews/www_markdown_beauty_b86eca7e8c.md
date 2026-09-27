---
title: "Show HN: Building a Markdown editor for Mac, iOS and web"
url: "https://www.markdown.beauty/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-09-27T19:09:32Z"
metadata:
  score: "39"
---

# Show HN: Building a Markdown editor for Mac, iOS and web

> Source: hackernews | Category: news | 2026-09-27T19:09:32Z

Score: 39 | Comments: 27

I&#x27;ve spent the last 10 months building Beauty: a local, powerful greco-roman Markdown editor where the page looks finished while you type. It runs on the Mac, iPhone and in the browser, and the browser version opens without an account: <a href="https:&#x2F;&#x2F;app.markdown.beauty" rel="nofollow">https:&#x2F;&#x2F;app.markdown.beauty</a><p>I was frustrated with writing apps, and like most I used Apple Notes. After 2+ years immersed in Cursor, Codex and CC, I wished some interactions existed in a text editor.<p>The Markdown renders in place as you write it, including tables (which you can drag and resize without lining up pipes), KaTeX math and Mermaid diagrams. A lot of thought went into typography and the writing experience.<p>Your notes on the Mac are plain .md files in a folder with images next to them, so they open in anything else too. Each note keeps 200 versions. If you share a note with a link it syncs peer to peer over WebRTC while someone has it open, and the server that connects you only ever sees a random room id.<p>Most of the ~1,000 commits went into the editor itself. It&#x27;s a contenteditable, and I don&#x27;t let the browser restructure the document at all, which was a lot more work than I expected. Building this to be performant and cross-platform required some novel approaches, which I&#x27;ll later open source. The editor is free with no account or ads, and there&#x27;s an optional subscription for sync through your own iCloud.<p><a href="https:&#x2F;&#x2F;www.markdown.beauty" rel="nofollow">https:&#x2F;&#x2F;www.markdown.beauty</a>
