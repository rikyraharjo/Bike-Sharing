"""
Author: riky raharjo
Date: 03/03/2024
Usage:
- This module is used to create a dashboard for the bike sharing data.
"""

# Import semua packages/library yang digunakan
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
file_path = "./data/CleareData.csv"
data_cleaned = pd.read_csv(file_path)

# Judul dashboard
st.title('Dashboard Analisis Data: Bike Sharing Dataset')

# Header untuk Pertanyaan 1
st.header('Pertanyaan 1: Berapa rata-rata penyewa sepeda tiap bulannya pada tahun 2012?')

# Filter data untuk tahun 2012
data_2012 = data_cleaned[data_cleaned['year'] == 2012]

# Menghitung rata-rata total_count per bulan untuk tahun 2012
monthly_average_2012 = data_2012.groupby('month')['total_count'].mean()

# Plot rata-rata penyewa sepeda tiap bulannya pada tahun 2012
st.line_chart(monthly_average_2012)

# Menampilkan penjelasan
st.write("""
Berdasarkan grafik di atas, terlihat bahwa rata-rata jumlah penyewa sepeda tiap bulannya pada tahun 2012 
berfluktuasi. Terjadi peningkatan yang signifikan pada bulan Agustus dan September, kemudian terjadi penurunan 
yang cukup tajam pada bulan Oktober hingga Desember.
""")

# Header untuk Pertanyaan 2
st.header('Pertanyaan 2: Dibulan apa penyewaan sepeda terbanyak dan terendah tahun 2012?')

# Mengelompokkan data berdasarkan bulan dan menghitung total_count
month_counts = data_2012.groupby('month').agg({'total_count':'sum'}).reset_index()

# Menentukan bulan dengan total_count terbesar dan terkecil
bulan_terbanyak = month_counts.loc[month_counts['total_count'].idxmax()]['month']
bulan_terendah = month_counts.loc[month_counts['total_count'].idxmin()]['month']

# Plot total penyewaan sepeda per bulan dalam tahun 2012
fig, ax = plt.subplots()
ax.bar(month_counts['month'], month_counts['total_count'], color='skyblue')
ax.set_title('Total Penyewaan Sepeda per Bulan (Tahun 2012)')
ax.set_xlabel('Bulan')
ax.set_ylabel('Total Penyewaan Sepeda')
ax.grid(True)
st.pyplot(fig)

# Menampilkan penjelasan
st.write(f"Penyewaan sepeda terbanyak terjadi di bulan {bulan_terbanyak}, sedangkan penyewaan sepeda terendah terjadi di bulan {bulan_terendah}.")

# Export data yang sudah bersih ke csv (opsional)
# data_cleaned.to_csv('CleareData.csv', index=False)

st.caption('Copyright (c) riky-raharjo 2024')
