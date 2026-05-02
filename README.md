# 🎧 Psychedelic Audio Visualizer  
### Groq ✦ Ollama ✦ LLaMA 3.1 ✦ Pure Canvas Chaos

> Turn sound into colour, chaos, and controlled hallucinations 🌈

[![Live Demo](https://img.shields.io/badge/demo-live-green?style=for-the-badge)](https://visualizer-ten-drab.vercel.app/)
![Groq](https://img.shields.io/badge/Groq-LLM-blue?style=for-the-badge)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-black?style=for-the-badge)
![JavaScript](https://img.shields.io/badge/JS-Vanilla-yellow?style=for-the-badge)
![HTML](https://img.shields.io/badge/HTML-Canvas-orange?style=for-the-badge)

---

## 🧠 What is this?

A **browser-based audio visualizer** that doesn’t just react to sound — it **interprets it**.

Drop a track, and the system:

* extracts audio features 🎵  
* classifies the **emotional vibe** using an LLM 🤖  
* generates a matching **psychedelic visual system** 🌌  

---

## 🔥 Live Demo

👉 https://visualizer-ten-drab.vercel.app/

No install. Drop a file. Trip instantly.

---

## ⚡ Modes

### 1. ☁️ Groq (Cloud LLM)
- Uses `llama-3.1-8b-instant`
- Fast inference
- Requires API key

### 2. 🖥️ Ollama (Local LLM) (Use the Ollama tagged file)
- Fully offline
- Runs `llama3.1`, `mistral`, `gemma`, etc.
- No API cost
- Configurable in UI (top-left badge)

> The UI you see (Ollama badge + modal) is built directly into the app :contentReference[oaicite:0]{index=0}

---

## 🧪 Tech Stack

* 🧠 LLM:
  * Groq (`llama-3.1-8b-instant`)
  * Ollama (local models)
* 🎨 Frontend:
  * Vanilla JS
  * Canvas API
  * Web Audio API
* ⚙️ Backend:
  * Serverless (`/api/vibe.js`) for Groq
* ☁️ Hosting:
  * Vercel

---

## 🔮 How it works

```text
Audio File → Feature Extraction → Prompt
            ↓
     (Groq OR Ollama)
            ↓
        "vibe label"
            ↓
   Visual + Colour Engine
            ↓
     ✨ Psychedelic Output ✨
