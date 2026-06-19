---
title: "Show HN: Talos – Open-source WASM interpreter for Lean"
url: "https://github.com/cajal-technologies/talos"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-06-19T11:55:41Z"
metadata:
  score: "60"
---

# Show HN: Talos – Open-source WASM interpreter for Lean

> Source: hackernews | Category: news | 2026-06-19T11:55:41Z

Score: 60 | Comments: 8

At Cajal (YC W26) we’re excited to share Talos (<a href="https:&#x2F;&#x2F;github.com&#x2F;cajal-technologies&#x2F;talos" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;cajal-technologies&#x2F;talos</a>), an open source framework for formal verification of WebAssembly modules in Lean.<p>AI is now writing tons of the code that gets pushed to production. As code generation gets cheaper, verification becomes the bottleneck. We believe in a future where every piece of software comes with a mathematical proof that it does what its author intended - in doing so, eliminating many classes of exploits. Talos is part of the foundation for that.<p>Talos provides a Wasm interpreter optimized for reasoning at the binary level, together with a weakest-precondition calculus layer for proving properties about programs. Because we reason directly about WebAssembly, any language with a Wasm backend is in scope: Rust, C++, Go, C, Swift, Kotlin, Zig, C#, and many more.<p>To make this possible, we use Lean: a programming language and theorem prover that lets you both write software and mathematically prove that it&#x27;s correct - all in one system. That&#x27;s what lets Talos double as both an executable interpreter and the formal object Lean reasons about. Lean also integrates with modern AI proving tools, discharging goals automatically via both proof search and direct evaluation.<p>To see Talos in action check out a proof for Stein&#x27;s GCD algorithm, implemented in the popular Rust crate num-integer: <a href="https:&#x2F;&#x2F;github.com&#x2F;cajal-technologies&#x2F;talos&#x2F;blob&#x2F;main&#x2F;programs&#x2F;lean&#x2F;Project&#x2F;NumInteger&#x2F;Spec.lean#L562-L588" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;cajal-technologies&#x2F;talos&#x2F;blob&#x2F;main&#x2F;progra...</a>.<p>Our roadmap:<p>- Full Wasm coverage by first passing the official W3C testsuite, then later verifying against SpecTec (formal Wasm spec)
- Arbitrary crate verification - any Rust crate that compiles to Wasm should be in scope
- Building our proof library codelib, to make verifying increasingly complex programs tractable<p>We would love to hear the community’s feedback on Talos and comments on the state of formal verification right now. Contributions are also welcome!
