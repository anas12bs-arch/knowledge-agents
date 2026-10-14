---
title: "rtk-ai/rtk ⭐83232"
url: "https://github.com/rtk-ai/rtk"
source: "github-trending"
category: "tool"
tags: ["github", "trending", "rust", "agentic-coding", "ai-coding", "anthropic", "claude-code"]
date: "2026-10-14T00:52:36Z"
metadata:
  stars: "83232"
  language: "Rust"
---

# rtk-ai/rtk ⭐83232

> Source: github-trending | Category: tool | 2026-10-14T00:52:36Z

**rtk-ai/rtk** — ⭐ 83232

Language: Rust | Topics: agentic-coding, ai-coding, anthropic, claude-code, cli, command-line-tool

CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. Single Rust binary, zero dependencies

<p align="center">
  <img src="https://avatars.githubusercontent.com/u/258253854?v=4" alt="RTK - Rust Token Killer" width="500">
</p>

<p align="center">
  <strong>Agent-agnostic token optimization: compress, route, filter, and more.</strong>
  <br><br>
  One composable pipeline across everything your AI agent reads and sends — built on RTK's battle-tested bash-output compression (up to 90% smaller).
</p>

<p align="center">
  <a href="https://github.com/rtk-ai/rtk/actions"><img src="https://github.com/rtk-ai/rtk/workflows/Security%20Check/badge.svg" alt="CI"></a>
  <a href="https://github.com/rtk-ai/rtk/releases"><img src="https://img.shields.io/github/v/release/rtk-ai/rtk" alt="Release"></a>
  <a href="#license"><img src="https://img.shields.io/badge/license-Apache--2.0%20%2B%20BUSL--1.1-blue.svg" alt="License: Apache-2.0 and BUSL-1.1"></a>
  <a href="https://discord.gg/RySmvNF5kF"><img src="https://img.shields.io/discord/1470188214710046894?label=Discord&logo=discord" alt="Discord"></a>
  <a href="https://formulae.brew.sh/formula/rtk"><img src="https://img.shields.io/homebrew/v/rtk" alt="Homebrew"></a>
</p>

<p align="center">
  <a href="https://www.rtk-ai.app">Website</a> &bull;
  <a href="#installation">Install</a> &bull;
  <a href="https://www.rtk-ai.app/guide/resources/troubleshooting">Troubleshooting</a> &bull;
  <a href="docs/contributing/ARCHITECTURE.md">Architecture</a> &bull;
  <a href="https://discord.gg/RySmvNF5kF">Discord</a>
</p>

<p align="center">
  <a href="README.md">English</a> &bull;
  <a href="README_fr.md">Francais</a> &bull;
  <a href="README_zh.md">中文</a> &bull;
  <a href="README_ja.md">日本語</a> &bull;
  <a href="README_ko.md">한국어</a> &bull;
  <a href="README_es.md">Espanol</a> &bull;
  <a href="README_pt.md">Português</a>
</p>

---

<p align="center">
 <a href="https://www.star-history.com/rtk-ai/rtk">
  <picture><source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/badge?repo=rtk-ai/rtk&type=rank&theme=dark" /><source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/badge?repo=rtk-ai/rtk&type=rank" /><img alt="Star History Rank" src="https://api.star-history.com/badge?repo=rtk-ai/rtk&type=rank" /></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/badge?repo=rtk-ai/rtk&type=trending&theme=dark" /><source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/badge?repo=rtk-ai/rtk&type=trending" /><img alt="GitHub Trending Repository of the Day" src="https://api.star-history.com/badge?repo=rtk-ai/rtk&type=trending" /></picture>
 </a>
</p>

rtk filters and compresses command outputs before they reach your LLM context. Single Rust binary, 100+ supported commands, <10ms overhead.

## What RTK Does

RTK intercepts shell commands and compresses their output before your agent reads it.

| Operation | What RTK does to the output |
|-----------|-----------------------------|
| `ls` / `tree` | Tree format wi
