---
title: "Scope GitHub Actions concurrency to your Terraform state, not your branch"
url: "https://dev.to/toyama0919/scope-github-actions-concurrency-to-your-terraform-state-not-your-branch-1kfe"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-11-14T19:32:26Z"
metadata:
  tag: "devops"
---

# Scope GitHub Actions concurrency to your Terraform state, not your branch

> Source: devto | Category: news | 2026-11-14T19:32:26Z

A production CI story about serializing terraform apply with GitHub Actions concurrency - why the group key should be the state object, why the read-only plan job must stay out of the group, and what cancel-in-progress does not protect.

Reactions: 1
