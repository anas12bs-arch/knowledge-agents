---
title: "PyPI: qdrant-client v1.18.0"
url: "https://pypi.org/project/qdrant-client/"
source: "pypi"
category: "skill"
tags: ["pypi", "python", "package", "qdrant-client"]
date: "2026-05-30T14:32:06Z"
metadata:
  version: "1.18.0"
  package: "qdrant-client"
---

# PyPI: qdrant-client v1.18.0

> Source: pypi | Category: skill | 2026-05-30T14:32:06Z

**qdrant-client** v1.18.0

Client library for the Qdrant vector search engine



<p align="center">
  <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://github.com/qdrant/qdrant/raw/master/docs/logo-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://github.com/qdrant/qdrant/raw/master/docs/logo-light.svg">
      <img height="100" alt="Qdrant" src="https://github.com/qdrant/qdrant/raw/master/docs/logo.svg">
  </picture>
</p>

<p align="center">
    <b>Python Client library for the <a href="https://github.com/qdrant/qdrant">Qdrant</a> vector search engine.</b>
</p>


<p align=center>
    <a href="https://pypi.org/project/qdrant-client/"><img src="https://badge.fury.io/py/qdrant-client.svg" alt="PyPI version" height="18"></a>
    <a href="https://api.qdrant.tech/"><img src="https://img.shields.io/badge/Docs-OpenAPI%203.0-success" alt="OpenAPI Docs"></a>
    <a href="https://github.com/qdrant/qdrant-client/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-Apache%202.0-success" alt="Apache 2.0 License"></a>
    <a href="https://qdrant.to/discord"><img src="https://img.shields.io/badge/Discord-Qdrant-5865F2.svg?logo=discord" alt="Discord"></a>
    <a href="https://qdrant.to/roadmap"><img src="https://img.shields.io/badge/Roadmap-2025-bc1439.svg" alt="Roadmap 2025"></a>
</p>

# Python Qdrant Client

Client library and SDK for the [Qdrant](https://github.com/qdrant/qdrant) vector search engine.

Library contains type definitions for all Qdrant API and allows to make both Sync and Async requests.

Client allows calls for all [Qdrant API methods](https://api.qdrant.tech/) directly.
It also provides some additional helper methods for frequently required operations, e.g. initial collection uploading.

See [QuickStart](https://qdrant.tech/documentation/quick-start/#create-collection) for more details!

## Installation

```
pip install qdrant-client
```

## Features

- Type hints for all API methods
- Local mode - use same API without running server
- REST and gRPC support
- Minimal dependencies
- Extensive Test Coverage

## Local mode

<p align="center">
  <!--- https://github.com/qdrant/qdrant-client/raw/master -->
  <img max-height="180" src="https://github.com/qdrant/qdrant-client/raw/master/docs/images/try-develop-deploy.png" alt="Qdrant">
</p>

Python client allows you to run same code in local mode without running Qdrant server.

Simply initialize client like this:

```python
from qdrant_client import QdrantClient

client = QdrantClient(":memory:")
# or
client = QdrantC
