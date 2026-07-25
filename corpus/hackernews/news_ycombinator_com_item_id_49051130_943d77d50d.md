---
title: "Show HN: Writemark, a dependency free web component for inline Markdown editing"
url: "https://news.ycombinator.com/item?id=49051130"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-25T22:07:50Z"
metadata:
  score: "8"
---

# Show HN: Writemark, a dependency free web component for inline Markdown editing

> Source: hackernews | Category: news | 2026-07-25T22:07:50Z

Score: 8 | Comments: 3

I like writing Markdown, but do not like writing it inside a plain textarea.<p>I wanted something I could use anywhere by dropping in a single web component:<p>```<p>&lt;writemark-editor name=&quot;body&quot;&gt;&lt;&#x2F;writemark-editor&gt;<p>```<p>That became Writemark.<p>It renders Markdown while you write, but Markdown remains the value you read, store, and submit. It also has source, split, and preview modes, along with slash commands, tables, task lists, code blocks, native form support, and an API for adding your own controls. There are no runtime dependencies and no required framework or built in toolbar.<p>It is fully vibecoded. The process was very iterative. I knocked something out, tried using it, found bugs, fixed them, and repeated that cycle until I had something I liked writing in and that performed reasonably well.<p>It did not begin as an experiment about AI generated software -- just did not want to use textareas anymore. I like Markdown, and I wanted one component that I could use anywhere without bringing along an entire editor framework.<p>It is still very young. The parser is handwritten, the component is essentially one large JavaScript file, and I am certain there are edge cases waiting to be found. If you find one, I am happy to fix it.<p>I have tried to give it a decent safety net. It currently has 951 Playwright checks across Chromium, Firefox, and WebKit, along with hostile input cases, sanitizer fuzzing, and differential tests against CommonMark.<p>I built this because I wanted it for myself, but I think it turned into something kind of cool. I hope some of you enjoy it. I would love hearing what you think, especially if you try it and manage to break something.<p>- Github: <a href="https:&#x2F;&#x2F;github.com&#x2F;Brostoffed&#x2F;writemark" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;Brostoffed&#x2F;writemark</a><p>- NPM: <a href="https:&#x2F;&#x2F;www.npmjs.com&#x2F;package&#x2F;writemark-editor" rel="nofollow">https:&#x2F;&#x2F;www.npmjs.com&#x2F;package&#x2F;writemark-editor</a>
