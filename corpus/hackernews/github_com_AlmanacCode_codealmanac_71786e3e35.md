---
title: "Show HN: CodeAlmanac – Karpathy-style codebase wiki from your conversations"
url: "https://github.com/AlmanacCode/codealmanac/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-21T18:23:58Z"
metadata:
  score: "8"
---

# Show HN: CodeAlmanac – Karpathy-style codebase wiki from your conversations

> Source: hackernews | Category: news | 2026-07-21T18:23:58Z

Score: 8 | Comments: 3

Hey HN! This is Divit from Almanac (YC S26). We built CodeAlmanac, a wiki for your coding agents that updates as you talk to them. It is open-source, local, and free.<p>Here’s a demo: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=XNQWV3TFBWM" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=XNQWV3TFBWM</a><p>Your CC&#x2F;Codex conversations contain a LOT of knowledge that is forgotten because it was never documented. People have their own methods of documenting their chats. We used to make Markdown files like MANUAL.md and DESIGN.md, and would prompt Claude to keep them updated. The problem is that these files quickly become outdated and messy, and there’s only so much you can put in a single file.<p>So we set out to build CodeAlmanac. We wanted something that was 1) maintained automatically, 2) lived inside our repository, and 3) used our existing Codex&#x2F;Claude Code subscriptions.<p>CodeAlmanac maintains an almanac&#x2F; folder inside your repository. It contains connected Markdown pages that cover things not documented in the codebase, including decisions you have made and why the codebase is shaped this way.<p>The pages are indexed in SQLite and are queryable through a CLI. We add instructions to AGENTS.md or CLAUDE.md so future sessions automatically search the wiki before they start coding.<p>Every five hours, CodeAlmanac uses the Codex&#x2F;CC SDK to spin up an agent that reads your new conversations and updates the relevant pages. We went with a time-based trigger instead of commits because we saw people commit very frequently, which would lead to high token costs.<p>We originally made CodeAlmanac for individual developers, but the team use case has become much more obvious to us while using it ourselves. We are a team of three, and each of us works with our own coding agents. Before this, I would make some change after a lot of thinking and then later have to call my cofounders and explain why it looked this way. There is almost a sense of relief now knowing that the decisions I made are written down somewhere their agents will actually read.<p>It’s live today for everyone to try. Please let me know your feedback and I’ll be here to answer any questions. Would also love to hear how you all maintain context across conversations today!
