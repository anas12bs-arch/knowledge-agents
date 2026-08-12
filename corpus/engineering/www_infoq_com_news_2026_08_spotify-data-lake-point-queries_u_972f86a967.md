---
title: "[infoq] Spotify Builds External Index to Enable Low Latency Point Queries on Its Data Lake"
url: "https://www.infoq.com/news/2026/08/spotify-data-lake-point-queries/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-08-12T15:35:14Z"
metadata:
  {}
---

# [infoq] Spotify Builds External Index to Enable Low Latency Point Queries on Its Data Lake

> Source: engineering | Category: engineering | 2026-08-12T15:35:14Z

Spotify Builds External Index to Enable Low Latency Point Queries on Its Data Lake

Spotify introduced  external indexing architecture for Apache Parquet data lakes that enables low-latency point queries without replicating datasets into operational databases. The approach maps lookup keys to Parquet files and row locations, allowing targeted reads from cloud object storage while supporting analytics, machine learning, AI applications, and online services from the same datasets.   By Leela Kumili
