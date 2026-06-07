<div align="center">

<br />

```
██████╗ ███████╗ █████╗ ██████╗ ██╗    ██╗██╗███████╗███████╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗██║    ██║██║██╔════╝██╔════╝
██████╔╝█████╗  ███████║██║  ██║██║ █╗ ██║██║███████╗█████╗  
██╔══██╗██╔══╝  ██╔══██║██║  ██║██║███╗██║██║╚════██║██╔══╝  
██║  ██║███████╗██║  ██║██████╔╝╚███╔███╔╝██║███████║███████╗
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝  ╚══╝╚══╝ ╚═╝╚══════╝╚══════╝
```

### *Drop a PDF. Ask anything. Get answers.*

<br />

[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io)
[![OpenRouter](https://img.shields.io/badge/Powered%20by-OpenRouter-6366f1?style=flat-square)](https://openrouter.ai)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=flat-square)](LICENSE)
[![Free](https://img.shields.io/badge/Models-100%25%20Free-f97316?style=flat-square)](https://openrouter.ai/models)

<br />

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%">

</div>

<br />

## &nbsp;✦ &nbsp;What is Readwise?

**Readwise** is an AI-powered PDF chat assistant built with Streamlit and OpenRouter. Upload any PDF — research paper, contract, textbook, report — and have a real conversation with it. No summaries that miss the point. No copy-pasting into ChatGPT. Just ask, and get precise answers grounded in your document.

> *Built in a weekend. Runs on free models. Actually works.*

<br />

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%">

<br />

## &nbsp;⚡ &nbsp;Features

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   📄  Full PDF parsing — reads the entire document         │
│   💬  Multi-turn chat — remembers conversation context     │
│   🔀  Auto model fallback — never gets stuck on 429s       │
│   🆓  100% free — OpenRouter free tier, no billing         │
│   ⚡  Quick prompts — one-click common queries             │
│   🎨  Clean UI — warm, editorial, human-designed           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

<br />

## &nbsp;🤖 &nbsp;Models Available

| Model | Type | Best For |
|---|---|---|
| `openrouter/free` | **Auto router** | Picks the best available free model |
| `meta-llama/llama-3.3-70b-instruct:free` | Llama 3.3 70B | General Q&A, summaries |
| `deepseek/deepseek-r1:free` | DeepSeek R1 | Reasoning, analysis |
| `mistralai/mistral-small-3.2-24b-instruct:free` | Mistral Small | Fast responses |
| `google/gemini-2.5-flash:free` | Gemini 2.5 Flash | Long documents |
| `qwen/qwen3-235b-a22b:free` | Qwen3 235B | Multilingual PDFs |

> **Tip:** Leave it on Auto — it intelligently picks the best model and falls back automatically if one is rate-limited.

<br />

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%">

<br />

## &nbsp;🚀 &nbsp;Getting Started

### 1 &nbsp;—&nbsp; Clone the repo

```bash
git clone https://github.com/Anikett77/readwise.git
cd readwise
```

### 2 &nbsp;—&nbsp; Install dependencies

```bash
pip install -r requirements.txt
```

### 3 &nbsp;—&nbsp; Get your free API key

1. Go to **[openrouter.ai](https://openrouter.ai)**
2. Sign up → API Keys → **Create Key**
3. Free credits on signup, no billing required

### 4 &nbsp;—&nbsp; Set up your environment

Create a `.env` file in the root directory:

```env
OPENROUTER_API_KEY=sk-or-v1-your-key-here
```

### 5 &nbsp;—&nbsp; Run it

```bash
streamlit run RAG.py
```

Open **http://localhost:8501** and you're good to go. 🎉

<br />

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%">

<br />

## &nbsp;☁️ &nbsp;Deploy to Streamlit Cloud

Deploy for free in under 5 minutes:

```
1.  Push this repo to GitHub
2.  Go to share.streamlit.io
3.  Connect your GitHub repo
4.  Set main file → RAG.py
5.  Add secret → OPENROUTER_API_KEY = "sk-or-..."
6.  Hit Deploy
```

Your app will be live at `https://yourapp.streamlit.app` ✨

<br />

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%">

<br />

## &nbsp;📁 &nbsp;Project Structure

```
readwise/
│
├── RAG.py              ← Main app (UI + logic)
├── requirements.txt    ← Python dependencies
├── .env                ← Your API key (never commit this)
├── .gitignore          ← Ignores .env and cache files
└── README.md           ← You are here
```

<br />

## &nbsp;📦 &nbsp;Requirements

```txt
streamlit
requests
python-dotenv
pypdf
```

<br />

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%">

<br />

## &nbsp;🛠️ &nbsp;How It Works

```
  User uploads PDF
        │
        ▼
  pypdf extracts full text
        │
        ▼
  Text injected into system prompt
        │
        ▼
  User asks a question
        │
        ▼
  OpenRouter API called with model of choice
        │
        ├── 200 OK → return answer ✓
        │
        └── 429 / 404 → auto-fallback to next model → retry
```

Every message in the conversation carries the **full document context** — so follow-up questions work perfectly without re-uploading.

<br />

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%">

<br />

## &nbsp;⚠️ &nbsp;Limitations

- Works best with **text-based PDFs** (not scanned image PDFs without OCR)
- Free tier models may occasionally be **slow or rate-limited** — auto-fallback handles this
- Very large PDFs are **truncated at ~60,000 characters** to fit model context windows

<br />

## &nbsp;🤝 &nbsp;Contributing

PRs are welcome. If you find a bug or have a feature idea, open an issue.

```bash
# Fork → clone → create branch → push → open PR
git checkout -b feature/your-feature-name
```

<br />

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%">

<br />

<div align="center">

Built with ♥ by **[Aniket](https://github.com/Anikett77)**

*Google Gemini Campus Ambassador · Full Stack Developer · OIST Bhopal*

<br />

**[⭐ Star this repo](https://github.com/Anikett77/readwise)** &nbsp;·&nbsp; **[🐛 Report Bug](https://github.com/Anikett77/readwise/issues)** &nbsp;·&nbsp; **[💡 Request Feature](https://github.com/Anikett77/readwise/issues)**

<br />

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%">

</div>