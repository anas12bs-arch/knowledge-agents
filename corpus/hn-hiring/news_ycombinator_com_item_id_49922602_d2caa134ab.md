---
title: "HN Hiring (Ask HN: Who is hiring? (October 2026))"
url: "https://news.ycombinator.com/item?id=49922602"
source: "hn-hiring"
category: "job-skills"
tags: ["hiring", "tech-stack", "skills", "market-demand"]
date: "2026-10-01T16:27:06Z"
metadata:
  {}
---

# HN Hiring (Ask HN: Who is hiring? (October 2026))

> Source: hn-hiring | Category: job-skills | 2026-10-01T16:27:06Z

Location: Pisa, Italy (CET)
Remote: Yes, remote only
Willing to relocate: No
Technologies: Python, LLM&#x2F;agent orchestration, local embeddings, retrieval evaluation, AWS (Lambda&#x2F;SQS&#x2F;EventBridge), Terraform, Django, PostgreSQL, LightGBM&#x2F;PyTorch, NLP&#x2F;Transformers
Résumé&#x2F;CV: linkedin.com&#x2F;in&#x2F;vslovik
Code: github.com&#x2F;vslovik&#x2F;fenix — local-embedding search whose relevance is actually measured: labelled control probes, blinded human ranking, precision@k. No API keys.
Email: valeriya.slovikovskaya@gmail.com<p>Software architect, 15+ years in production systems, almost entirely startups and internal startups — fintech, e-commerce, pharma, publishing.<p>The work I get pulled into is the recurring startup problem: a service shipped fast under launch pressure, without adequate tests, that later has to be made reliable without being stopped. Incident response, re-architecture, and the release discipline that keeps it from happening again. Most recently that has meant a regulated UK consumer-credit platform — loan servicing, arrears, forbearance, statutory breathing space, and early-settlement calculations written against consumer-credit legislation. Regulation as code, behind a test suite larger than the production codebase.<p>I&#x27;ve done that in all three configurations: taking a core system from problem statement to release, leading the team that carried it (1 to 7 engineers in ten months), and now doing the same work again with agentic tooling covering what the team used to.<p>On the data side: a LightGBM acquisition model over a 38M-row base — 0.77 test AUC, 8x lift in the top 1% — scoring 2.9M households for a live campaign. The part I&#x27;d rather be judged on is what happened next: I found a validation-set defect in my own pipeline (early stopping on the test split), quantified its effect across every figure I had already reported, restated them, and added a pure-noise regression test that pins the model to chance when fed random features — so that class of leak cannot come back quietly. NLP is hands-on rather than API-deep: my degree thesis fine-tuned BERT, RoBERTa and XLNet to state of the art on the FNC-1 stance-detection benchmark, published at LREC 2020.<p>Building on my own time: github.com&#x2F;vslovik&#x2F;fenix — it ranks an incoming stream against a free-text description of what you&#x27;re looking for, and answers questions over the same corpus with citations back to source chunks. Ollama embeddings, sqlite-vec, no API keys. The part worth looking at is the evaluation: the ranking anchor is scored against a labelled probe set with a deliberate control group of things I don&#x27;t want, and live results are rated blind — scores hidden, order shuffled — so the human judgement stays independent of the ranking it is judging. Doing that produced a measured finding I did not expect: an embedding has no notion of negation, so naming a technology in order to reject it moves the anchor toward it. Nu
