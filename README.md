# 🍅 Sistem Deteksi Penyakit Tanaman Tomat Menggunakan YOLOv11

Sistem Deteksi Penyakit Tanaman Tomat merupakan aplikasi berbasis web yang dikembangkan untuk mendeteksi penyakit pada daun dan buah tomat secara **realtime** menggunakan model **YOLOv11**. Aplikasi ini memanfaatkan webcam sebagai media input, kemudian menampilkan hasil deteksi berupa nama penyakit, tingkat kepercayaan (Confidence), metrik evaluasi model, deskripsi gejala, serta menyimpan hasil deteksi beserta gambar ke dalam database **MySQL**.

---

# 📌 Informasi Project

| Keterangan | Informasi |
|------------|-----------|
| **Nama Project** | Sistem Deteksi Penyakit Tanaman Tomat Menggunakan YOLOv11 |
| **Bahasa Pemrograman** | Python |
| **Framework** | Flask |
| **Model AI** | YOLOv11 |
| **Database** | MySQL |
| **Web Server** | XAMPP |
| **Author** | Rofi Fitriyani |
| **Program Studi** | Informatika |
| **Universitas** | Universitas Majalengka |

---

# ✨ Fitur Aplikasi

- 📷 Deteksi penyakit tanaman tomat secara realtime menggunakan webcam
- 🤖 Menggunakan model YOLOv11
- 🍅 Mendeteksi 11 kelas penyakit dan kondisi tanaman tomat
- 📊 Menampilkan nilai Confidence
- 📈 Menampilkan metrik evaluasi model:
  - IoU
  - Precision
  - Recall
  - mAP50
  - mAP50-95
- 📖 Menampilkan deskripsi gejala penyakit
- 💾 Menyimpan hasil deteksi ke database MySQL
- 🖼️ Menyimpan gambar hasil deteksi
- 🌐 Antarmuka berbasis web menggunakan Flask

---

# 🗂 Struktur Folder

```
DATA SISTEM/
│
├── database/
│   ├── hasil_deteksi.sql
│   └── dummy.sql
│   └── schema.sql
│
├── docs/
│   └── Laporan Skripsi.pdf
│   └── Manual_Penggunaan.pdf
│
├── models/
│   └── best.pt
│   └── last.pt
│   └── Uji1.ipynb
│   └── Uji2.ipynb
│
├── results/
│   └── cek_target_90_persen_perkelas_test.csv
│   └── Uji 1.zip
│   └── Uji 2.zip
│
├── scripts/
│   ├── 1.selection_dataset.py
│   └── 2.preprocessing_dataset.py
│   └── 3.convert_jpeg_to_jpg.py
│   └── 4.balance_dataset_tomat.py
│   └── 5.split_dataset_yolo.py
│
├── src/
│   ├── static/
│   │   ├── style.css
│   │   ├── script.js
│   │   └── uploads/
│   │
│   ├── templates/
│   │   └── index.html
│   │
│   └── app.py
│
├── requirements.txt
└── README.md
```

---

# 💻 Teknologi yang Digunakan

- Python 3.10
- Flask
- Ultralytics YOLOv11
- OpenCV
- Pandas
- PyMySQL
- MySQL
- XAMPP
- HTML
- CSS
- JavaScript

---

# 📦 Library yang Digunakan

Library dapat diinstal menggunakan:

```bash
pip install -r requirements.txt
```

Beberapa library utama:

- ultralytics
- flask
- opencv-python
- pandas
- pymysql
- torch
- torchvision
- numpy

---

# ⚙ Cara Menjalankan Aplikasi

## 1. Clone atau Download Repository

```bash
git clone <repository-url>
```

atau ekstrak file project.

---

## 2. Masuk ke Folder Project

```bash
cd DATA SISTEM
```

---

## 3. Aktifkan Virtual Environment

Windows

```bash
venv\Scripts\activate
```

---

## 4. Install Semua Library

```bash
pip install -r requirements.txt
```

---

## 5. Jalankan XAMPP

Aktifkan service berikut:

- Apache
- MySQL

---

## 6. Import Database

Buka phpMyAdmin.

Import file:

```
database/schema.sql
```

Kemudian (opsional):

```
database/dummy.sql
```

---

## 7. Jalankan Program

```bash
python src/app.py
```

---

## 8. Buka Browser

```
http://127.0.0.1:5000
```

---

# 🗄 Database

Nama Database

```
deteksi_tomat_db
```

Nama Tabel

```
hasil_deteksi
```

Data yang disimpan meliputi:

- Gambar hasil deteksi
- Nama penyakit
- Confidence
- IoU
- Precision
- Recall
- mAP50
- mAP50-95
- Deskripsi gejala
- Waktu deteksi

---

# 🤖 Model AI

Model yang digunakan adalah:

```
YOLOv11
```

Lokasi model:

```
models/best.pt
```

---

# 🍅 Kelas Deteksi

Model mampu mendeteksi 11 kelas:

1. bacterial_spot_leaf
2. early_blight_leaf
3. healthy_leaf
4. late_blight_leaf
5. mosaic_virus
6. septoria_leaf_spot
7. bacterial_spot_fruit
8. blossom_end_rot
9. catface
10. healthy_fruit
11. serangan_hama

---

# 📊 Output Sistem

Sistem menghasilkan informasi berupa:

- Nama penyakit
- Confidence
- IoU
- Precision
- Recall
- mAP50
- mAP50-95
- Deskripsi gejala
- Gambar hasil deteksi
- Riwayat hasil deteksi yang tersimpan pada MySQL

---

# 📖 Dokumentasi

Dokumentasi penggunaan aplikasi terdapat pada folder:

```
docs/
```

---

# 👩‍💻 Pengembang

**Rofi Fitriyani**

Program Studi Informatika

Fakultas Teknik

Universitas Majalengka

---

# 📄 Lisensi

Project ini dikembangkan sebagai bagian dari penelitian dan penyusunan **Tugas Akhir (Skripsi)** pada Program Studi Informatika Universitas Majalengka.

Seluruh kode sumber dan dokumentasi digunakan untuk keperluan akademik.