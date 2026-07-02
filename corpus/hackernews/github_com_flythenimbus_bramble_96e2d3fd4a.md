---
title: "Show HN: Bramble – Local-first password manager"
url: "https://github.com/flythenimbus/bramble"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-02T21:21:30Z"
metadata:
  score: "5"
---

# Show HN: Bramble – Local-first password manager

> Source: hackernews | Category: news | 2026-07-02T21:21:30Z

Score: 5 | Comments: 0

I&#x27;m currently working on Bramble, an open source password manager with P2P cross-device sync. Initially I released the Chrome extension, but recently I also published the Android app and iOS is pending Apple&#x27;s approval. Besides that, the latest version also includes passkey storage for all platforms!<p>About Bramble:<p>It aims to be as feature-rich as all popular and a replacement for cloud-based providers. I don&#x27;t think we need to store our data in the cloud and be at the whims of companies raising their prices every year. There&#x27;s always a breach and then we find out that some fields aren&#x27;t encrypted, metadata is visible, and so on. I&#x27;m frustrated with this and the increasing lack of transparency during these breaches.<p>The P2P sync in Bramble uses a Nostr relay (which can be self-hosted) to keep your devices in sync. The relay just introduces the devices to each other; the data then flows directly over WebRTC, so there&#x27;s no vault server and no cloud copy of your passwords anywhere. What leaves your device is end-to-end encrypted and your devices authenticate each other directly, so a snooping or MITM relay gets practically nothing.<p>Crypto is all done in Rust so I can control exactly how key material lives and dies in memory (secrets get zeroed out, no GB leaving copies lying around). In Chromium it&#x27;s a wasm module, on mobile it&#x27;s native builds bridged over via uniffi.<p>Android app:<p>I&#x27;m still deciding whether to publish the app on Play store or simply provide the signed APK which users can sideload. Reason for that is Google&#x27;s plan to lock down Android and take away ownership from its users. Read more about it here: <a href="https:&#x2F;&#x2F;keepandroidopen.com&#x2F;" rel="nofollow">https:&#x2F;&#x2F;keepandroidopen.com&#x2F;</a><p>The app uses no Play APIs whatsoever and runs perfectly on GrapheneOS, where I actually did all my testing.<p>Questions, feedback, feature requests - all welcome!<p>TL;DR: I dislike private-equity and venture funded companies messing with our security, so I created my own Password Manager which is local-first, free, open source and as transparent as it gets.
