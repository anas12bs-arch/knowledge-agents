---
title: "Show HN: I mapped 8.5M research papers into an interactive atlas"
url: "https://tomesphere.com/atlas"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-09T18:21:56Z"
metadata:
  score: "20"
---

# Show HN: I mapped 8.5M research papers into an interactive atlas

> Source: hackernews | Category: news | 2026-07-09T18:21:56Z

Score: 20 | Comments: 3

When I read papers, I have to jump between multiple tabs to find the dataset, code, videos, peer reviews, and so on. I tried to fix this with this project.<p>It started as a project just for papers on arXiv, but after its initial success on Twitter (got like 1.9k views: the most I have gotten for a post), I have now expanded it to include other openly available papers from PubMed Central, bioRxiv, medRxiv, and eLife. These papers have been linked with their genes, proteins, diseases, drugs, clinical trials, 3D protein structures, code, and cited and similar papers.<p>This project now has four parts:<p>First, a map. I embedded nearly 8.5M papers (with SPECTER2), ran UMAP for 2D representation, and rendered them as a scatterplot. The dots can be clicked to see brief information about the papers, like an LLM TLDR, key findings, peer reviews, linked entities, and more. The clusters are also labeled, though you might have to zoom in.<p>Second, I built a detailed paper page for each paper. They give you the paper&#x27;s full text, images, videos, peer reviews (from OpenReview), GitHub links, Hugging Face dataset&#x2F;model links, clinical trials, genes, diseases, 3D protein structures, cited papers, and similar papers. You can also copy the whole page, including the full paper text and image URLs, as markdown for your LLM.<p>Third, I have released an extension so you can read all this information in your sidebar by clicking &quot;open in Tomesphere&quot; that shows up in arXiv, PMC, bioRxiv, Google Scholar, or medRxiv. I have tried to provide as much information as possible in the extension, though for things like viewing all the images or a 3D protein structure, you might still have to go to the paper page using the link provided in the extension.<p>Fourth, all this data is available for your LLM via MCP. The MCP does have a 50-query free limit (this jumps 10x with signup).<p>Note: this project is still in beta, so papers might have some mismatched information. I am rolling out feedback forms soon to improve the data quality. Thank you so much for taking the time to read this.
