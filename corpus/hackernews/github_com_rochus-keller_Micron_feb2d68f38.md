---
title: "Show HN: Micron – Oberon with the Power of C"
url: "https://github.com/rochus-keller/Micron"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-11-11T23:28:35Z"
metadata:
  score: "49"
---

# Show HN: Micron – Oberon with the Power of C

> Source: hackernews | Category: news | 2026-11-11T23:28:35Z

Score: 49 | Comments: 13

I have been developing Micron (for &quot;MicroOberon&quot;), a lean, statically typed, modular systems programming language that combines Oberon’s simplicity and explicit module structure with C’s low-level capabilities and interoperability.<p>Micron is not my first langage design. I first built Oberon+, a modernized and unified Oberon, in order to under­
stand, by implementing it and by porting real systems to it, what Wirth’s design actually gives and where it fails. The systems ported to Oberon+ included the 2013 Project Oberon System and different versions of Oberon System 3. I then explored the opposite direction with Luon, a higher-level language for managed application progamming. Micron is the synthesis of this and my 30 years experience with C&#x2F;C++ in systems programming.<p>The goal of Micron is to use the same language for boot code, device drivers, an operating system kernel, and ordinary applications, without requiring a garbage collector or routing machine access through a separate, unchecked system dialect (such as Oberon&#x27;s SYSTEM.ADR&#x2F;GET&#x2F;PUT which operates on LONGINT). The language supports explicit memory layouts, signed and unsigned integer types, pointer operations, and direct calls to C without wrappers. One of its central design choices is language levels. Each module declars the level and thus the feature it needs, ranging from code that requires neither stack nor heap to garbage-collected objects. A module can import only modules at the same or a lower level. For example, a kernel module declared at level 1 cannot accidentally acquire a dependency on heap allocation through an import. Other features include generic modules, structural interfaces, and compile-time procedures. Much of what would require a preprocessor in C is expressed through typed language features.<p>There is a working compiler, interpreter, and IDE, along with a free textbook (<a href="http:&#x2F;&#x2F;software.rochus-keller.ch&#x2F;micron-textbook.pdf" rel="nofollow">http:&#x2F;&#x2F;software.rochus-keller.ch&#x2F;micron-textbook.pdf</a>). The book explains both how the language works and the reasons behind its design. Its systems-programming section walks through a port of Wirth and Gutknecht’s Project Oberon operating system to Micron, cross-compiled and linked into a single executabl that runs on an emulated RISC-V machine.<p>The examples also include ports of a Smalltalk-80 VM, Scheme 9, and the original P4 Pascal compiler. The compiler and interpreter implement the language specification; native backends and tooling are still work in progress, and the current native code generation prioritises simplicity over optimisation.<p>For more information see <a href="https:&#x2F;&#x2F;github.com&#x2F;rochus-keller&#x2F;Micron&#x2F;blob&#x2F;master&#x2F;Readme.md" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;rochus-keller&#x2F;Micron&#x2F;blob&#x2F;master&#x2F;Readme.m...</a>.
