---
title: "Show HN: Fuse – statically typed functional programming language"
url: "https://fuselang.org"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-08-02T12:40:14Z"
metadata:
  score: "5"
---

# Show HN: Fuse – statically typed functional programming language

> Source: hackernews | Category: news | 2026-08-02T12:40:14Z

Score: 5 | Comments: 0

Hi HN! I&#x27;ve been working on the fuse programming language, it&#x27;s a statically typed purely functional language with higher-kinder types and ad-hoc polymorphism. It compiles to the GRIN whole-program optimizer, producing LLVM-generated native code.<p>Fuse supports ADTs, Generics, Type Methods, Traits, Pattern matching etc. all in a functional style with no mutations.<p>I’ve been developing the language for 5 years, with code written in Scala. I’ve started coding the language from the base of System F that was implemented as part of the book: Types and Programming Languages (tapl). And then extending with concepts such as Bidirectional Type Checking with Higher-Rank Polymorphism.<p>I’ve mainly drawn inspiration from Rust, Haskell, Scala and Python (in terms of syntax). It all started because I wanted a language that has Rust-like concepts such as: ADT, Traits, Impl block syntax, etc. but have the pure functional semantics.<p>I&#x27;d would love feedback on the language design and its general usage.
