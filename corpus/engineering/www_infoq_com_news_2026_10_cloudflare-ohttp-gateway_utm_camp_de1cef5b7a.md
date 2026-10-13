---
title: "[infoq] Cloudflare’s OHTTP Gateway Refuses to Decrypt Requests That Arrive Through Cloudflare"
url: "https://www.infoq.com/news/2026/10/cloudflare-ohttp-gateway/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-10-13T22:00:09Z"
metadata:
  {}
---

# [infoq] Cloudflare’s OHTTP Gateway Refuses to Decrypt Requests That Arrive Through Cloudflare

> Source: engineering | Category: engineering | 2026-10-13T22:00:09Z

Cloudflare’s OHTTP Gateway Refuses to Decrypt Requests That Arrive Through Cloudflare

Cloudflare has opened a closed beta of its OHTTP Gateway, a managed endpoint that decrypts Oblivious HTTP requests for an origin. The design choice drawing attention is a refusal: the Gateway will not decrypt requests arriving from Cloudflare Workers or from hosts proxied through Cloudflare, because that would put client identifiers and request contents in the same hands.   By Steef-Jan Wiggers
