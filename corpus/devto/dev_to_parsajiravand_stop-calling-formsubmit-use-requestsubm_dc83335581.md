---
title: "Stop Calling form.submit(). Use requestSubmit() Instead."
url: "https://dev.to/parsajiravand/stop-calling-formsubmit-use-requestsubmit-instead-52ho"
source: "devto"
category: "news"
tags: ["devto", "programming", "tech-article"]
date: "2026-10-28T23:11:44Z"
metadata:
  tag: "programming"
---

# Stop Calling form.submit(). Use requestSubmit() Instead.

> Source: devto | Category: news | 2026-10-28T23:11:44Z

A Save button living outside the <form> tag, wired to form.submit(), looks like it works — until a blank required field sails through and the page does a full reload your fetch handler never saw coming. requestSubmit() is the method that actually clicks the button for you.

Reactions: 6
