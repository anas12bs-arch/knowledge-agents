---
title: "Show HN: Live breath detection and biofeedback from a phone microphone"
url: "https://github.com/shiihaa-app/shiihaa-breath-detection"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-06-02T22:13:27Z"
metadata:
  score: "15"
---

# Show HN: Live breath detection and biofeedback from a phone microphone

> Source: hackernews | Category: news | 2026-06-02T22:13:27Z

Score: 15 | Comments: 7

Hi everyone, I am Felix, a famliy doctor from ZH, Switzerland. 
A couple of month ago I started this little project called 
shii • haa, a breathing app that uses the phone`s microphone 
for live biofeedback<p>My prior work in emergency medicine and intensive care was 
closesly linked to breathing, mostly in critical situations...
and let me to reevaluate my own way of breathing. over time 
one question popped into my mind: can medical knowledge and 
biofeedback make an app actually promote self-awareness instead 
of attaching your goals to the award system of the app.<p>it combines signal processing, a breathing state machine and ML. 
The state machine follows inhale, exhale and transitions in the 
mic signal. A quality layer rejects noisy or ambiguous windows 
before signals are used for feedback. All processing is done 
on-device, no speech or raw audio is uploaded.<p>What I&#x27;m trying to avoid is turning breathing into another score 
or game. The app gives feedback on rhythm, depth and regularity, 
but the point is more &quot;notice what you are doing&quot; than &quot;perform 
well&quot;.<p>I&#x27;d be interested in feedback, especially from people who have 
worked on signal processing, health UX, or Android&#x2F;iOS audio 
issues.
