---
title: "Show HN: Overtone – Transcribe, correct and cut captions for any screen shape"
url: "https://github.com/lonthq/overtone-captions"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-10-29T20:30:42Z"
metadata:
  score: "8"
---

# Show HN: Overtone – Transcribe, correct and cut captions for any screen shape

> Source: hackernews | Category: news | 2026-10-29T20:30:42Z

Score: 8 | Comments: 0

Hi HN, I&#x27;m Ruud, co-founder of Lont. We turn company emails into personalized videos.<p>Video captions cost us manual work twice: fixing misheard words, then fixing layout, like lines ending on “the”.<p>Overtone uses multiple models to listen to the audio: gpt-transcribe, Azure STT, and Elevenlabs Scribe. When they return conflicting results, Overtone sends small clips to the models again, and then lets an LLM decide what was actually said.<p>The LLM is like a human doing a sanity check on the transcription model. Humans would easily recognize a word to be different based on context. The LLM basically does the same, using an optional context prompt + its world knowledge. Because of this the Word Error Rate (WER) on many test files is lower when using Overtone, compared to just using a model without it.<p>Sure, the cost is higher because we use up to 3 different STT models + an LLM, but it still removes mistakes, reducing the time needed to fix captions to a minimum, and reducing the chance you&#x27;ll miss something. For us it&#x27;s worth it. For ultra high volume use cases it may not be.<p>The rules-based cutter nicely cuts the transcript into captions that look good, depending on screen size: 16:9 is different from 9:16, and the Overtone Format we created supports any type really. Pauses become breaks, captions are grouped per speaker, and names&#x2F;numbers are never spread out over multiple captions.<p>How to add these captions to your videos? A videojs plugin can do this automatically, so you don&#x27;t burn in your captions. The plugin lets you cycle between styled captions, plain captions, and off. You can burn them into an MP4 file with overtone burn.<p>Quickly try it out just the cutter? Try:<p><pre><code>  npx overtone-captions recut yoursub.srt
</code></pre>
Transcribing audio with API keys works too. Use --dry-run to show a cost estimate before you send.<p>We open-sourced this first version (MIT) because we believe many people can benefit from this, especially if your captions just need to be good. There&#x27;s plenty of room to improve though, so we&#x27;ve made it easy to help contribute to add style packs, languages, and providers&#x2F;models.<p>You can find a demo at: <a href="https:&#x2F;&#x2F;overtone.lont.ai&#x2F;" rel="nofollow">https:&#x2F;&#x2F;overtone.lont.ai&#x2F;</a><p>Find the code and benchmarks here: <a href="https:&#x2F;&#x2F;github.com&#x2F;lonthq&#x2F;overtone-captions" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;lonthq&#x2F;overtone-captions</a>
