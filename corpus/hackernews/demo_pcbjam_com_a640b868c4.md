---
title: "Show HN: KiCad in the Browser"
url: "https://demo.pcbjam.com/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-05T14:38:37Z"
metadata:
  score: "25"
---

# Show HN: KiCad in the Browser

> Source: hackernews | Category: news | 2026-07-05T14:38:37Z

Score: 25 | Comments: 8

KiCad, a PCB EDA suite is now working in a browser, you can try it at the link, there&#x27;s a demo project or you can bring your own. Firefox is best, Chrome is good, Safari is &quot;working&quot;.<p>We’re Emergence Engineering, a dev shop from Hungary, mostly working with rich text editors, CRDTs. PCBJam started as my (Viktor, CTO, ex-electrical engineer) hobby project but as time went on I put more
and more energy into it, and a product started shaping up in my head, in the last few months we’ve started to focus on this project a bit more, and this is the first MVP~ish result.<p>This project is a ton of fun, ton of learning, ton of improvements over improvements:<p>- I thought there must be ways to emulate the PCB canvas OpenGL code on the web. And yes, there are a lot of ways, all of them very buggy. Turns out it’s faster to just write WebGL code that works with
KiCad’s Graphics Abstraction Layer if you add the right intermediate debugging steps. I (with Claude) implemented the features and compared them to native at every step, then the app loaded up the first 
time and just worked. I spent weeks hunting weird emulation bugs before that.<p>- There was an old wxWidgets web port as a starting point that helped a lot, bringing it up to the level KiCad needed is a long (and still ongoing) task. Thanks ahilss!<p>- Pthreads on the web: with Emscripten it’s possible to port multithreaded apps (used by DRC, software 3D renderer). A lot of Emscripten features (Asyncify, Pthreads, native exceptions) are in a war with each other, but it’s possible.<p>- Asyncify with native exceptions: Asyncify (used to make the WASM code suspend then call into the JS land, emulating blocking C++ calls by rewriting the WASM directly) is not compatible with native exceptions, even on the latest Binaryen version it can’t suspend inside catch arms. If you write a new Binaryen pass then it can, making the bundle 30-40% smaller and the app load in a second instead of 10.<p>- Optimizing bundle size is a fun game. We just moved Open CASCADE into a separate lazy-loaded WASM module, moving from 180 to 130 MB (24 MB brotli), still on -O1. -O2 &#x2F; -Oz etc will be more work than it
looks.<p>And a ton more problems like these above on a daily basis.<p>A few months ago I had a barely loading laggy pcbnew that crashed when you looked at it wrong, now we have the whole application working. I should say with quite a few bugs still, but now it feels pretty
close to native.<p>There’s a lot of built up knowledge &#x2F; code that we want to release as blogposts, mainline our changes to Binaryen &#x2F; KiCad &#x2F; wxWidgets, but I want to focus on the release first. Our wxWidgets port is quite 
close to the core, the KiCad is ~150 changed core files (mostly build scripts, some code changes too). The goal is to keep as close to the mainline as possible, and merge eventually.<p>We’ll have a free tier for sure and something around $30&#x2F;mo for bigger&#x2F;closed projects, optional paid AI integration &#x2F; self hosting &#x2F; enterprise features &#x2F; native &amp; mobile version down the line.<p>The goal is to build a product on top of KiCad (collaboration, AI integration, sharing, integrations), kind of like what Red Hat did with Linux back then. We’re heads down making it functional and have the
first version up in a ~month or so.<p>And of course we’re standing on the shoulders of the people who made KiCad &amp; wxWidgets and we want to give back and contribute as much as possible, if you have an idea on how to do that best let me know, I
released a few moderately successful open source projects, but I’ve never been a contributor. All of the front-end code is GPL (it has to be) and you can run this project if you want.<p>You can find the sources at: <a href="https:&#x2F;&#x2F;github.com&#x2F;emergence-engineering&#x2F;pcbjam" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;emergence-engineering&#x2F;pcbjam</a>.<p>Our company site is at:
<a href="https:&#x2F;&#x2F;emergence-engineering.com&#x2F;" rel="nofollow">https:&#x2F;&#x2F;emergence-engineering.com&#x2F;</a><p>Our crappy LP is at: 
<a href="https:&#x2F;&#x2F;www.pcbjam.com&#x2F;" rel="nofollow">https:&#x2F;&#x2F;www.pcbjam.com&#x2F;</a>
