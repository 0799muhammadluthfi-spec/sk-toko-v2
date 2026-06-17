# ==========================================
# utils/css_styles.py — SK TOKO V2
# ==========================================

CSS_GLOBAL = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&display=swap');

    /* ============ BASE ============ */
    .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stMainBlockContainer"],
    .main {
        background: linear-gradient(160deg, #f8fafc 0%, #f1f5f9 100%) !important;
        color-scheme: light !important;
    }

    /* ============ HIDE ELEMENTS ============ */
    #MainMenu { display: none !important; }
    footer { display: none !important; }
    .stAppDeployButton { display: none !important; }
    [data-testid="manage-app-button"] { display: none !important; }
    [data-testid="stStatusWidget"] { display: none !important; }
    button[title="View fullscreen"] { display: none !important; }

    /* ============ SIDEBAR ============ */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a 0%, #1e293b 50%, #0f172a 100%) !important;
        border-right: 1px solid rgba(255,255,255,0.05) !important;
    }

    [data-testid="stSidebar"] > div {
        background: transparent !important;
    }

    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] span {
        font-family: 'Inter', sans-serif !important;
        color: #e2e8f0 !important;
    }

    /* ============ SIDEBAR PAGE LINKS ============ */
    [data-testid="stSidebar"] [data-testid="stPageLink"] > a {
        background: transparent !important;
        border: 1px solid rgba(255,255,255,0.06) !important;
        color: #cbd5e1 !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.78rem !important;
        font-weight: 600 !important;
        padding: 10px 14px !important;
        border-radius: 8px !important;
        text-decoration: none !important;
        transition: all 0.2s ease !important;
    }

    [data-testid="stSidebar"] [data-testid="stPageLink"] > a:hover {
        background: rgba(255,255,255,0.08) !important;
        color: #f1f5f9 !important;
        border-color: rgba(255,255,255,0.15) !important;
        transform: translateX(3px) !important;
    }

    /* ============ TOMBOL HIDE SIDEBAR ============ */
    [data-testid="stSidebar"] button[kind="header"] {
        background: rgba(255,255,255,0.25) !important;
        border: 2px solid rgba(255,255,255,0.50) !important;
        border-radius: 8px !important;
        opacity: 1 !important;
    }

    [data-testid="stSidebar"] button[kind="header"] svg * {
        fill: #ffffff !important;
        stroke: #ffffff !important;
    }

    [data-testid="collapsedControl"] {
        background: #ffffff !important;
        border: 2px solid #475569 !important;
        border-radius: 8px !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15) !important;
        opacity: 1 !important;
    }

    [data-testid="collapsedControl"] svg * {
        fill: #0f172a !important;
        stroke: #0f172a !important;
    }

    /* ============ TYPOGRAPHY ============ */
    .main h1, .main h2, .main h3,
    .main p, .main label, .main input,
    .main [data-testid="stMarkdownContainer"] p,
    .main [data-testid="stWidgetLabel"] label,
    .main [data-testid="stWidgetLabel"] p,
    .main .stButton > button,
    .main .stDownloadButton > button {
        font-family: 'Inter', -apple-system, sans-serif !important;
    }

    .main h1 {
        font-size: 1.6rem !important;
        font-weight: 800 !important;
        color: #0f172a !important;
        letter-spacing: -0.03em !important;
    }

    .main h2 {
        font-size: 1.2rem !important;
        font-weight: 700 !important;
        color: #1e293b !important;
    }

    .main h3 {
        font-size: 1rem !important;
        font-weight: 600 !important;
        color: #334155 !important;
    }

    .main p {
        font-size: 0.9rem !important;
        color: #374151 !important;
    }

    /* ============ INPUT — PUTIH BERSIH ============ */
    div[data-baseweb="input"],
    div[data-baseweb="base-input"] {
        background: #ffffff !important;
        border: 1.5px solid #cbd5e1 !important;
        border-radius: 10px !important;
        padding: 0 !important;
        transition: all 0.2s ease !important;
    }

    div[data-baseweb="input"]:hover,
    div[data-baseweb="base-input"]:hover {
        border-color: #94a3b8 !important;
    }

    div[data-baseweb="input"]:focus-within,
    div[data-baseweb="base-input"]:focus-within {
        border-color: #2563eb !important;
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15) !important;
    }

    div[data-baseweb="input"] input,
    div[data-baseweb="base-input"] input {
        background: #ffffff !important;
        color: #0f172a !important;
        font-size: 0.92rem !important;
        font-weight: 500 !important;
        padding: 12px 16px !important;
        border: none !important;
        outline: none !important;
    }

    div[data-baseweb="input"] input::placeholder {
        color: #94a3b8 !important;
        font-weight: 400 !important;
    }

    /* ============ SELECTBOX ============ */
    div[data-baseweb="select"] > div {
        background: #ffffff !important;
        border: 1.5px solid #cbd5e1 !important;
        border-radius: 10px !important;
    }

    div[data-baseweb="select"] > div:hover {
        border-color: #94a3b8 !important;
    }

    /* ============ TEXT AREA ============ */
    textarea {
        background: #ffffff !important;
        color: #0f172a !important;
        border: 1.5px solid #cbd5e1 !important;
        border-radius: 10px !important;
        font-size: 0.92rem !important;
        font-weight: 500 !important;
        padding: 12px 16px !important;
    }

    textarea:focus {
        border-color: #2563eb !important;
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15) !important;
        outline: none !important;
    }

    /* ============ HILANGKAN TOMBOL +/- ============ */
    button[data-testid="stNumberInputStepDown"],
    button[data-testid="stNumberInputStepUp"] {
        display: none !important;
    }

    /* ============ LABEL ============ */
    label[data-testid="stWidgetLabel"] p {
        font-size: 0.82rem !important;
        font-weight: 600 !important;
        color: #0f172a !important;
        text-transform: uppercase !important;
        letter-spacing: 0.02em !important;
        margin-bottom: 6px !important;
    }

    /* ============ METRIC ============ */
    [data-testid="stMetric"] {
        background: #ffffff !important;
        border: 1px solid #e5e7eb !important;
        border-radius: 12px !important;
        padding: 16px 20px !important;
        box-shadow: 0 1px 4px rgba(0,0,0,0.04) !important;
    }

    [data-testid="stMetricLabel"] {
        font-size: 0.7rem !important;
        font-weight: 600 !important;
        text-transform: uppercase !important;
        color: #6b7280 !important;
    }

    [data-testid="stMetricValue"] {
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 1.55rem !important;
        font-weight: 700 !important;
        color: #111827 !important;
    }

    /* ============ BUTTONS ============ */
    .main .stButton > button {
        font-size: 0.85rem !important;
        font-weight: 600 !important;
        border-radius: 10px !important;
        color: #374151 !important;
        border: 1.5px solid #d1d5db !important;
        background: #ffffff !important;
        padding: 10px 16px !important;
        transition: all 0.2s ease !important;
    }

    .main .stButton > button:hover {
        background: #f9fafb !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06) !important;
        transform: translateY(-1px) !important;
    }

    .main .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #3b82f6, #2563eb) !important;
        border: none !important;
        color: #ffffff !important;
    }

    .main .stButton > button[kind="primary"]:hover {
        background: linear-gradient(135deg, #2563eb, #1d4ed8) !important;
        box-shadow: 0 4px 14px rgba(37,99,235,0.28) !important;
    }

    /* ============ DOWNLOAD BUTTON ============ */
    .main .stDownloadButton > button {
        background: linear-gradient(135deg, #10b981, #059669) !important;
        color: #ffffff !important;
        border: none !important;
        font-weight: 600 !important;
        border-radius: 10px !important;
        padding: 10px 16px !important;
    }

    .main .stDownloadButton > button:hover {
        background: linear-gradient(135deg, #059669, #047857) !important;
    }

    /* ============ CHECKBOX JADI TOMBOL PILL ============ */
    [data-testid="stCheckbox"] {
        margin-bottom: 8px !important;
        width: 100% !important;
    }

    [data-testid="stCheckbox"] > label {
        background: #ffffff !important;
        border: 1.5px solid #cbd5e1 !important;
        border-radius: 10px !important;
        padding: 12px 18px !important;
        cursor: pointer !important;
        transition: all 0.2s ease !important;
        width: 100% !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        text-align: center !important;
    }

    [data-testid="stCheckbox"] > label:hover {
        border-color: #2563eb !important;
        background: #eff6ff !important;
        transform: translateY(-1px) !important;
    }

    [data-testid="stCheckbox"] > label > div:first-child {
        display: none !important;
    }

    [data-testid="stCheckbox"] > label p {
        font-size: 0.85rem !important;
        font-weight: 600 !important;
        color: #475569 !important;
        margin: 0 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.02em !important;
        text-align: center !important;
    }

    [data-testid="stCheckbox"] > label:has(input:checked) {
        background: linear-gradient(135deg, #3b82f6, #2563eb) !important;
        border-color: #2563eb !important;
        box-shadow: 0 4px 14px rgba(37, 99, 235, 0.35) !important;
    }

    [data-testid="stCheckbox"] > label:has(input:checked) p {
        color: #ffffff !important;
    }

    /* ============ FORM ============ */
    [data-testid="stForm"] {
        background: #ffffff !important;
        border: 1px solid #e5e7eb !important;
        border-radius: 14px !important;
        padding: 24px !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04) !important;
    }

    /* ============ EXPANDER ============ */
    [data-testid="stExpander"] {
        border: 1px solid #e5e7eb !important;
        border-radius: 12px !important;
        background: #ffffff !important;
    }

    /* ============ DATAFRAME ============ */
    [data-testid="stDataFrame"] {
        border-radius: 12px !important;
        border: 1px solid #e5e7eb !important;
    }

    [data-testid="stDataFrame"] th {
        font-family: 'Inter', sans-serif !important;
        font-size: 0.72rem !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        color: #4b5563 !important;
        background: #f9fafb !important;
    }

    [data-testid="stDataFrame"] td {
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 0.8rem !important;
        color: #374151 !important;
    }

    /* ============ ALERT ============ */
    .main [data-testid="stAlert"] {
        border-radius: 10px !important;
    }

    .main [data-testid="stAlert"] p {
        font-size: 0.86rem !important;
        font-weight: 500 !important;
    }

    /* ============ TABS ============ */
    .main [data-testid="stTabs"] [role="tab"] {
        font-family: 'Inter', sans-serif !important;
        font-size: 0.85rem !important;
        font-weight: 600 !important;
        color: #64748b !important;
    }

    .main [data-testid="stTabs"] [role="tab"][aria-selected="true"] {
        color: #2563eb !important;
    }

    /* ============ DIVIDER ============ */
    .main hr {
        border: none !important;
        border-top: 1px solid #e5e7eb !important;
        margin: 16px 0 !important;
    }

    /* ============ SCROLLBAR ============ */
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-thumb {
        background: #cbd5e1;
        border-radius: 4px;
    }

    /* ============ BLOCK CONTAINER ============ */
    .main .block-container {
        max-width: 85%;
        margin: 0 auto;
        padding-top: 1.5rem !important;
        animation: pageEnter 0.4s ease both;
    }

    @keyframes pageEnter {
        from { opacity: 0; transform: translateY(10px); }
        to   { opacity: 1; transform: translateY(0); }
    }

    @media (max-width: 768px) {
        .main .block-container {
            max-width: 100%;
            padding-left: 1rem;
            padding-right: 1rem;
        }
    }

    /* ============ ANIMASI KONTEN ============ */
    [data-testid="stMetric"],
    [data-testid="stForm"],
    [data-testid="stDataFrame"] {
        animation: fadeUp 0.4s ease both;
    }

    @keyframes fadeUp {
        from { opacity: 0; transform: translateY(8px); }
        to   { opacity: 1; transform: translateY(0); }
    }
</style>
"""


def inject_css():
    import streamlit as st
    st.markdown(CSS_GLOBAL, unsafe_allow_html=True)
