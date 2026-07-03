---
title: "Show HN: Opbox – CRDT based sync for text files on disk"
url: "https://www.opbox.dev/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-03T21:20:04Z"
metadata:
  score: "4"
---

# Show HN: Opbox – CRDT based sync for text files on disk

> Source: hackernews | Category: news | 2026-07-03T21:20:04Z

Score: 4 | Comments: 0

Hi! I’m one of the founders of s2.dev, and recently have been hacking on opbox, which is an open-source daemon that turns directories of text files (code, markdown, etc) into collaborative, multi-player workspaces.<p>This started as a bit of an intellectual curiosity, to see if it was possible to do real-time sync at the filesystem level (i.e., in an editor-agnostic way).<p>The idea is pretty simple:<p><pre><code>  - Opbox workspaces are roughly analogous to git repositories (and can be used alongside existing git repos, to share live changes between commits)
  - When the opbox daemon is running in a workspace (ob start), it listens for local filesystem events within its directory (writes, deletes, new files), and translates them into operations (the titular “op”) on shadow CRDT documents (Yrs) corresponding to each text file (as well as one doc for the namespace as a whole, which handles paths)
  - These shadow CRDT docs are maintained in a workspace-local sqlite db (Turso)
  - The ops, which represent diffs on a corresponding CRDT document, are then appended to a durable stream (S2) that acts as a shared journal for all sync participants
  - Opbox also reads from that journal, receiving ops from other participants, which are then used to update the local documents, first in the db, then by materializing them into actual files on disk
</code></pre>
This has worked surprisingly well for sharing things like Obsidian graphs in real-time.<p>It’s most helpful in cases where you want the ability to edit local files from arbitrary editors, but still collaborate live. The experience is best from editors where you can configure an aggressive autosave policy, and where edits to an open file are reflected in the editor in a timely way.<p>To gain confidence in the correctness of the core opbox flows (particularly all the nuances around bidirectional sync) I invested in wiring up deterministic simulation testing using the turmoil library, which has been incredibly helpful (see the opbox-sim crate in the repo).
