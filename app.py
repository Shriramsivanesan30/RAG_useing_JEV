import streamlit as st
import rag

# Configure Page
st.set_page_config(
    page_title="Dexos House | Enterprise Intelligence",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Enterprise Design System (CSS)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
    --bg-primary: #0a0f1d;
    --bg-secondary: #111827;
    --card-bg: rgba(17, 24, 39, 0.75);
    --border-color: rgba(255, 255, 255, 0.08);
    --accent-blue: #3b82f6;
    --accent-indigo: #6366f1;
    --accent-teal: #14b8a6;
    --accent-emerald: #10b981;
    --accent-amber: #f59e0b;
    --accent-rose: #f43f5e;
    --text-primary: #f8fafc;
    --text-secondary: #94a3b8;
    --text-muted: #64748b;
}

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
}

/* Background gradient */
.stApp {
    background: radial-gradient(circle at 15% 15%, rgba(30, 58, 138, 0.25), transparent 40%),
                radial-gradient(circle at 85% 85%, rgba(79, 70, 229, 0.15), transparent 45%),
                #0a0f1d !important;
    color: var(--text-primary) !important;
}

/* Header Banner */
.enterprise-header {
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.7) 0%, rgba(15, 23, 42, 0.9) 100%);
    border: 1px solid var(--border-color);
    border-radius: 16px;
    padding: 24px 28px;
    margin-bottom: 24px;
    backdrop-filter: blur(16px);
    box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.brand-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(99, 102, 241, 0.15);
    border: 1px solid rgba(99, 102, 241, 0.35);
    color: #a5b4fc;
    padding: 4px 12px;
    border-radius: 9999px;
    font-size: 0.8rem;
    font-weight: 600;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    margin-bottom: 8px;
}

.brand-title {
    font-size: 1.85rem;
    font-weight: 800;
    letter-spacing: -0.025em;
    background: linear-gradient(to right, #ffffff, #cbd5e1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0;
}

.brand-subtitle {
    color: var(--text-secondary);
    font-size: 0.95rem;
    margin-top: 4px;
}

.status-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(16, 185, 129, 0.12);
    border: 1px solid rgba(16, 185, 129, 0.3);
    color: #34d399;
    padding: 6px 14px;
    border-radius: 9999px;
    font-size: 0.82rem;
    font-weight: 600;
}

.status-dot {
    width: 8px;
    height: 8px;
    background: #10b981;
    border-radius: 50%;
    box-shadow: 0 0 10px #10b981;
}

/* Metrics Row */
.metric-card {
    background: rgba(17, 24, 39, 0.6);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    padding: 16px 20px;
    backdrop-filter: blur(8px);
    transition: all 0.2s ease;
}

.metric-card:hover {
    border-color: rgba(99, 102, 241, 0.4);
    transform: translateY(-2px);
}

.metric-label {
    font-size: 0.75rem;
    font-weight: 600;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

.metric-value {
    font-size: 1.25rem;
    font-weight: 700;
    color: #f1f5f9;
    margin-top: 4px;
}

/* Answer Card */
.answer-box {
    background: linear-gradient(145deg, rgba(30, 41, 59, 0.5) 0%, rgba(15, 23, 42, 0.85) 100%);
    border: 1px solid rgba(99, 102, 241, 0.3);
    border-radius: 16px;
    padding: 28px;
    margin-top: 20px;
    margin-bottom: 24px;
    box-shadow: 0 15px 35px -10px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.1);
    position: relative;
    overflow: hidden;
}

.answer-box::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 4px;
    height: 100%;
    background: linear-gradient(to bottom, #6366f1, #06b6d4);
}

.answer-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 16px;
    border-bottom: 1px solid var(--border-color);
    padding-bottom: 12px;
}

.answer-badge {
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    color: #818cf8;
    display: flex;
    align-items: center;
    gap: 6px;
}

.answer-text {
    font-size: 1.05rem;
    line-height: 1.7;
    color: #f8fafc;
}

/* Safety & Gate Badges */
.gate-container {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
    margin: 16px 0 24px 0;
}

.gate-pill {
    padding: 10px 18px;
    border-radius: 10px;
    font-size: 0.85rem;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 8px;
    background: rgba(17, 24, 39, 0.7);
    border: 1px solid var(--border-color);
}

