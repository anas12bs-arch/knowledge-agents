---
title: "langchain-ai/langchain langchain-core==1.6.0 released"
url: "https://github.com/langchain-ai/langchain/releases/tag/langchain-core%3D%3D1.6.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "langchain"]
date: "2026-08-19T16:17:07Z"
metadata:
  repo: "langchain-ai/langchain"
  version: "langchain-core==1.6.0"
---

# langchain-ai/langchain langchain-core==1.6.0 released

> Source: github-releases | Category: changelog | 2026-08-19T16:17:07Z

## langchain-ai/langchain — langchain-core==1.6.0

Changes since langchain-core==1.5.6

release(core): 1.6.0 (#39760)
fix(core): resolve postponed annotations in `StructuredTool._injected_args_keys` (#39602)
feat(core): add standard model exception types (#39538)
fix(core): allow deserializing `RunnablePick` (#39753)
fix(core): make `convert_to_openai_function` handle callables and non-dict mappings (#39750)
fix(core): make subprocess and temporary file tests portable on Windows (#39664)
fix(core): fail fast when tool schemas can't resolve forward refs during serialization (#39570)
test(core): avoid version-dependent runnable snapshots (#39705)
fix(core): require all nested properties for strict tool schemas (#39306)
fix(core): remove stale sync-stream `xfail` [closes #39720] (#39723)
perf(core): Lazily import transformers (#38037)
fix(core): accept non-dict Mapping values in mustache templates (#39680)
docs(core): clarify `Runnable` pipe coercion [closes #39075] (#39707)
fix(core): finalize chain-group runs on `BaseException` (#39699)
