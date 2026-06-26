import streamlit as st
import tempfile
import sys
import os

# 🔥 Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.predict import predict_emotion
from src.chatbot import generate_ai_response

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Emotion AI Assistant",
    layout="wide",
    page_icon="🧠"
)

# ---------------- PAGE ROUTING ----------------
query_page = st.query_params.get("page")
if "page" not in st.session_state:
    st.session_state.page = query_page if query_page in ["landing", "app"] else "landing"


def go_to_app_page():
    st.session_state.page = "app"
    st.query_params["page"] = "app"


def show_landing_page():
    st.markdown("""
    <style>
    .landing-container{
        text-align:center;
        padding-top:40px;
        padding-bottom:30px;
    }

    .landing-badge{
        display:inline-block;
        padding:8px 20px;
        border-radius:50px;
        background:rgba(95,195,212,0.1);
        border:1px solid rgba(95,195,212,0.3);
        color:#5fc3d4;
        font-size:14px;
        font-weight:600;
        letter-spacing:1px;
        margin-bottom:20px;
    }

    .landing-title{
        font-size:4rem;
        font-weight:800;
        line-height:1.1;
        background:linear-gradient(135deg, #ffffff 0%, #5fc3d4 50%, #7b8cde 100%);
        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;
        margin-bottom:20px;
        font-family: 'Syne', sans-serif;
    }

    .landing-subtitle{
        max-width:800px;
        margin:auto;
        color:#9ca3af;
        font-size:1.1rem;
        line-height:1.8;
        margin-bottom:40px;
    }

    .workflow-title{
        text-align:center;
        color:white;
        font-size:1.6rem;
        font-weight:700;
        margin-top:40px;
        margin-bottom:20px;
        font-family: 'Syne', sans-serif;
    }

    .workflow-box{
        background:rgba(255,255,255,0.04);
        border:1px solid rgba(255,255,255,0.08);
        border-radius:20px;
        padding:20px;
        text-align:center;
    }

    .workflow-step{
        font-size:1rem;
        color:white;
        font-weight:600;
    }

    .workflow-arrow{
        color:#5fc3d4;
        font-size:2rem;
        text-align:center;
        padding-top:20px;
    }

    .brain{
        font-size:100px;
        animation: float 4s ease-in-out infinite;
    }

    @keyframes float {
        0% {transform: translateY(0px);}
        50% {transform: translateY(-15px);}
        100% {transform: translateY(0px);}
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="landing-container">
        <div class="landing-badge">AI Powered Emotion Recognition</div>
        <div class="landing-title">
            Decode Your Emotions<br>
            With Artificial Intelligence
        </div>
        <div class="landing-subtitle">
            Upload a photo, detect emotions instantly using Deep Learning,
            chat with an AI that adapts to your mood,
            receive personalized recommendations,
            and monitor emotional trends over time.
        </div>
        <div class="brain">🧠</div>
    </div>
    """, unsafe_allow_html=True)

    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric("Accuracy", "92%")
    with m2:
        st.metric("Emotions", "7")
    with m3:
        st.metric("AI Powered", "24/7")
    with m4:
        st.metric("Analytics", "Real-Time")

    st.write("")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("""
        <div class="glass-card">
            <div class="card-icon">📸</div>
            <div class="card-title">Emotion Detection</div>
            <div class="card-desc">Detect facial emotions instantly using a deep learning model.</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="glass-card">
            <div class="card-icon">🤖</div>
            <div class="card-title">Adaptive Chatbot</div>
            <div class="card-desc">AI responses automatically adjust to your emotional state.</div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="glass-card">
            <div class="card-icon">💡</div>
            <div class="card-title">Smart Recommendations</div>
            <div class="card-desc">Personalized tips and suggestions to improve wellbeing.</div>
        </div>
        """, unsafe_allow_html=True)
    with c4:
        st.markdown("""
        <div class="glass-card">
            <div class="card-icon">📊</div>
            <div class="card-title">Analytics Dashboard</div>
            <div class="card-desc">Visualize emotional patterns and trends over time.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="workflow-title">How It Works</div>', unsafe_allow_html=True)
    w1, w2, w3, w4, w5 = st.columns([2, 1, 2, 1, 2])
    with w1:
        st.markdown('<div class="workflow-box"><div class="workflow-step">Upload Image</div></div>', unsafe_allow_html=True)
    with w2:
        st.markdown('<div class="workflow-arrow">→</div>', unsafe_allow_html=True)
    with w3:
        st.markdown('<div class="workflow-box"><div class="workflow-step">Detect Emotion</div></div>', unsafe_allow_html=True)
    with w4:
        st.markdown('<div class="workflow-arrow">→</div>', unsafe_allow_html=True)
    with w5:
        st.markdown('<div class="workflow-box"><div class="workflow-step">Chat + Analytics</div></div>', unsafe_allow_html=True)

    st.write("")
    _, center_col, _ = st.columns([1, 2, 1])
    with center_col:
        if st.button("Get Started", use_container_width=True, type="primary"):
            go_to_app_page()
            st.rerun()

# ===================== CUSTOM CSS =====================
st.markdown("""
<style>
/* ── Google Fonts ── */
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;800&family=Inter:wght@300;400;500;600&family=DM+Sans:wght@300;400;500;600&display=swap');

/* ── Root Variables ── */
:root {
    --bg-deep:    #06080f;
    --bg-panel:   rgba(255,255,255,0.04);
    --border:     rgba(255,255,255,0.09);
    --text-main:  #e8eaf0;
    --text-muted: #8b93a8;
    --happy:      #f9c846;
    --sad:        #7b8cde;
    --angry:      #e05d6f;
    --fear:       #b066e0;
    --disgust:    #5dba82;
    --surprise:   #f0884f;
    --neutral:    #5fc3d4;
    --accent:     #5fc3d4;
    --glow:       0 0 40px rgba(95,195,212,0.18);
}

/* ── Global Reset ── */
html, body, [data-testid="stAppViewContainer"] {
    background: var(--bg-deep) !important;
    font-family: 'Inter', sans-serif !important;
    color: var(--text-main) !important;
}

/* ── CHANGE 1: Tab content uses Inter instead of DM Sans ── */
[data-testid="stTabs"] [data-testid="stTabsContent"] *:not(h1):not(h2):not(.section-heading):not(.hero-banner h1) {
    font-family: 'Inter', sans-serif !important;
}

[data-testid="stSidebar"] { display: none; }

/* ── Animated Starfield Background ── */
[data-testid="stAppViewContainer"]::before {
    content: '';
    position: fixed;
    inset: 0;
    background:
        radial-gradient(ellipse 80% 50% at 20% 10%, rgba(95,195,212,0.07) 0%, transparent 60%),
        radial-gradient(ellipse 60% 40% at 80% 80%, rgba(123,140,222,0.07) 0%, transparent 60%),
        radial-gradient(ellipse 40% 30% at 50% 50%, rgba(176,102,224,0.04) 0%, transparent 70%);
    pointer-events: none;
    z-index: 0;
}

/* Particle dots */
[data-testid="stAppViewContainer"]::after {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
        radial-gradient(circle 1px at 15% 20%, rgba(255,255,255,0.25) 0%, transparent 100%),
        radial-gradient(circle 1px at 35% 65%, rgba(255,255,255,0.18) 0%, transparent 100%),
        radial-gradient(circle 1px at 55% 30%, rgba(255,255,255,0.22) 0%, transparent 100%),
        radial-gradient(circle 1px at 72% 55%, rgba(255,255,255,0.15) 0%, transparent 100%),
        radial-gradient(circle 1px at 88% 18%, rgba(255,255,255,0.20) 0%, transparent 100%),
        radial-gradient(circle 1px at 8%  80%, rgba(255,255,255,0.18) 0%, transparent 100%),
        radial-gradient(circle 1px at 92% 88%, rgba(255,255,255,0.20) 0%, transparent 100%),
        radial-gradient(circle 2px at 45% 90%, rgba(95,195,212,0.35) 0%, transparent 100%),
        radial-gradient(circle 2px at 78% 35%, rgba(123,140,222,0.35) 0%, transparent 100%),
        radial-gradient(circle 2px at 25% 45%, rgba(176,102,224,0.30) 0%, transparent 100%);
    pointer-events: none;
    z-index: 0;
}

/* ── Hero Banner ── */
.hero-banner {
    position: relative;
    z-index: 1;
    text-align: center;
    padding: 3rem 1rem 2rem;
}

.hero-banner .hero-eyebrow {
    font-family: 'Inter', sans-serif;
    font-size: 0.72rem;
    font-weight: 500;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 0.8rem;
}

/* ── TITLE kept as Syne (unchanged) ── */
.hero-banner h1 {
    font-family: 'Syne', sans-serif !important;
    font-size: clamp(2.2rem, 5vw, 3.8rem) !important;
    font-weight: 800 !important;
    line-height: 1.1 !important;
    background: linear-gradient(135deg, #e8eaf0 0%, var(--accent) 60%, #7b8cde 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0 0 1rem !important;
    padding: 0 !important;
}

.hero-banner .hero-sub {
    font-size: 1rem;
    color: var(--text-muted);
    max-width: 500px;
    margin: 0 auto;
    line-height: 1.6;
}

/* ── Emotion Pill / Aura ── */
.emotion-aura {
    display: inline-flex;
    align-items: center;
    gap: 0.6rem;
    padding: 0.55rem 1.4rem;
    border-radius: 999px;
    border: 1px solid rgba(95,195,212,0.4);
    background: rgba(95,195,212,0.1);
    color: var(--accent);
    font-family: 'Syne', sans-serif;
    font-size: 1rem;
    font-weight: 600;
    letter-spacing: 0.04em;
    box-shadow: 0 0 24px rgba(95,195,212,0.25), inset 0 0 12px rgba(95,195,212,0.06);
    animation: aura-pulse 3s ease-in-out infinite;
    margin: 0.5rem auto;
}

@keyframes aura-pulse {
    0%, 100% { box-shadow: 0 0 24px rgba(95,195,212,0.25), inset 0 0 12px rgba(95,195,212,0.06); }
    50%       { box-shadow: 0 0 48px rgba(95,195,212,0.50), inset 0 0 24px rgba(95,195,212,0.12); }
}

/* ── Glass Cards ── */
.glass-card {
    position: relative;
    z-index: 1;
    background: var(--bg-panel);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 1.8rem;
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    margin-bottom: 1.5rem;
    transition: border-color 0.3s;
}

.glass-card:hover {
    border-color: rgba(95,195,212,0.22);
}

.glass-card .card-icon {
    font-size: 2rem;
    margin-bottom: 0.5rem;
    display: block;
}

.glass-card h3 {
    font-family: 'Syne', sans-serif !important;
    font-size: 1.15rem !important;
    font-weight: 700 !important;
    color: var(--text-main) !important;
    margin: 0 0 0.3rem !important;
}

.glass-card p {
    font-size: 0.88rem;
    color: var(--text-muted);
    margin: 0;
}

/* ── Section Headings (kept as Syne) ── */
.section-heading {
    font-family: 'Syne', sans-serif;
    font-size: 1.6rem;
    font-weight: 800;
    color: var(--text-main);
    margin: 0.5rem 0 1.2rem;
    position: relative;
    z-index: 1;
    display: flex;
    align-items: center;
    gap: 0.6rem;
}

.section-heading::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(to right, rgba(95,195,212,0.3), transparent);
}

/* ── Tip Cards ── */
.tip-item {
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    padding: 0.9rem 1.1rem;
    background: rgba(255,255,255,0.03);
    border: 1px solid var(--border);
    border-radius: 12px;
    margin-bottom: 0.6rem;
    transition: background 0.2s;
}

.tip-item:hover { background: rgba(95,195,212,0.06); }

.tip-number {
    font-family: 'Inter', sans-serif;
    font-size: 0.72rem;
    font-weight: 800;
    letter-spacing: 0.1em;
    color: var(--accent);
    background: rgba(95,195,212,0.12);
    border-radius: 6px;
    padding: 0.2rem 0.5rem;
    white-space: nowrap;
    margin-top: 0.1rem;
}

/* ── CHANGE 4: Bigger tip text font ── */
.tip-text {
    font-size: 1rem;
    color: var(--text-main);
    line-height: 1.6;
    font-family: 'Inter', sans-serif;
}

/* ── Dominant Mood Badge ── */
.mood-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5rem 1.2rem;
    background: rgba(249,200,70,0.1);
    border: 1px solid rgba(249,200,70,0.3);
    border-radius: 999px;
    color: var(--happy);
    font-family: 'Syne', sans-serif;
    font-size: 0.95rem;
    font-weight: 700;
    margin-bottom: 1.2rem;
}

