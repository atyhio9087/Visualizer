# 🎧 Psychedelic Audio Visualizer (Groq + LLaMA 3.1)

> Turn sound into colour, chaos, and controlled hallucinations 🌈

---

## 🧠 What is this?

A **browser-based audio visualizer** that doesn’t just react to sound — it **understands the vibe**.

Upload a track, and the system:

* extracts audio features 🎵
* classifies the **emotional vibe** using **Groq + LLaMA 3.1 (8B Instant)** 🤖
* generates a matching **psychedelic visual experience** 🌌

---

## ⚡ Demo Behaviour

| Input                    | Output               |
| ------------------------ | -------------------- |
| High bass + bright highs | 🔥 Energetic visuals |
| Low energy + soft tones  | 🌊 Serene ambience   |
| Weird mix                | 🌀 Psychedelic chaos |

---

## 🧪 Tech Stack

* 🧠 LLM: `llama-3.1-8b-instant` via Groq
* 🎨 Frontend: Vanilla HTML + Canvas + Web Audio API
* ⚙️ Backend: Serverless (`/api/vibe.js`)
* ☁️ Hosting: Vercel

---

## 🔮 How it works

```text
Audio File → Feature Extraction → Prompt
            ↓
        /api/vibe
            ↓
     Groq (LLM)
            ↓
       "energetic"
            ↓
   Visual + Colour Engine
            ↓
     ✨ Psychedelic Output ✨
```

---

## 🧩 Core Idea

Instead of hardcoding visuals:

```js
if (bass > 0.7) vibe = "energetic";
```

We do:

```text
"Given this audio profile, what is the vibe?"
```

👉 Let the model decide
👉 Then map that to visuals

---

## 🎯 Supported Vibes

* `euphoric`
* `melancholic`
* `energetic`
* `dreamy`
* `tense`
* `serene`
* `dark`
* `psychedelic`

---

## 🚀 Run Locally

```bash
git clone <your-repo>
cd your-repo
```

### 1. Install deps

```bash
npm install
```

### 2. Add env file

```bash
GROQ_API_KEY=your_key_here
```

### 3. Run server

```bash
node server.js
```

### 4. Open

```
http://localhost:3000
```

---

## ☁️ Deploy to Vercel

1. Go to Vercel
2. Import project (or upload folder)
3. Add env var:

   ```
   GROQ_API_KEY=your_key_here
   ```
4. Deploy 🚀

---

## ⚠️ Notes

* 🔐 API key is **server-side only**
* 🎯 LLM output is constrained to valid vibe labels
* ⚡ Uses heuristic fallback if LLM fails

---

## 🧠 Future Ideas

* 🎼 Beat sync animations
* 🎨 Dynamic palette evolution over time
* 🧬 Blend multiple vibes instead of single label
* 🕶️ VR / immersive mode

---

## 💥 Why this exists

Because:

> Visualizers that just bounce to bass are boring.

This one **interprets emotion**.

---

## 👾 Credits

* LLM inference powered by Groq
* Deployment via Vercel

---

## 🌈 Final Thought

> You’re not just seeing the music.
> You’re seeing how it *feels*.

---

✨ Enjoy the trip.
