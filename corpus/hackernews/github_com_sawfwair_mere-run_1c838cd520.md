---
title: "Show HN: Local text, image, video, music and 3D from one CLI, no Python"
url: "https://github.com/sawfwair/mere-run"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-30T22:40:29Z"
metadata:
  score: "9"
---

# Show HN: Local text, image, video, music and 3D from one CLI, no Python

> Source: hackernews | Category: news | 2026-07-30T22:40:29Z

Score: 9 | Comments: 1

Hi HN! I&#x27;m the author of mere.run a local first inference runtime built around an installable CLI. I believe that whenever possible we should use the stuff we already own (like our Mac laptops, decent machines gathering dust, our gaming PC) and the limited electrical power we have easy access to, like the socket in the wall next to most of us. We shouldn&#x27;t have to send our data to the cloud hoping some T&amp;C will prevent it from being used in a way that we&#x27;d regret. Most of the local AI solutions are technical, involved, and land a curious body in some package hell. People are optimizing for one system and not another, the fun stuff is on PC if you own a Mac, and on Mac if you own a PC.<p>So mere.run was my choice to begin to patch many of those things that I saw as problematic. Text, chat, code, image gen, speech tts+asr, vision (caption&#x2F;ground&#x2F;segment&#x2F;track&#x2F;pose&#x2F;depth&#x2F;face&#x2F;OCR&#x2F;etc), music, sfx, video, 2d-&gt;3d, persistent worlds, lora training plus a few more things I am probably forgetting all in one place to work the way you work, with a scriptable CLI, an openAI compatible serve, and optionally a native app on Mac.<p>It&#x27;s native swift on MLX, no python, PyTorch, diffusers for inference. For text lanes with GGUF it uses llama.cpp and for a&#x2F;v muxing its FFmpeg.  Most upstream releases that don&#x27;t have an MLX variant are converted offline and hosted on huggingface. All release packages are built for arm64 (Mac &amp; Cuda) plus x86. They&#x27;re signed and ship SHA256SUMS. No windows at the moment.<p>&gt; mere.run model capabilities --recommended # That inspects your machine before recommending to prevent pulling models that don&#x27;t fit your spec<p>There&#x27;s a workflow layer with typed, validated graphs so you can create immutable job bundles and run them locally, over an ssh executor or using a fleet of machines and the relay service. (It&#x27;s hosted at relay.mere.run and is currently invite only while I test, but its also totally open MIT so you can set it up yourself)<p>The whole runtime is MIT along with the companion packages, models carry their own licenses and the CLI makes it clear when something has specific terms. Once you&#x27;ve pulled the models, everything works fully offline.<p>I&#x27;ve been working on a (hopefully) comprehensive docs -&gt; <a href="https:&#x2F;&#x2F;docs.mere.run" rel="nofollow">https:&#x2F;&#x2F;docs.mere.run</a><p>No account, no API key, no analytics or phone home.  Any network calls in the source are all at your request only like huggingface.co (models), GitHub.com (Pi install).<p>I&#x27;m just getting started, but it&#x27;s finally at the point I&#x27;d love feedback, contributions, and just folks to generally find it useful.  I hope it helps you make things and explore what&#x27;s possible with the stuff you&#x27;ve already got in your home.<p>Would love any thoughts, questions, ideas and maybe a star if you do that kinda thing.<p>-Kyle
