---
title: "[infoq] AWS Nitro Sandboxes Put Each EKS Pod in Its Own MicroVM with One RuntimeClass Field"
url: "https://www.infoq.com/news/2026/11/aws-nitro-sandboxes-eks/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-11-16T17:33:20Z"
metadata:
  {}
---

# [infoq] AWS Nitro Sandboxes Put Each EKS Pod in Its Own MicroVM with One RuntimeClass Field

> Source: engineering | Category: engineering | 2026-11-16T17:33:20Z

AWS Nitro Sandboxes Put Each EKS Pod in Its Own MicroVM with One RuntimeClass Field

AWS has launched Nitro Sandboxes, running each opted-in EKS pod, ECS task or EC2 workload in its own Firecracker microVM with a separate kernel, enabled by one runtimeClassName field at no extra charge. A confidential mode adds attestation-gated key release. The documentation lists the trade-offs: no GPU passthrough, at most five sandboxes per vCPU, and half the compute on SMT instances.   By Steef-Jan Wiggers
