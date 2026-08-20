# Analisis dan Implementasi Pelabelan Penyakit Tomat pada Citra Digital Daun dan Buah Menggunakan Algoritma YOLOv11

![Badge Status](https://img.shields.io/badge/Status-Selesai-success)
![Badge Tipe](https://img.shields.io/badge/Tipe-Tugas%20Akhir-blue)
![Badge Prodi](https://img.shields.io/badge/Prodi-Informatika%20UNMA-maroon)

**Diajukan untuk memenuhi persyaratan Akademik di Program Studi Informatika, Universitas Majalengka.**

---

## 👨‍🎓 Identitas Pengembang
* **Nama Lengkap:** Rofi Fitriyani
* **NIM:** 221410067
* **Dosen Pembimbing:** Tri Ferga Prasetyo, S.T., M.Kom. dan Tantri Wahyuni, S.T., M.T.

---

## 📖 Deskripsi Aplikasi
> Sistem Deteksi Penyakit Tanaman Tomat Menggunakan YOLOv11 merupakan aplikasi berbasis web yang digunakan untuk mendeteksi kondisi dan penyakit pada daun serta buah tanaman tomat secara realtime melalui webcam. Sistem menggunakan model YOLOv11 untuk mengidentifikasi 11 kelas kondisi tanaman, kemudian menampilkan nama hasil deteksi, nilai confidence, informasi gejala, dan metrik evaluasi model. Hasil deteksi juga dapat disimpan dalam bentuk gambar dan data ke database MySQL sebagai riwayat pemeriksaan.

**Fitur Utama:**
* ✅ [Sebutkan Fitur Unggulan 1]
* ✅ [Sebutkan Fitur Unggulan 2]
* ✅ [Sebutkan Fitur Unggulan 3]

---

## 🛠 Teknologi (Tech Stack)
Aplikasi ini dikembangkan menggunakan teknologi berikut:

| Kategori | Teknologi |
| :--- | :--- |
| **Bahasa Pemrograman** | Python 3.10 |
| **Framework** | Flask |
| **Database** | MySQL |
| **Tools Lain** | YOLOv11 |

---

## ⚙️ Persyaratan Sistem (Prerequisites)
Sebelum menjalankan source code ini, pastikan komputer Anda memiliki:
1.  Software Web Server (XAMPP / Laragon / Docker)
2.  Runtime Environment sesuai bahasa (PHP / Python / Node.js)
3.  Terminal / Command Prompt / Git Bash

---

## 🚀 Panduan Instalasi

### 1. Clone Repositori
```bash
git clone https://github.com/username-anda/nama-repo.git
cd nama-repo
```

### 2. Instalasi Dependensi
```bash
# Sesuaikan dengan bahasa pemrograman Anda
composer install   # Untuk PHP
pip install -r requirements.txt   # Untuk Python
```

### 3. Konfigurasi Database
1.  Duplikat file `.env.example` menjadi `.env`.
2.  Sesuaikan nama database, username, dan password di file `.env`.
3.  Import file database yang ada di folder `/database` atau jalankan migrasi.

### 4. Jalankan Aplikasi
```bash
php artisan serve  # Contoh Laravel
python app.py      # Contoh Python
```

---

## 📸 Tangkapan Layar
Simpan gambar screenshot aplikasi Anda di dalam folder `doc/`.

### 1. Halaman Utama
![Halaman Utama](doc/screenshot_1.png)

### 2. Fitur Pendukung
![Fitur Pendukung](doc/screenshot_2.png)

---

## 📜 Lisensi
Hak Cipta © 2026 - Program Studi Informatika, Universitas Majalengka.
Dibuat oleh Rofi Fitriyani.
