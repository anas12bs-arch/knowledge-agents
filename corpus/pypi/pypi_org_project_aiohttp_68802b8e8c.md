---
title: "PyPI: aiohttp v3.13.5"
url: "https://pypi.org/project/aiohttp/"
source: "pypi"
category: "skill"
tags: ["pypi", "python", "package", "aiohttp"]
date: "2026-05-30T14:32:07Z"
metadata:
  version: "3.13.5"
  package: "aiohttp"
---

# PyPI: aiohttp v3.13.5

> Source: pypi | Category: skill | 2026-05-30T14:32:07Z

**aiohttp** v3.13.5

Async http client/server framework (asyncio)

==================================
Async http client/server framework
==================================

.. image:: https://raw.githubusercontent.com/aio-libs/aiohttp/master/docs/aiohttp-plain.svg
   :height: 64px
   :width: 64px
   :alt: aiohttp logo

|

.. image:: https://github.com/aio-libs/aiohttp/workflows/CI/badge.svg
   :target: https://github.com/aio-libs/aiohttp/actions?query=workflow%3ACI
   :alt: GitHub Actions status for master branch

.. image:: https://codecov.io/gh/aio-libs/aiohttp/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/aio-libs/aiohttp
   :alt: codecov.io status for master branch

.. image:: https://badge.fury.io/py/aiohttp.svg
   :target: https://pypi.org/project/aiohttp
   :alt: Latest PyPI package version

.. image:: https://img.shields.io/pypi/dm/aiohttp
   :target: https://pypistats.org/packages/aiohttp
   :alt: Downloads count

.. image:: https://readthedocs.org/projects/aiohttp/badge/?version=latest
   :target: https://docs.aiohttp.org/
   :alt: Latest Read The Docs

.. image:: https://img.shields.io/endpoint?url=https://codspeed.io/badge.json
   :target: https://codspeed.io/aio-libs/aiohttp
   :alt: Codspeed.io status for aiohttp


Key Features
============

- Supports both client and server side of HTTP protocol.
- Supports both client and server Web-Sockets out-of-the-box and avoids
  Callback Hell.
- Provides Web-server with middleware and pluggable routing.


Getting started
===============

Client
------

To get something from the web:

.. code-block:: python

  import aiohttp
  import asyncio

  async def main():

      async with aiohttp.ClientSession() as session:
          async with session.get('http://python.org') as response:

              print("Status:", response.status)
              print("Content-type:", response.headers['content-type'])

              html = await response.text()
              print("Body:", html[:15], "...")

  asyncio.run(main())

This prints:

.. code-block::

    Status: 200
    Content-type: text/html; charset=utf-8
    Body: <!doctype html> ...

Coming from `requests <https://requests.readthedocs.io/>`_ ? Read `why we need so many lines <https://aiohttp.readthedocs.io/en/latest/http_request_lifecycle.html>`_.

Server
------

An example using a simple server:

.. code-block:: python

    # examples/server_simple.py
    from aiohttp import web

    async def handle(request):
        name = request.match_info.get('name', "Anonymous")
        text = "Hello, " + name
   
