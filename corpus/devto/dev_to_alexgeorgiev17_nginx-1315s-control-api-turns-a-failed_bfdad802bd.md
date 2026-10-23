---
title: "nginx 1.31.5's control API turns a failed reload into an HTTP 422 instead of a log line"
url: "https://dev.to/alexgeorgiev17/nginx-1315s-control-api-turns-a-failed-reload-into-an-http-422-instead-of-a-log-line-48bc"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-10-23T16:17:40Z"
metadata:
  tag: "devops"
---

# nginx 1.31.5's control API turns a failed reload into an HTTP 422 instead of a log line

> Source: devto | Category: news | 2026-10-23T16:17:40Z

I opened nginx's new control API over plain TCP with no credentials and used it to read live worker PIDs and swap a running config from outside the container. The unix-socket default stopped a non-owning user cold, reload itself gained no speed, and just having the listener open cost about 300KB of resident memory.

Reactions: 6
