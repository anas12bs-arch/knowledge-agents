---
title: "fatedier/frp ⭐106980"
url: "https://github.com/fatedier/frp"
source: "github-trending"
category: "tool"
tags: ["github", "trending", "go", "expose", "firewall", "frp", "go"]
date: "2026-05-30T14:30:43Z"
metadata:
  stars: "106980"
  language: "Go"
---

# fatedier/frp ⭐106980

> Source: github-trending | Category: tool | 2026-05-30T14:30:43Z

**fatedier/frp** — ⭐ 106980

Language: Go | Topics: expose, firewall, frp, go, http-proxy, nat

A fast reverse proxy to help you expose a local server behind a NAT or firewall to the internet.

# frp

[![Build Status](https://circleci.com/gh/fatedier/frp.svg?style=shield)](https://circleci.com/gh/fatedier/frp)
[![GitHub release](https://img.shields.io/github/tag/fatedier/frp.svg?label=release)](https://github.com/fatedier/frp/releases)
[![Go Report Card](https://goreportcard.com/badge/github.com/fatedier/frp)](https://goreportcard.com/report/github.com/fatedier/frp)
[![GitHub Releases Stats](https://img.shields.io/github/downloads/fatedier/frp/total.svg?logo=github)](https://somsubhra.github.io/github-release-stats/?username=fatedier&repository=frp)

[README](README.md) | [中文文档](README_zh.md)

## Sponsors

frp is an open source project with its ongoing development made possible entirely by the support of our awesome sponsors. If you'd like to join them, please consider [sponsoring frp's development](https://github.com/sponsors/fatedier).

<h3 align="center">Gold Sponsors</h3>
<!--gold sponsors start-->
<p align="center">
  <a href="https://jb.gg/frp" target="_blank">
    <img width="420px" src="https://raw.githubusercontent.com/fatedier/frp/dev/doc/pic/sponsor_jetbrains.jpg">
	<br>
	<b>The complete IDE crafted for professional Go developers</b>
  </a>
</p>

<p align="center">
  <a href="https://github.com/beclab/Olares" target="_blank">
    <img width="420px" src="https://raw.githubusercontent.com/fatedier/frp/dev/doc/pic/sponsor_olares.jpeg">
	<br>
	<b>The sovereign cloud that puts you in control</b>
	<br>
	<sub>An open source, self-hosted alternative to public clouds, built for data ownership and privacy</sub>
  </a>
</p>

<div align="center">

## Recall.ai - API for meeting recordings

If you're looking for a meeting recording API, consider checking out [Recall.ai](https://www.recall.ai/?utm_source=github&utm_medium=sponsorship&utm_campaign=fatedier-frp),

an API that records Zoom, Google Meet, Microsoft Teams, in-person meetings, and more.

</div>
<!--gold sponsors end-->

## What is frp?

frp is a fast reverse proxy that allows you to expose a local server located behind a NAT or firewall to the Internet. It currently supports **TCP** and **UDP**, as well as **HTTP** and **HTTPS** protocols, enabling requests to be forwarded to internal services via domain name.

frp also offers a P2P connect mode.

## Table of Contents

<!-- vim-markdown-toc GFM -->

* [Development Status](#development-status)
    * [About V2](#about-v2)
* [Architecture](#architecture)
* [Example Usage](#example-usage)
    * [Access your computer in a LAN network via SSH](#access-your-computer-in-a-lan-network-via-ssh)
    * [Multiple SSH services sharing the same port](#multiple-ssh-services-sharing-the-same-port)
    * [Accessing Internal Web Services with Custom Domains in LAN](#accessing-internal-web-services-with-custom-domains-in-lan)
    * [Forward DNS query requests](#forward-dns-query-requests)
    * [Forward Unix Domain Socket](#forward-unix-domain-socket)
    * [Expose a simple HTTP file server](#expose-a-simple-http-file-server)
    * [Enable HTTPS for
