---
title: "unionlabs/union ⭐74027"
url: "https://github.com/unionlabs/union"
source: "github-trending"
category: "tool"
tags: ["github", "trending", "rust", "astro", "blockchain", "cosmos", "cosmwasm"]
date: "2026-05-30T14:30:40Z"
metadata:
  stars: "74027"
  language: "Rust"
---

# unionlabs/union ⭐74027

> Source: github-trending | Category: tool | 2026-05-30T14:30:40Z

**unionlabs/union** — ⭐ 74027

Language: Rust | Topics: astro, blockchain, cosmos, cosmwasm, ethereum, evm

The trust-minimized, zero-knowledge bridging protocol, designed for censorship resistance, extremely high security, and usage in decentralized finance.

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./.github/images/union-logo-white.svg">
    <source media="(prefers-color-scheme: light)" srcset="./.github/images/union-logo-black.svg">
    <img alt="Union"
         src="./.github/images/union-logo-black.svg"
         width="100%">
  </picture>
</div>

<br/>

<div align="center">

[![built with garnix](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Fgarnix.io%2Fapi%2Fbadges%2Funionlabs%2Funion%3Fbranch%3Dmain)](https://garnix.io)
[![Docs](https://img.shields.io/badge/docs-main-blue)][docs]
[![Discord badge]](https://discord.union.build)
[![Twitter handle]][twitter badge]

</div>

Union is the hyper-efficient zero-knowledge infrastructure layer for general message passing, asset transfers, NFTs, and DeFi. Its based on [Consensus Verification] and has no dependencies on trusted third parties, oracles, multi-signatures or MPC. It implements [IBC] for compatibility with [Cosmos] chains and connects to EVM chains like [Ethereum], [Berachain (beacon-kit)](https://github.com/berachain/beacon-kit), [Arbitrum], and more.

The upgradability of contracts on other chains, connections, token configurations, and evolution of the protocol will all be controlled by decentralized governance, aligning the priorities of Union with its users, validators, and operators.

## Components

| Component                                           | Description                                          | Language(s)           |
| --------------------------------------------------- | ---------------------------------------------------- | --------------------- |
| [`uniond`](./uniond/README.md)                      | The Union node implementation, using [`CometBLS`]    | [Go]                  |
| [`galoisd`](./galoisd)                              | The zero-knowledge prover implementation             | [Go] [Gnark]          |
| [`voyager`](./voyager)                              | Modular hyper-performant cross-ecosystem relayer     | [Rust]                |
| [`cosmwasm`](./cosmwasm)                            | [CosmWasm] smart contract stack                      | [Rust]                |
| [`light-clients`](./cosmwasm/lightclient)           | [Light Clients] for various ecosystems               | [Rust]                |
| [`unionvisor`](./unionvisor/README.md)              | Node supervisor intended for production usage        | [Rust]                |
| [`drip`](./drip)                                    | Faucet for [Cosmos] chains: [app.union.build/faucet] | [Rust]                |
| [`evm`](./evm)                                      | [EVM] smart contract stack                           | [Solidity]            |
| [`app`](./app2)                                     | [app.union.build]                                    | [TypeScript] [Svelte] |
| [`site`](./site)                                    | [union.build]                                        | [TypeScript] [Astro
