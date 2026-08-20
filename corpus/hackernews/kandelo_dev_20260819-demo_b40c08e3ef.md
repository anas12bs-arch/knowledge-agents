---
title: "Show HN: Kandelo – a POSIX-compatible multi-process WASM kernel for the browser"
url: "https://kandelo.dev/20260819-demo/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-08-20T19:24:00Z"
metadata:
  score: "6"
---

# Show HN: Kandelo – a POSIX-compatible multi-process WASM kernel for the browser

> Source: hackernews | Category: news | 2026-08-20T19:24:00Z

Score: 6 | Comments: 2

Kandelo is an open-source, Wasm-based multi-process kernel that runs POSIX programs in browsers and Node.js.<p>Kandelo is still experimental, but it already runs a substantial range of existing software.<p><i>Do you have use cases for this?</i><p>We are trying Kandelo as a new foundation for WordPress Playground which runs server-side WordPress entirely in the browser. Kandelo also looks promising as a sandbox for running agents in the the browser and on the command line. On the side, we&#x27;ve been playing with porting games and desktop environments and even compiling runnable programs within Kandelo.<p>Yet it feels like there are many possibilities we haven&#x27;t considered.<p>How would you like to use something like this?<p><i>Demos:</i><p>Some notes: The demos have been tested in desktop browsers. Unfortunately, YMMV on mobile today. Some of the disk images are large (~50MB) and may take a while to boot initially.<p>Main set, with Shell (bash, vim, nethack, and more), Nginx, PHP, WordPress, and Doom:
<a href="https:&#x2F;&#x2F;kandelo.dev&#x2F;20260819-demo&#x2F;" rel="nofollow">https:&#x2F;&#x2F;kandelo.dev&#x2F;20260819-demo&#x2F;</a><p>LÖVE game engine:
<a href="https:&#x2F;&#x2F;kandelo.dev&#x2F;20260819-demo-love&#x2F;" rel="nofollow">https:&#x2F;&#x2F;kandelo.dev&#x2F;20260819-demo-love&#x2F;</a><p>SNKRX running under LÖVE:
<a href="https:&#x2F;&#x2F;kandelo.dev&#x2F;20260819-demo-love&#x2F;?vfs=love-snkrx-abi44.vfs.zst" rel="nofollow">https:&#x2F;&#x2F;kandelo.dev&#x2F;20260819-demo-love&#x2F;?vfs=love-snkrx-abi44...</a><p>Commander Keen running in DOSBox:
<a href="https:&#x2F;&#x2F;kandelo.dev&#x2F;20260819-demo-dos&#x2F;?demo=keen" rel="nofollow">https:&#x2F;&#x2F;kandelo.dev&#x2F;20260819-demo-dos&#x2F;?demo=keen</a><p>LXDE desktop PoC:
<a href="https:&#x2F;&#x2F;kandelo.dev&#x2F;20260819-demo-lxde&#x2F;?demo=desktop-lxde" rel="nofollow">https:&#x2F;&#x2F;kandelo.dev&#x2F;20260819-demo-lxde&#x2F;?demo=desktop-lxde</a><p><i>Background</i><p>I wanted an authentic OS-level foundation for running systems software in the browser and started this as a vibe-coded exploration. I figured it would end up being too slow and that we would have to offer many different ways to compromise default POSIX behavior to get anything usable. But after weeks of fighting agents, insisting on genuine POSIX compatibility as the default, I was surprised at how well the system worked without those compromises.<p>Nginx, PHP, Python, Ruby, Redis, and even MariaDB were able to be built using the SDK with minimal hacks.<p>Then we started porting games, having fun, and playing to see how far we could push it.<p><i>Notes on architecture:</i><p>There is a central, single-worker kernel, aiming to provide all supportable POSIX syscalls. Each process is a dedicated worker with independent memory. Each process thread is a dedicated worker that shares memory with threads from the same process. Syscalls are done with the process SharedArrayBuffer and the Atomics API. fork() is supported. The system is centered around virtual file system (VFS) images, and the VFS can contain lazy references to programs that may or may not be used. Vim is such a reference in the shell demo.<p><i>On GitHub:</i>
<a href="https:&#x2F;&#x2F;github.com&#x2F;Automattic&#x2F;kandelo" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;Automattic&#x2F;kandelo</a>
