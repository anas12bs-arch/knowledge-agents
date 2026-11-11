---
title: "[martin-fowler] Tests as data: ensuring AI-generated code does what we want"
url: "https://martinfowler.com/articles/tests-as-data.html"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "martin-fowler"]
date: "2026-11-11T17:11:31Z"
metadata:
  {}
---

# [martin-fowler] Tests as data: ensuring AI-generated code does what we want

> Source: engineering | Category: engineering | 2026-11-11T17:11:31Z

Tests as data: ensuring AI-generated code does what we want

Automated testing in the age of AI coding assistants is problematic:
     when AI agents write both production and test code, developers risk losing
     the assurance that automated tests protect against functional errors.
      Matteo Vaccari  makes three claims: (1) when AI writes the
     code, developers become its customers; (2) therefore customer tests, not
     developer tests, become the primary contract between humans and AI; (3)
     moving that contract into test data rather than test code makes it easier
     to protect it from unexpected modifications by coding agents. All of this
     optimizes for human-readable tests that establish a contract between humans
     and AI. While in the past DSL parsers and custom test runners were
     expensive to write and maintain, now AI makes them cheap. 

  more…
