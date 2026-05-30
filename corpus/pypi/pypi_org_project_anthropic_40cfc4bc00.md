---
title: "PyPI: anthropic v0.105.2"
url: "https://pypi.org/project/anthropic/"
source: "pypi"
category: "skill"
tags: ["pypi", "python", "package", "anthropic"]
date: "2026-05-30T14:32:03Z"
metadata:
  version: "0.105.2"
  package: "anthropic"
---

# PyPI: anthropic v0.105.2

> Source: pypi | Category: skill | 2026-05-30T14:32:03Z

**anthropic** v0.105.2

The official Python library for the anthropic API

# Claude SDK for Python

[![PyPI version](https://img.shields.io/pypi/v/anthropic.svg)](https://pypi.org/project/anthropic/)

The Claude SDK for Python provides access to the [Claude API](https://docs.anthropic.com/en/api/) from Python applications.

## Documentation

Full documentation is available at **[platform.claude.com/docs/en/api/sdks/python](https://platform.claude.com/docs/en/api/sdks/python)**.

## Installation

```sh
pip install anthropic
```

## Getting started

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)

message = client.messages.create(
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Hello, Claude",
        }
    ],
    model="claude-opus-4-6",
)
print(message.content)
```

## Requirements

Python 3.9+

## Contributing

See [CONTRIBUTING.md](https://github.com/anthropics/anthropic-sdk-python/tree/main/./CONTRIBUTING.md).

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/anthropics/anthropic-sdk-python/tree/main/LICENSE) file for details.

