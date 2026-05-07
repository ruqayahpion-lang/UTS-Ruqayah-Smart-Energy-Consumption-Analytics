# ⚡ Smart Energy Consumption Analytics (Big Data Pipeline)
**Proyek UTS Praktikum Big Data Technology - IT UIN Antasari**

Repositori ini berisi sistem monitoring dan prediksi konsumsi energi yang mengintegrasikan pengolahan data besar dengan Apache Spark dan visualisasi interaktif menggunakan Streamlit. Sistem ini mensimulasikan monitoring pada sektor Industrial dan Residential untuk mendeteksi lonjakan beban energi.

## 🚀 Fitur Utama
- [cite_start]**Data Engine (PySpark):** Melakukan agregasi data 150 menit secara batch dengan efisiensi memori tinggi[cite: 42, 100].
- [cite_start]**Columnar Storage (Parquet):** Menggunakan format Parquet untuk penyimpanan data hasil olahan guna memastikan pembacaan data yang sangat cepat oleh layer visualisasi[cite: 43, 134].
- [cite_start]**AI Forecasting:** Prediksi konsumsi energi di masa depan menggunakan algoritma *Linear Regression*[cite: 44, 251].
- [cite_start]**Interactive Dashboard:** Visualisasi tren *time-series* secara real-time menggunakan Plotly[cite: 246, 247].

## 🏗️ Arsitektur Pipeline
Sistem mengikuti alur kerja standar industri:
[cite_start]`Data Generation` → `Spark Transformation` → `Parquet Storage` → `ML Modeling` → `Serving (Streamlit)`[cite: 36].

## 🛠️ Persiapan Lingkungan (Setup)
[cite_start]Pastikan Anda menjalankan proyek ini di lingkungan **Linux/WSL** dan menggunakan **VS Code**[cite: 13, 14].

1. **Instal Library yang Diperlukan:**
   ```bash
   pip install pyspark streamlit plotly scikit-learn pandas
Pengaturan Path:
Proyek ini menggunakan Absolute Path untuk menjamin stabilitas aplikasi saat dijalankan di lingkungan server. 

📖 Cara Menjalankan
Proyek dibagi menjadi dua tahap utama sesuai instruksi praktikum:  
1. Jalankan Engine (ETL & Processing)
Eksekusi script ini untuk memproses data mentah menjadi format Parquet di folder output/.
Bash
python3 main_energy_230104040208.py
Tunggu hingga muncul pesan: "✅ SEMUA DATA BERHASIL DISIMPAN KE FOLDER OUTPUT".
<img width="1401" height="275" alt="Cuplikan layar 2026-05-07 095333" src="https://github.com/user-attachments/assets/bf526fef-84eb-411e-8ce2-e7c82bd8e8ed" />
2. Jalankan Dashboard (Visualization & AI)
Jalankan perintah berikut untuk membuka dashboard interaktif di browser Anda.
Bash
python3 -m streamlit run dashboard_energy_230104040208.py
<img width="1467" height="660" alt="Cuplikan layar 2026-05-07 095344" src="https://github.com/user-attachments/assets/99291207-8181-47aa-9f8b-93f244ea8add" />

📊 Analisis Hasil (Case Study: Residential_C)
Berdasarkan data simulasi:
<img width="1920" height="1080" alt="Cuplikan layar 2026-05-07 094754" src="https://github.com/user-attachments/assets/03b813c5-2234-4a30-8889-6950526cd6ab" />
<img width="1834" height="381" alt="Cuplikan layar 2026-05-07 094807" src="https://github.com/user-attachments/assets/eb33dbd9-2ad5-4d9d-8479-721a08f499d1" />
<img width="1920" height="1080" alt="Cuplikan layar 2026-05-07 094754" src="https://github.com/user-attachments/assets/1a2e227e-167b-4ae4-8212-f22a7f6dc8d6" />

Total Konsumsi: Sektor Residential_C mencatat akumulasi beban sebesar 81,296 kWh.
Prediksi AI: Model memprediksi konsumsi pada jam ke-12:00 sebesar 518 kWh.
Tren: Terjadi fluktuasi dinamis pada interval 10 menit yang mencerminkan pola penggunaan energi di kawasan tersebut.

Author: Ruqayah 
Mata Kuliah: Big Data Technology
Dosen Pengampu: Muhayat, M.IT
