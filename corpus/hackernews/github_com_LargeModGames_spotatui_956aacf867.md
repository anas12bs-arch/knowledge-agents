---
title: "Show HN: Spotatui, a Spotify TUI/GUI without web API rate limits"
url: "https://github.com/LargeModGames/spotatui"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-10-13T22:00:11Z"
metadata:
  score: "32"
---

# Show HN: Spotatui, a Spotify TUI/GUI without web API rate limits

> Source: hackernews | Category: news | 2026-10-13T22:00:11Z

Score: 32 | Comments: 2

About 11 months ago i revived the amazing but unfortunately unmaintained spotify-tui. Since then I have been working on it almost non stop, finding a lot of problems on the way.<p>One of the main issues I ran into were the Spotify web API rate limits. Third party clients like spotatui are dependent on a developer app made in the Spotify developer dashboard, which get rate limited a lot and Spotify has slowly been deprecating endpoints from it. The workaround for this used to be using a shared client id from ncspot but unfortunately that got rate limited too. This is when i started adding other playback sources, including YouTube, Navidrome&#x2F;Subsonic, Internet radio with +- 30.000 stations, local files, Qobuz for lossless audio and Apple Music for macOS only where it controls the music app remotely.<p>I fixed both the deprecated endpoints and the rate limits with one solution. It still uses librespot in the back, my spotatui specific fork, but gets all data from it instead of only playback. The data comes from the internal API of the official clients, that API gives metadata, playlists, the user library, devices, lyrics and audio analysis. For searching it uses Pathfinder, the internal GraphQL API.<p>There are no web API rate limits because there is no shared app quota. Every user uses their own session as if it was the official client. The only potential problem is that Spotify does not document this API so any change on their side would break it. I intend to fix any of those issues as soon as they pop up.<p>It all started as a TUI back in 2019 but since then I&#x27;ve added a GUI to it too. The GUI is still a bit behind the TUI in terms of features, it only ships Spotify for now, but full parity between the TUI and GUI is coming soon. After that full parity with the official client is next. That is also why I made the GUI looks almost the same as the official client. That way its easier for me and users to find missing features.<p>Spotatui also has lua scripting support, a optional Web companion on spotatui.com, and if you have a AI coding agent like ChatGPT codex or Claude Code you can enable the MCP tools, which lets AI become your personal DJ just by talking to it.<p>Its written in Rust, uses ratatui for the terminal UI and Tauri 2 for the GUI. The Rust core starts a small web server with localhost that only your pc can reach which the GUI then serves. Both frontends share the same playback logic, the same login and the same Spotify code. The only difference is how you interact with it.<p>On first launch it opens a web browser where you need to login with your Spotify premium account (premium is not optional), that is the whole setup done. I would love any feedback about bugs you encounter or features you would like to see.
GitHub: <a href="https:&#x2F;&#x2F;github.com&#x2F;LargeModGames&#x2F;spotatui" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;LargeModGames&#x2F;spotatui</a>
Releases: <a href="https:&#x2F;&#x2F;github.com&#x2F;LargeModGames&#x2F;spotatui&#x2F;releases&#x2F;latest" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;LargeModGames&#x2F;spotatui&#x2F;releases&#x2F;latest</a>
Website: <a href="https:&#x2F;&#x2F;spotatui.com&#x2F;" rel="nofollow">https:&#x2F;&#x2F;spotatui.com&#x2F;</a><p>Thanks to librespot for making this all possible
