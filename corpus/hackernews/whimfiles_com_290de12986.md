---
title: "Show HN: Fast, native Mac file manager (filters, fuzzy find, 9 MB, no Electron)"
url: "https://whimfiles.com"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-07T11:32:52Z"
metadata:
  score: "14"
---

# Show HN: Fast, native Mac file manager (filters, fuzzy find, 9 MB, no Electron)

> Source: hackernews | Category: news | 2026-07-07T11:32:52Z

Score: 14 | Comments: 8

My Downloads folder had been left unkept for a really long time and cleaning it up using Finder was quite cumbersome. So I started creating a simple app to help me filter out and delete or move the files in the folder.<p>It started out very basic and the filtering options genuinely helped me clean out the Downloads folder, then as I thought of more features I would like to see in a file manager I started to add them. Some of the features are:<p>- Fuzzy go to folder&#x2F;file where you only need to write a few letters of a full path, get suggestions and can jump to the correct path instantly
- Hover over a file to preview an image or PDF without opening it
- Dual-pane view and tabs that remember selected filters
- Command palette to find actions fast
- Batch rename (with regex support and presets for common operations), image conversion (HEIC&#x2F;WebP&#x2F;AVIF to JPG&#x2F;PNG), zip creation
- Bookmarks, Quick Look, single-click open, keyboard control<p>And many other small quality of life features.<p>I used Claude Code for making the app and the tech stack is .NET&#x2F;C# with AppKit. The app is compiled to Native AOT so the total app size is only around 9 MB. Since file operations are very important to get right (I don’t want to lose any important files) I put a lot of time into hardening file move&#x2F;copy&#x2F;delete operations. Copies are written to a temp file and atomically renamed into place. I also made a dedicated audit of move&#x2F;copy&#x2F;delete and verified each operation by hand.<p>Another thing that’s important to me is apps that are privacy first so the only network request the app makes is to check if there’s a new version (this is not done at all for the trial version, the trial expiry date is enforced locally by just checking the date and trusting the user) and the only information that is sent is the current app version.<p>The app is Apple Silicon, macOS 12+ and has a 30-day free trial with a one-time launch price of $19.99 (no subscription).
