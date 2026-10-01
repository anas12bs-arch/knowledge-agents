---
title: "Show HN: Yantra – an LALR(1) parser generator for C++"
url: "https://github.com/TantrixAuto/yantra"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-10-01T09:13:36Z"
metadata:
  score: "23"
---

# Show HN: Yantra – an LALR(1) parser generator for C++

> Source: hackernews | Category: news | 2026-10-01T09:13:36Z

Score: 23 | Comments: 15

Yantra is a C++ parser generator: lexer, parser, and AST walker all generated from one tool.
It builds the whole AST first, then walks it.<p>Most LALR parser generators (Yacc, Bison, Lemon) run your semantic actions during parsing, as each rule reduces, bottom-up.<p>That means at the time a rule&#x27;s action runs, you don&#x27;t yet know what its parent looks like. This pushes a lot of grammars toward hand-built AST classes and a separate walking pass whenever you need to look ahead into siblings or defer a decision until more context is available.<p>On the other hand, Yantra always builds the whole AST first, then walks it top-down in a separate pass, calling your semantic actions as it goes. A parent rule&#x27;s action can run before its children are visited.<p>A single grammar can define more than one walker. For example, one that emits C++, another that emits Java, from the same parse. The AST and the walker classes are both generated for you.<p>A small example (full version, with compile commands, in the README):<p><pre><code>  start := expr;

  expr := expr(a) PLUS expr(b)
  %{
      std::cout &lt;&lt; &quot;Adding&quot; &lt;&lt; std::endl;
  %}

  expr := NUMBER(N)
  %{
      std::cout &lt;&lt; &quot;Number: &quot; &lt;&lt; N.text &lt;&lt; std::endl;
  %}

  NUMBER := &quot;\d+&quot;;
  PLUS := &quot;\+&quot;;
  WS := &quot;\s+&quot;!;
</code></pre>
Running this on &quot;1 + 2 + 3&quot; prints:<p><pre><code>  Adding
  Number: 1
  Adding
  Number: 2
  Number: 3
</code></pre>
The outer &quot;Adding&quot;, the root of the tree, prints first, before either of its children. That&#x27;s only possible because the whole tree exists before any action runs.<p>Some other things about it: integrated lexer with mode support (for things like nested comments), an optional amalgamated single-file output mode with a generated main(), C++23, MIT licensed.<p>It&#x27;s young (0.5.1, pre-1.0) and single-maintainer, so treat it as early.
I&#x27;d rather know what breaks than have it look more finished than it is.<p>Known gaps are listed at
<a href="https:&#x2F;&#x2F;github.com&#x2F;TantrixAuto&#x2F;yantra&#x2F;blob&#x2F;main&#x2F;docs&#x2F;known_limitations.md" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;TantrixAuto&#x2F;yantra&#x2F;blob&#x2F;main&#x2F;docs&#x2F;known_l...</a><p>Repo: <a href="https:&#x2F;&#x2F;github.com&#x2F;TantrixAuto&#x2F;yantra" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;TantrixAuto&#x2F;yantra</a><p>Feedback and questions are all welcome. I&#x27;ll be around.
