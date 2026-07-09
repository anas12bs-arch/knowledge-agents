---
title: "Show HN: Sighthound - open-source vulnerability scanner for source code"
url: "https://github.com/Corgea/Sighthound"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-09T21:42:21Z"
metadata:
  score: "6"
---

# Show HN: Sighthound - open-source vulnerability scanner for source code

> Source: hackernews | Category: news | 2026-07-09T21:42:21Z

Score: 6 | Comments: 0

We&#x27;re open-sourcing Sighthound today, our rules-based static security scanner. What makes it special is that it&#x27;s coded in rust and uses tree-sitter as it&#x27;s AST making it very fast and easily extensible.<p>Why build another scanner in 2026? We wanted to improve some of our detection outcomes but noticed the current open source scanners like Semgrep&#x2F;Opengrep we&#x27;re capped by a bunch of adoption limitations such as being written in OCaml, requiring a lot of work to add a language parser, and the rulesets were licensed differently and required paid offerings. It also felt that licensing was moving backwards rather than forward.<p>We wanted something that was very fast, was easily extensible and had a great set of rules that we could use. This led us to using Rust and Tree-sitter since they are both fast and have great community adoption making extending Sighthound natural.<p>We wanted it to focus on source-code vulnerability classes like Sql Injection, and Xss. We haven&#x27;t yet done any secrets scanning as there are a lot of great options in the market at the moment. Right now, Sighthound supports Python, JS&#x2F;TS, Java, Go, C#, HTML, PHP and Ruby.<p>We still have a lot of work to do so, we&#x27;d love for your feedback, and contributions in however they come from adding new languages, new rules or bug fixes.
