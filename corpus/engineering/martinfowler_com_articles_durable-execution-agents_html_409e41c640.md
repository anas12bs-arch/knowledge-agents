---
title: "[martin-fowler] Long-horizon agents and durable execution"
url: "https://martinfowler.com/articles/durable-execution-agents.html"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "martin-fowler"]
date: "2026-11-10T17:43:42Z"
metadata:
  {}
---

# [martin-fowler] Long-horizon agents and durable execution

> Source: engineering | Category: engineering | 2026-11-10T17:43:42Z

Long-horizon agents and durable execution

Long-horizon agents can automate complex tasks that take days or weeks
     to complete and involve multiple exchanges with people and external
     systems. Many things can go wrong during this time, including process
     crashes, network failures, and unanticipated real-world behavior.
      Kiran Prakash  explains durable execution: an emerging
     pattern that helps agents recover from these failures and move towards
     their goal. In this programming model, the runtime keeps a record of the
     result of each step that interacts with the outside world so that, when a
     failure occurs, the program runs again, completed steps are skipped, and
     the program's state is rebuilt from the record. 

  more…
