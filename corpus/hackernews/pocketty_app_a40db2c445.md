---
title: "Show HN: Pocketty – iPhone SSH terminal that pings you when an agent is blocked"
url: "https://pocketty.app/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-10-09T00:18:30Z"
metadata:
  score: "9"
---

# Show HN: Pocketty – iPhone SSH terminal that pings you when an agent is blocked

> Source: hackernews | Category: news | 2026-10-09T00:18:30Z

Score: 9 | Comments: 6

Hello~! pocketty is an SSH terminal for iPhone and iPad, made for herdr. herdr keeps your agent panes alive on your computer and knows the state of each one: working, needs you, or done.<p>I made this in anger&#x2F;desperation for the latter half of my recent paternity leave. Nap traps are sweet, but there&#x27;s only so much doom-scrolling and movie-watching I can handle... In any event, I&#x27;ve been using it for the last couple months and no longer <i>have</i> to be my desk anymore to be productive. Now the nap-traps are still productive (when i want them to be) !<p>How it works:<p>- The app talks to your computer directly over plain SSH. Tailscale is the easy way to reach it from anywhere but any SSH host you can reach works.<p>- A small Rust daemon on the host watches herdr. When a pane needs you, it seals the alert to your phone&#x27;s key with HPKE (X25519, ChaCha20-Poly1305). A stateless relay (pocketty&#x27;s) on Cloudflare Workers passes the sealed bytes to APNs (Apple Push Notification servers), and a notification extension opens them on the phone. The relay can&#x27;t read them and keeps nothing.<p>- Your SSH key is made in the Secure Enclave and can&#x27;t be exported.<p>- The terminal uses libghostty-vt for state and draws with wgpu on Metal, so full-screen TUIs look like they do on your desk, albeit narrower.<p>- Diffs for each agent turn, a file browser, and previews of `localhost` dev servers your agent starts, all through the same SSH connection. No port forwarding to set up.<p>herdr and the daemon are optional. Without them, it&#x27;s a normal SSH client.<p>There&#x27;s no account to set up and no analytics or tracking in the app. 
The app runs a 14-day free trial, with full feature access. Then, if you&#x27;re as happy as I am with it, then it can be yours forever with a one-time purchase: $99 for the first two weeks (launch promo) then $129 after that.<p>Happy to answer anything about the sealed push setup or running libghostty on iOS.