/* ── Warning / Info Boxes ── */
.warn-box {
    background: rgba(224,93,111,0.08);
    border: 1px solid rgba(224,93,111,0.25);
    border-radius: 12px;
    padding: 0.9rem 1.2rem;
    color: #e05d6f;
    font-size: 1rem;
    display: flex;
    align-items: center;
    gap: 0.6rem;
    font-family: 'Inter', sans-serif;
}

.info-box {
    background: rgba(95,195,212,0.07);
    border: 1px solid rgba(95,195,212,0.2);
    border-radius: 12px;
    padding: 0.9rem 1.2rem;
    color: var(--accent);
    font-size: 1rem;
    display: flex;
    align-items: center;
    gap: 0.6rem;
    font-family: 'Inter', sans-serif;
}

/* ── Confidence Bar ── */
.conf-bar-wrap {
    margin-top: 1rem;
}

.conf-label {
    font-size: 0.85rem;
    color: var(--text-muted);
    margin-bottom: 0.4rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    font-family: 'Inter', sans-serif;
}

.conf-bar {
    height: 6px;
    background: rgba(255,255,255,0.07);
    border-radius: 99px;
    overflow: hidden;
}

.conf-fill {
    height: 100%;
    background: linear-gradient(to right, var(--accent), #7b8cde);
    border-radius: 99px;
    transition: width 1s ease;
}

/* ── Insight Box ── */
.insight-box {
    background: rgba(95,195,212,0.06);
    border: 1px solid rgba(95,195,212,0.2);
    border-radius: 14px;
    padding: 1.2rem 1.4rem;
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    margin-top: 0.8rem;
}

.insight-icon { font-size: 1.6rem; }

/* ── CHANGE 4: Bigger insight text ── */
.insight-text {
    font-size: 1rem;
    color: var(--text-main);
    line-height: 1.6;
    font-family: 'Inter', sans-serif;
}

/* ── Footer ── */
.footer {
    text-align: center;
    padding: 2rem 0 1rem;
    font-size: 0.78rem;
    color: var(--text-muted);
    letter-spacing: 0.05em;
    position: relative;
    z-index: 1;
    font-family: 'Inter', sans-serif;
}

/* ── Streamlit Tab overrides ── */
[data-testid="stTabs"] [data-baseweb="tab-list"] {
    background: rgba(255,255,255,0.03) !important;
    border-radius: 14px !important;
    padding: 4px !important;
    border: 1px solid var(--border) !important;
    gap: 2px !important;
}

[data-testid="stTabs"] [data-baseweb="tab"] {
    background: transparent !important;
    border-radius: 10px !important;
    color: var(--text-muted) !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.88rem !important;
    font-weight: 500 !important;
    padding: 0.5rem 1.1rem !important;
    border: none !important;
    transition: all 0.2s !important;
}

[data-testid="stTabs"] [aria-selected="true"] {
    background: rgba(95,195,212,0.12) !important;
    color: var(--accent) !important;
    font-weight: 600 !important;
}

[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.03) !important;
    border: 2px dashed rgba(95,195,212,0.25) !important;
    border-radius: 16px !important;
    padding: 1rem !important;
}

