---
title: "Show HN: Pulpie – Models for Cleaning the Web"
url: "https://usefeyn.com/blog/pulpie-pareto-optimal-models-for-cleaning-the-web/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-06T18:14:28Z"
metadata:
  score: "33"
---

# Show HN: Pulpie – Models for Cleaning the Web

> Source: hackernews | Category: news | 2026-07-06T18:14:28Z

Score: 33 | Comments: 5

Hey HN, I&#x27;m Shreyash, founder of Feyn. We built Pulpie, a family of Pareto optimal models for cleaning the web. Pulpie strips boilerplate (ads, footers, sidebars) from raw HTML and returns just the main content as HTML or Markdown.<p>We match SOTA extraction quality while being 20x cheaper. Cleaning 1 billion webpages costs $7,900 with Pulpie versus $159,000 with Dripper, the current leading extractor.<p>The gains come from architecture. Today&#x27;s leading extractors are decoders that generate output one token at a time. Each step reads the full model from memory to produce a single token. Conversely, Pulpie models are encoders. They run one forward pass over the full input HTML and label each block as boilerplate or content. As a result, Pulpie is compute-bound while decoders are memory-bound. Cheaper GPUs have relatively more compute than memory bandwidth. This makes Pulpie easy to run optimally.<p>Here&#x27;s Pulpie and Dripper cleaning the same pages side by side: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=ibd-tIiQECo" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=ibd-tIiQECo</a>. You can try a side-by-side comparison yourself: <a href="https:&#x2F;&#x2F;huggingface.co&#x2F;spaces&#x2F;feyninc&#x2F;pulpie" rel="nofollow">https:&#x2F;&#x2F;huggingface.co&#x2F;spaces&#x2F;feyninc&#x2F;pulpie</a><p>Our motivation for Pulpie came from building a deep research harness. Every search API returns noisy content that contains ads, nav elements, and sidebars. In one instance, an ad for &quot;Gemini on Pixel&quot; slipped into our search results, got passed into LLM context, and ended up in the final answer served to the user. Pretty embarrassing moment for us but it helped us realize how bad data kills model intelligence. We built Pulpie to get clean data for cheap.<p>All models are open source on Hugging Face. You can read about our training process and how to use Pulpie here: <a href="https:&#x2F;&#x2F;usefeyn.com&#x2F;blog&#x2F;pulpie-pareto-optimal-models-for-cleaning-the-web&#x2F;#get-started">https:&#x2F;&#x2F;usefeyn.com&#x2F;blog&#x2F;pulpie-pareto-optimal-models-for-cl...</a><p>Happy to answer any questions!
