---
title: "Show HN: Flashpaper – Self-destructing secret sharing with no database"
url: "https://flashpaper.app/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-28T17:02:04Z"
metadata:
  score: "7"
---

# Show HN: Flashpaper – Self-destructing secret sharing with no database

> Source: hackernews | Category: news | 2026-07-28T17:02:04Z

Score: 7 | Comments: 2

Hi everyone! This is my first HN and I’m very new to the scene. My name is Min from Bangkok.<p>At first, I just want to create a dead man&#x27;s switch for personal use and for fun. then, I think about information that self destruct like a spy movie. after that, I try to come up with the better version of Privnote or Bitwarden with self-destruct and some kind of censoring or blocking download ability. Somehow, end up with this product. :O<p>Flashpaper is for sending any information that would be burned after reading (with counting down timer like Mission Impossible movie ! or after 24 hrs max if not opened) Encryption happens in browser and because the key stays after # in the link; server never sees the key (Zero-knowledge for web use) and— because I’m a newbie. I don’t want to connect to database because I don’t have the money and I want things light and simple. So, that’s why Flashpaper keeps things in RAM-only, no database.<p>For AI Agent side, Flashpaper provides a REST API and an MCP server so agents can create secret links easily in dead-drop style that can be claimed only once. The second claim would get a 404 which means someone already took it. However, for the agent API flow, the server sees the plaintext for a moment before encrypting, so this flow is not zero-knowledge like the web flow.<p>Overall, I think it work quite well for web use, but for agent API use, I am not sure this is enough security. All the limitations are listed in SECURITY.md. Some feedback would be appreciated.  
I make it open source with MIT license, with honorware policy for Enterprise use, like self-hosted docker.<p>Here is my repo <a href="https:&#x2F;&#x2F;github.com&#x2F;mmmpym&#x2F;flashpaper" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;mmmpym&#x2F;flashpaper</a>
and you can try it here <a href="https:&#x2F;&#x2F;flashpaper.app" rel="nofollow">https:&#x2F;&#x2F;flashpaper.app</a><p>Again ! Please feel free to tell me what I missed.<p>Min
