---
title: "Show HN: Lowfat – pluggable CLI filter that saved 91.8% of my LLM tokens"
url: "https://github.com/zdk/lowfat"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-06-05T18:26:43Z"
metadata:
  score: "57"
---

# Show HN: Lowfat – pluggable CLI filter that saved 91.8% of my LLM tokens

> Source: hackernews | Category: news | 2026-06-05T18:26:43Z

Score: 57 | Comments: 42

Hi HN, not sure if anyone would be interested, but just wanted to share that I&#x27;ve been maintaining my small tool called &#x27;lowfat&#x27; that helps me filters some of my verbose CLI output. It&#x27;s a single binary, works as an agent hook or a shell wrapper. It has a plugin system to customize filters per command.<p>The idea is pretty simple: agents don&#x27;t need the full kubectl get -o yaml or any 10k-line dump to make decisions. 
So that lowfat sits in between, strips the noise, and passes through what matters. Here&#x27;s my real report after 2 months of personal use:<p><pre><code>  lowfat history --all

  lowfat plugin candidates
  ─────────────────────────────────────────────────────────

    #  command                    runs   avg raw      cost   savings  source    status  
    1  kubectl get                101x     14.4K      1.5M     93.9%  plugin    good    
    2  grep                       103x     13.5K      1.4M     96.2%  plugin    good    
    3  git diff                    81x       995     80.6K     57.9%  built-in  good    
    4  kubectl                     90x       485     43.6K     33.6%  plugin    good    
    5  docker                     127x      5.5K    693.6K     96.1%  built-in  good    
    6  ls                         489x       117     57.3K     56.2%  built-in  good    
    7  find                        30x     16.5K    495.0K     95.5%  plugin    good    
    8  git show                    63x       490     30.9K     38.0%  built-in  good    
    9  git                        177x       368     65.2K     76.1%  built-in  good    
   10  git log                     86x       556     47.8K     78.5%  built-in  good    
   11  kubectl logs                 5x      3.6K     17.8K     43.0%  plugin    good    
   12  git status                  86x       152     13.1K     58.0%  built-in  good    
   13  docker ps                   20x       467      9.3K     52.8%  plugin    good    
   14  kubectl describe             6x       656      3.9K      1.2%  plugin    weak    
   15  docker images                9x       940      8.5K     61.8%  built-in  good    
   16  k get                        2x      2.1K      4.2K     35.9%  plugin    good    
   17  terraform                   10x       395      3.9K     32.1%  plugin    good    
   18  git commit                  32x        77      2.5K      0.0%  built-in  weak    
   19  docker build                 8x       487      3.9K     37.6%  built-in  good    
   20  docker compose              22x       979     21.5K     89.4%  built-in  good    

  total: 4.4M raw → 4.1M saved (91.8%)
</code></pre>
My toolset above is kind limited, but it works pretty well for my usecase without any interruption
Kinda help me not reaching the token limit for my company Bedrock limit usage and keep optimizing the saving on the go for later usage.<p>But, why not alternatives (<a href="https:&#x2F;&#x2F;github.com&#x2F;zdk&#x2F;lowfat#alternatives" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;zdk&#x2F;lowfat#alternatives</a>) ? 
The answers are:
  - My goal is to make the core lightweight but extensible via plugins i.e. not trying to bundle every command in the installed binary so that people own their output filters.
  - Customizable per usecase via plugin or filter pipelines as I am using my own toolset.
  - Customizable for non-public CLI tools, for example, some enterprise might have their interal CLI tools that public won&#x27;t have access.
  - People should own their data. So the design is local-first, No telemetry forever.
  - I kinda love UNIX-style composible pipes, so lowfat-filter has implemented this style.
  - Be able to adjust aggressiveness of the filter, so we can control that we won&#x27;t strip something the agent needed.<p>GitHub: <a href="https:&#x2F;&#x2F;github.com&#x2F;zdk&#x2F;lowfat" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;zdk&#x2F;lowfat</a><p>Anyway, if anyone is interested, feedbacks and questions are welcome!<p>Thanks!
