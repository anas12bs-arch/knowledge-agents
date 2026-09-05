---
title: "toISOString() put 328 invoices in the wrong tax month"
url: "https://dev.to/stackedboost/toisostring-put-328-invoices-in-the-wrong-tax-month-2fj4"
source: "devto"
category: "news"
tags: ["devto", "javascript", "tech-article"]
date: "2026-09-05T09:23:18Z"
metadata:
  tag: "javascript"
---

# toISOString() put 328 invoices in the wrong tax month

> Source: devto | Category: news | 2026-09-05T09:23:18Z

toISOString() renders UTC. Our billing platform issues invoices at 00:00 Europe/Warsaw, so every invoice in the monthly run was dated the previous day. Not the wrong day. The wrong VAT month.

Reactions: 1
