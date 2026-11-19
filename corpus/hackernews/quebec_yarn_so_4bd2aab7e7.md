---
title: "Show HN: An API for word timestamps from speech, 75% within 20ms"
url: "https://quebec.yarn.so"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-11-19T12:28:40Z"
metadata:
  score: "27"
---

# Show HN: An API for word timestamps from speech, 75% within 20ms

> Source: hackernews | Category: news | 2026-11-19T12:28:40Z

Score: 27 | Comments: 5

Hey HN, we&#x27;re Yarn (W24) and we make a video editing app for startups, and we built Quebec (<a href="https:&#x2F;&#x2F;quebec.yarn.so">https:&#x2F;&#x2F;quebec.yarn.so</a>), an API that gives you accurate word timestamps from speech. We needed it because cutting a word even 50ms off from its true timing can ruin talking head footage (examples in the write up).<p>Accurate word timestamps usually come from a forced aligner, which takes the speech audio and a transcript and works out exactly when each word starts and ends. We weren&#x27;t satisfied with the accuracy of Montreal Forced Aligner (MFA) or new models like ElevenLabs Cue (<a href="https:&#x2F;&#x2F;elevenlabs.io&#x2F;blog&#x2F;cue-aligner" rel="nofollow">https:&#x2F;&#x2F;elevenlabs.io&#x2F;blog&#x2F;cue-aligner</a>). Giving LLMs access to a waveform&#x2F;spectrogram didn&#x27;t help much either.<p>So we built our own. There are two particularly interesting parts:
- We wrote our own decoder around MFA&#x27;s acoustic model that only lets each word land within 200ms of the rough timings. That made search small enough to solve exactly, so we don&#x27;t need to use MFA&#x27;s beam search.
- We added a small CNN, built on the first two layers of Whisper Tiny, that nudges each word boundary by up to 50ms. We couldn&#x27;t find enough hand-labelled speech that allowed for commercial use, so we had Gemini label our own (17k word boundaries). It took a couple of hours and cost under $200. A net trained on Gemini&#x27;s labels scored the same as one trained on human labels (73.9% vs. 74%).<p>One way to measure accuracy is % of word boundaries within 20ms of hand labels. Here are the results on Buckeye (hand-labelled American speech that we didn&#x27;t train on):<p>- Quebec 75%<p>- MFA 61%<p>- ElevenLabs Cue 30%<p>If you want to try it, it&#x27;s free until tomorrow night. 
You can point your agent at our docs at <a href="https:&#x2F;&#x2F;quebec.yarn.so">https:&#x2F;&#x2F;quebec.yarn.so</a>, and send audio on its own or with your own transcript. After that, it costs $0.32 per hour with no signup (minimum $10 top-up). We serve it at cost. Caveats: only tested in English and slower than ElevenLabs.<p>Let us know if Quebec works well for you, and send us any samples that work badly (you can email support at yarn dot so). Also let us know if you&#x27;ve built or found a better aligner. In theory we would just switch to a better aligner, although we would probably just push a bit harder to make ours better.<p>Thanks!<p>Jasper
