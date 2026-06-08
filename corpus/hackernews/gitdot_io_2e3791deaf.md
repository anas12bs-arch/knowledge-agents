---
title: "Show HN: Gitdot – a better GitHub. Open-source, anti-AI, and written in Rust"
url: "https://gitdot.io/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-06-08T21:25:11Z"
metadata:
  score: "42"
---

# Show HN: Gitdot – a better GitHub. Open-source, anti-AI, and written in Rust

> Source: hackernews | Category: news | 2026-06-08T21:25:11Z

Score: 42 | Comments: 29

What works now: user signups, org creations, private&#x2F;public repos, and importing GitHub repositories (both as read-only mirrors and full migrations). So basically, you can create, push and pull to a repo, but we don&#x27;t have many features quite yet (issues, PRs, CI).<p>What is a bit unique is: 1) we built it in Rust and 2) the website is a little odd. Its design is inspired by CLIs (e.g., fzf, broot, vim) instead of web apps, and as such, lacks some affordances that you might typically expect in favor of keyboard-driven instant navigations (we have the very ambitious goal of an FCP of 100ms). In case you&#x27;re curious, here&#x27;s how we we built it: <a href="https:&#x2F;&#x2F;gitdot.io&#x2F;designs">https:&#x2F;&#x2F;gitdot.io&#x2F;designs</a><p>We recognize that we&#x27;re making some bold claims here and are also well aware that we have much to learn. Building software is still hard, and that&#x27;s a fact we seem to relearn everyday.<p>But we wanted to share what we built so far nonetheless.<p>Cheers, thank y&#x27;all for reading, and till the next
—paul &amp; mikkel.
