---
title: "Caddy 2.11.6 turns a silent config failure on /load into an HTTP 400"
url: "https://dev.to/alexgeorgiev17/caddy-2116-turns-a-silent-config-failure-on-load-into-an-http-400-4656"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-10-24T23:38:29Z"
metadata:
  tag: "devops"
---

# Caddy 2.11.6 turns a silent config failure on /load into an HTTP 400

> Source: devto | Category: news | 2026-10-24T23:38:29Z

A Caddy reload that broke my running server used to come back HTTP 200. On 2.11.6 and 2.11.7 it's a 400 with a real error, and a related fix cuts a stuck Unix socket from about two minutes to instant.

Reactions: 7
