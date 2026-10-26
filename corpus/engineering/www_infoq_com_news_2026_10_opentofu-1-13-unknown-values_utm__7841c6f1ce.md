---
title: "[infoq] OpenTofu 1.13 Lets Module Authors Reduce Unknown Values at Plan Time"
url: "https://www.infoq.com/news/2026/10/opentofu-1-13-unknown-values/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-10-26T22:57:07Z"
metadata:
  {}
---

# [infoq] OpenTofu 1.13 Lets Module Authors Reduce Unknown Values at Plan Time

> Source: engineering | Category: engineering | 2026-10-26T22:57:07Z

OpenTofu 1.13 Lets Module Authors Reduce Unknown Values at Plan Time

OpenTofu 1.13 adds convert and assume... functions that let module authors give the planner type and value hints for unknown values, so more expressions resolve during tofu plan. If a value unknown during planning later violates a guarantee, OpenTofu reports an error during apply.   By Mark Silvester
