---
title: "[infoq] CSIRO Uses Serverless Architecture to Query 100x More Genomic Variants on AWS"
url: "https://www.infoq.com/news/2026/10/csiro-serverless-genomic-variant/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-10-23T16:17:30Z"
metadata:
  {}
---

# [infoq] CSIRO Uses Serverless Architecture to Query 100x More Genomic Variants on AWS

> Source: engineering | Category: engineering | 2026-10-23T16:17:30Z

CSIRO Uses Serverless Architecture to Query 100x More Genomic Variants on AWS

CSIRO has developed Serverless Beacon, a serverless architecture for querying genomic variants without copying VCF files into a central database. The system combines Amazon S3, Lambda, Athena and DynamoDB, using metadata indexes and HTTP byte range requests to query compressed genomic regions. Tests reported 1.52 second average latency for 10,000 base pair queries.   By Leela Kumili
