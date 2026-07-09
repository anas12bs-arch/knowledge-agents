---
title: "Show HN: I built a web tool to see and edit what an AI thinks before it answers"
url: "https://lucid.earthpilot.ai"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-09T21:42:19Z"
metadata:
  score: "8"
---

# Show HN: I built a web tool to see and edit what an AI thinks before it answers

> Source: hackernews | Category: news | 2026-07-09T21:42:19Z

Score: 8 | Comments: 0

I run a small AI lab and playground and got super excited about Anthropics paper &quot;Verbalizable Representations Form a Global Workspace in Language Models&quot; (<a href="https:&#x2F;&#x2F;transformer-circuits.pub&#x2F;2026&#x2F;workspace&#x2F;index.html" rel="nofollow">https:&#x2F;&#x2F;transformer-circuits.pub&#x2F;2026&#x2F;workspace&#x2F;index.html</a>)<p>It talks about how they use a tool they call a Jacobian Lens to view inside the middle layers of LLM while it&#x27;s working before it commits to a word (token).<p>I wanted to see if I could get a version of this running on the open models and to my surprise it worked! I ran some experiments with it and build a public facing free tool anyone can use with your own prompts.<p>Ask the model to describe a symbol of &quot;three curving lines of water&quot; and you can watch &quot;ocean&quot;, &quot;sea&quot;, and &quot;surf&quot; light up a few layers deeper before it settles on &quot;waves&quot;.<p>You can also edit the internal state. Insert &quot;fire&quot; into the middle layer of the ocean prompt and the answer shifts to something about heat.<p>For fun &#x2F; curiosity sake, I also developed way to let the model read its own inner workspace and then decide to suppress or amplify a concept, and run the prompt again.<p>Interesting finding from running it across models. J-lens beats a plain logit lens on some architectures and does nothing on others, and it isn&#x27;t about size. A 0.5B Qwen reads better than a 2.8B Pythia. Every Pythia I tried gained basically nothing; the Llama and Qwen models gained a lot. <a href="https:&#x2F;&#x2F;lucid.earthpilot.ai&#x2F;research" rel="nofollow">https:&#x2F;&#x2F;lucid.earthpilot.ai&#x2F;research</a><p>This is a 48 hour old project based on emerging research and built on a small model, a small probe set on rented GPUs - but I found it genuinely exciting. The code is open.<p>I also included a page context &quot;Docent&quot; AI agent you can chat with about whatever you see to help understand what is going on.<p>Happy to have folks poke around and break it.<p>I imagine the applications for allowing models to self-reflect &#x2F; edit internal states can be useful for alignment, confidence, bias detection, etc. and this tool lets you play with the early stages of that.
