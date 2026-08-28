---
title: "[devops-com] Certificate Renewal Is a Deployment Workflow, Not a Cron Job"
url: "https://devops.com/certificate-renewal-is-a-deployment-workflow-not-a-cron-job/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "devops-com"]
date: "2026-08-28T22:25:53Z"
metadata:
  {}
---

# [devops-com] Certificate Renewal Is a Deployment Workflow, Not a Cron Job

> Source: devops | Category: infrastructure | 2026-08-28T22:25:53Z

Certificate Renewal Is a Deployment Workflow, Not a Cron Job

Certificate renewal is often treated as a scheduled task: run an ACME client, obtain a new certificate, and move on. In practice, that view is too narrow for production systems. A certificate is not useful because it exists on disk. It is useful because the right service is presenting it to users. Between issuance and [&#8230;]
