---
title: "[hacker-news-sec] CVSS 10.0 LXD, MicroCloud Flaw Lets Attackers Impersonate Trusted Clients Without a Private Key"
url: "https://thehackernews.com/2026/11/critical-lxd-and-microcloud-flaw-cvss.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-11-01T20:33:29Z"
metadata:
  {}
---

# [hacker-news-sec] CVSS 10.0 LXD, MicroCloud Flaw Lets Attackers Impersonate Trusted Clients Without a Private Key

> Source: security | Category: security | 2026-11-01T20:33:29Z

CVSS 10.0 LXD, MicroCloud Flaw Lets Attackers Impersonate Trusted Clients Without a Private Key

A critical flaw in Canonical's LXD and MicroCloud let an attacker log in as a trusted client without holding that client's private key. To do it, the attacker had to reach their HTTPS API over the network and have the trusted client's public certificate.

Once in, the attacker would act as that client, with access to the cluster and its virtual machines. If the impersonated account is
