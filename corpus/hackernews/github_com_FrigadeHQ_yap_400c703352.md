---
title: "Show HN: Yap – OSS on-device voice dictation for macOS with no model to download"
url: "https://github.com/FrigadeHQ/yap"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-28T04:18:33Z"
metadata:
  score: "34"
---

# Show HN: Yap – OSS on-device voice dictation for macOS with no model to download

> Source: hackernews | Category: news | 2026-07-28T04:18:33Z

Score: 34 | Comments: 6

Hey HN! I wanted to share this OSS project I&#x27;ve been working on.<p>It&#x27;s called Yap and its a small menu-bar app for macOS that does voice to text for any input. You&#x27;ll set a hotkey, press it, talk, press it again, and the text gets pasted into whatever field you were in. Everything runs locally and never leaves your computer. Fully OSS and MIT licensed.<p>With macOS 26, Apple recently added two new APIs, SpeechAnalyzer and SpeechTranscriber, that do streaming on-device speech to text using models the OS ships and manages. So the app ships no model of its own and loads nothing before the first word. A recent benchmark put Apple&#x27;s model slightly ahead of Whisper Small on accuracy and about 3x faster (see: <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=48894752">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=48894752</a>). On Mac, there&#x27;s really no need anymore to download models or pay for expensive APIs.<p>A lot of existing dictation tools do one of a few things I wanted to avoid with this OSS project. They either:<p>- cost money (for something that&#x27;s literally built into the OS)<p>- bundle memory-intensive models (e.g. Whisper or Parakeet)<p>- webapps wrapped in Electron<p>- Intel macs straight up don&#x27;t work<p>- closed source<p>- use third-party APIs that will have access to all your transcripts<p>It&#x27;s around 3,000 lines of native Swift in a 4 MB app and idles near 60 MB of memory. Audio comes off AVAudioEngine into SpeechAnalyzer with volatile results turned on for the live preview, history is stored in SwiftData. There&#x27;s no network code in it at all.<p>Repo and a demo available here: <a href="https:&#x2F;&#x2F;github.com&#x2F;FrigadeHQ&#x2F;yap" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;FrigadeHQ&#x2F;yap</a><p>Happy to answer questions and would love to hear any feature requests!
