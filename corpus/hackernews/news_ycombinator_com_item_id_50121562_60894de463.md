---
title: "Anthropic Console overcharged my card 100x due to internationalization input bug"
url: "https://news.ycombinator.com/item?id=50121562"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-10-16T21:51:14Z"
metadata:
  score: "76"
---

# Anthropic Console overcharged my card 100x due to internationalization input bug

> Source: hackernews | Category: news | 2026-10-16T21:51:14Z

Score: 76 | Comments: 28

I am a LegalTech Attorney leading a developer team from Costa Rica. While trying to load credits onto my Anthropic API account (claude.com), I experienced a critical internationalization (i18n) and UX failure that has placed an unfair financial burden on me due to a severe oversight in their payment pipeline.<p>The platform prompted me for a payment. Since I am in a Spanish-speaking region where localized systems and keyboards handle dots and commas differently, I typed 5.04.<p>Anthropic’s input system completely failed to sanitize or validate the data. Instead of throwing a formatting error or converting it properly, it silently stripped the decimal internally and instantly charged my credit card $504.00 USD instead of $5.04 USD.<p>To make matters worse, there was no confirmation modal or review screen summarizing the final amount before processing the transaction. It was a single-click, instantaneous overcharge.<p>Anticipating the Obvious Skepticism:
Before anyone suggests &quot;you should have checked your regional settings&quot; or &quot;just wait for the chargeback&quot;:<p>1. Users are not the QA team: In financial software, a system is never supposed to guess or automatically manipulate a numerical input without explicit validation. If an input is ambiguous due to locale differences, the application must reject it or ask for clarification, not execute a 100x overcharge.<p>2. Scale of the vulnerability: This time it was $504.00, which is an unfair and frustrating burden for independent developers. But because this pipeline completely lacks a confirmation screen and basic input sanitization, the exact same bug could happen to someone typing 50.00 and end up charging them $5,000.00 or more instantly. It is a systemic financial risk.<p>3. The Chargeback Illusion: Yes, I have already initiated a chargeback with my bank in Costa Rica. However, banking processes here are slow and take up to 120 days to resolve. In the meantime, the $504.00 has already been deducted and charged to my credit card statement. I am forced to pay for Anthropic’s engineering mistake out of my own pocket right now.<p>The Support Wall:
I filed an official complaint on the exact same day, minutes after it happened. I wasn&#x27;t met with a human; I was blocked by an automated support BOT. The bot repeatedly and rigidly denied the refund, closing the ticket by citing generic policies without a single human ever looking at the fact that the overcharge was caused by a technical bug in their own platform.<p>As developers, we build systems that process people&#x27;s money. Omitting a confirmation screen on a financial transaction, failing to sanitize localized numerical inputs, and then hiding behind unyielding AI support bots to keep money that doesn&#x27;t belong to you is completely unacceptable.<p>If anyone from Anthropic&#x27;s billing or engineering team is reading this, please look into this bug and review my case. It is a critical flaw that is actively harming international developers who are just trying to build on your ecosystem.<p>Pura vida!<p>R.S.G.
