---
title: "[kubernetes] How to Pretty-Print Your Kubernetes YAML as KYAML and Why You'd Want To"
url: "https://kubernetes.io/blog/2026/08/11/how-to-pretty-print-kubernetes-yaml-as-kyaml/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-08-12T04:26:14Z"
metadata:
  {}
---

# [kubernetes] How to Pretty-Print Your Kubernetes YAML as KYAML and Why You'd Want To

> Source: devops | Category: infrastructure | 2026-08-12T04:26:14Z

How to Pretty-Print Your Kubernetes YAML as KYAML and Why You'd Want To

YAML has been the standard way to write Kubernetes manifests for years. Every example, tutorial, and configuration file you come across is written in it. The problem isn't that YAML is a bad format. It's that YAML gives you a lot of choices, and not all of them are equally good for writing Kubernetes manifests. Some features make files harder to read, some are easy to misuse and others can lead to surprising behavior. 
 The interesting part is that Kubernetes doesn't actually need most of those features. It only relies on a small subset of YAML. This led to a simple question: if Kubernetes only needs a small part of YAML, why not  standardize  on that part and avoid the rest? Instead of introducing a new configuration language,  SIG CLI  introduced  KYAML , a stricter, more consistent way to write YAML. 
 What is KYAML?      KYAML is a strict subset (or &quot;dialect&quot;) of standard YAML, designed to be parseable by the existing ecosystem without any changes, as proposed in  KEP 5295 .   It does not introduce a new format or a new parser. It just narrows the scope of choices you make when writing YAML, so everyone ends up making the same ones. 
 Think of it less like a new language and more like an agreed-upon style.   Everything valid in KYAML is valid YAML.   
 How KYAML solves it    Standard YAML has a few well-known traps and JSON is not without its own. 
  Whitespace sensitivity.  Indentation defines structure in YAML, which means a wrongly indented file can remain syntactically valid while representing a different object than intended. This gets especially painful with templating tools like Helm, where you are manipulating indentation from outside the YAML context. 
  Silent type coercion.  String quoting is optional in YAML, which sounds convenient until it is not. Some values that look like strings get coerced into other types without warning. The classic example is the  &quot;Norway Bug&quot; . 
      country  :     NO  
       In standard YAML,  NO  i
