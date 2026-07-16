---
title: "Show HN: Leaves – a text-UI disk usage treemap visualizer"
url: "https://github.com/patonw/leaves"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-16T16:54:34Z"
metadata:
  score: "4"
---

# Show HN: Leaves – a text-UI disk usage treemap visualizer

> Source: hackernews | Category: news | 2026-07-16T16:54:34Z

Score: 4 | Comments: 0

GUI disk analyzers are great for figuring out what&#x27;s filling up your laptop&#x2F;desktop drive.<p>On containers or remote servers, the options are limited to purely text based
utilities (e.g. du) or list-centric TUIs (e.g. ncdu) which are usually limited
to viewing one directory at a time.<p>I created <i>leaves</i> to fill that gap.<p>Inspired by classic utilities like WinDirStat and KDirStat, it uses a
2-dimensional treemap^1 visualization to show the entire directory hierarchy
with proportionally sized rectangles.<p>It&#x27;s performant enough to handle millions of files, thanks to Rust and
multi-threading. However, block characters aren&#x27;t as suited as pixels for
resolving a large number of items. Leaves can show file-type summaries per
directory or partition the top-level directories by extension, allowing you to
see not only where space is being used, but also how.<p>For instance, I can see the largest chunk of my home directory is taken up by
uv caches for python and old Linux ISOs that I could easily re-download if
needed. Or in a particular container, +600MB is used by standard Rust
documentation and tutorials, and that it is the only location with HTML&#x2F;JS files,
when only the libraries and build tools are needed (note to self: remember to
use the <i>minimal</i> profile next time).<p>^1: <a href="https:&#x2F;&#x2F;github.com&#x2F;shundhammer&#x2F;qdirstat&#x2F;blob&#x2F;master&#x2F;doc&#x2F;Treemap.md" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;shundhammer&#x2F;qdirstat&#x2F;blob&#x2F;master&#x2F;doc&#x2F;Tree...</a>
