---
title: "floci-io/floci ⭐31287"
url: "https://github.com/floci-io/floci"
source: "github-trending"
category: "tool"
tags: ["github", "trending", "devops", "aws", "aws-emulation", "devops", "docker"]
date: "2026-11-11T02:10:14Z"
metadata:
  stars: "31287"
  language: "Java"
---

# floci-io/floci ⭐31287

> Source: github-trending | Category: tool | 2026-11-11T02:10:14Z

**floci-io/floci** — ⭐ 31287

Language: Java | Topics: aws, aws-emulation, devops, docker, ec2, ecs

Light, fluffy, and always free - The AWS Local Emulator alternative

<p align="center">
  <img src="docs/assets/floci-black.svg#gh-light-mode-only" alt="Floci" width="500" />
  <img src="docs/assets/floci-white.svg#gh-dark-mode-only" alt="Floci" width="500" />
</p>

<p align="center">
  <strong>Any Cloud. Locally.</strong><br />
  Light, fluffy, and always free<br />
  No account. No auth token. No feature gates. Just <code>docker compose up</code>.
</p>

<p align="center">
  <a href="https://github.com/floci-io/floci/releases/latest"><img src="https://img.shields.io/github/v/release/floci-io/floci?label=latest%20release&color=blue" alt="Latest Release"></a>
  <a href="https://github.com/floci-io/floci/actions/workflows/release.yml"><img src="https://img.shields.io/github/actions/workflow/status/floci-io/floci/release.yml?label=build" alt="Build Status"></a>
  <a href="https://hub.docker.com/r/floci/floci"><img src="https://img.shields.io/docker/pulls/floci/floci?label=docker%20pulls" alt="Docker Pulls"></a>
  <a href="https://hub.docker.com/r/floci/floci"><img src="https://img.shields.io/docker/image-size/floci/floci/latest?label=image%20size" alt="Docker Image Size"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/license-MIT-green" alt="License: MIT"></a>
  <a href="https://github.com/floci-io/floci/stargazers"><img src="https://img.shields.io/github/stars/floci-io/floci?style=flat" alt="GitHub Stars"></a>
</p>

<p align="center">
  <a href="#quick-start">Quick Start</a> ·
  <a href="#features">Features</a> ·
  <a href="#supported-services">Services</a> ·
  <a href="#sdk-integration">SDKs</a> ·
  <a href="#testcontainers">Testcontainers</a> ·
  <a href="#migrating-from-localstack">Migration</a> ·
  <a href="https://floci.io/floci/">Docs</a>
</p>

---

## What is Floci?

Floci is a free, open-source local AWS emulator for development, testing, and CI.

It gives you AWS-shaped services on your machine without requiring a cloud account, an auth token, or paid feature gates. Point your AWS SDK, CLI, Terraform, CDK, OpenTofu, or test suite at `http://localhost:4566` and keep your existing workflows.

Already using LocalStack? Floci is a drop-in replacement: swap the image and keep going. See [Migrating from LocalStack](#migrating-from-localstack).

Floci is the AWS member of the [Floci](https://github.com/floci-io) emulator family, named after [floccus](https://en.wikipedia.org/wiki/Cirrocumulus_floccus), the cloud formation that looks like popcorn.

| Emulator | Cloud | Port |
|---|---|:---:|
| **[floci](https://github.com/floci-io/floci)** | **AWS** | **4566** |
| [floci-az](https://github.com/floci-io/floci-az) | Azure | 4577 |
| [floci-gcp](https://github.com/floci-io/floci-gcp) | GCP | 4588 |
| [floci-oci](https://github.com/floci-io/floci-oci) | OCI | 4599 |

## Quick Start

The fastest way to run Floci is with the official [CLI](https://github.com/floci-io/floci-cli)

```bash
floci start
```

No Docker? Each [release](https://github.com/floci-io/floci/releases) also 
