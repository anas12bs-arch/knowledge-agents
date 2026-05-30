---
title: "Kong/kong ⭐43489"
url: "https://github.com/Kong/kong"
source: "github-trending"
category: "tool"
tags: ["github", "trending", "devops", "ai", "ai-gateway", "api-gateway", "api-management"]
date: "2026-05-30T14:30:46Z"
metadata:
  stars: "43489"
  language: "Lua"
---

# Kong/kong ⭐43489

> Source: github-trending | Category: tool | 2026-05-30T14:30:46Z

**Kong/kong** — ⭐ 43489

Language: Lua | Topics: ai, ai-gateway, api-gateway, api-management, apis, artificial-intelligence

🦍 The API and AI Gateway

[![][kong-logo]][kong-url]

![Stars](https://img.shields.io/github/stars/Kong/kong?style=flat-square) ![GitHub commit activity](https://img.shields.io/docker/pulls/_/kong?style=flat-square) [![Build Status][badge-action-image]][badge-action-url] ![Version](https://img.shields.io/github/v/release/Kong/kong?color=green&label=Version&style=flat-square)  ![License](https://img.shields.io/badge/License-Apache%202.0-blue?style=flat-square) [![Twitter Follow](https://img.shields.io/twitter/follow/thekonginc?style=social)](https://x.com/thekonginc)


Kong or Kong Gateway is a cloud-native, platform-agnostic, scalable **API 𖧹 LLM 𖧹 MCP** Gateway distinguished for its high performance and extensibility via plugins. It also provides advanced AI traffic capabilities with multi-LLM support, semantic security, MCP traffic security and analytics, and more.

By providing functionality for proxying, routing, load balancing, health checking, authentication (and [more](#features)), Kong serves as the central layer for orchestrating microservices or conventional API traffic - and agentic LLM and MCP as well - with ease.

Kong runs natively on Kubernetes thanks to its official [Kubernetes Ingress Controller](https://github.com/Kong/kubernetes-ingress-controller).

<br />

[![][kong-diagram]][kong-url]

---

[Installation](https://konghq.com/install/#kong-community) | [Documentation](https://docs.konghq.com) | [Discussions](https://github.com/Kong/kong/discussions) | [Forum](https://discuss.konghq.com) | [Blog](https://konghq.com/blog) | [Builds][kong-master-builds] | [AI Gateway](https://konghq.com/products/kong-ai-gateway) | [Cloud Hosted Kong](https://konghq.com/kong-konnect/)

---

## Getting Started

If you prefer to use a cloud-hosted Kong, you can [sign up for a free trial of Kong Konnect](https://konghq.com/products/kong-konnect/register?utm_medium=Referral&utm_source=Github&utm_campaign=kong-gateway&utm_content=konnect-promo-in-gateway&utm_term=get-started) and get started in minutes. If not, you can follow the instructions below to get started with Kong on your own infrastructure.

Let’s test drive Kong by adding authentication to an API in under 5 minutes.

We suggest using the docker-compose distribution via the instructions below, but there is also a [docker installation](https://docs.konghq.com/gateway/latest/install/docker/#install-kong-gateway-in-db-less-mode) procedure if you’d prefer to run the Kong Gateway in DB-less mode.

Whether you’re running in the cloud, on bare metal, or using containers, you can find every supported distribution on our [official installation](https://konghq.com/install/#kong-community) page.

1) To start, clone the Docker repository and navigate to the compose folder.
```cmd
  $ git clone https://github.com/Kong/docker-kong
  $ cd docker-kong/compose/
```

2) Start the Gateway stack using:
```cmd
  $ KONG_DATABASE=postgres docker-compose --profile database up
```

The Gateway is now available on the following ports on localh
