---
title: "[infoq] Google Cloud Moves the Compute Engine API to Immutable Date-Based Versions"
url: "https://www.infoq.com/news/2026/11/compute-engine-api-versioning/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-11-14T08:01:01Z"
metadata:
  {}
---

# [infoq] Google Cloud Moves the Compute Engine API to Immutable Date-Based Versions

> Source: engineering | Category: engineering | 2026-11-14T08:01:01Z

Google Cloud Moves the Compute Engine API to Immutable Date-Based Versions

Google Cloud has made date-based versioning of the Compute Engine API generally available, replacing the single mutable /v1 surface with immutable quarterly snapshots such as 2026-09-01, selected per request with a header or query parameter. New versions can change defaults, error formats, and IAM checks without touching /v1 callers, a model Azure Resource Manager and Stripe have used for years.   By Steef-Jan Wiggers
