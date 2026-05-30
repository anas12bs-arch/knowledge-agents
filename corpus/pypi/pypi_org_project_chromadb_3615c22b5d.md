---
title: "PyPI: chromadb v1.5.9"
url: "https://pypi.org/project/chromadb/"
source: "pypi"
category: "skill"
tags: ["pypi", "python", "package", "chromadb"]
date: "2026-05-30T14:32:06Z"
metadata:
  version: "1.5.9"
  package: "chromadb"
---

# PyPI: chromadb v1.5.9

> Source: pypi | Category: skill | 2026-05-30T14:32:06Z

**chromadb** v1.5.9

Chroma.

![Chroma](./docs/assets/chroma-wordmark-color.png#gh-light-mode-only)
![Chroma](./docs/assets/chroma-wordmark-white.png#gh-dark-mode-only)

<p align="center">
    <b>Chroma - the open-source data infrastructure for AI</b>. <br />
</p>

<p align="center">
  <a href="https://discord.gg/MMeYNTmh3x" target="_blank">
      <img src="https://img.shields.io/discord/1073293645303795742?cacheSeconds=3600" alt="Discord">
  </a> |
  <a href="https://github.com/chroma-core/chroma/blob/master/LICENSE" target="_blank">
      <img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg" alt="License">
  </a> |
  <a href="https://docs.trychroma.com/" target="_blank">
      Docs
  </a> |
  <a href="https://www.trychroma.com/" target="_blank">
      Homepage
  </a>
</p>

```bash
pip install chromadb # python client
# for javascript, npm install chromadb!
# for client-server mode, chroma run --path /chroma_db_path
```

## Chroma Cloud

Our hosted service, Chroma Cloud, powers serverless vector, hybrid, and full-text search. It's extremely fast, cost-effective, scalable and painless. Create a DB and try it out in under 30 seconds with $5 of free credits.

[Get started with Chroma Cloud](https://trychroma.com/signup)

## API

The core API is only 4 functions (run our [💡 Google Colab](https://colab.research.google.com/drive/1QEzFyqnoFxq7LUGyP1vzR4iLt9PpCDXv?usp=sharing)):

```python
import chromadb
# setup Chroma in-memory, for easy prototyping. Can add persistence easily!
client = chromadb.Client()

# Create collection. get_collection, get_or_create_collection, delete_collection also available!
collection = client.create_collection("all-my-documents")

# Add docs to the collection. Can also update and delete. Row-based API coming soon!
collection.add(
    documents=["This is document1", "This is document2"], # we handle tokenization, embedding, and indexing automatically. You can skip that and add your own embeddings as well
    metadatas=[{"source": "notion"}, {"source": "google-docs"}], # filter on these!
    ids=["doc1", "doc2"], # unique for each doc
)

# Query/search 2 most similar results. You can also .get by id
results = collection.query(
    query_texts=["This is a query document"],
    n_results=2,
    # where={"metadata_field": "is_equal_to_this"}, # optional filter
    # where_document={"$contains":"search_string"}  # optional filter
)
```

Learn about all features on our [Docs](https://docs.trychroma.com)

## Get involved

Chroma is a rapidly developing proj