[data-testid="stFileUploader"]:hover {
    border-color: rgba(95,195,212,0.5) !important;
    background: rgba(95,195,212,0.04) !important;
}

/* ── CHANGE 2: Smaller uploaded image ── */
[data-testid="stImage"] img {
    max-width: 180px !important;
    max-height: 180px !important;
    width: auto !important;
    height: auto !important;
    border-radius: 12px !important;
    object-fit: cover;
}

/* ── CHANGE 3: Chat tab — larger fonts ── */
[data-testid="stChatMessage"] p,
[data-testid="stChatMessage"] span,
[data-testid="stChatMessage"] div {
    font-family: 'Inter', sans-serif !important;
    font-size: 1.15rem !important;
    line-height: 1.8 !important;
}

[data-testid="stChatMessage"] {
    background: rgba(255,255,255,0.03) !important;
    border: 1px solid var(--border) !important;
    border-radius: 14px !important;
    padding: 1.2rem 1.6rem !important;
    margin-bottom: 0.9rem !important;
}

/* ── CHANGE 3: Larger chat input textarea ── */
[data-testid="stChatInput"] textarea {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    color: var(--text-main) !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 1.12rem !important;
    min-height: 96px !important;
    padding: 1.1rem 1.4rem !important;
    line-height: 1.7 !important;
}

