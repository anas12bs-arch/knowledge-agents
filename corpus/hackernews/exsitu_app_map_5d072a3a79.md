---
title: "Show HN: Ex Situ – Open-source spatial index of displaced cultural artifacts"
url: "https://exsitu.app/map"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-21T06:14:35Z"
metadata:
  score: "15"
---

# Show HN: Ex Situ – Open-source spatial index of displaced cultural artifacts

> Source: hackernews | Category: news | 2026-07-21T06:14:35Z

Score: 15 | Comments: 1

Hi, I designed and developed a spatial index that maps museum artefacts as connecting arcs&#x2F;hyperlinks from their origin site to institutional location&#x2F;sources. The Index specifically looks at western&#x2F;euro-american institutions and maps their collection categorised by them under Islamic art, Asian&#x2F;African art, ethnological collections, Middle East, South America etc.<p>Started as my MA thesis in 2022, kept building since, mostly solo with a little funding. Fully open source, self-hosted, AGPL-3.0, Next.js + Deck.gl on the frontend, Strapi backend, Python ETL pulling from museum open-access APIs. Currently indexing over 100k artifacts from all over the world, across 8 collections (Met, V&amp;A, SMB Berlin). Recently added an md export so researchers can download provenance data for a filtered set of artifacts.<p>The infrastructure is conceptualized as an indexer, not a hoster. Even images are kept as URLs pointing to the source institutions. It&#x27;s connective tissue between archives that were never designed to speak to each other, with an origin-first search UI concept. The data model is on purpose flat, to avoid encoding problematic taxonomies, and routes researchers directly to the source giving responsibility to the source institutions rather than duplicating institutional data. It indexes the relationship between origin sites and destination collections.<p>Coming from a design background, taking this project from prototype to production app has been incredibly rewarding, but honestly it’s getting a little bit overwhelming to scale alone. I would love community’s feedback on performance scaling, any code contributions, data pipelines for missing museum apis or general feedback.<p>Repo: <a href="https:&#x2F;&#x2F;github.com&#x2F;hburakyel&#x2F;ex-situ" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;hburakyel&#x2F;ex-situ</a><p>Live: <a href="https:&#x2F;&#x2F;exsitu.app" rel="nofollow">https:&#x2F;&#x2F;exsitu.app</a>
