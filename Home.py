# ==========================================
# Home.py — SK TOKO V2
# ==========================================
import streamlit as st
import os
import base64
import urllib.request

from utils.css_styles import inject_css

# ==========================================
# KONFIGURASI HALAMAN
# ==========================================
st.set_page_config(
    page_title="SK TOKO UPTD PASAR KANDANGAN",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# FUNGSI LOGO
# ==========================================
def get_logo_base64():
    for nama_file in ["logo_hss.png", "logo.png", "Logo_HSS.png"]:
        if os.path.exists(nama_file):
            with open(nama_file, "rb") as f:
                return base64.b64encode(f.read()).decode()
    urls = [
        "https://upload.wikimedia.org/wikipedia/commons/3/3e/Lambang_Kabupaten_Hulu_Sungai_Selatan.png",
    ]
    for url in urls:
        try:
            req = urllib.request.Request(
                url, headers={"User-Agent": "Mozilla/5.0"}
            )
            with urllib.request.urlopen(req, timeout=5) as response:
                img_data = response.read()
                if len(img_data) > 100:
                    return base64.b64encode(img_data).decode()
        except Exception:
            continue
    return None

if "logo_b64" not in st.session_state:
    st.session_state["logo_b64"] = get_logo_base64()

# ==========================================
# INJECT CSS
# ==========================================
inject_css()

# ==========================================
# SIDEBAR
# ==========================================
with st.sidebar:
    logo_b64 = st.session_state.get("logo_b64")
    if logo_b64:
        st.markdown(
            f"""
            <div style="text-align:center; padding:18px 0 6px 0;">
                <img src="data:image/png;base64,{logo_b64}"
                     width="78" height="auto"
                     style="display:inline-block;
                            filter:drop-shadow(0 2px 8px rgba(0,0,0,0.4));">
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <div style="text-align:center; padding:18px 0 6px 0;">
                <div style="font-size:3rem; line-height:1;">🏛️</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <div style="text-align:center; padding:4px 0 14px 0;
                    border-bottom:1px solid rgba(255,255,255,0.08);
                    margin-bottom:14px;">
            <p style="font-family:'Inter',sans-serif;
                      font-size:1rem; font-weight:800;
                      color:#f1f5f9 !important;
                      letter-spacing:-0.02em;
                      margin:0 0 4px 0; line-height:1.3;">
                SK TOKO
            </p>
            <p style="font-family:'Inter',sans-serif;
                      font-size:0.72rem; font-weight:600;
                      color:#94a3b8 !important;
                      margin:0; line-height:1.4;">
                UPTD PASAR KANDANGAN
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="padding: 8px 4px;">
            <p style="font-family:'Inter',sans-serif;
                      font-size:0.7rem; font-weight:600;
                      color:#64748b !important;
                      text-transform:uppercase;
                      letter-spacing:0.06em;
                      margin:0 0 8px 0;">
                NAVIGASI
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.page_link("Home.py", label="🏠  Beranda", use_container_width=True)
    st.page_link("pages/1_📝_Pengantaran.py", label="📝  Pengantaran", use_container_width=True)
    st.page_link("pages/2_📤_Pengambilan.py", label="📤  Pengambilan", use_container_width=True)
    st.page_link("pages/3_📊_Data.py", label="📊  Data SK", use_container_width=True)

    st.markdown(
        """
        <div style="text-align:center; padding:24px 0 8px 0;
                    border-top:1px solid rgba(255,255,255,0.06);
                    margin-top:40px;">
            <p style="font-family:'Inter',sans-serif;
                      font-size:0.56rem; font-weight:400;
                      color:#64748b !important;
                      margin:0; line-height:1.7;">
                Developed by
            </p>
            <p style="font-family:'Inter',sans-serif;
                      font-size:0.68rem; font-weight:700;
                      color:#94a3b8 !important;
                      margin:2px 0 0 0;">
                M. Luthfi Renaldi
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ==========================================
# HALAMAN WELCOME
# ==========================================
logo_b64 = st.session_state.get("logo_b64")
logo_html = (
    f'<img src="data:image/png;base64,{logo_b64}" '
    f'width="140" height="auto" style="display:inline-block;">'
    if logo_b64
    else '<div style="font-size:6rem; line-height:1;">🏛️</div>'
)

st.markdown(
    f"""
    <style>
        .welcome-wrapper {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 65vh;
            text-align: center;
            padding: 20px;
        }}

        .welcome-logo {{
            animation: logoEntry 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
            opacity: 0;
            filter: drop-shadow(0 8px 20px rgba(0,0,0,0.12));
        }}

        @keyframes logoEntry {{
            0%   {{ opacity: 0; transform: scale(0.4) translateY(20px); }}
            60%  {{ opacity: 1; }}
            80%  {{ transform: scale(1.05) translateY(-3px); }}
            100% {{ opacity: 1; transform: scale(1) translateY(0); }}
        }}

        .welcome-title {{
            animation: textUp 0.6s ease 0.3s forwards;
            opacity: 0;
            font-family: 'Inter', sans-serif;
            font-size: 2rem;
            font-weight: 800;
            color: #0f172a;
            letter-spacing: -0.03em;
            margin: 24px 0 0 0;
            line-height: 1.2;
        }}

        .welcome-subtitle {{
            animation: textUp 0.6s ease 0.45s forwards;
            opacity: 0;
            font-family: 'Inter', sans-serif;
            font-size: 1rem;
            font-weight: 500;
            color: #64748b;
            margin: 8px 0 0 0;
        }}

        .welcome-line {{
            animation: lineExpand 0.5s ease 0.6s forwards;
            opacity: 0;
            width: 0;
            height: 3px;
            background: linear-gradient(90deg, #3b82f6, #60a5fa);
            margin: 20px auto;
            border-radius: 2px;
        }}

        @keyframes lineExpand {{
            from {{ opacity: 0; width: 0; }}
            to   {{ opacity: 1; width: 100px; }}
        }}

        .welcome-hint {{
            animation: textUp 0.6s ease 0.75s forwards;
            opacity: 0;
            font-family: 'Inter', sans-serif;
            font-size: 0.88rem;
            color: #94a3b8;
            margin: 8px 0 0 0;
        }}

        @keyframes textUp {{
            from {{ opacity: 0; transform: translateY(14px); }}
            to   {{ opacity: 1; transform: translateY(0); }}
        }}

        .info-cards {{
            display: flex;
            gap: 16px;
            margin-top: 40px;
            justify-content: center;
            flex-wrap: wrap;
            animation: textUp 0.6s ease 0.9s forwards;
            opacity: 0;
        }}

        .info-card {{
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 12px;
            padding: 16px 20px;
            min-width: 140px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        }}

        .info-card-label {{
            font-family: 'Inter', sans-serif;
            font-size: 0.7rem;
            font-weight: 600;
            color: #6b7280;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin: 0 0 4px 0;
        }}

        .info-card-value {{
            font-family: 'Inter', sans-serif;
            font-size: 1.2rem;
            font-weight: 700;
            color: #2563eb;
            margin: 0;
        }}
    </style>

    <div class="welcome-wrapper">
        <div class="welcome-logo">{logo_html}</div>
        <p class="welcome-title">SK TOKO<br>UPTD PASAR KANDANGAN</p>
        <p class="welcome-subtitle">Kabupaten Hulu Sungai Selatan</p>
        <div class="welcome-line"></div>
        <p class="welcome-hint">
            Sistem perpanjangan & penerbitan Surat Keputusan Toko
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
