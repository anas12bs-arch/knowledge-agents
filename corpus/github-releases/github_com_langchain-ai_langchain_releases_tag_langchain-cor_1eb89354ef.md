---
title: "langchain-ai/langchain langchain-core==1.5.5 released"
url: "https://github.com/langchain-ai/langchain/releases/tag/langchain-core%3D%3D1.5.5"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "langchain"]
date: "2026-08-14T19:01:00Z"
metadata:
  repo: "langchain-ai/langchain"
  version: "langchain-core==1.5.5"
---

# langchain-ai/langchain langchain-core==1.5.5 released

> Source: github-releases | Category: changelog | 2026-08-14T19:01:00Z

## langchain-ai/langchain — langchain-core==1.5.5

Changes since langchain-core==1.5.4

release(core): 1.5.5 (#39655)
fix(core): make abatch_iterate consistent with batch_iterate for None and zero size (#39367)
fix(core): respect pydantic aliases when validating tool inputs (#39572)
fix(core): issues in merging chunks (#39535)
fix(core): handle v1 base model validation in async path (#39576)
fix(core): handle tool descriptions for infer_schema=False (#39573)
fix(core): clear usage metadata callback on exceptions in context manager (#39616)
fix(core): handle falsy LLM and chat model caches (#39283)
chore(core): add httpx as an explicit dep (#39612)
fix(core): preserve non-str/non-dict items in `DictPromptTemplate` list values (#39588)
fix(core): raise ValueError when explicit tool_outputs length mismatches tool_calls in tool_example_to_messages (#39142)
fix(core): guard malformed Anthropic content blocks (#38670)
