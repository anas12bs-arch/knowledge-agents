---
title: "[infoq] Pinterest Uses Event Time Watermarks to Finalize Petabyte Scale Data Partitions"
url: "https://www.infoq.com/news/2026/10/pinterest-event-time-partition/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-10-19T19:29:26Z"
metadata:
  {}
---

# [infoq] Pinterest Uses Event Time Watermarks to Finalize Petabyte Scale Data Partitions

> Source: engineering | Category: engineering | 2026-10-19T19:29:26Z

Pinterest Uses Event Time Watermarks to Finalize Petabyte Scale Data Partitions

Pinterest has introduced event time-based partition finalization for its database ingestion framework. The mechanism uses Apache Flink to track event time and Apache Iceberg metadata to publish a non-regressing watermark, helping downstream jobs determine when continuously ingested CDC data is sufficiently complete for processing.   By Leela Kumili
