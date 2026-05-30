---
title: "go-gitea/gitea ⭐56020"
url: "https://github.com/go-gitea/gitea"
source: "github-trending"
category: "tool"
tags: ["github", "trending", "devops", "bitbucket", "cicd", "devops", "docker-registry-v2"]
date: "2026-05-30T14:30:45Z"
metadata:
  stars: "56020"
  language: "Go"
---

# go-gitea/gitea ⭐56020

> Source: github-trending | Category: tool | 2026-05-30T14:30:45Z

**go-gitea/gitea** — ⭐ 56020

Language: Go | Topics: bitbucket, cicd, devops, docker-registry-v2, git, git-gui

Git with a cup of tea! Painless self-hosted all-in-one software development service, including Git hosting, code review, team collaboration, package registry and CI/CD

# Gitea

[![](https://github.com/go-gitea/gitea/actions/workflows/release-nightly.yml/badge.svg?branch=main)](https://github.com/go-gitea/gitea/actions/workflows/release-nightly.yml?query=branch%3Amain "Release Nightly")
[![](https://img.shields.io/discord/322538954119184384.svg?logo=discord&logoColor=white&label=Discord&color=5865F2)](https://discord.gg/Gitea "Join the Discord chat at https://discord.gg/Gitea")
[![](https://goreportcard.com/badge/gitea.dev)](https://goreportcard.com/report/gitea.dev "Go Report Card")
[![](https://pkg.go.dev/badge/gitea.dev?status.svg)](https://pkg.go.dev/gitea.dev "GoDoc")
[![](https://img.shields.io/github/release/go-gitea/gitea.svg)](https://github.com/go-gitea/gitea/releases/latest "GitHub release")
[![](https://www.codetriage.com/go-gitea/gitea/badges/users.svg)](https://www.codetriage.com/go-gitea/gitea "Help Contribute to Open Source")
[![](https://opencollective.com/gitea/tiers/backers/badge.svg?label=backers&color=brightgreen)](https://opencollective.com/gitea "Become a backer/sponsor of gitea")
[![](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT "License: MIT")
[![](https://badges.crowdin.net/gitea/localized.svg)](https://translate.gitea.com "Crowdin")

[繁體中文](./README.zh-tw.md) | [简体中文](./README.zh-cn.md)

## Purpose

The goal of this project is to make the easiest, fastest, and most
painless way of setting up a self-hosted Git service.

As Gitea is written in Go, it works across **all** the platforms and
architectures that are supported by Go, including Linux, macOS, and
Windows on x86, amd64, ARM and PowerPC architectures.
This project has been
[forked](https://blog.gitea.com/welcome-to-gitea/) from
[Gogs](https://gogs.io) since November of 2016, but a lot has changed.

For online demonstrations, you can visit [demo.gitea.com](https://demo.gitea.com).

For accessing free Gitea service (with a limited number of repositories), you can visit [gitea.com](https://gitea.com/user/login).

To quickly deploy your own dedicated Gitea instance on Gitea Cloud, you can start a free trial at [cloud.gitea.com](https://cloud.gitea.com).

## Documentation

You can find comprehensive documentation on our official [documentation website](https://docs.gitea.com/).

It includes installation, administration, usage, development, contributing guides, and more to help you get started and explore all features effectively.

If you have any suggestions or would like to contribute to it, you can visit the [documentation repository](https://gitea.com/gitea/docs)

## Building

From the root of the source tree, run:

    TAGS="bindata" make build

The `build` target is split into two sub-targets:

- `make backend` which requires [Go Stable](https://go.dev/dl/), the required version is defined in [go.mod](/go.mod).
- `make frontend` which requires [Node.js LTS](https://nodejs.org/en/download/) or greater and [pnpm](https://pnpm.io/installation).

Internet connectivity is required to download 
