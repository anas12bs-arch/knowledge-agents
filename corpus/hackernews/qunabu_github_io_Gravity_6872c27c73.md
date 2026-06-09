---
title: "Show HN: Gravity – interactive solar-system simulator, from Newton to Einstein"
url: "https://qunabu.github.io/Gravity/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-06-09T18:29:39Z"
metadata:
  score: "96"
---

# Show HN: Gravity – interactive solar-system simulator, from Newton to Einstein

> Source: hackernews | Category: news | 2026-06-09T18:29:39Z

Score: 96 | Comments: 23

Just for fun and self education, I&#x27;ve built this over a weekend to teach myself why orbits exist, not just show planets going around. Something that was never clearly explain to me in school. 
It opens with a guided tour that builds the idea up step by step: two bodies and the equal&#x2F;opposite force, inertia (the Sun is removed and Earth just drifts straight), then &quot;an orbit is falling and continuously missing,&quot; cosmic velocities with a little rocket, Voyager 1 &amp; 2&#x27;s real gravity assists (the clock runs the actual 1977–1989 dates so the planets orbit into their grand-tour alignment and the slingshots line up), and it ends on Einstein — gravity as curved spacetime, the classic rubber-sheet well.
What&#x27;s real: every body uses its real radius&#x2F;mass and J2000 orbital elements; positions come from solving Kepler&#x27;s equation each  frame. You can toggle to an N-body mode (symplectic leapfrog) that shows live energy drift (~1e-6%) so you can see the integrator is honest. The only thing faked is scale — at true scale you can&#x27;t see anything — so there&#x27;s a toggle between true scale and a log-remapped &quot;visual&quot; scale, with physics always running in real AU.
Tech: TypeScript + Three.js + Vite, fully client-side, no backend, works offline (surface textures are generated procedurally from value-noise; only Earth uses a real image). Source: <a href="https:&#x2F;&#x2F;github.com&#x2F;qunabu&#x2F;Gravity" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;qunabu&#x2F;Gravity</a><p>Happy to answer questions — and feedback on the physics or the explanations is very welcome. This project might be totally inaccurate in terms of real physics, this is how i do understand this on my own - i&#x27;m happy to confront this with reality
