---
title: "[hacker-news-sec] GoAhead TLS Flaws Allow Revoked Client Certificates and Enable Session Decryption"
url: "https://thehackernews.com/2026/10/goahead-tls-flaws-allow-revoked-client.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-10-27T22:19:28Z"
metadata:
  {}
---

# [hacker-news-sec] GoAhead TLS Flaws Allow Revoked Client Certificates and Enable Session Decryption

> Source: security | Category: security | 2026-10-27T22:19:28Z

GoAhead TLS Flaws Allow Revoked Client Certificates and Enable Session Decryption

The GoAhead embedded web server loaded a certificate revocation list into its default TLS backend but never turned revocation checking on, so a revoked client certificate could still pass login on affected setups.

The flaw is in builds that use the OpenSSL backend with mutual-TLS, where the server checks a client certificate and vice versa, and a revocation list is configured to block revoked