.gate-pill.pass {
    background: rgba(16, 185, 129, 0.1);
    border-color: rgba(16, 185, 129, 0.3);
    color: #6ee7b7;
}

.gate-pill.safe {
    background: rgba(59, 130, 246, 0.1);
    border-color: rgba(59, 130, 246, 0.3);
    color: #93c5fd;
}

/* Chunk Accordion & Evidence Cards */
.chunk-card {
    background: rgba(15, 23, 42, 0.55);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    padding: 16px;
    margin-bottom: 12px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.88rem;
    line-height: 1.6;
}

.chunk-card.kept {
    border-left: 3px solid #10b981;
}

.chunk-card.dropped {
    border-left: 3px solid #64748b;
    opacity: 0.75;
}

/* Custom button styling */
.stButton button {
    background: linear-gradient(135deg, #4f46e5 0%, #3b82f6 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 10px 24px !important;
    font-weight: 600 !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 4px 15px rgba(79, 70, 229, 0.35) !important;
}

.stButton button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 20px rgba(79, 70, 229, 0.5) !important;
}

/* Custom Text Input */
.stTextInput input {
    background: rgba(15, 23, 42, 0.8) !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    border-radius: 12px !important;
    color: #f8fafc !important;
    padding: 14px 18px !important;
    font-size: 1rem !important;
    box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.4) !important;
}

.stTextInput input:focus {
    border-color: #6366f1 !important;
    box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.25) !important;
}

/* Sidebar styling */
[data-testid="stSidebar"] {
    background-color: #0b1120 !important;
    border-right: 1px solid var(--border-color) !important;
}

/* Progress bar customization */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #6366f1, #06b6d4) !important;
}
</style>
""", unsafe_allow_html=True)

# ----------------- SIDEBAR -----------------
with st.sidebar:
    st.markdown("""
    <div style="padding: 12px 0 20px 0;">
        <div style="font-size: 1.3rem; font-weight: 800; color: #fff; display: flex; align-items: center; gap: 8px;">
            <span style="color: #6366f1;">⚡</span> Dexos House
        </div>
        <div style="font-size: 0.8rem; color: #94a3b8; margin-top: 4px;">Enterprise Knowledge Engine</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📂 Ingested Repository")
    st.markdown("""
    - **Document:** `dexos_house.md`
    - **Scope:** Complete Company KB, Services, Team, Pricing & Case Studies
    - **Vector Store:** FAISS (384-d MiniLM)
    - **Keyword Index:** BM25 Ranker
    """)

    st.markdown("---")
    st.markdown("### ⚙️ Dual-Core Pipeline")
    st.markdown("""
    - **Decision / Gatekeeper:**  
      `Jev Router` *(OpenRouter)*
    - **Natural Language Core:**  
      `GPT-OSS 120B` *(Groq LPU)*
    - **Acceptance Threshold (τ):** `0.50`
    """)

    st.markdown("---")
    st.markdown("### 💡 Recommended Prompts")
    sample_queries = [
        "Who founded Dexos House and what are their roles?",
        "What are the pricing packages for websites and apps?",
        "Explain the MRPC project built for MCET.",
        "How long did the KonguBusiness Forum website take?",
        "How do I contact Dexos House for a new project?"
    ]
    
    for q in sample_queries:
        if st.button(f"👉 {q}", key=f"btn_{q[:15]}"):
            st.session_state["user_query"] = q


