---
title: "Show HN: NES Contra (1987) port (ASM –> C and then C –> WebAssembly)"
url: "https://epoyraz.github.io/nes-contra-us/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-10-31T23:35:31Z"
metadata:
  score: "32"
---

# Show HN: NES Contra (1987) port (ASM –> C and then C –> WebAssembly)

> Source: hackernews | Category: news | 2026-10-31T23:35:31Z

Score: 32 | Comments: 19

Based on vermiceli&#x27;s annotated disassembly of Contra: <a href="https:&#x2F;&#x2F;github.com&#x2F;vermiceli&#x2F;nes-contra-us" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;vermiceli&#x2F;nes-contra-us</a>. Thanks for the great work.<p>I ported it in two steps. First to C: the game logic is translated routine by routine from the 6502 assembly, and checked frame by frame against the original in the Mesen emulator. Then the C code to WebAssembly so it runs in the browser.<p>The cherry on top: online multiplayer, so two players can play co-op over the internet.<p>Source: <a href="https:&#x2F;&#x2F;github.com&#x2F;epoyraz&#x2F;nes-contra-us" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;epoyraz&#x2F;nes-contra-us</a>
