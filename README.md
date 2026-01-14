Nama          : Nita Yulia Rahmani - 2441072
Program Studi : Sistem Informasi
Mata Kuliah   : Machine Learning
Jenis Tugas   : Ujian Akhir Semester (UAS)


# House Price Prediction using Machine Learning 

## Deskripsi Proyek
Proyek ini merupakan tugas Ujian Akhir Semester (UAS) pada mata kuliah Machine Learning.  
Proyek ini bertujuan untuk membangun sebuah sistem prediksi harga rumah menggunakan metode Machine Learning berbasis regresi.

Model Machine Learning dilatih menggunakan dataset harga rumah, kemudian disimpan dan diintegrasikan ke dalam aplikasi berbasis FastAPI. Aplikasi ini memungkinkan pengguna untuk melakukan prediksi harga rumah melalui antarmuka web secara sederhana.

## Tujuan Proyek
Tujuan dari pengembangan proyek ini adalah:
- Menerapkan konsep Machine Learning pada permasalahan nyata
- Melakukan pelatihan model regresi untuk memprediksi harga rumah
- Mengimplementasikan model Machine Learning ke dalam aplikasi berbasis web
- Memahami alur kerja Machine Learning mulai dari pengolahan data hingga deployment sederhana

## Dataset
Dataset yang digunakan dalam proyek ini berasal dari House Sales in King County, USA, yang tersedia secara publik melalui platform Kaggle. Dataset ini mencakup data penjualan rumah di King County, Washington (USA) pada periode Mei 2014 hingga Mei 2015, dengan jumlah lebih dari 21.000 observasi serta berbagai fitur rumah yang relevan untuk keperluan prediksi harga.
Dataset ini memuat beragam atribut rumah, seperti luas bangunan, jumlah kamar, kondisi rumah, serta fitur-fitur lainnya yang digunakan sebagai variabel input dalam proses pelatihan dan pengembangan model machine learning.
Dataset yang digunakan dalam proyek ini merupakan dataset harga rumah yang disimpan dalam format **CSV** dan **Excel**, yaitu:
- `kc_house_data.csv`
- `kc_house_data.xlsx`

## Algoritma Yang Digunakan
Algoritma Machine Learning yang digunakan dalam proyek ini adalah **Regresi Linier (Linear Regression)**.
Regresi Linier digunakan karena algoritma ini cocok untuk memprediksi nilai numerik kontinu, seperti harga rumah.  
Algoritma ini bekerja dengan mempelajari hubungan linear antara variabel input (fitur rumah) dan variabel target (harga rumah).
Selain itu, Regresi Linier memiliki keunggulan dalam hal kemudahan implementasi, interpretasi hasil, serta efisiensi komputasi, sehingga sesuai untuk tujuan pembelajaran pada mata kuliah Machine Learning.

## Variabel Independen dan Dependen
Dalam proyek ini, data dibagi menjadi dua jenis variabel, yaitu:

- **Variabel Independen (X)**  
  Variabel input yang digunakan untuk memprediksi harga rumah, terdiri dari:
  - bedrooms
  - bathrooms
  - sqft_living (Square Feet)
  - floors

- **Variabel Dependen (Y)**  
  Variabel target yang diprediksi oleh model, yaitu:
  - price (harga rumah)


## Metode dan Teknologi
Proyek ini menggunakan teknologi dan metode sebagai berikut:
- Metode Machine Learning: Regresi
- Bahasa Pemrograman: Python
- Framework API: FastAPI
- Library Pendukung:
  - pandas
  - numpy
  - scikit-learn
  - fastapi
  - uvicorn

## Struktur Folder Proyek
uas-machine-learning-house-price/
├── train.py                # Script untuk melatih model Machine Learning
├── main.py                 # Aplikasi FastAPI untuk prediksi harga rumah
├── house_price_model.pkl   # File model hasil training
├── index.html              # Tampilan antarmuka web
├── kc_house_data.csv       # Dataset harga rumah (CSV)
├── kc_house_data.xlsx      # Dataset harga rumah (Excel)
├── requirements.txt        # Daftar library yang digunakan
└── README.md               # Dokumentasi proyek

## Cara menjalankan Program Windows
1️. Membuat Virtual Environment
  - python -m venv .venv
2. Mengaktifkan Virtual Environment
  - .venv\Scripts\activate
3. Menginstal Library
  - pip install -r requirements.txt
4. Melatih Model
  - python train.py
5. Menjalankan Aplikasi FastAPI
  - uvicorn main:app --reload

## Implementasi Sistem
Model Machine Learning yang telah dilatih disimpan dalam format .pkl dan digunakan kembali oleh aplikasi FastAPI.
Pengguna dapat memasukkan data rumah melalui antarmuka web untuk mendapatkan hasil prediksi harga rumah secara langsung.

## Kesimpulan 
Proyek ini berhasil menerapkan konsep Machine Learning dalam memprediksi harga rumah serta mengintegrasikannya ke dalam aplikasi berbasis web menggunakan FastAPI.
Melalui proyek ini, diharapkan mahasiswa dapat memahami alur lengkap pengembangan sistem Machine Learning dari pengolahan data hingga deployment sederhana.


