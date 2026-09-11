---
title: "My .catch() Never Ran. The Bug Was Two Lines Above It"
url: "https://dev.to/parsajiravand/my-catch-never-ran-the-bug-was-two-lines-above-it-3nil"
source: "devto"
category: "news"
tags: ["devto", "programming", "tech-article"]
date: "2026-09-11T13:53:23Z"
metadata:
  tag: "programming"
---

# My .catch() Never Ran. The Bug Was Two Lines Above It

> Source: devto | Category: news | 2026-09-11T13:53:23Z

A function that sometimes throws synchronously instead of returning a promise will skip every .catch() chained to it — because the promise never gets created. Promise.try() fixes it, and does one thing try/catch can't.

Reactions: 5
