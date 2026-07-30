---
title: "[infoq] AWS Lambda's Self-Managed Code Storage Lifts the Account Quota, Not the Function Size Limit"
url: "https://www.infoq.com/news/2026/07/lambda-self-managed-storage/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-07-30T08:43:06Z"
metadata:
  {}
---

# [infoq] AWS Lambda's Self-Managed Code Storage Lifts the Account Quota, Not the Function Size Limit

> Source: engineering | Category: engineering | 2026-07-30T08:43:06Z

AWS Lambda's Self-Managed Code Storage Lifts the Account Quota, Not the Function Size Limit

AWS Lambda can now reference deployment packages directly in customer-owned S3 buckets, removing the per-Region code storage quota and raising the managed default from 75 GB to 300 GB. Per-function package limits are unchanged, and UpdateFunctionCode is still required after replacing an object. Terraform provider support remains an open enhancement request.   By Steef-Jan Wiggers
