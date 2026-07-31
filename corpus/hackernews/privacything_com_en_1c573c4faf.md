---
title: "Show HN: I built a cross-browser extension that controls fingerprinting surfaces"
url: "https://privacything.com/en/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-31T16:18:04Z"
metadata:
  score: "4"
---

# Show HN: I built a cross-browser extension that controls fingerprinting surfaces

> Source: hackernews | Category: news | 2026-07-31T16:18:04Z

Score: 4 | Comments: 0

Hello Hacker News! I’m Tomasz, creator of Privacy Thing, a browser extension for Firefox and Chromium-based browsers. I’ve just released its Preview version.<p>Privacy Thing aims to reduce browser fingerprinting—the tracking of users without cookies.<p>It began as an internal project: a simple location simulator. Over time, I expanded it to cover more fingerprinting surfaces. It now has 13 protection categories affecting 50+ browser APIs and methods: Geolocation, time and locale settings, Canvas, WebGL, Audio, Navigator, Screen, Client Hints, Battery, WebRTC, Dedicated Workers, Service Workers, and Shared Workers. The list is still growing.<p>The extension is fully configurable. Users can create regional profiles and assign them to domain rules, with separate protection settings for each domain. Or they can skip domain rules and rely on the global configuration—I’m not here to decide what works best for them :-)<p>Privacy Thing uses Manifest V3, with all its pros and cons. Chrome and Firefox appear to offer similar extension APIs, but differ fundamentally at the level where Privacy Thing operates. This matters because its scripts must load as early as possible to be effective.<p>Its X-Ray module communicates with scripts running in the page context to show which APIs a site uses and how often it queries them. An aggregate count appears on the extension’s toolbar badge by default.<p>Each release includes processed, compact datasets covering Chrome build numbers, supported language codes, language-to-country mappings, popular screen resolutions, and hardware configurations. This keeps the extension independent of external services and there is no good reason to build extra infrastructure for it.<p>There are two exceptions. The regional preset wizard uses OpenStreetMap’s Nominatim geocoding service, but only after the user consents to sending the query. Maps are displayed using OpenFreeMap.<p>Presets can also be created manually. Users who know the coordinates can enter them directly without contacting any 3rd-party service.<p>The extension does not transmit telemetry or usage data. This makes development harder, but it is fundamental to its identity: user data belongs to the user. Privacy Thing configuration can be exported, edited and imported.<p>The Preview is currently distributed under a proprietary license. This is not ideal; I ultimately intend to release the source under an open-source license, most likely the AGPL.<p>More about the development process:
<a href="https:&#x2F;&#x2F;tomaszjanusz.dev&#x2F;en&#x2F;projects&#x2F;privacy-thing&#x2F;" rel="nofollow">https:&#x2F;&#x2F;tomaszjanusz.dev&#x2F;en&#x2F;projects&#x2F;privacy-thing&#x2F;</a><p>Download:<p>- Mozilla Addons:
<a href="https:&#x2F;&#x2F;addons.mozilla.org&#x2F;en-US&#x2F;firefox&#x2F;addon&#x2F;privacy-thing&#x2F;" rel="nofollow">https:&#x2F;&#x2F;addons.mozilla.org&#x2F;en-US&#x2F;firefox&#x2F;addon&#x2F;privacy-thing...</a><p>- Chrome Web Store:
<a href="https:&#x2F;&#x2F;chromewebstore.google.com&#x2F;detail&#x2F;privacy-thing-preview&#x2F;aklkmohdkhakelpdigmbpkfepebgceji" rel="nofollow">https:&#x2F;&#x2F;chromewebstore.google.com&#x2F;detail&#x2F;privacy-thing-previ...</a><p>The extension is STILL under review in the Microsoft Edge Add-ons store -_-<p>Thank you for your suggestions and feedback. Please remember that this is still a preview: some things may not work, may be slower, or may not behave as intended. I sincerely hope such issues will be few and far between.<p>P.S. Yes, Privacy Thing fully supports Firefox Containers. I like the concept and believe extensions should support containers whenever possible. Privacy Thing will support them elsewhere too, including Brave, if Brave Software makes its container API public.