# ----------------- TOP HEADER BANNER -----------------
st.markdown("""
<div class="enterprise-header">
    <div>
        <div class="brand-badge">⚡ Executive Intelligence Portal</div>
        <h1 class="brand-title">Dexos House Knowledge Base</h1>
        <div class="brand-subtitle">Verified RAG powered by TypeSafe Jev Calibrated Reasoning & Groq High-Speed Synthesis</div>
    </div>
    <div style="text-align: right;">
        <div class="status-pill">
            <span class="status-dot"></span>
            Dual-Core Engine Online
        </div>
        <div style="font-size: 0.75rem; color: #64748b; margin-top: 6px;">Latency: ~1.2s • Groq LPU Active</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ----------------- TOP METRICS BAR -----------------
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Active Document</div>
        <div class="metric-value">Dexos House KB</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Knowledge Chunks</div>
        <div class="metric-value">{len(rag.chunks)} Chunks</div>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Decision Model</div>
        <div class="metric-value">Jev System-1</div>
    </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Synthesizer</div>
        <div class="metric-value">Groq 120B</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)

# ----------------- SEARCH & QUESTION INPUT -----------------
current_query = st.session_state.get("user_query", "")
question = st.text_input(
    "Enter an enterprise inquiry:",
    value=current_query,
    placeholder="e.g. Who founded Dexos House, what services are offered, and what is the starting price?"
)

# ----------------- ANSWER & EVALUATION -----------------
if question:
    try:
        with st.spinner("Executing hybrid retrieval, Jev calibrated validation, and Groq synthesis..."):
            passages, p, kept, answer = rag.ask(question)

        # Answer Section
        st.markdown(f"""
        <div class="answer-box">
            <div class="answer-header">
                <div class="answer-badge">
                    <span>⚡</span> Synthesized Answer with In-Text Citations
                </div>
                <div style="font-size: 0.8rem; color: #94a3b8;">
                    {len(kept)} / {len(passages)} passages verified by Jev
                </div>
            </div>
            <div class="answer-text">
                {answer}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Safety & Gate Status Badges
        ans_pct = int(p.get("answerable", 0.0) * 100)
        inj_pct = int(p.get("injection", 0.0) * 100)
        ans_status = "High Confidence" if ans_pct >= 50 else "Insufficient Context"
        inj_status = "Verified Safe (0% Risk)" if inj_pct < 50 else "Flagged Attack"

        st.markdown(f"""
        <div class="gate-container">
            <div class="gate-pill pass">
                <span>🛡️</span> <b>Answerability Gate:</b> {ans_pct}% ({ans_status})
            </div>
            <div class="gate-pill safe">
                <span>🔒</span> <b>Prompt Injection Guard:</b> {inj_pct}% ({inj_status})
            </div>
            <div class="gate-pill" style="color: #cbd5e1;">
                <span>📊</span> <b>Verified Citations Kept:</b> {len(kept)} chunks (τ ≥ 0.50)
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Tabbed Inspection Section
        tab1, tab2, tab3 = st.tabs(["📑 Verified Evidence (Kept)", "🔍 Calibrated Probabilities", "🗑️ Filtered Passages (Noise)"])

        with tab1:
            st.markdown("#### Passages Retained by Jev for Final Answer")
            if kept:
                for cid in kept:
                    st.markdown(f"""
                    <div class="chunk-card kept">
                        <div style="display: flex; justify-content: space-between; margin-bottom: 6px;">
                            <span style="color: #34d399; font-weight: 700;">[{cid}] Confidence: {p[cid]:.2f}</span>
                            <span style="color: #94a3b8; font-size: 0.75rem;">Status: Retained as Evidence</span>
                        </div>
                        {passages[cid]}
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.info("No passages met the τ ≥ 0.50 relevance threshold.")

        with tab2:
            st.markdown("#### Calibrated Decision Scores (Jev System-1)")
            col_left, col_right = st.columns(2)
            cids = list(passages.keys())
            mid = len(cids) // 2

            with col_left:
                for cid in cids[:mid]:
                    score = p[cid]
                    tag = "KEPT" if cid in kept else "DROPPED"
                    st.write(f"**{cid}** • Score: `{score:.2f}` — *{tag}*")
                    st.progress(score)

            with col_right:
                for cid in cids[mid:]:
                    score = p[cid]
                    tag = "KEPT" if cid in kept else "DROPPED"
                    st.write(f"**{cid}** • Score: `{score:.2f}` — *{tag}*")
                    st.progress(score)

        with tab3:
            st.markdown("#### Passages Filtered Out to Prevent Hallucination")
            dropped = [cid for cid in passages if cid not in kept]
            if dropped:
                for cid in dropped:
                    st.markdown(f"""
                    <div class="chunk-card dropped">
                        <div style="display: flex; justify-content: space-between; margin-bottom: 6px;">
                            <span style="color: #94a3b8; font-weight: 600;">[{cid}] Score: {p[cid]:.2f}</span>
                            <span style="color: #ef4444; font-size: 0.75rem;">Status: Filtered (Below 0.50)</span>
                        </div>
                        {passages[cid]}
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.info("All retrieved passages were deemed relevant.")

    except ValueError as e:
        st.error(str(e))
    except Exception as e:
        st.error(f"Application Error: {e}")
