---
title: "Show HN: SpinWin – A macOS menu bar app to visually rotate or spin any window"
url: "https://github.com/alokdhir/spinwin"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-26T00:09:42Z"
metadata:
  score: "3"
---

# Show HN: SpinWin – A macOS menu bar app to visually rotate or spin any window

> Source: hackernews | Category: news | 2026-07-26T00:09:42Z

Score: 3 | Comments: 0

SpinWin is an open source menu bar app to visually rotate any individual window. You can rotate &#x2F; spin as many as you want one by one.<p>I was scrolling reels when one came on where the content creator suggested &quot;turning the phone upside down&quot; for a portion. I was sitting at my mac, and decided to see if I could find something that did this. To my surprise, nothing exists, so I decided to build it.<p>Turns out macOS doesn&#x27;t provide any public API to do anything like this, so I wound up using the Accessibility API to move the target window offscreen, where it keeps rendering. Then we capture it&#x27;s contents with ScreenCaptureKit, and display that on a transparent, borderless overlay window which has a CALayer to rotate it.<p>It&#x27;s written in Swift, open source, MIT license, and signed&#x2F;notarized.<p>Have fun - would love to hear your comments.