/* ── CHANGE 4 & 5: Dashboard — bigger metric text ── */
div[data-testid="stMetric"] {
    background: rgba(255,255,255,0.03) !important;
    border: 1px solid var(--border) !important;
    border-radius: 14px !important;
    padding: 1rem 1.2rem !important;
}

div[data-testid="stMetric"] label,
div[data-testid="stMetric"] [data-testid="stMetricLabel"] p {
    font-family: 'Inter', sans-serif !important;
    font-size: 0.95rem !important;
    font-weight: 600 !important;
    color: var(--text-muted) !important;
    letter-spacing: 0.03em !important;
}

div[data-testid="stMetric"] [data-testid="stMetricValue"] {
    font-family: 'Inter', sans-serif !important;
    font-size: 1.6rem !important;
    font-weight: 700 !important;
    color: var(--text-main) !important;
}

/* ── CHANGE 5: Dashboard — clear chart axis/tick labels ── */
[data-testid="stVegaLiteChart"] text,
[data-testid="stVegaLiteChart"] .vega-embed text {
    fill: #c8ccd8 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 13px !important;
    font-weight: 500 !important;
}

[data-testid="stVegaLiteChart"] .role-axis-label text {
    fill: #e8eaf0 !important;
    font-size: 13px !important;
    font-weight: 600 !important;
}

