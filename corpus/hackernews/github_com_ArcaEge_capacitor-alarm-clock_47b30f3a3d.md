---
title: "Show HN: Capacitor Alarm Clock"
url: "https://github.com/ArcaEge/capacitor-alarm-clock"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-06-17T13:01:06Z"
metadata:
  score: "52"
---

# Show HN: Capacitor Alarm Clock

> Source: hackernews | Category: news | 2026-06-17T13:01:06Z

Score: 52 | Comments: 17

I made an alarm clock that blows up capacitors to wake you up.<p>There are more details on the Github repo but it&#x27;s made from an esp32-c3 as the microcontroller, with 3 capacitor slots. There are relays on each capacitor slot to put 15v reverse voltage on the capacitor, with 5.1 ohm resistors on each slot for current limiting in case the capacitor shorts out. I also chucked in an SSD1315 OLED to show the time and a menu to configure it, although there&#x27;s a web UI as well. The esp32 also means you can fetch the time from NTP.<p>It also functions as a small heater since I used LDOs to step down 15v to 3.3v for the esp32, I was lazy and didn&#x27;t use a buck converter circuit :)
