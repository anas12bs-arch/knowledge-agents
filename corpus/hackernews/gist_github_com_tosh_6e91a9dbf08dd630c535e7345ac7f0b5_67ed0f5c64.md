---
title: "Show HN: Agent in 9 Lines Python"
url: "https://gist.github.com/tosh/6e91a9dbf08dd630c535e7345ac7f0b5"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-22T17:07:04Z"
metadata:
  score: "9"
---

# Show HN: Agent in 9 Lines Python

> Source: hackernews | Category: news | 2026-07-22T17:07:04Z

Score: 9 | Comments: 3

I asked myself: what would a minimal implementation of an agent look like?<p>Something that works out of the box, is a real agent with tool calling, but without 1000s of lines of code, without dozens or hundreds of npm or pypi dependencies. Something with just a few &#x27;essential&#x27; features (not a whole kitchen sink that most agent harnesses come with nowadays).<p>An implementation close to pseudocode that you can look at in one page, everything there at a glance, no scrolling.<p>This is the agent.py I ended up with so far:<p><pre><code>  import json,sys;from subprocess import getoutput as sh;from urllib.request import Request as R,urlopen
  url=sys.argv[1];h=[];b=dict(model=&quot;gpt-5.6&quot;,input=h,tools=[dict(type=&quot;custom&quot;,name=&quot;sh&quot;)])
  while p:=input(&quot;&gt; &quot;):
    h+=[dict(role=&quot;user&quot;,content=p)];H={&quot;Content-Type&quot;:&quot;application&#x2F;json&quot;}
    while True:
      o=(r:=json.load(urlopen(R(url,json.dumps(b).encode(),H))))[&quot;output&quot;]
      h+=o;c=[i for i in o if i[&quot;type&quot;]==&quot;custom_tool_call&quot;];z=r[&quot;usage&quot;][&quot;total_tokens&quot;]&#x2F;10500
      if not c:print(o[-1][&quot;content&quot;][0][&quot;text&quot;],f&#x27;\n[{z:06.3f}%]&#x27;);break
      h+=[dict(type=&quot;custom_tool_call_output&quot;,call_id=i[&quot;call_id&quot;],output=sh(i[&quot;input&quot;])) for i in c]
</code></pre>
It is a bit code golfed but I think it is fairly readable<p>- imports are all from stdlib (0 external dependencies!)<p>- assumes there is an inference api endpoint running somewhere<p>- assumes the inference api endpoint is openai-like<p>- model hardcoded to &quot;gpt 5.6&quot; (=&gt; Sol), can easily be changed to e.g. open weight (kimi k3, glm 5.2 etc)<p>- api endpoint url is passed as arg to the python script<p>- configures only 1 custom tool: &#x27;sh&#x27;<p>- &#x27;sh&#x27; is sufficient for interacting with the environment in an open ended way<p>- new api output gets added to history (&quot;h&quot;)<p>- if api output contains tool calls the tool calls get executed<p>- agent gives control back to user when the last model response is without tool calls<p>- agent message to user shows % of context window used<p>Noteworthy:<p>no dependencies other than python stdlib (!)<p>- less startup time<p>- less dependency churn<p>- less supply chain attack vector surface<p>- less code to verify and understand<p>no mcp, no plugins, no security theater<p>- if you want to add something specific: add it explicitly<p>- adapt the environment to give the agent access or restrict access to tools, resources, network etc (the env is the security boundary, not the harness)<p>no system prompt<p>- every token in context window is precious<p>- current strong models do fine without steering via system prompt (or are even harmed by long overly specific system prompts designed for models from months ago)<p>- system prompt or agents.md context can easily be added if needed (agent can also discover it or get prompted to read from environment as is)<p>how to run&#x2F;deploy the agent<p>- design the environment you want to give the agent (container, docker, sandbox of your choice)<p>- start an inference api endpoint that is openai-like (support the request&#x2F;response shape used in agent.py above)<p>- inference api endpoint can be as simple as a proxy to openai api that adds credentials&#x2F;api key<p>- adapt as you want&#x2F;need it, change the model, remove&#x2F;alter context window behaviour, add tools, etc etc<p>Looking for any feedback you have to make it more clear or even simpler!
