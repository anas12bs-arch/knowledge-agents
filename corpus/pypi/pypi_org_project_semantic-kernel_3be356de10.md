---
title: "PyPI: semantic-kernel v1.42.0"
url: "https://pypi.org/project/semantic-kernel/"
source: "pypi"
category: "skill"
tags: ["pypi", "python", "package", "semantic-kernel"]
date: "2026-05-30T14:32:05Z"
metadata:
  version: "1.42.0"
  package: "semantic-kernel"
---

# PyPI: semantic-kernel v1.42.0

> Source: pypi | Category: skill | 2026-05-30T14:32:05Z

**semantic-kernel** v1.42.0

Semantic Kernel Python SDK

# Get Started with Semantic Kernel Python

> [!IMPORTANT]
> Semantic Kernel is now [Microsoft Agent Framework](https://github.com/microsoft/agent-framework)! Microsoft Agent Framework (MAF) is the enterprise‑ready successor to Semantic Kernel. Microsoft Agent Framework is now available at version 1.0 as a production-ready release: stable APIs, and a commitment to long-term support. Whether you're building a single assistant or orchestrating a fleet of specialized agents, Microsoft Agent Framework 1.0 gives you enterprise-grade multi-agent orchestration, multi-provider model support, and cross-runtime interoperability via A2A and MCP.
>
> Learn more about Semantic Kernel and Agent Framework here: [Semantic Kernel and Microsoft Agent Framework on the Agent Framework blog](https://devblogs.microsoft.com/agent-framework/semantic-kernel-and-microsoft-agent-framework/), and try out the [Semantic Kernel migration guide](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-semantic-kernel).

Highlights
- Flexible Agent Framework: build, orchestrate, and deploy AI agents and multi-agent systems
- Multi-Agent Systems: Model workflows and collaboration between AI specialists
- Plugin Ecosystem: Extend with Python, OpenAPI, Model Context Protocol (MCP), and more
- LLM Support: OpenAI, Azure OpenAI, Hugging Face, Mistral, Google AI, ONNX, Ollama, NVIDIA NIM, and others
- Vector DB Support: Azure AI Search, Elasticsearch, Chroma, and more
- Process Framework: Build structured business processes with workflow modeling
- Multimodal: Text, vision, audio

## Quick Install

```bash
pip install --upgrade semantic-kernel
# Optional: Add integrations
pip install --upgrade semantic-kernel[hugging_face]
pip install --upgrade semantic-kernel[all]
```

Supported Platforms:
- Python: 3.10+
- OS: Windows, macOS, Linux

## 1. Setup API Keys

Set as environment variables, or create a .env file at your project root:

```bash
OPENAI_API_KEY=sk-...
OPENAI_CHAT_MODEL_ID=...
...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
...
```

You can also override environment variables by explicitly passing configuration parameters to the AI service constructor:

```python
chat_service = AzureChatCompletion(
    api_key=...,
    endpoint=...,
    deployment_name=...,
    api_version=...,
)
```

See the following [setup guide](https://github.com/microsoft/semantic-kernel/tree/main/python/samples/concepts/setup) for more information.

## 2. U
