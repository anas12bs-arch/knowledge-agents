---
title: "Show HN: CLI that helps AI agents avoid vulnerable dependencies"
url: "https://github.com/clidey/deptrust"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-03T01:15:15Z"
metadata:
  score: "9"
---

# Show HN: CLI that helps AI agents avoid vulnerable dependencies

> Source: hackernews | Category: news | 2026-07-03T01:15:15Z

Score: 9 | Comments: 1

deptrust is a CLI that checks package versions for known vulnerabilities across npm, PyPI, crates.io, Go modules, RubyGems, NuGet, Maven, Packagist, pub.dev, CocoaPods, Hex.pm, Hackage, GitHub Actions, and more.<p>It runs locally as a CLI and as an MCP server. It calls public package registry and OSV APIs directly; there is no hosted deptrust service.<p>I built this because AI coding agents kept suggesting outdated or vulnerable package versions. I kept having to manually tell tools like Claude and Codex to use newer, safer versions.<p>deptrust gives the agent a quick way to verify whether a dependency version has known vulnerabilities before it installs or recommends it.<p>You can install it with:<p>1. pnpx @clidey&#x2F;deptrust@latest install<p>2. brew install clidey&#x2F;tap&#x2F;deptrust<p>3. Or directly with go: go install github.com&#x2F;clidey&#x2F;deptrust&#x2F;cmd&#x2F;deptrust@latest