[data-testid="stVegaLiteChart"] .role-title text {
    fill: #e8eaf0 !important;
    font-size: 14px !important;
    font-weight: 700 !important;
}

/* Chart containers */
[data-testid="stVegaLiteChart"], [data-testid="element-container"] canvas {
    border-radius: 12px !important;
}

/* ── CHANGE 4: Dashboard chart section labels ── */
[data-testid="stTabs"] [data-testid="stTabsContent"] div[style*="font-size:0.8rem"] {
    font-size: 0.95rem !important;
    font-family: 'Inter', sans-serif !important;
    color: #b0b8cc !important;
    font-weight: 600 !important;
    letter-spacing: 0.08em !important;
}

/* Remove default white backgrounds */
.stAlert { border-radius: 12px !important; }

section[data-testid="stMain"] > div { position: relative; z-index: 1; }

/* Scrollbar */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(95,195,212,0.25); border-radius: 99px; }
</style>
""", unsafe_allow_html=True)

if st.session_state.page == "landing":
    show_landing_page()
    st.stop()

# ===================== HERO BANNER =====================
st.markdown("""
<div class="hero-banner">
    <div class="hero-eyebrow">⚡ Powered by Computer Vision + LLM</div>
    <h1>Emotion-Aware<br>AI Assistant</h1>
    <p class="hero-sub">
        Upload your image, detect your emotional state in real time,
        and receive a personalized AI experience tailored to how you feel.
    </p>
