---
title: "Show HN: Nectar, a Rust-like React that compiles to WebAssembly"
url: "https://buildnectar.com"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-12T20:11:32Z"
metadata:
  score: "14"
---

# Show HN: Nectar, a Rust-like React that compiles to WebAssembly

> Source: hackernews | Category: news | 2026-07-12T20:11:32Z

Score: 14 | Comments: 7

After a pretty rough gig experience, I wanted to remind myself that I was a vaguely capable developer. I had recently jumped on the Rust train and wanted a Rust equivalent of React that is more performant and easier to work with. I also wondered if I could effectively eject Javascript. This project came from that... Nectar is a programming language that compiles your entire app, logic, state, and rendering, to WebAssembly. JavaScript is reduced to a roughly 10 KB syscall layer that only bridges WASM to the DOM.<p>The origin: I set out to get React-style ergonomics with better performance, and about halfway in I realized I had hit the ceiling of what was possible going through the browser&#x27;s DOM (Blink&#x2F;C++) and a diffing step. So I stopped fighting it and built my own signal-driven rendering layer that compiles to WASM and updates exactly the DOM nodes that changed, in O(1), with no virtual DOM and no garbage collector.<p>What it is right now:<p>- One binary. The same compiler does formatting, linting, testing, a dev server, an LSP, and SSR (although SSR is underdeveloped).
- Fine-grained signals. Each binding updates on its own, so there is no diffing pass.
- A Rust-inspired borrow checker for compile-time safety.
- Language-level keywords for the patterns you reach for constantly on the web: component, store, router, form, auth, payment.
- SEO and Screen Readers. It compiles to two DOMs from the same source so the app stays visible to screen readers and crawlers.<p>Honest status, because this is early and it is mostly one person:<p>- The &quot;no JavaScript&quot; line has an asterisk. WASM cannot touch the DOM directly, so there is a small JS bridge (about 10 KB) that as of this moment I cannot overcome on major browsers. 
- The numbers on the site (a counter is ~10 KB versus ~387 KB for React plus JS) are real but small examples, not a full-app shootout. I would not read them as more than they are. They are intentionally poorly architected to measure throughput at massive scales. (contrived)
- License is BSL 1.1, so read that before you build anything real on it.<p>Live demo, 10,000 products with a canvas rendering engine, plus a side by side against Svelte 5:
<a href="https:&#x2F;&#x2F;buildnectar.com&#x2F;app&#x2F;canvas" rel="nofollow">https:&#x2F;&#x2F;buildnectar.com&#x2F;app&#x2F;canvas</a><p>Site: <a href="https:&#x2F;&#x2F;buildnectar.com" rel="nofollow">https:&#x2F;&#x2F;buildnectar.com</a>
Code: <a href="https:&#x2F;&#x2F;github.com&#x2F;HibiscusConsulting&#x2F;nectar-lang" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;HibiscusConsulting&#x2F;nectar-lang</a><p>I would genuinely like it torn apart. If the core bet is wrong, crush my dreams but tell me how we can make it better, please. I still am not completely sure this is even a good idea. I honestly thought this would be a lot easier to build than it has been. If I had known at the start, I would have never built it, but here we are.
