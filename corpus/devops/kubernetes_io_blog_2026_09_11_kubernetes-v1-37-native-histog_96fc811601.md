---
title: "[kubernetes] Kubernetes v1.37: Native Histograms Graduates to Beta"
url: "https://kubernetes.io/blog/2026/09/11/kubernetes-v1-37-native-histograms-beta/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-09-12T02:04:13Z"
metadata:
  {}
---

# [kubernetes] Kubernetes v1.37: Native Histograms Graduates to Beta

> Source: devops | Category: infrastructure | 2026-09-12T02:04:13Z

Kubernetes v1.37: Native Histograms Graduates to Beta

I'm excited to announce that native histogram support for Kubernetes metrics is graduating to Beta and is enabled by default in Kubernetes v1.37! 
  Native histograms  (previously introduced as Alpha in Kubernetes v1.36 under  KEP-5808 )
bring high-resolution, low-cardinality observability to Kubernetes metrics.
By adopting  Prometheus Native Histograms , Kubernetes components now expose latency and duration metrics with far greater accuracy while significantly reducing telemetry storage and scraping overhead. 
 Why move beyond classic histograms?    Since the early days of Kubernetes observability, duration and latency metrics (such as API server request latencies or scheduling durations) have relied on  classic Prometheus histograms . 
 Classic histograms require metric authors to define a static list of cumulative bucket boundaries ( le  labels), such as  0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 10 . While familiar, this approach introduces three major challenges: 
 
  The Bucket Guessing Game : If a workload's latency profile changes, for example, shifting into microsecond ranges or experiencing long-tail tail latencies beyond the highest bucket, the histogram loses visibility. Specifying bucket boundaries upfront requires knowing the distribution before observing it 
  High Cardinality &amp; Storage Cost : With classic histograms, each bucket boundary is exported as a separate time series ( _bucket{le=&quot;...&quot;} ). A histogram with 10 buckets across multiple labels multiplies the number of time series by 10, increasing memory consumption in Prometheus and inflating time series database (TSDB) storage costs 
  Interpolation Error in Quantiles : Calculating percentiles using  histogram_quantile()  relies on linear interpolation between static bucket boundaries. When bucket spans are coarse, quantile calculations can suffer from significant estimation error 
 
 What are Prometheus native histograms?     Prometheus Native Histograms  replace sta
