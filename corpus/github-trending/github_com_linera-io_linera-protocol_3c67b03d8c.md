---
title: "linera-io/linera-protocol ⭐32118"
url: "https://github.com/linera-io/linera-protocol"
source: "github-trending"
category: "tool"
tags: ["github", "trending", "wasm", "blockchain", "rust", "wasm"]
date: "2026-05-30T14:31:00Z"
metadata:
  stars: "32118"
  language: "Rust"
---

# linera-io/linera-protocol ⭐32118

> Source: github-trending | Category: tool | 2026-05-30T14:31:00Z

**linera-io/linera-protocol** — ⭐ 32118

Language: Rust | Topics: blockchain, rust, wasm

Main repository for the Linera protocol

# <img src="https://github.com/linera-io/linera-protocol/assets/1105398/fe08c941-93af-4114-bb83-bcc0eaec95f9" width="250" height="85" />

[![License](https://img.shields.io/github/license/linera-io/linera-protocol)](LICENSE)
[![Build Status for Docker](https://github.com/linera-io/linera-protocol/actions/workflows/docker-compose.yml/badge.svg)](https://github.com/linera-io/linera-protocol/actions/workflows/docker-compose.yml)
[![Build Status for Rust](https://github.com/linera-io/linera-protocol/actions/workflows/rust.yml/badge.svg)](https://github.com/linera-io/linera-protocol/actions/workflows/rust.yml)
[![Build Status for Documentation](https://github.com/linera-io/linera-protocol/actions/workflows/documentation.yml/badge.svg)](https://github.com/linera-io/linera-protocol/actions/workflows/documentation.yml)
[![Twitter](https://img.shields.io/twitter/follow/linera_io)](https://x.com/linera_io)
[![Discord](https://img.shields.io/discord/984941796272521226)](https://discord.com/invite/linera)

<!-- [![Build Status for Kubernetes](https://github.com/linera-io/linera-protocol/actions/workflows/kubernetes.yml/badge.svg)](https://github.com/linera-io/linera-protocol/actions/workflows/kubernetes.yml) -->

[Linera](https://linera.io) is a decentralized blockchain infrastructure designed for highly scalable,
secure, low-latency Web3 applications.

## Documentation

Visit our [developer page](https://linera.dev) and read our
[whitepaper](https://linera.io/whitepaper) to learn more about the Linera protocol.

## Repository Structure

The main crates and directories of this repository can be summarized as follows: (listed
from low to high levels in the dependency graph)

* [`linera-base`](https://linera-io.github.io/linera-protocol/linera_base/index.html) Base
  definitions, including cryptography.

* [`linera-version`](https://linera-io.github.io/linera-protocol/linera_version/index.html)
  A library to manage version info in binaries and services.

* [`linera-views`](https://linera-io.github.io/linera-protocol/linera_views/index.html) A
  library mapping complex data structures onto a key-value store. The corresponding
  procedural macros are implemented in `linera-views-derive`.

* [`linera-execution`](https://linera-io.github.io/linera-protocol/linera_execution/index.html)
  Persistent data and the corresponding logic for runtime and execution of Linera
  applications.

* [`linera-chain`](https://linera-io.github.io/linera-protocol/linera_chain/index.html)
  Persistent data and the corresponding logic for chains of blocks, certificates, and
  cross-chain messaging.

* [`linera-storage`](https://linera-io.github.io/linera-protocol/linera_storage/index.html)
  Defines the storage abstractions for the protocol on top of `linera-chain`.

* [`linera-core`](https://linera-io.github.io/linera-protocol/linera_core/index.html) The
  core Linera protocol, including client and server logic, node synchronization, etc.

* [`linera-rpc`](https://linera-io.github.io
