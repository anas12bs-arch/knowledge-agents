---
title: "Show HN: Clx – Compile Lua to Native Executables Through C++20"
url: "https://github.com/samyeyo/clx"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-16T23:10:26Z"
metadata:
  score: "69"
---

# Show HN: Clx – Compile Lua to Native Executables Through C++20

> Source: hackernews | Category: news | 2026-07-16T23:10:26Z

Score: 69 | Comments: 1

Hi HN,<p>clx is an ahead-of-time compiler for standard Lua that generates C++20 and produces standalone native executables through GCC, Clang or MSVC.<p>The project started as an experiment to see whether modern C++ could be used as a portable compiler backend instead of LLVM or direct machine code generation. The generated code is then compiled and optimized by the host toolchain.<p>The latest release replaces the previous NaN-tagged value representation with a new shadow-types implementation, adds full int64 support, improves native arithmetic code generation and adds ARM64 macOS coroutine support.<p>Performance is typically much faster than the Lua interpreter and can outperform LuaJIT on some computation-heavy workloads while remaining fully ahead-of-time compiled.<p>The repository also contains graphical examples written in Lua, including a Pong game and a Mandelbrot explorer using a Sokol binary module (using the clx C++ API)<p>I&#x27;d be very interested in feedback on clx :)
