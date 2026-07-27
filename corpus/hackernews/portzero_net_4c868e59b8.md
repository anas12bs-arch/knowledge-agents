---
title: "Show HN: Port Zero – how I learned to stop worrying and love PORT=0"
url: "https://portzero.net/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-27T01:11:53Z"
metadata:
  score: "3"
---

# Show HN: Port Zero – how I learned to stop worrying and love PORT=0

> Source: hackernews | Category: news | 2026-07-27T01:11:53Z

Score: 3 | Comments: 0

Hi HN,<p>Recently I wasted several hours wrangling my dev environment only to find out that the browser frontend was talking to the wrong version of the backend. This got me thinking--why on earth are we still using simple <i>numbers</i> to describe which process to connect to? Why not use <i>names</i> instead? I thought of all the times a program wouldn&#x27;t start because of port conflicts. The more I thought about it, the crazier it seemed.<p>Modern operating systems already offer no-conflict ports: if you make your TCP server listen on port 0, the OS assigns you a random available port. But that only solves half the problem.<p>I built the other half: PortZero. It&#x27;s a GPLv3 program that watches for processes (and docker containers!) with a special PZ_TUNNEL environment variable:<p><pre><code>  PZ_TUNNEL=myapp-{branch}.portzero.local:80 npm run dev
</code></pre>
When it sees such a process or container, PortZero does this:<p>1. Create a virtual NIC (if it hasn&#x27;t already)<p>2. Create a new virtual IP address<p>3. Create a DNS record that substitutes things like {branch} based on the working directory of the process, and points at that virtual IP address<p>4. Start listening on that virtual IP address on the port of your choice (e.g. port 80 for http, port 443 for https, port 5432 for postgresql)<p>5. Forward any TCP connections to that virtual IP address &#x2F; virtual port to the random, OS-assigned port that your process or container is actually listening on<p>The result is you don&#x27;t have to think about ports anymore, you just have to think about subdomains. You can have multiple services available on port 80 without conflicts, as long as they have different portzero.local subdomains.<p>It does some other cool stuff like:<p>- Enable HTTPS on local HTTP services by creating a local CA and registering it on your machine<p>- Enable cloud tunnels so you can access your apps on other devices (paid feature)<p>Links:<p><a href="https:&#x2F;&#x2F;portzero.net&#x2F;docs&#x2F;" rel="nofollow">https:&#x2F;&#x2F;portzero.net&#x2F;docs&#x2F;</a><p><a href="https:&#x2F;&#x2F;github.com&#x2F;PortZeroNetwork&#x2F;portzero" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;PortZeroNetwork&#x2F;portzero</a>
