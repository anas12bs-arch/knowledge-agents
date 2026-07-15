---
title: "Show HN: Low-latency local LLM runner via OpenJDK Panama FFM (Java 22)"
url: "https://github.com/projectargus-cc/libargus.cc"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-15T21:34:42Z"
metadata:
  score: "10"
---

# Show HN: Low-latency local LLM runner via OpenJDK Panama FFM (Java 22)

> Source: hackernews | Category: news | 2026-07-15T21:34:42Z

Score: 10 | Comments: 2

I wanted to run AI from inside the JVM. I started out with the standard REST sidecar, ripped that out to use Project Panama (Foreign Function &amp; Memory API) in the new JDK versions to interface directly with llama.cpp.  I still wasn&#x27;t happy with how that functioned, so I built libargus.cc to get a clean ABI to expose a structured API up in the JVM landscape. It still uses Project Panama to interface directly with llama.cpp, whisper.cpp, and ggml compute graphs.<p>I have zero-allocation on the hot paths, memory segments for prompts and tokens are allocated once inside confined Arenas.  Raw pointers pass straight through down to the low C level. This avoids primitive array cloning and heap churn.<p>I mapped out the native structures from llama.cpp and whisper.cpp while matching the compiler&#x27;s padding to maintain safe memory access.<p>I bundle pre-compiled native binaries in the jar for easy deployment.<p>This execution engine provides the foundation I need for work I&#x27;m doing on a spatio-temporal memory layer (L-TABB) to replace RAGs. I&#x27;d love to get technical feedback to polish any issues while I continue working on the next layer. 
Deep-dives from anyone hacking on Project Panama or low-latency systems in modern JDK would be very appreciated!<p>I&#x27;m much better with code than prose, so I&#x27;ll let the code do most of the talking.<p>Happy Hacking!
&#x2F;David<p>Code: <a href="https:&#x2F;&#x2F;libargus.cc" rel="nofollow">https:&#x2F;&#x2F;libargus.cc</a>
Project Landing Page: <a href="https:&#x2F;&#x2F;projectargus.cc" rel="nofollow">https:&#x2F;&#x2F;projectargus.cc</a>
