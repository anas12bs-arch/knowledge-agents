---
title: "Sixteen XORs and not a single if"
url: "https://dev.to/arcker/sixteen-xors-and-not-a-single-if-3k9i"
source: "devto"
category: "news"
tags: ["devto", "programming", "tech-article"]
date: "2026-09-13T17:39:40Z"
metadata:
  tag: "programming"
---

# Sixteen XORs and not a single if

> Source: devto | Category: news | 2026-09-13T17:39:40Z

Verbose is a small proof-carrying language whose compiler is written in itself. Its TLS 1.3 design doc claimed 'no cryptography in the host' — and its own section 7 proved that false: six computations still lived in Python. They are now six Verbose rules with zero compiler changes, including a constant-time tag comparison where sixteen XORs fold into each other and never branch. Why a plain if would leak the secret, and the oracle that settles it: a real handshake against openssl.

Reactions: 0
