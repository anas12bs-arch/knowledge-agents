---
title: "CodeBendKit/codeseek ⭐534"
url: "https://github.com/CodeBendKit/codeseek"
source: "github-trending"
category: "tool"
tags: ["github", "trending", "embedding", "bm25", "c-li", "call-graph", "claude-code"]
date: "2026-07-06T00:17:48Z"
metadata:
  stars: "534"
  language: "Rust"
---

# CodeBendKit/codeseek ⭐534

> Source: github-trending | Category: tool | 2026-07-06T00:17:48Z

**CodeBendKit/codeseek** — ⭐ 534

Language: Rust | Topics: bm25, c-li, call-graph, claude-code, cli, code-analysis

Rust-powered code intelligence CLI for AI coding agents. Builds call graphs and hybrid semantic search indexes (Dense + Sparse + RRF + Reranker) across 7 languages. Ships as native MCP tools for Claude Code and Codex CLI.

# CodeSeek

**Code intelligence CLI tool for Claude Code.** AST-based call graph analysis + semantic search — right from your terminal.

## Quick Start

```bash
# Install via npm (handles setup wizard + binary download automatically)
npm install -g codeseek

# First run — interactive setup wizard configures your embedding model
codeseek

# Index your project
codeseek init

# Search code by symbol name
codeseek search main --limit 10

# Query call graph
codeseek callers main
codeseek callees process_data

# Register with Claude Code / Codex as MCP tools
codeseek install

# Check status
codeseek status

# Auto-index on git commits
codeseek install-hooks
```

Natural Language Code Search example

```bash
╰─$ codeseek search 'how the code embedding work'
1. get_embedding (0.7973)
   /home/do/ssd/iohub/dev/codeseek/rust-core/src/services/embedding_service.rs:0
2. EmbeddingService (0.2855)
   /home/do/ssd/iohub/dev/codeseek/rust-core/src/services/embedding_service.rs:0
3. EmbeddingData (0.1449)
   /home/do/ssd/iohub/dev/codeseek/rust-core/src/services/embedding_service.rs:0
4. EmbeddingResponse (0.1304)
   /home/do/ssd/iohub/dev/codeseek/rust-core/src/services/embedding_service.rs:0
5. default_model (0.0450)
   /home/do/ssd/iohub/dev/codeseek/rust-core/src/config.rs:0

```

## Install

### npm

```bash
npm install -g codeseek
```

The npm package ships a lightweight JS wrapper that handles:

| Step | Description |
|------|-------------|
| **First-run wizard** | Interactive CLI prompts for embedding API token, model, and base URL |
| **Binary download** | Automatically pulls the correct Rust binary for your platform from GitHub Releases |
| **Pass-through** | All commands (`init`, `search`, `callers`, etc.) are forwarded to the native binary |

Supported platforms:

| Platform | Architecture |
|----------|-------------|
| macOS | arm64 (Apple Silicon), x64 (Intel) |
| Linux | x64 |

### Homebrew

```bash
brew tap CodeBendKit/codeseek git@github.com:CodeBendKit/codeseek.git
brew install codeseek
```

### From source

```bash
# install protoc
# macos: brew install protobuf
# ubuntu: sudo apt install protoc

git clone https://github.com/CodeBendKit/codeseek.git
cd codeseek
./build.sh --release
```

`build.sh` compiles both the TypeScript wrapper (`dist/`) and the Rust binary, then installs to `~/.codeseek/bin/`.

## Commands

| Command | Description |
|---------|-------------|
| `codeseek` | First-time setup wizard (configures embedding model interactively) |
| `codeseek init` | Build/update code index (full on first run, MD5-incremental thereafter) |
| `codeseek status` | Index statistics: functions, files, last update |
| `codeseek search <query>` | Symbol name search (falls back from vector → graph name match) |
| `codeseek callers <symbol>` | Find functions that call this symbol |
| `codeseek callees <symbol>` | Find functions this symbol calls |
| `codeseek list` | List all indexed projects with paths |
| `codeseek install` | Register codeseek as MCP 
