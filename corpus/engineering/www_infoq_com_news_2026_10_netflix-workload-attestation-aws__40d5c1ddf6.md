---
title: "[infoq] Netflix Bridges AWS IAM and Internal Identity with Workload Attestation"
url: "https://www.infoq.com/news/2026/10/netflix-workload-attestation-aws/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-10-21T16:07:22Z"
metadata:
  {}
---

# [infoq] Netflix Bridges AWS IAM and Internal Identity with Workload Attestation

> Source: engineering | Category: engineering | 2026-10-21T16:07:22Z

Netflix Bridges AWS IAM and Internal Identity with Workload Attestation

Netflix has developed a workload attestation mechanism for Apache Spark jobs running on Amazon EMR. The design combines AWS IAM identity with signed claims from Netflix’s control plane before issuing short-lived internal X.509 certificates, allowing managed compute workloads to authenticate to internal services without directly injecting credentials.   By Leela Kumili
