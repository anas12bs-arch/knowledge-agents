---
title: "Yon – a topos-oriented language with a content-addressed lattice heap"
url: "https://yon-lang.org/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-06-07T15:04:45Z"
metadata:
  score: "28"
---

# Yon – a topos-oriented language with a content-addressed lattice heap

> Source: hackernews | Category: news | 2026-06-07T15:04:45Z

Score: 28 | Comments: 12

Hello everyone. In the last two years I spent, as a dev, part of my free time
stretching the limits of my knowledge. Not being a mathematician myself, I
discovered that formalizing concepts in mathematical language could nonetheless
be useful to improve symbolic reasoning about the concepts themselves. I made
use of both books and AI, and I followed the development of the latter, mainly
with a critical eye. I have several open projects, and from some observations
and explorations on one of them I started asking myself what the current limits
of reasoning, of logic, of mathematics itself are. So I explored categories,
and topoi, above all starting from Mazzola&#x27;s theory of music. I asked myself
whether this could influence type theory in programming, and I ran some
experiments. Out of this came this programming language, Yon, inspired by
Yoneda and by morphisms. From another project I drew observations on the Leech
lattice; from yet another, some experiments with mmap and coordinate-based
allocation in a structure that would be advantageous, again, in a topological
sense.
The language certainly has mistakes here and there and I wrote the
documentation in a hurry; the work took 3 weeks in total. It compiles to LLVM
for performance reasons, and for now I preferred to avoid a VM and a GC. It
contains unusual data structures that turn out to be performant. It&#x27;s worth a
look, and I hope it will win some converts, and that someone will want to help
me with its development. I&#x27;d love for it to bring fresh stimuli to programming
and maybe open a few new frontiers.
A few concrete details, for those who want to look under the hood. The compiler
is a real pipeline, not an interpreter: an OCaml frontend takes .yon source
into a custom MLIR dialect I called &quot;topos&quot;, where the categorical constructs
live as first-class operations; its lowering passes take everything down to
LLVM IR and from there to a native executable. A single command, yonc, drives
the whole chain, and you can stop at any intermediate stage to see what a
categorical construct actually becomes on its way to silicon.
The runtime is where the Leech lattice observations ended up. The heap is
content-addressed over Λ₂₄: every value is mapped to a lattice point and
canonicalized under the Conway group Co₀ (via libmmgroup), so the same content
always lives at the same address. That buys three things I would now find hard
to give up: equality is a single machine comparison no matter how big the value
is (string equality benches flat at ~17 ns up to 32,768-character strings,
because it compares handles, never bytes); deduplication is global and
automatic, with no interning logic in user code; and giving up the GC stopped
being a renunciation, since cells are immutable and content-addressed, so there
is nothing to trace and nothing to move.
Concurrency I kept deliberately simple-minded: no threads, no shared mutable
state. A program splits into isolated &quot;Spaces&quot; (separate processes, isolation
enforced by the MMU) that talk over shared-memory channels with explicit
failure semantics.
About what is verified and what is just hope: the ground truth is a regression
suite of 112 examples plus a cross-Space scenario suite, with exit codes
identical on Linux x86-64 and macOS Apple Silicon (Intel Macs: untested). The
book on the site, 21 chapters plus appendices, had every snippet compiled and
run before being written down. The benchmarks appendix declares its environment
and method; I tried not to publish any number without one. The limits of 1.0
are written down as well, in a baseline document that lists every fixed pool
(256 heaps per chain, 64 Spaces, 16 concurrent RPC sessions, and so on), with
the rationale that a hard limit that fails loudly is a specification, while a
soft limit that degrades silently is a bug.
For the license I went with the GCC model: compiler and toolchain are AGPLv3,
the runtime is AGPLv3 with an explicit linking exception, so the language
itself stays free, and the programs you write in it are entirely yours, under
any license you choose.<p>Site + book: <a href="https:&#x2F;&#x2F;yon-lang.org" rel="nofollow">https:&#x2F;&#x2F;yon-lang.org</a>
Repo: <a href="https:&#x2F;&#x2F;github.com&#x2F;yon-language&#x2F;yon" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;yon-language&#x2F;yon</a> (tag v1.0.0)<p>Happy to answer anything: the topos dialect, why a lattice rather than a hash,
what the categorical constructs lower to, what broke along the way.
