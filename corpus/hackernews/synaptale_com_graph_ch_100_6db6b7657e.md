---
title: "Show HN: What 180k words look like as a temporal knowledge graph (Oz series)"
url: "https://synaptale.com/graph?ch=100"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-26T03:51:05Z"
metadata:
  score: "6"
---

# Show HN: What 180k words look like as a temporal knowledge graph (Oz series)

> Source: hackernews | Category: news | 2026-07-26T03:51:05Z

Score: 6 | Comments: 0

The graph is free to explore and requires no registration.<p>SynapTale builds a model of a story as a temporal graph made up of nodes (entities) and edges (their actions and relationships).
The graph is not a visualization of the wiki. The wiki, timelines, relationship histories, and analytics are projections of the graph.<p>The current demo contains 232 entities, 1,852 edges, and a snapshot of the story’s state at every chapter. By chapter 100, it still remembers a promise made in chapter 8 and turns the story into a set of source-verifiable facts.<p>The most interesting things can be found in the graph itself and in the Analytics tab. A few things I found:<p>1. The character with the highest kill count is the Tin Woodman—the same character who cries over a beetle he accidentally crushed. Dorothy comes second, with three killing events.
2. Dorothy never deceives anyone during the first 100 chapters of the series.
3. The Scarecrow’s debt to the stork has remained active for 92 chapters, starting in chapter 8.
4. The Cowardly Lion ranks third by number of threats.
5. The first 100 chapters contain 60 secrets and 254 dialogue events.<p>Technical details<p>1. Five different multi-agent pipelines combining LLMs and NLP: a prescan, ontology construction, chapter-by-chapter graph extraction, retrospective validation over spans of dozens of chapters, and a linguistic prescan for speech profiles and linguistic edges.<p>2. A living story needs a living graph. It has to account for time, because entities and the relationships between them evolve. A simple is_active field is not enough.<p>I ended up with three types of edges:<p>event: an instantaneous action;
identity: a fact;
state: a persistent action whose termination requires justification and a supporting quote from the text.<p>The vast majority of edges are events and end in the same chapter in which they began. This allows the system to scale well, since only a minority of state and identity edges remain continuously active.<p>3. Ontology. You cannot simply ask an LLM to extract entities and relationships into a graph. With every chapter, even the smartest model will keep inventing unimportant fields, creating new aliases for existing fields, and representing the same fields inconsistently.<p>Before extracting the graph, the system therefore performs an ontology scan across the entire story. It captures story-specific entity and edge types, along with their fields and descriptions.<p>4. Epistemics. Events are only one part of a story. It is also important to understand how information is distributed, which is difficult to represent using event edges alone.<p>I addressed this by introducing a new node type: epistemic nodes, which capture different entities’ perspectives on the same fact. Subtle hints can still be missed, the system is not yet perfect in this area.
