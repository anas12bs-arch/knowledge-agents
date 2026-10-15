---
title: "Stop Electing a Leader Tab. SharedWorker Just Holds the Connection."
url: "https://dev.to/parsajiravand/stop-electing-a-leader-tab-sharedworker-just-holds-the-connection-1623"
source: "devto"
category: "news"
tags: ["devto", "webdev", "tech-article"]
date: "2026-10-15T21:37:12Z"
metadata:
  tag: "webdev"
---

# Stop Electing a Leader Tab. SharedWorker Just Holds the Connection.

> Source: devto | Category: news | 2026-10-15T21:37:12Z

Electing a leader tab to own one shared WebSocket works great — until the leader is the tab someone closes. SharedWorker skips the election: the connection lives in the worker, not in any tab, so there's no leader to lose.

Reactions: 7
