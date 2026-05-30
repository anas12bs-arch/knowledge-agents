---
title: "PyPI: starlette v1.2.0"
url: "https://pypi.org/project/starlette/"
source: "pypi"
category: "skill"
tags: ["pypi", "python", "package", "starlette"]
date: "2026-05-30T14:32:07Z"
metadata:
  version: "1.2.0"
  package: "starlette"
---

# PyPI: starlette v1.2.0

> Source: pypi | Category: skill | 2026-05-30T14:32:07Z

**starlette** v1.2.0

The little ASGI library that shines.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Kludex/starlette/main/docs/img/starlette_dark.svg" width="420px">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Kludex/starlette/main/docs/img/starlette.svg" width="420px">
    <img alt="starlette-logo" src="https://raw.githubusercontent.com/Kludex/starlette/main/docs/img/starlette.svg">
  </picture>
</p>

<p align="center">
    <em>✨ The little ASGI framework that shines. ✨</em>
</p>

---

[![Build Status](https://github.com/Kludex/starlette/workflows/Test%20Suite/badge.svg)](https://github.com/Kludex/starlette/actions)
[![Package version](https://badge.fury.io/py/starlette.svg)](https://pypi.python.org/pypi/starlette)
[![Supported Python Version](https://img.shields.io/pypi/pyversions/starlette.svg?color=%2334D058)](https://pypi.org/project/starlette)
[![Discord](https://img.shields.io/discord/1051468649518616576?logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://discord.gg/RxKUF5JuHs)

---

**Documentation**: <a href="https://starlette.dev/" target="_blank">https://starlette.dev</a>

**Source Code**: <a href="https://github.com/Kludex/starlette" target="_blank">https://github.com/Kludex/starlette</a>

---

# Starlette

Starlette is a lightweight [ASGI][asgi] framework/toolkit,
which is ideal for building async web services in Python.

It is production-ready, and gives you the following:

* A lightweight, low-complexity HTTP web framework.
* WebSocket support.
* In-process background tasks.
* Startup and shutdown events.
* Test client built on `httpx`.
* CORS, GZip, Static Files, Streaming responses.
* Session and Cookie support.
* 100% test coverage.
* 100% type annotated codebase.
* Few hard dependencies.
* Compatible with `asyncio` and `trio` backends.
* Great overall performance [against independent benchmarks][techempower].

## Installation

```shell
$ pip install starlette
```

You'll also want to install an ASGI server, such as [uvicorn](https://uvicorn.dev), [daphne](https://github.com/django/daphne/), or [hypercorn](https://hypercorn.readthedocs.io/en/latest/).

```shell
$ pip install uvicorn
```

## Example

```python title="main.py"
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def homepage(request):
    return JSONResponse({'hello': 'world'})

routes = [
    Route("/", en
