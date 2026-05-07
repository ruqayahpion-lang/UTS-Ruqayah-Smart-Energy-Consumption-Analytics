import streamlit as st
import pandas as pd
import plotly.express as px
from pyspark.sql import SparkSession
from sklearn.linear_model import LinearRegression
import os

# Pengaturan Path Absolute agar folder 'output' terbaca [cite: 170, 171]
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

# Konfigurasi Tampilan Web [cite: 173]
st.set_page_config(page_title="Energy Analytics Dashboard", layout="wide")
st.title("⚡ Smart Energy Consumption Dashboard")
st.markdown("Monitoring lonjakan konsumsi listrik kawasan industri secara real-time.")

@st.cache_resource
def get_spark():
    return SparkSession.builder.appName("Dashboard_App").getOrCreate()

spark = get_spark()

# Fungsi untuk membaca file Parquet [cite: 192, 196]
def load_parquet_data(folder_name):
    path = os.path.join(OUTPUT_DIR, folder_name)
    if not os.path.exists(path):
        st.error(f"❌ Folder {folder_name} tidak ditemukan! Jalankan main script dulu.")
        st.stop()
    return spark.read.parquet(path).toPandas()

# Memuat data ke dalam format Pandas (agar bisa dibaca Plotly) [cite: 199, 201]
try:
    df_total = load_parquet_data("energy_total")
    df_time = load_parquet_data("energy_time")
    df_ml = load_parquet_data("ml_energy")
except Exception as e:
    st.error(f"Gagal memuat data: {e}")
    st.stop()

# Sidebar untuk memilih Sektor [cite: 207, 212]
st.sidebar.header("Filter Kawasan")
selected_sector = st.sidebar.selectbox("Pilih Sektor Analisis", df_total["sector"].unique())

# Menampilkan KPI (Key Performance Indicator) [cite: 225, 233]
st.subheader("Key Performance Indicators")
col1, col2 = st.columns(2)
with col1:
    total_val = df_total[df_total["sector"] == selected_sector]["total_usage"].values[0]
    st.metric(f"Total Konsumsi {selected_sector}", f"{total_val:,} kWh")
with col2:
    st.metric("Status Sistem", "Aktif/Normal")

# Grafik Tren 10 Menit menggunakan Plotly [cite: 237, 247]
st.markdown("---")
st.subheader("📈 Tren Konsumsi Energi (Interval 10 Menit)")
# Mengambil waktu mulai dari kolom window [cite: 245]
df_time["start_time"] = df_time["window"].apply(lambda x: x[0] if isinstance(x, (tuple, list)) else x.start)
fig = px.line(df_time, x="start_time", y="total_usage", color="sector", markers=True)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.subheader("🤖 AI Forecasting (Linear Regression)")

# Menyiapkan data untuk AI [cite: 253, 254]
X = df_ml[["hour"]]
y = df_ml["power_usage"]

# Melatih Model secara instan [cite: 257]
model = LinearRegression()
model.fit(X, y)

# Input jam melalui Slider [cite: 259]
hour_input = st.slider("Prediksi Konsumsi pada Jam Ke-", 0, 23, 12)
pred_value = model.predict([[hour_input]])

# Menampilkan Hasil Prediksi [cite: 261]
st.success(f"Prediksi konsumsi energi pada jam {hour_input}:00 adalah **{int(pred_value[0])} kWh**")