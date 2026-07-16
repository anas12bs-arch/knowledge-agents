---
title: "[hacker-news-sec] n8n Token Exchange Flaw Could Let Attackers Log In as Users From Another Issuer"
url: "https://thehackernews.com/2026/07/n8n-token-exchange-flaw-could-let.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-07-16T15:47:04Z"
metadata:
  {}
---

# [hacker-news-sec] n8n Token Exchange Flaw Could Let Attackers Log In as Users From Another Issuer

> Source: security | Category: security | 2026-07-16T15:47:04Z

n8n Token Exchange Flaw Could Let Attackers Log In as Users From Another Issuer

n8n, the workflow automation platform, handed out the wrong accounts at login. On Enterprise instances configured to trust more than one external token issuer, it matched an incoming JWT to a local user on the&nbsp;sub&nbsp;claim alone and ignored&nbsp;iss.

A valid token from issuer A carrying a&nbsp;sub&nbsp;that belongs to someone under issuer B logged you in as them. Their password never
