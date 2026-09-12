---
title: "addDays() Mutated a Date Three Components Away From Where I Called It"
url: "https://dev.to/parsajiravand/adddays-mutated-a-date-three-components-away-from-where-i-called-it-3400"
source: "devto"
category: "news"
tags: ["devto", "programming", "tech-article"]
date: "2026-09-12T14:23:08Z"
metadata:
  tag: "programming"
---

# addDays() Mutated a Date Three Components Away From Where I Called It

> Source: devto | Category: news | 2026-09-12T14:23:08Z

A date utility that calls .setDate() and returns the same object looks pure. It isn't — Date is mutable, so the caller and everyone else holding that reference get changed out from under them. Temporal, now shipping in real browsers, fixes it by making dates immutable.

Reactions: 1
