---
title: "Show HN: VolAnti – Open-source acoustic detector for fibre-optic FPV drones"
url: "https://github.com/agamrossen/VolAnti"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-09-09T04:57:05Z"
metadata:
  score: "5"
---

# Show HN: VolAnti – Open-source acoustic detector for fibre-optic FPV drones

> Source: hackernews | Category: news | 2026-09-09T04:57:05Z

Score: 5 | Comments: 0

This project has been a month in the making, and 9 fully functional units will be sent tomorrow to an undisclosed civilian site across the Israel - Lebanon border. All of my findings are shared online to anyone on the globe who could benefit from them, or make their own units.<p>I&#x27;m an engineering student at the University of York, originally from Israel, studying in England.<p>I too often have been hearing about tragic cases involving civilians in war zones being chased and attacked by small FPV drones mounted with an explosive. Especially around the north of Israel, Ukraine and Russian. My intentions for this project were clear: create a device small, portable and cheap enough for civilian use, that could drastically change the outcome of a drone infiltration through early alerting.<p>I decided to dedicate a month of my summer to go back to the university labs and to work on this as personal project.<p>These drone attacks are not run on normal wireless drones, instead they are run on small FPV drones that are connected to the operator through a long spool of fibre optic cable. This simply means that drone detection through Radio, the current industry standard, is not applicable.<p>My solution was to build an acoustic detector. A device that uses 4 MEMS microphones to capture the drone&#x27;s propellers&#x27; emitted noise as they cut through the air, runs that data through several algorithms to enhance the SNR, reduce noise (directional, possible confusers), recognises their comb looking shape when plotted by frequency, and alert the user through multiple outputs (display, beeper, buzzer, led) along with alerting all nearby units using a LoRa module also fitted in the device.<p>The units have been tested against a custom drone rig, housing the exact same specs as the drones used in the Israel-Lebanon border (four 2807 motors, 7 in tri blades, FPV airframe), which was stationed 104.2m away from the device in a street with passer-by&#x27;s and mild wind. That test ran successfully and the device was able to detect the drone.<p>This device was built for detection and alerting only, so no jamming.<p>Every online resource i could think of in regarding this project exists in the Github, along with a neat website that shows off more media with explanations, also housing a live detector simulation that runs in the browser: <a href="https:&#x2F;&#x2F;volantitech.com&#x2F;#simulator" rel="nofollow">https:&#x2F;&#x2F;volantitech.com&#x2F;#simulator</a>
