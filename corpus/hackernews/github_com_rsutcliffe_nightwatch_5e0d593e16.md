---
title: "Show HN: Nightwatch – a Mac menu-bar app that tells you when tonight is clear"
url: "https://github.com/rsutcliffe/nightwatch"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-10-06T01:33:44Z"
metadata:
  score: "72"
---

# Show HN: Nightwatch – a Mac menu-bar app that tells you when tonight is clear

> Source: hackernews | Category: news | 2026-10-06T01:33:44Z

Score: 72 | Comments: 11

Here in the north of England clear nights are at a premium, and it&#x27;s never guaranteed that you&#x27;ll be able to see anything but cloud. That&#x27;s why I developed Nightwatch, so that I could be notified when one of those precious few nights where I could see into the heavens was available. Finding out whether tonight was worth setting up meant reading forecast charts every evening, usually to learn that it was not. Nightwatch does that reading for me.<p>It sits in the Mac&#x27;s menu bar and refreshes the forecast every 30 minutes. An hour before sunset it sends one notification, and only if there is an unbroken run of clear sky in astronomical darkness long enough to image in. Otherwise it says nothing: no news means &quot;clouds&quot;.<p>I hope this is useful for other hobbyist stargazers too!<p>When I was a child I wanted desperately to be an astronaut or a dinosaur. I&#x27;m now old enough to be the latter and was born in a country where the former was never an option. I&#x27;ve had a fascination with the stars since a a friend of my father gifted me a telescope, and have faded memories of sharing time with my father staring at the stars. My father passed away a few years back and the memory of those nights came back, along with the want to share the same experience with my kids and grandchild.<p>The app uses two forecasts: Apple&#x27;s WeatherKit is the main source and Open-Meteo is a second opinion. When they disagree, the alert says so instead of averaging them.<p>Thin high cloud counts for half. Stacking many short frames works through a veil of cirrus, so treating it as full cloud threw away usable nights.<p>It works on your own horizon: hills come from terrain data, and you set the houses and trees in each direction, so they are accounted for when it says what is up.<p>It works out, a year ahead, when the Moon will pass in front of a planet, a bright star or the Pleiades as seen from your site.<p>You don&#x27;t need an account. What leaves the Mac is the coordinates of the place being forecast, sent to the forecast and sky-survey services listed in PRIVACY.md.<p>Limits: Mac only, and the aurora alerts are UK only. The worldwide light-pollution data is new this week. I have checked it against Britain&#x27;s finer grid and a handful of cities, so I would especially like to hear from people elsewhere whether the darkness it suggests for your site looks right.