</div>
""", unsafe_allow_html=True)

# ── Feature Cards Row ──
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""
    <div class="glass-card">
        <span class="card-icon">🔬</span>
        <h3>Vision Detection</h3>
        <p>Deep learning model reads your facial expression with precision</p>
    </div>""", unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="glass-card">
        <span class="card-icon">🤖</span>
        <h3>Adaptive Chat</h3>
        <p>AI responses shift tone and empathy based on your detected mood</p>
    </div>""", unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="glass-card">
        <span class="card-icon">💡</span>
        <h3>Smart Tips</h3>
        <p>Curated recommendations to elevate your mental wellbeing</p>
    </div>""", unsafe_allow_html=True)
with col4:
    st.markdown("""
    <div class="glass-card">
        <span class="card-icon">📊</span>
        <h3>Mood Analytics</h3>
        <p>Live dashboard tracking your emotional patterns over time</p>
    </div>""", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "emotion" not in st.session_state:
    st.session_state.emotion = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------------- TABS ----------------
tab1, tab2, tab3, tab4 = st.tabs([
    "🖼️  Detect Emotion",
    "🤖  AI Chatbot",
    "💡  Recommendations",
    "📊  Dashboard"
])

# ===================== IMAGE TAB =====================
with tab1:
    st.markdown('<div class="section-heading">🖼️ Emotion Detection</div>', unsafe_allow_html=True)

    left, right = st.columns([1, 1], gap="large")

    with left:
        st.markdown("""
        <div class="info-box">
            📸 Upload a clear front-facing photo for best accuracy
        </div>
        """, unsafe_allow_html=True)
        st.write("")

        uploaded_file = st.file_uploader(
            "Drop your image here or browse",
            type=["jpg", "png", "jpeg"],
            label_visibility="collapsed"
        )

        if uploaded_file:
            with tempfile.NamedTemporaryFile(delete=False) as tmp:
                tmp.write(uploaded_file.read())
                temp_path = tmp.name

            # CHANGE 2: width=180 keeps the image compact
            st.image(uploaded_file, caption="📷 Uploaded Image", width=180)

    with right:
        if uploaded_file:
            emotion, confidence = predict_emotion(temp_path)
            st.session_state.emotion = emotion

            emotion_icons = {
                "happy": "😄", "sad": "😢", "angry": "😠",
                "fear": "😨", "disgust": "🤢", "surprise": "😲", "neutral": "😐"
            }
            icon = emotion_icons.get(emotion.lower(), "🧠")

            st.markdown(f"""
            <div style="margin-top:1.5rem;">
                <div class="conf-label">Detected Emotion</div>
                <div class="emotion-aura" style="display:flex; gap:0.6rem; align-items:center;
                     padding:0.8rem 1.6rem; font-size:1.3rem; width:fit-content; margin:0.6rem 0;">
                    {icon} {emotion.upper()}
                </div>
                <div class="conf-bar-wrap">
                    <div class="conf-label">Confidence — {confidence:.0%}</div>
                    <div class="conf-bar">
                        <div class="conf-fill" style="width:{confidence*100:.1f}%"></div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.write("")
            st.markdown(f"""
            <div class="insight-box">
                <span class="insight-icon">🧠</span>
                <span class="insight-text">
                    The model detected <strong>{emotion}</strong> with <strong>{confidence:.0%}</strong> confidence.
                    Head to the <em>AI Chatbot</em> tab to start a conversation tuned to your mood.
                </span>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="height:260px; display:flex; align-items:center; justify-content:center;
                 flex-direction:column; gap:1rem; opacity:0.4;">
                <span style="font-size:4rem;">🌐</span>
                <span style="font-size:0.9rem; color:#8b93a8; font-family:Inter,sans-serif;">
                    Your result will appear here
                </span>
            </div>
            """, unsafe_allow_html=True)


# ===================== CHATBOT TAB =====================
with tab2:
    st.markdown('<div class="section-heading">🤖 Emotion-Aware Chat</div>', unsafe_allow_html=True)

    if not st.session_state.chat_history:
        st.markdown("""
        <div class="info-box">
            💬 Your conversation will appear here once you start chatting
        </div>
        """, unsafe_allow_html=True)

    if st.session_state.emotion is None:
        st.markdown("""
        <div class="warn-box">
            ⚠️ Please detect your emotion first by uploading an image in the <strong>Detect Emotion</strong> tab
        </div>
        """, unsafe_allow_html=True)
    else:
        emotion_icons = {
            "happy": "😄", "sad": "😢", "angry": "😠",
            "fear": "😨", "disgust": "🤢", "surprise": "😲", "neutral": "😐"
        }
        icon = emotion_icons.get(st.session_state.emotion.lower(), "🧠")

        st.markdown(f"""
        <div style="margin-bottom:1.2rem;">
            <span style="font-size:0.9rem; color:#8b93a8; text-transform:uppercase;
                  letter-spacing:0.1em; font-family:Inter,sans-serif;">Active Mood Profile</span><br>
            <div class="emotion-aura" style="display:inline-flex; margin-top:0.4rem;
                 width:fit-content; font-size:0.95rem;">
                {icon} {st.session_state.emotion.upper()}
            </div>
        </div>
        """, unsafe_allow_html=True)

        user_input = st.chat_input("How are you feeling? Let's talk...")

        if user_input:
            response = generate_ai_response(
                st.session_state.emotion,
                user_input
            )
            st.session_state.chat_history.append({
                "emotion": st.session_state.emotion,
                "user": user_input,
                "bot": response
            })

        for chat in st.session_state.chat_history:
            with st.chat_message("user"):
                st.markdown(chat["user"])
            with st.chat_message("assistant"):
                st.markdown(chat["bot"])


# ===================== RECOMMENDATIONS TAB =====================
from src.recommendations import get_all_recommendations

with tab3:
    st.markdown('<div class="section-heading">💡 Personalized Recommendations</div>', unsafe_allow_html=True)

    if not st.session_state.chat_history:
        st.markdown("""
        <div class="warn-box">
            ⚠️ No session data yet — start chatting first to get personalized tips
        </div>
        """, unsafe_allow_html=True)
    else:
        emotions = [chat["emotion"] for chat in st.session_state.chat_history]
        emotion_counts = {}
        for e in emotions:
            emotion_counts[e] = emotion_counts.get(e, 0) + 1

        dominant = max(emotion_counts, key=emotion_counts.get)
        emotion_icons = {
            "happy": "😄", "sad": "😢", "angry": "😠",
            "fear": "😨", "disgust": "🤢", "surprise": "😲", "neutral": "😐"
        }
        icon = emotion_icons.get(dominant.lower(), "🧠")

        st.markdown(f"""
        <div class="mood-badge">{icon} Dominant Mood: {dominant.upper()}</div>
        """, unsafe_allow_html=True)

        tips = get_all_recommendations(dominant)

        st.markdown('<div style="font-family:Inter,sans-serif; font-weight:700; font-size:1rem; color:#8b93a8; margin-bottom:0.8rem; text-transform:uppercase; letter-spacing:0.08em;">10 Tips to Improve Your Mood</div>', unsafe_allow_html=True)

        tip_emojis = ["🌱","🧘","🎵","💧","🌿","📖","🌤","🤝","🎯","✨"]
        for i, tip in enumerate(tips, 1):
            emoji = tip_emojis[i-1] if i <= len(tip_emojis) else "•"
            st.markdown(f"""
            <div class="tip-item">
                <span class="tip-number">{i:02d}</span>
                <span class="tip-text">{emoji}&nbsp; {tip}</span>
            </div>
            """, unsafe_allow_html=True)


# ===================== DASHBOARD TAB =====================
with tab4:
    st.markdown('<div class="section-heading">📊 Emotion Analytics</div>', unsafe_allow_html=True)

    if not st.session_state.chat_history:
        st.markdown("""
        <div class="info-box">
            📊 Analytics will appear here as you have more conversations
        </div>
        """, unsafe_allow_html=True)
    else:
        emotions = [chat["emotion"] for chat in st.session_state.chat_history]
        emotion_counts = {}
        for emo in emotions:
            emotion_counts[emo] = emotion_counts.get(emo, 0) + 1

        # Metric Row
        dominant = max(emotion_counts, key=emotion_counts.get)
        m1, m2, m3 = st.columns(3)
        m1.metric("💬 Total Sessions", len(emotions))
        m2.metric("🎯 Dominant Emotion", dominant.capitalize())
        m3.metric("🌈 Unique Emotions", len(emotion_counts))

        st.write("")

        c1, c2 = st.columns(2, gap="large")

        with c1:
            # CHANGE 5: Larger, clearer chart label
            st.markdown('<div style="font-size:1rem; font-weight:700; text-transform:uppercase; letter-spacing:0.08em; color:#c8ccd8; font-family:Inter,sans-serif; margin-bottom:0.6rem;">Emotion Distribution</div>', unsafe_allow_html=True)
            st.bar_chart(emotion_counts, use_container_width=True)

        with c2:
            positive = ["happy", "surprise"]
            negative = ["sad", "angry", "fear", "disgust"]
            pos_count = sum(1 for e in emotions if e in positive)
            neg_count = sum(1 for e in emotions if e in negative)
            neu_count = sum(1 for e in emotions if e == "neutral")

            pie_data = {"Positive 😊": pos_count, "Neutral 😐": neu_count, "Negative 😔": neg_count}
            st.markdown('<div style="font-size:1rem; font-weight:700; text-transform:uppercase; letter-spacing:0.08em; color:#c8ccd8; font-family:Inter,sans-serif; margin-bottom:0.6rem;">Mental State Overview</div>', unsafe_allow_html=True)
            st.bar_chart(pie_data, use_container_width=True)

        st.write("")
        st.markdown('<div style="font-size:1rem; font-weight:700; text-transform:uppercase; letter-spacing:0.08em; color:#c8ccd8; font-family:Inter,sans-serif; margin-bottom:0.6rem;">Mood Trend Over Sessions</div>', unsafe_allow_html=True)
        emotion_score = {
            "happy": 5, "surprise": 4, "neutral": 3,
            "sad": 2, "angry": 1, "fear": 1, "disgust": 1
        }
        trend = [emotion_score.get(e, 3) for e in emotions]
        st.line_chart(trend, use_container_width=True)

        # Insight box
        if dominant in ["sad", "angry", "fear"]:
            st.markdown("""
            <div class="insight-box" style="border-color:rgba(224,93,111,0.3); background:rgba(224,93,111,0.06);">
                <span class="insight-icon">⚠️</span>
                <span class="insight-text" style="color:#e05d6f;">
                    <strong>Heads up:</strong> Negative emotions are frequent in your sessions.
                    Try the relaxation tips in the <em>Recommendations</em> tab.
                </span>
            </div>""", unsafe_allow_html=True)
        elif dominant == "neutral":
            st.markdown("""
            <div class="insight-box">
                <span class="insight-icon">🙂</span>
                <span class="insight-text">Your emotional state is mostly balanced and stable.</span>
            </div>""", unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="insight-box" style="border-color:rgba(249,200,70,0.3); background:rgba(249,200,70,0.06);">
                <span class="insight-icon">🌟</span>
                <span class="insight-text" style="color:#f9c846;">
                    <strong>Great news:</strong> You're mostly in a positive emotional state — keep it up!
                </span>
            </div>""", unsafe_allow_html=True)

# ── Footer ──
st.markdown("""
<div class="footer">
    🧠 Emotion AI Assistant &nbsp;·&nbsp; Computer Vision + LLM + Analytics &nbsp;·&nbsp;
    Built with ❤️ using Streamlit
</div>
""", unsafe_allow_html=True)