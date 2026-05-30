---
title: "PyPI: instructor v1.15.1"
url: "https://pypi.org/project/instructor/"
source: "pypi"
category: "skill"
tags: ["pypi", "python", "package", "instructor"]
date: "2026-05-30T14:32:04Z"
metadata:
  version: "1.15.1"
  package: "instructor"
---

# PyPI: instructor v1.15.1

> Source: pypi | Category: skill | 2026-05-30T14:32:04Z

**instructor** v1.15.1

structured outputs for llm

# Instructor: Structured Outputs for LLMs

Get reliable JSON from any LLM. Built on Pydantic for validation, type safety, and IDE support.

```python
import instructor
from pydantic import BaseModel


# Define what you want
class User(BaseModel):
    name: str
    age: int


# Extract it from natural language
client = instructor.from_provider("openai/gpt-4o-mini")
user = client.chat.completions.create(
    response_model=User,
    messages=[{"role": "user", "content": "John is 25 years old"}],
)

print(user)  # User(name='John', age=25)
```

**That's it.** No JSON parsing, no error handling, no retries. Just define a model and get structured data.

[![PyPI](https://img.shields.io/pypi/v/instructor?style=flat-square)](https://pypi.org/project/instructor/)
[![Downloads](https://img.shields.io/pypi/dm/instructor?style=flat-square)](https://pypi.org/project/instructor/)
[![GitHub Stars](https://img.shields.io/github/stars/567-labs/instructor?style=flat-square)](https://github.com/567-labs/instructor)
[![Discord](https://img.shields.io/discord/1192334452110659664?style=flat-square)](https://discord.gg/bD9YE9JArw)
[![Twitter](https://img.shields.io/twitter/follow/jxnlco?style=flat-square)](https://twitter.com/jxnlco)

> **Use Instructor for fast extraction, reach for PydanticAI when you need agents.** Instructor keeps schema-first flows simple and cheap. If your app needs richer agent runs, built-in observability, or shareable traces, try [PydanticAI](https://ai.pydantic.dev/). PydanticAI is the official agent runtime from the Pydantic team, adding typed tools, replayable datasets, evals, and production dashboards while using the same Pydantic models. Dive into the [PydanticAI docs](https://ai.pydantic.dev/) to see how it extends Instructor-style workflows.

## Why Instructor?

Getting structured data from LLMs is hard. You need to:

1. Write complex JSON schemas
2. Handle validation errors  
3. Retry failed extractions
4. Parse unstructured responses
5. Deal with different provider APIs

**Instructor handles all of this with one simple interface:**

<table>
<tr>
<td><b>Without Instructor</b></td>
<td><b>With Instructor</b></td>
</tr>
<tr>
<td>

```python
response = openai.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "..."}],
    tools=[
        {
            "type": "function",
            "function": {
                "name": "extract_user",
                "parameters": {
                    "type": "object",
         
