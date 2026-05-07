import os
import shutil
import random
from datetime import datetime, timedelta
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, window, sum as _sum, hour

# Mendapatkan Absolute Path agar folder output selalu ditemukan [cite: 62]
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

# Inisialisasi Spark Session [cite: 71, 74]
spark = SparkSession.builder \
    .appName("Energy_Processing_Engine") \
    .config("spark.sql.parquet.compression.codec", "snappy") \
    .getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

print("⚡ Spark Ready: Memulai Pemrosesan Data Energi...")

# Membersihkan folder output lama agar data bersih [cite: 88, 89]
if os.path.exists(OUTPUT_DIR):
    shutil.rmtree(OUTPUT_DIR)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Parameter data sesuai tugas praktikum
sectors = ["Industrial_A", "Industrial_B", "Residential_C"]
start_time = datetime(2026, 5, 7, 8, 0)
sensor_data = []

# Loop untuk membuat data 150 menit
for i in range(150):
    for sec in sectors:
        sensor_data.append((
            start_time + timedelta(minutes=i),
            sec,
            random.randint(100, 1000) # Konsumsi 100-1000 kWh
        ))

# Mengubah data menjadi DataFrame Spark [cite: 108]
df = spark.createDataFrame(sensor_data, ["timestamp", "sector", "power_usage"])

# 1. Total energi per sektor
df_total = df.groupBy("sector").agg(_sum("power_usage").alias("total_usage"))

# 2. Agregasi per 10 menit (Trend Waktu) [cite: 124, 125]
df_time = df.groupBy(window(col("timestamp"), "10 minutes"), "sector") \
            .agg(_sum("power_usage").alias("total_usage"))

# 3. Dataset untuk AI (berdasarkan jam) [cite: 128]
df_ml = df.withColumn("hour", hour(col("timestamp")))

# Menyimpan ke format Parquet [cite: 137, 142]
df_total.write.mode("overwrite").parquet(os.path.join(OUTPUT_DIR, "energy_total"))
df_time.write.mode("overwrite").parquet(os.path.join(OUTPUT_DIR, "energy_time"))
df_ml.write.mode("overwrite").parquet(os.path.join(OUTPUT_DIR, "ml_energy"))

print("✅ SEMUA DATA BERHASIL DISIMPAN KE FOLDER OUTPUT")
spark.stop() # Menutup session agar memori bersih [cite: 150]