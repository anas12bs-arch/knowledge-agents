---
title: "[hacker-news-sec] Official MCP Python SDK Flaw Can Let Malicious Servers Steal OAuth Credentials"
url: "https://thehackernews.com/2026/09/official-mcp-python-sdk-flaw-can-let.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-09-29T09:08:11Z"
metadata:
  {}
---

# [hacker-news-sec] Official MCP Python SDK Flaw Can Let Malicious Servers Steal OAuth Credentials

> Source: security | Category: security | 2026-09-29T09:08:11Z

Official MCP Python SDK Flaw Can Let Malicious Servers Steal OAuth Credentials

A malicious MCP server could trick an application built on the official&nbsp;MCP Python SDK&nbsp;into handing over the OAuth credentials it uses to log in to a real service, the SDK's maintainers said in a security advisory.

Affected versions sent the client secret, the authorization code, and the PKCE proof key to a token endpoint the attacker controlled. The fix is in versions 1.30.0 and
