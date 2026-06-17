# ==========================================
# utils/helpers.py
# ==========================================
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

# ==========================================
# TIMEZONE
# ==========================================
def now_wita():
    return datetime.now(ZoneInfo("Asia/Makassar"))

def today_wita():
    return now_wita().date()

# ==========================================
# WORKSHEET & KOLOM
# ==========================================
WS_SK = "DATA_SK"

KOLOM_SK = [
    "No",
    "No_Surat",
    "Lokasi_Pasar",
    "Tanggal_Pengantaran",
    "Tanggal_Pengambilan",
    "Nama_Toko",
    "No_Toko",
    "Nama_Pemilik_Asli",
    "No_NIK",
    "Tempat_Lahir",
    "Tanggal_Lahir",
    "Alamat",
    "Pekerjaan",
    "Nama_Pengantar_Berkas",
    "No_HP_Pengantar",
    "Penerima_Berkas",
    "Kelurahan_Desa",
    "Kecamatan",
    "Kabupaten",
    "Modal_Usaha",
    "Jenis_Usaha",
    "Waktu_Kegiatan",
    "Sarana_Usaha",
    "Tanggal_Ditetapkan",
    "Masa_Berlaku_Tahun",
    "Tanggal_Berakhir",
    "Kelengkapan_Berkas",
    "Drive_Folder_URL",
    "Status_SK"
]

# ==========================================
# DROPDOWN OPTIONS
# ==========================================
LOKASI_PASAR_OPTIONS = [
    "PASAR KANDANGAN",
    "PASAR ANGKINANG",
    "PASAR RAKYAT TERPADU"
]

MASA_BERLAKU_OPTIONS = [2, 3, 5]

KELENGKAPAN_BERKAS = [
    "SK ASLI MENEMPATI",
    "PAS FOTO 3X4 (2 LBR)",
    "MATERAI 10.000 (2 LBR)",
    "FC KTP PEMILIK",
    "FC KARTU SEWA",
    "SURAT KUASA",
    "SURAT KEHILANGAN"
]

# ==========================================
# FORMAT & KONVERSI
# ==========================================
def to_float(val):
    try:
        txt = str(val).strip().replace(",", "")
        if txt in ["", "-", "nan", "None", "null", "<NA>"]:
            return 0.0
        return float(txt)
    except:
        return 0.0

def rupiah(val):
    try:
        num = int(round(float(val)))
        if num < 0:
            return f"-Rp {abs(num):,}".replace(",", ".")
        return f"Rp {num:,}".replace(",", ".")
    except:
        return "Rp 0"

def format_tgl_indo(tgl):
    """Format tanggal jadi: Senin, 17 Juni 2026"""
    if not tgl or str(tgl).strip() in ["-", "nan", "", "None"]:
        return ""
    try:
        if isinstance(tgl, str):
            tgl_bersih = tgl.strip().replace("/", "-")
            if len(tgl_bersih.split("-")[-1]) == 2:
                dt = datetime.strptime(tgl_bersih, "%d-%m-%y")
            else:
                dt = datetime.strptime(tgl_bersih, "%d-%m-%Y")
        else:
            dt = tgl

        hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"][dt.weekday()]
        bulan = [
            "Januari", "Februari", "Maret", "April", "Mei", "Juni",
            "Juli", "Agustus", "September", "Oktober", "November", "Desember"
        ][dt.month - 1]
        return f"{hari}, {dt.day} {bulan} {dt.year}"
    except:
        return str(tgl)

def hitung_tanggal_berakhir(tgl_ditetapkan, tahun_berlaku):
    """Hitung tanggal berakhir SK = tanggal ditetapkan + N tahun"""
    try:
        if isinstance(tgl_ditetapkan, str):
            tgl_bersih = tgl_ditetapkan.strip().replace("/", "-")
            if len(tgl_bersih.split("-")[-1]) == 2:
                dt = datetime.strptime(tgl_bersih, "%d-%m-%y")
            else:
                dt = datetime.strptime(tgl_bersih, "%d-%m-%Y")
        else:
            dt = tgl_ditetapkan

        tgl_akhir = dt.replace(year=dt.year + int(tahun_berlaku))
        return tgl_akhir.strftime("%d-%m-%Y")
    except:
        return "-"

def normalisasi_no(val):
    try:
        txt = str(val).replace("\u00a0", "").replace("'", "").strip()
        try:
            return str(int(float(txt)))
        except:
            return txt
    except:
        return ""

# ==========================================
# DATAFRAME UTILS
# ==========================================
def get_empty_df():
    return pd.DataFrame(columns=KOLOM_SK)

def pastikan_kolom(df, kolom_list):
    for col in kolom_list:
        if col not in df.columns:
            df[col] = "-"
    return df

def urutkan_no(df, ascending=False):
    try:
        if df.empty or "No" not in df.columns:
            return df
        d = df.copy()
        d["_sort_no"] = pd.to_numeric(d["No"], errors="coerce")
        d = d.sort_values(by="_sort_no", ascending=ascending, na_position="last").drop(columns="_sort_no")
        return d
    except:
        return df

def get_next_no(df, col="No"):
    try:
        if df.empty or col not in df.columns:
            return 1
        nums = pd.to_numeric(df[col], errors="coerce").dropna()
        return int(nums.max()) + 1 if not nums.empty else 1
    except:
        return 1

def tampilkan_n_terakhir(df, n=30):
    try:
        if df.empty:
            return df
        return urutkan_no(df, ascending=False).head(n)
    except:
        return df

# ==========================================
# LOAD & SAVE
# ==========================================
def load_data(conn_obj, worksheet=WS_SK):
    try:
        df = conn_obj.read(worksheet=worksheet, ttl=60)

        if 
