---
title: "[kubernetes] Gateway API v1.6: TCPRoute and UDPRoute Graduate to Standard"
url: "https://kubernetes.io/blog/2026/08/03/gateway-api-v1-6-release/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-08-03T18:05:02Z"
metadata:
  {}
---

# [kubernetes] Gateway API v1.6: TCPRoute and UDPRoute Graduate to Standard

> Source: devops | Category: infrastructure | 2026-08-03T18:05:02Z

Gateway API v1.6: TCPRoute and UDPRoute Graduate to Standard

The Kubernetes SIG Network community is thrilled to share the release of  Gateway API v1.6.0 , which was released on June 30th of this year! 
 Gateway API has become the standard for modern, role-oriented,
and expressive service networking in Kubernetes.
In previous releases, Gateway API established a production-grade foundation
for HTTP and TLS layer 7 traffic.
With version 1.6.0, Gateway API takes a major step forward by expanding
standard layer 4 protocol routing and introducing cleaner API boundaries for experimental innovation. 
 Here is a quick summary of what's new in Gateway API v1.6.0: 
 
  TCPRoute and UDPRoute Graduate to Standard : Raw L4 TCP and UDP traffic routing reach GA stability in the  v1  API version. 
  Experimental API Group Separation : Experimental resources transition to a distinct API group ( gateway.networking.x-k8s.io ) with an  X  prefix to make experimental vs. standard boundaries crystal clear. 
 
 Let's dive into the details! 
 TCPRoute and UDPRoute graduate to Standard    Leads:  Nick Young ,  Ricardo Katz  and  Zac Nixon  
 
  GEP-2644 - TCPRoute  
  GEP-2645 - UDPRoute  
 
 Until now, Gateway API only offered a stable routing model for HTTP and TLS traffic.
Workloads that speak a raw protocol over TCP or UDP - databases,
DNS, VoIP, gaming, IoT telemetry - had no portable way to plug
into a Gateway. Users either fell back to a plain Kubernetes Service,
or to an implementation-specific CRD that doesn't travel between Gateway controllers. 
  TCPRoute  and  UDPRoute  close that gap: they route traffic to backends based on protocol and port alone, no L7 awareness required.
With this release, both have graduated from the Experimental channel to Standard, and moved to the  v1  API version.
The  v1alpha2  version of each was deprecated as of the v1.6 release, and will be removed in a future release. 
 How it works    A Gateway needs a listener that allows TCPRoute attachment: 
      apiVersion  :     gateway.networking.k8s.io/v1
