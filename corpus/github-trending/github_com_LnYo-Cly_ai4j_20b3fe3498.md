---
title: "LnYo-Cly/ai4j ⭐421"
url: "https://github.com/LnYo-Cly/ai4j"
source: "github-trending"
category: "tool"
tags: ["github", "trending", "embedding", "agent", "chatglm", "chatgpt", "coding-agent"]
date: "2026-07-07T01:27:07Z"
metadata:
  stars: "421"
  language: "Java"
---

# LnYo-Cly/ai4j ⭐421

> Source: github-trending | Category: tool | 2026-07-07T01:27:07Z

**LnYo-Cly/ai4j** — ⭐ 421

Language: Java | Topics: agent, chatglm, chatgpt, coding-agent, deepseek, embedding

一款JavaSDK用于快速接入AI大模型应用，整合多平台大模型，如OpenAi、智谱Zhipu(ChatGLM)、深度求索DeepSeek、月之暗面Moonshot(Kimi)、腾讯混元Hunyuan、零一万物(01)等等，提供统一的输入输出(对齐OpenAi)消除差异化，优化函数调用(Tool Call)，优化RAG调用、支持向量数据库(Pinecone)、内置联网增强，并且支持JDK1.8，为用户提供快速整合AI的能力。

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:6A5ACD,100:2E86C1&height=180&section=header&text=ai4j&fontSize=46&fontColor=ffffff&animation=fadeIn&desc=Java%20AI%20Agentic%20SDK%20for%20JDK%208%2B&descAlignY=68" alt="ai4j banner" />
</p>

<p align="center">
  <a href="https://search.maven.org/artifact/io.github.lnyo-cly/ai4j">
    <img src="https://img.shields.io/maven-central/v/io.github.lnyo-cly/ai4j?color=2E86C1&label=Maven%20Central" alt="Maven Central" />
  </a>
  <a href="https://lnyo-cly.github.io/ai4j/">
    <img src="https://img.shields.io/badge/Docs-GitHub%20Pages-0A7EA4" alt="Docs" />
  </a>
  <a href="https://www.apache.org/licenses/LICENSE-2.0.txt">
    <img src="https://img.shields.io/badge/License-Apache%202.0-1F6FEB" alt="License" />
  </a>
  <img src="https://img.shields.io/badge/JDK-8%2B-2EA043" alt="JDK 8+" />
  <img src="https://img.shields.io/badge/Agentic-Enabled-6F42C1" alt="Agentic Enabled" />
  <img src="https://img.shields.io/badge/MCP-Supported-0F766E" alt="MCP Supported" />
  <img src="https://img.shields.io/badge/RAG-Built--in-B45309" alt="RAG Built-in" />
  <img src="https://img.shields.io/badge/CLI%20%2F%20TUI%20%2F%20ACP-Built--in-475569" alt="CLI TUI ACP Built-in" />
</p>

# ai4j
一款面向 JDK8+ 的 Java AI Agentic 开发套件，既提供统一的大模型调用与常用 AI 基座能力，也提供更完善的智能体式 Agent 开发能力。  
覆盖多平台模型接入、统一输入输出、Tool Call、MCP、RAG、统一 `VectorStore`、ChatMemory、Agent Runtime、Coding Agent、CLI / TUI / ACP、FlowGram 集成，以及 Dify / Coze / n8n 等已发布 AgentFlow 端点接入能力，帮助 Java 应用从基础模型接入扩展到更完整的 agentic 应用开发。

当前仓库已经演进为多模块 SDK，除核心 `ai4j` 外，还提供 `ai4j-extension-api`、`ai4j-plugin-ask-user`、`ai4j-agent`、`ai4j-coding`、`ai4j-cli`、`ai4j-spring-boot-starter`、`ai4j-flowgram-spring-boot-starter`、`ai4j-bom`。如果只需要基础大模型调用，优先引入 `ai4j`；如果需要插件包、Agent、Coding Agent、CLI / ACP、Spring Boot 或 FlowGram 集成，再按模块引入对应能力。

## 赞助商

+ [TroveBox AI 中转平台](https://codex.trovebox.online/)：提供 AI API 中转服务，低至 0.1x 倍率。

## 适用场景与常见方案对比

| 方案 | Java 基线 | 应用形态 | 能力侧重点 |
| --- | --- | --- | --- |
| `ai4j` | `JDK8+` | 普通 Java / Spring | 统一大模型接入、Tool / MCP / RAG、Agent Runtime、Coding Agent、CLI / TUI / ACP |
| `Spring AI` | `Java 17+` | `Spring Boot 3.x` | Spring 原生 AI 集成、模型访问、Tool Calling、MCP、RAG |
| `Spring AI Alibaba` | `Java 17+` | `Spring Boot 3.x` | Spring 与阿里云 AI 生态整合 |
| `LangChain4j` | `Java 17+` | 普通 Java / Spring / Quarkus 等 | 通用 Java LLM / Agent / RAG 抽象、AI Services、多框架集成 |

## 支持的平台
+ OpenAi(包含与OpenAi请求格式相同/兼容的平台)
+ Jina（Rerank / Jina-compatible Rerank）
+ Zhipu(智谱)
+ DeepSeek(深度求索)
+ Moonshot(月之暗面)
+ Hunyuan(腾讯混元)
+ Lingyi(零一万物)
+ Ollama
+ MiniMax
+ Baichuan

## 支持的服务
+ Chat Completions（流式与非流式）
+ Responses
+ Embedding
+ Rerank
+ Audio
+ Image
+ Realtime

## 已适配的 AgentFlow / 工作流平台
+ Dify（Chat / Workflow）
+ Coze（Chat / Workflow）
+ n8n（Webhook Workflow）

## 特性
+ 支持MCP服务，内置MCP网关，支持建立动态MCP数据源。
+ 支持Spring以及普通Java应用、支持Java 8以上的应用
+ 多平台、多服务
+ 提供 `AgentFlow` 能力，可直接接入 Dify、Coze、n8n 等已发布 Agent / Workflow 端点
+ 提供 `ai4j-agent` 通用 Agent 运行时，支持 ReAct、subagent、agent teams、
