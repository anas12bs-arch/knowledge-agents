---
title: "Pepperwind, a fictional company dataset with 223 tables and 79M rows"
url: "https://news.ycombinator.com/item?id=50333045"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-11-02T10:03:11Z"
metadata:
  score: "8"
---

# Pepperwind, a fictional company dataset with 223 tables and 79M rows

> Source: hackernews | Category: news | 2026-11-02T10:03:11Z

Score: 8 | Comments: 0

Hi HN. I&#x27;m a software engineer, building Misata Studio.<p>Pepperwind Trading Co, is a fictional spice and tea trader from Kochi, selling in India, Europe and the US for three years. It has a storefront, a subscription club, a warehouse, ledgers in 3 currencies, support, CRM, marketing, product analytics, HR, payroll and company mail. It is around 223 tables, 79 M rows that is around 7GB of parquet files. It was made with the help of the backend engine behind misata studio.<p>What I found while I was researching about the synthetic dataset needs was that products that is being built for interconnected systems or analytical solutions that serve organisations often lack a real usable test dataset that is realistic enough to verify the performance and workflows accurately. And most of the time synthetic datasets don&#x27;t care about entity resolution, same customers existing in different places and in different IDs, FKs pointing at rows that doesnt exist, the values might not match exactly and this is a mess when it comes to finances of the datasets. There are plenty out there, but a single heavy and massive dataset is rare. It was from a similar pain that the idea behind building misata was born.<p>Some things I was focussed on while building Pepperwind was for it to have unique and valuable usability for different usecases, like: 
- The books balance in the ledger. 
- 20 incidents planted in. Courier failure in Diwali, Dutch VAT charged on EU invoices, a referral fraud, price rise that pushes subscription churn etc. I made these incidents consistent across the systems. 
- It ships with 92 KPIs and their values each month, along with 420 questions that can be asked against the dataset.<p>Misata is a from scratch multi-table synthetic data generation project with an open-source python library and a web tool I am developing for prompt to dataset generation. I had posted about this in December and have come a long way since then https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=46289055.<p>The page lets you explore a small slice of the dataset in your browser and you can follow a single customer through every system. The preview is free and the full version is paid for now, to cover the building cost ($30). Listed in huggingface under CC by 4.0 license: https:&#x2F;&#x2F;huggingface.co&#x2F;datasets&#x2F;misatadata&#x2F;pepperwind .<p>I would like to reach out to people across dozens of use cases. What would you use it for and how could this or another dataset similar to this help you build your product&#x2F;solution?
