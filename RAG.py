import streamlit as st
import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

MODELS = {
    "openrouter/free":                               "✦  Auto — best free",
    "meta-llama/llama-3.3-70b-instruct:free":        "Llama 3.3 · 70B",
    "deepseek/deepseek-r1:free":                     "DeepSeek R1",
    "mistralai/mistral-small-3.2-24b-instruct:free": "Mistral Small 3.2",
    "google/gemini-2.5-flash:free":                  "Gemini 2.5 Flash",
    "qwen/qwen3-235b-a22b:free":                     "Qwen3 · 235B",
}

st.set_page_config(page_title="Readwise", page_icon="📖", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;1,400;1,500&family=DM+Sans:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

*, *::before, *::after { box-sizing: border-box; }
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; background: #f7f3ee; color: #1c1917; }
#MainMenu, footer, header, .stDeployButton { display: none !important; visibility: hidden !important; }
.stApp { background: #f7f3ee; }

/* sidebar */
[data-testid="stSidebar"] { background: #1c1917 !important; border-right: none !important; }
[data-testid="stSidebar"] .block-container { padding: 2.5rem 1.8rem !important; }
[data-testid="stSidebar"] * { color: #e7e0d8 !important; }

.block-container { padding: 2.5rem 3rem 4rem 3rem !important; max-width: 1100px !important; }

.wordmark { font-family: 'Lora', serif; font-size: 1.4rem; font-weight: 600; color: #f7f3ee; letter-spacing: -0.02em; }
.wordmark-tagline { font-size: 0.65rem; color: #6b6460; letter-spacing: 0.12em; text-transform: uppercase; margin-top: 0.1rem; }

.page-title { font-family: 'Lora', serif; font-size: 2.2rem; font-weight: 600; color: #1c1917; letter-spacing: -0.03em; line-height: 1.2; margin-bottom: 0.4rem; }
.page-title em { font-style: italic; color: #c2692a; }
.page-sub { font-size: 0.88rem; color: #78716c; font-weight: 300; line-height: 1.6; margin-bottom: 2rem; }

/* upload */
[data-testid="stFileUploader"] { background: #fff !important; border: 1.5px dashed #d4cdc7 !important; border-radius: 6px !important; padding: 1.2rem !important; box-shadow: none !important; }
[data-testid="stFileUploader"]:hover { border-color: #c2692a !important; }

/* doc card */
.doc-card { background:#fff; border:1px solid #e2dcd6; border-radius:6px; padding:0.9rem 1.1rem; display:flex; align-items:center; gap:0.8rem; margin-bottom:1.2rem; }
.doc-name { font-size:0.88rem; font-weight:500; color:#1c1917; word-break:break-all; }
.doc-meta { font-size:0.7rem; color:#a8a09a; margin-top:0.1rem; }
.doc-dot { width:7px; height:7px; border-radius:50%; background:#4ade80; box-shadow:0 0 6px #4ade8099; flex-shrink:0; animation:blink 2.4s ease-in-out infinite; }
@keyframes blink { 0%,100%{opacity:1} 50%{opacity:0.3} }

/* section label */
.sec-label { font-size:0.65rem; color:#a8a09a; text-transform:uppercase; letter-spacing:0.14em; font-weight:500; margin-bottom:0.6rem; display:block; }

/* sidebar */
.sb-divider { border:none; border-top:1px solid #2c2724; margin:1.2rem 0; }
.sb-label { font-size:0.62rem; letter-spacing:0.14em; text-transform:uppercase; color:#6b6460 !important; margin-bottom:0.4rem; margin-top:1.4rem; display:block; }
.sb-key { background:#2c2724; border:1px solid #3d3733; border-radius:3px; padding:0.35rem 0.7rem; font-family:'JetBrains Mono',monospace; font-size:0.68rem; color:#4ade80 !important; display:inline-block; }

/* chat messages */
.msg-user { display:flex; justify-content:flex-end; margin-bottom:1rem; }
.msg-ai { display:flex; align-items:flex-start; gap:0.6rem; margin-bottom:1.2rem; }
.ai-avatar { width:26px; height:26px; border-radius:50%; background:#1c1917; color:#f7f3ee; display:flex; align-items:center; justify-content:center; font-family:'Lora',serif; font-style:italic; font-size:0.8rem; flex-shrink:0; margin-top:2px; }
.bubble-user { background:#1c1917; color:#f7f3ee !important; padding:0.75rem 1.1rem; border-radius:16px 16px 2px 16px; max-width:70%; font-size:0.87rem; line-height:1.6; }
.bubble-ai-wrap { max-width:80%; }
.bubble-ai-name { font-size:0.62rem; color:#c2692a; letter-spacing:0.1em; text-transform:uppercase; font-weight:600; margin-bottom:0.25rem; }
.bubble-ai { background:#fff; border:1px solid #e2dcd6; color:#1c1917 !important; padding:0.85rem 1.1rem; border-radius:2px 14px 14px 14px; font-size:0.87rem; line-height:1.75; }
.bubble-ai p, .bubble-ai li, .bubble-ai h1, .bubble-ai h2, .bubble-ai h3,
.bubble-ai strong, .bubble-ai em { color:#1c1917 !important; }
.bubble-ai code { background:#f0ece8; padding:0.1em 0.3em; border-radius:3px; font-family:'JetBrains Mono',monospace; font-size:0.82em; color:#c2692a !important; }

/* input */
[data-testid="stTextInput"] input { background:#fff !important; border:1.5px solid #e2dcd6 !important; border-radius:6px !important; color:#1c1917 !important; font-family:'DM Sans',sans-serif !important; font-size:0.9rem !important; padding:0.75rem 1rem !important; box-shadow:none !important; }
[data-testid="stTextInput"] input:focus { border-color:#c2692a !important; box-shadow:0 0 0 3px rgba(194,105,42,0.1) !important; }
[data-testid="stTextInput"] input::placeholder { color:#c4bbb6 !important; font-style:italic; }

/* buttons */
.stButton > button { background:#1c1917 !important; color:#f7f3ee !important; border:none !important; border-radius:6px !important; font-family:'DM Sans',sans-serif !important; font-size:0.83rem !important; font-weight:500 !important; padding:0.7rem 1.2rem !important; transition:background 0.2s !important; }
.stButton > button:hover { background:#c2692a !important; }

/* sidebar selectbox */
[data-testid="stSidebar"] [data-testid="stSelectbox"] > div > div { background:#2c2724 !important; border-color:#3d3733 !important; color:#e7e0d8 !important; border-radius:3px !important; font-size:0.82rem !important; }

/* stats */
.stat-row { display:flex; gap:0.8rem; margin-top:1rem; }
.stat-chip { background:#fff; border:1px solid #e2dcd6; border-radius:6px; padding:0.5rem 0.8rem; text-align:center; flex:1; }
.stat-num { font-family:'Lora',serif; font-size:1.3rem; font-weight:600; color:#c2692a; }
.stat-lbl { font-size:0.6rem; color:#a8a09a; text-transform:uppercase; letter-spacing:0.1em; }

.thin-line { border:none; border-top:1px solid #ede8e3; margin:1rem 0; }

/* loader */
.loader-wrap {
  display:flex; align-items:center; gap:0.9rem;
  padding:1rem 1.2rem;
  background:#fff; border:1px solid #e2dcd6;
  border-radius:2px 14px 14px 14px;
  max-width:78%; margin-bottom:1.2rem;
}
.loader-dots {
  display:flex; gap:5px; align-items:center;
}
.loader-dots span {
  width:7px; height:7px; border-radius:50%;
  background:#c2692a; display:inline-block;
  animation:bounce 1.2s infinite ease-in-out;
}
.loader-dots span:nth-child(2) { animation-delay:0.2s; }
.loader-dots span:nth-child(3) { animation-delay:0.4s; }
@keyframes bounce {
  0%,80%,100% { transform:scale(0.6); opacity:0.4; }
  40%         { transform:scale(1);   opacity:1; }
}
.loader-text {
  font-family:'Lora',serif; font-style:italic;
  font-size:0.85rem; color:#a8a09a;
}

[data-testid="stAlert"] { border-radius:6px !important; font-size:0.85rem !important; }
</style>
""", unsafe_allow_html=True)


# ── helpers ───────────────────────────────────────────────────────────────────
def extract_pdf_text(pdf_bytes):
    try:
        import pypdf, io
        reader = pypdf.PdfReader(io.BytesIO(pdf_bytes))
        return "\n".join(f"--- Page {i+1} ---\n{p.extract_text() or ''}" for i, p in enumerate(reader.pages)).strip()
    except Exception as e:
        return f"Error: {e}"

def build_messages(pdf_text, question, history):
    msgs = [{"role": "system", "content": (
        "You are a precise, thoughtful document analyst. "
        f"PDF content:\n\n=== DOCUMENT ===\n{pdf_text[:60000]}\n=== END ===\n\n"
        "Answer questions clearly. Cite page numbers when helpful. Use plain prose."
    )}]
    for t in history:
        msgs.append({"role": "assistant" if t["role"] == "assistant" else "user", "content": t["content"]})
    msgs.append({"role": "user", "content": question})
    return msgs

def call_model(model, messages):
    r = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {OPENROUTER_API_KEY}", "Content-Type": "application/json",
                 "HTTP-Referer": "http://localhost:8501", "X-Title": "Readwise"},
        json={"model": model, "messages": messages, "max_tokens": 2048, "temperature": 0.3},
        timeout=60,
    )
    if r.status_code == 200:
        return r.json()["choices"][0]["message"]["content"]
    return None, r.status_code, r.text

def query(pdf_text, question, history, model):
    msgs = build_messages(pdf_text, question, history)
    result = call_model(model, msgs)
    if isinstance(result, str):
        return result
    tried, errors = [model], [f"{model} → {result[1]}"]
    for fb in MODELS:
        if fb in tried: continue
        tried.append(fb)
        result = call_model(fb, msgs)
        if isinstance(result, str):
            return result
        errors.append(f"{fb} → {result[1]}")
    raise Exception("All models failed:\n" + "\n".join(errors))


# ── session state ─────────────────────────────────────────────────────────────
for k, v in {"chat_history": [], "pdf_bytes": None, "pdf_text": None,
             "pdf_name": None, "pdf_size": None, "last_error": None,
             "pending_prompt": None, "input_key": 0}.items():
    if k not in st.session_state:
        st.session_state[k] = v


# ── sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="wordmark">Readwise</div>', unsafe_allow_html=True)
    st.markdown('<div class="wordmark-tagline">Document Intelligence</div>', unsafe_allow_html=True)
    st.markdown('<hr class="sb-divider">', unsafe_allow_html=True)

    st.markdown('<span class="sb-label">API</span>', unsafe_allow_html=True)
    if OPENROUTER_API_KEY:
        st.markdown(f'<div class="sb-key">✓ &nbsp;connected</div>', unsafe_allow_html=True)
    else:
        st.error("OPENROUTER_API_KEY missing in .env")

    st.markdown('<span class="sb-label">Model</span>', unsafe_allow_html=True)
    model_choice = st.selectbox("model", list(MODELS.keys()),
                                format_func=lambda x: MODELS[x],
                                index=0, label_visibility="collapsed")

    st.markdown('<hr class="sb-divider">', unsafe_allow_html=True)
    st.markdown('<span class="sb-label">Document</span>', unsafe_allow_html=True)

    if st.session_state.pdf_name:
        kb = round(st.session_state.pdf_size / 1024, 1)
        st.markdown(f"""
        <div style="background:#2c2724;border:1px solid #3d3733;border-radius:4px;padding:0.7rem 0.9rem;margin-bottom:0.6rem">
          <div style="font-size:0.82rem;word-break:break-all;margin-bottom:0.2rem">📄 {st.session_state.pdf_name}</div>
          <div style="font-size:0.66rem;color:#6b6460">{kb} KB · {len(st.session_state.pdf_text or ''):,} chars</div>
        </div>
        <div style="font-size:0.73rem;color:#4ade80;margin-bottom:0.4rem">● Ready</div>
        """, unsafe_allow_html=True)
    else:
        st.markdown('<div style="font-size:0.75rem;color:#4b4744;font-style:italic">No document loaded</div>', unsafe_allow_html=True)

    if st.session_state.chat_history:
        st.markdown('<hr class="sb-divider">', unsafe_allow_html=True)
        if st.button("Clear conversation", use_container_width=True):
            st.session_state.chat_history = []
            st.session_state.last_error = None
            st.rerun()

    st.markdown('<hr class="sb-divider">', unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size:0.7rem;color:#4b4744;line-height:2.1">
    • Upload any PDF up to 20 MB<br>
    • All models are free tier<br>
    • Auto-fallback on rate limits<br>
    • Full conversation context
    </div>
    """, unsafe_allow_html=True)


# ── main layout ───────────────────────────────────────────────────────────────
left, right = st.columns([1, 1.6], gap="large")

# ── LEFT ──────────────────────────────────────────────────────────────────────
with left:
    st.markdown("""
    <div class="page-title">Read it.<br><em>Understand it.</em></div>
    <div class="page-sub">Drop a PDF and ask anything. Readwise reads the whole document so you don't have to.</div>
    """, unsafe_allow_html=True)

    uploaded = st.file_uploader("Upload PDF", type=["pdf"], label_visibility="collapsed")

    if uploaded:
        raw = uploaded.read()
        if st.session_state.pdf_name != uploaded.name:
            with st.spinner("Extracting text…"):
                txt = extract_pdf_text(raw)
            st.session_state.update({
                "pdf_bytes": raw, "pdf_text": txt,
                "pdf_name": uploaded.name, "pdf_size": len(raw),
                "chat_history": [], "last_error": None,
            })
            st.success(f"Ready — {len(txt):,} chars extracted.")
            time.sleep(0.4)
            st.rerun()

    if st.session_state.pdf_name:
        kb = round(st.session_state.pdf_size / 1024, 1)
        st.markdown(f"""
        <div class="doc-card">
          <span style="font-size:1.5rem">📄</span>
          <div style="flex:1;min-width:0">
            <div class="doc-name">{st.session_state.pdf_name}</div>
            <div class="doc-meta">{kb} KB · {len(st.session_state.pdf_text or ''):,} chars</div>
          </div>
          <div class="doc-dot"></div>
        </div>
        """, unsafe_allow_html=True)

        # Quick prompts — these set pending_prompt and rerun immediately
        st.markdown('<span class="sec-label">Try asking</span>', unsafe_allow_html=True)
        prompts = [
            ("Summarise", "Give me a concise summary of this document"),
            ("Key points", "What are the most important points?"),
            ("Data & numbers", "Extract all statistics and numbers mentioned"),
            ("Conclusions", "What conclusions does this document reach?"),
            ("Open questions", "What questions does this document raise?"),
        ]
        for label, full in prompts:
            if st.button(label, key=f"qp_{label}", use_container_width=True):
                st.session_state.pending_prompt = full
                st.rerun()

    if st.session_state.chat_history:
        q = len([m for m in st.session_state.chat_history if m["role"] == "user"])
        st.markdown(f"""
        <div class="stat-row">
          <div class="stat-chip"><div class="stat-num">{q}</div><div class="stat-lbl">Questions</div></div>
          <div class="stat-chip"><div class="stat-num">{len(st.session_state.chat_history)}</div><div class="stat-lbl">Messages</div></div>
        </div>
        """, unsafe_allow_html=True)


# ── RIGHT ─────────────────────────────────────────────────────────────────────
with right:
    st.markdown('<span class="sec-label">Conversation</span>', unsafe_allow_html=True)

    if st.session_state.last_error:
        st.error(st.session_state.last_error)

    # Only show chat history — no empty box
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            st.markdown(f"""
            <div class="msg-user">
              <div class="bubble-user">{msg["content"]}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="msg-ai">
              <div class="ai-avatar">r</div>
              <div class="bubble-ai-wrap">
                <div class="bubble-ai-name">Readwise</div>
                <div class="bubble-ai">{msg["content"]}</div>
              </div>
            </div>
            """, unsafe_allow_html=True)

    if not st.session_state.chat_history:
        if st.session_state.pdf_text:
            st.markdown("""
            <div style="text-align:center;padding:2.5rem 1rem;color:#c4bbb6">
              <div style="font-size:2rem;margin-bottom:0.6rem">💬</div>
              <div style="font-family:'Lora',serif;font-style:italic;font-size:0.95rem">Your document is ready.</div>
              <div style="font-size:0.78rem;margin-top:0.3rem">Ask anything on the left or type below.</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="text-align:center;padding:2.5rem 1rem;color:#c4bbb6">
              <div style="font-size:2rem;margin-bottom:0.6rem">📖</div>
              <div style="font-family:'Lora',serif;font-style:italic;font-size:0.95rem">Nothing here yet.</div>
              <div style="font-size:0.78rem;margin-top:0.3rem">Upload a PDF on the left to get started.</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<hr class="thin-line">', unsafe_allow_html=True)

    # ── input + send ──
    # Use pending_prompt if set (from quick prompt buttons)
    prefill = st.session_state.pending_prompt or ""

    ic, bc = st.columns([5, 1])
    with ic:
        user_input = st.text_input(
            "q", value=prefill,
            placeholder="Ask something about your document…",
            label_visibility="collapsed",
            key=f"user_query_{st.session_state.input_key}"
        )
    with bc:
        send = st.button("Send", use_container_width=True)

    # Fire if quick prompt was set OR user clicked send
    should_send = send or (st.session_state.pending_prompt is not None and st.session_state.pending_prompt != "")
    question = (user_input or prefill).strip()

    if should_send and question:
        if not OPENROUTER_API_KEY:
            st.error("OPENROUTER_API_KEY missing in .env")
        elif not st.session_state.pdf_text:
            st.warning("Upload a PDF first.")
        else:
            # Clear pending prompt and bump input key to reset the text box
            st.session_state.pending_prompt = None
            st.session_state.input_key += 1
            st.session_state.last_error = None
            st.session_state.chat_history.append({"role": "user", "content": question})

            # show loader
            loader = st.empty()
            loader.markdown("""
            <div style="display:flex;align-items:flex-start;gap:0.6rem;margin-bottom:1.2rem">
              <div class="ai-avatar">r</div>
              <div>
                <div class="bubble-ai-name">Readwise</div>
                <div class="loader-wrap">
                  <div class="loader-dots">
                    <span></span><span></span><span></span>
                  </div>
                  <div class="loader-text">Reading your document…</div>
                </div>
              </div>
            </div>
            """, unsafe_allow_html=True)

            try:
                ans = query(st.session_state.pdf_text, question,
                            st.session_state.chat_history[:-1], model_choice)
                st.session_state.chat_history.append({"role": "assistant", "content": ans})
            except Exception as e:
                st.session_state.last_error = str(e)
                st.session_state.chat_history.pop()

            loader.empty()
            st.rerun()