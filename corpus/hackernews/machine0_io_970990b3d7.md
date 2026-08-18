---
title: "Launch HN: machine0 (YC S26) – Persistent CPU and GPU VMs from the CLI"
url: "https://machine0.io"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-08-18T16:49:20Z"
metadata:
  score: "6"
---

# Launch HN: machine0 (YC S26) – Persistent CPU and GPU VMs from the CLI

> Source: hackernews | Category: news | 2026-08-18T16:49:20Z

Score: 6 | Comments: 2

Hi HN! I’m Barnaby, founder of machine0 (<a href="https:&#x2F;&#x2F;machine0.io">https:&#x2F;&#x2F;machine0.io</a>). I’m building a CLI for long horizon agent compute: `machine0 new mybox` gives your agent a persistent cloud VM, billed by the minute, from $0.013&#x2F;hr up to 60 vCPU &#x2F; 240 GB RAM and GPUs (H100s, H200s etc), with 99.99% VM level uptime. Agents self drive via CLI or MCP.<p>Demo: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=gyllkZ0M04E" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=gyllkZ0M04E</a><p>Agent workloads are moving from ephemeral to always-on. A coding agent working on a complex feature runs 6-8 hours. Agent orchestrated training &amp; RL runs take days. OpenClaw &amp; Hermes run 24&#x2F;7. As you run more in parallel:<p>- Resources: a few agents on a large codebase saturate RAM and CPU. Model training and RL needs GPUs you don&#x27;t have.<p>- Security: `--yolo` on your personal machine is one prompt injection away from exfiltrated credentials.<p>- Availability: close your laptop and the agent dies mid-task.<p>- Isolation: there&#x27;s no clean line between you and the minimum your agent actually needs.<p>machine0 gives every agent its own computer. It&#x27;s a CLI simple enough that both humans and agents use it without reading docs:
`machine0 new mybox` creates an SSH-ready VM with a static IP and HTTPS endpoint. Always on (with 99.99% VM level uptime) until you switch it off.<p>- Billed by the minute. 1 vCPU &#x2F; 1 GB at $0.013&#x2F;hr up to 60 vCPU &#x2F; 240 GB, plus GPUs from RTX 4000 Ada to 8×H200.<p>- Suspend, snapshot and resume. Making it easy to pause your work, and come back to it later. Or to make a golden master image to stamp out clones for a fleet.<p>- Block storage. Persistent volumes (from 10 GB to 16 TB) that you can manage with intuitive grammar: `--yolo` and attach to your VMs.<p>- Profiles. Bundles of credentials, MCP connections, prompts, and env vars, injected at VM creation. So each agent gets exactly the capabilities you choose, and nothing else.<p>- Agents self-serve. Hand the CLI or MCP server to Claude, Codex, or OpenCode and it manages its own fleet: spin up a box for a build, snapshot it, tear it down.<p>- Reproducible Builds. Using NixOS flakes or Ansible playbooks with Ubuntu.<p>How do people use it today?<p>- Agent fleets. People run a pilot agent that scopes work and delegates it to sub-agents, each on its own VM: shape a project with the pilot, and the workers implement it and open PRs. One customer runs hundreds of machines at once, spun up and torn down from the CLI.<p>- Model optimization &amp; RL environments. ML teams use machine0 for agent-orchestrated RL environments and model optimization work. One customer runs RL environments on 60 vCPU machines that stay up for days at a time; another keeps a suspended H100 around and points an agent at it overnight to grind on inference-speed optimizations.<p>- Product infrastructure. One customer builds their product on top of machine0 rather than using it themselves: every user session gets a fresh XL machine from a versioned image of their own agent runtime. They&#x27;ve shipped hundreds of versions of that image and launched thousands of machines, most alive for two minutes.<p>What’s under the hood?<p>Every machine is a full KVM virtual machine, not a container or sandbox. You get the real GPU exposed to the guest with its actual driver, kernel-level access (load any module or driver you want), and no syscall-interception layer between you and the hardware. The stack itself is deliberately dull: TypeScript, Postgres, Redis. We weigh heavily towards security, reliability and performance making machine0 ideal for sustained compute intensive workloads. 
About me<p>I&#x27;ve been building cloud infrastructure for about 15 years. I dropped out of a PhD at Imperial College London on cloud resource allocation, later spent six years as co-founder and CTO of Upflow (YC W20), owning DevOps, infra and security personally the whole way to 7-figures in ARR because it was too high-stakes to delegate. machine0 started as a tool for me, I’m my own first user :)
Asks<p>Would love you to try it out and give us your feedback (see below). Or if you’re a company looking for compute for software factories, model training or RL environments, feel free to reach out at barnaby@machine0.io<p><pre><code>  # install machine0 
  $ curl -LsSf https:&#x2F;&#x2F;machine0.io&#x2F;install.sh | sh

  # create a machine and ssh in
  $ machine0 new myvm
  $ machine0 ssh myvm</code></pre>
