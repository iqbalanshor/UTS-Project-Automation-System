# 🚀 JOB VACANCY DATA COLLECTOR BERBASIS CLI

<p align="center">
  <b>Automation Systems – Ujian Tengah Semester (UTS)</b>
  <br>
  Aplikasi Pengumpulan Data Lowongan Pekerjaan Berbasis Command Line Interface (CLI)
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Project-UTS-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Category-Automation%20Systems-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Platform-CLI-black?style=for-the-badge" />
</p>

## 👥 Tim Pengembang

Proyek ini dikembangkan secara berkelompok oleh mahasiswa Program Studi Teknik Informatika Universitas Pelita Bangsa.

| No. | Nama Anggota | NIM |
|:---:|---|:---:|
| 01 | **Muhammad Iqbal Al Anshori** | 312310659 |
| 02 | **Raihan Nurfadillah** | 312310134 |
| 03 | **Rizkyawan Mu'adz Daffa** | 312310264 |

## 🎓 Informasi Akademik

| Keterangan | Detail |
|---|---|
| Perguruan Tinggi | Universitas Pelita Bangsa |
| Program Studi | Teknik Informatika |
| Mata Kuliah | Automation Systems |
| Jenis Proyek | Ujian Tengah Semester (UTS) |
| Tahun Akademik | 2025 / 2026 |

---

## 📌 1. Deskripsi Proyek

**Job Vacancy Data Collector Berbasis CLI** merupakan sebuah aplikasi otomatisasi yang dikembangkan menggunakan bahasa pemrograman Python untuk melakukan pengumpulan (scraping), ekstraksi, pembersihan, serta penyimpanan data lowongan pekerjaan dari halaman website secara otomatis.

Proyek ini dibuat untuk memenuhi tugas Ujian Tengah Semester (UTS) mata kuliah Automation Systems dengan menerapkan konsep otomatisasi yang dipelajari dari materi Automate the Boring Stuff with Python, khususnya Chapter 9 sampai Chapter 13.

Aplikasi ini dirancang untuk membantu proses pengumpulan informasi lowongan pekerjaan yang sebelumnya dilakukan secara manual menjadi lebih praktis, cepat, dan terstruktur.

Dengan memanfaatkan teknik Web Scraping, aplikasi dapat mengambil informasi lowongan pekerjaan dari website sumber, kemudian mengolah data tersebut menggunakan Regular Expressions (Regex) untuk menghasilkan informasi yang lebih bersih dan konsisten.

Selanjutnya, data yang telah diproses akan disimpan secara otomatis dalam format CSV dan TXT, serta dapat dikompres ke dalam format ZIP sebagai file backup.

Seluruh proses aplikasi dijalankan melalui Command Line Interface (CLI), sehingga pengguna dapat mengatur proses scraping menggunakan perintah dan parameter yang tersedia.

## ✨ 2. Fitur Utama

**🔍 Web Scraping:** Mengambil data lowongan pekerjaan secara otomatis dari website.

**🔎 Keyword Filtering:** Menyaring lowongan berdasarkan kata kunci pekerjaan.

**🧹 Data Cleaning:** Membersihkan dan memvalidasi data menggunakan Regex.

**📄 Export Data:** Menyimpan hasil scraping dalam format CSV dan TXT.

**📁 Automatic Folder:** Membuat folder penyimpanan secara otomatis.

**📦 ZIP Backup:** Mengamankan hasil scraping dalam format ZIP.

**⚠️ Error Handling:** Menangani kesalahan koneksi dan proses pengambilan data.

**💻 CLI Interface:** Menjalankan aplikasi melalui terminal dengan parameter yang tersedia.

## 🛠️ 3. Teknologi yang Digunakan

| Teknologi | Fungsi |
|---|---|
| Python 3 | Bahasa pemograman |
| Request | Mengambil halaman website |
| BeautifulSoup4 | Mengekstrak data HTML |
| Regex | Membersihkan dan memvalidasi data |
| CSV | Menyimpan hasil scriping |
| Pathlib | Mengelola folder dan file |
| Zipfile | Membuat backup ZIP |
| Argparse | Mengelola perintah CLI |

## 📊 4. Data yang Dikumpulkan

Data lowongan pekerjaan yang dikumpulkan meliputi:

1. Judul pekerjaan.
2. Nama perusahaan.
3. Lokasi pekerjaan.
4. Tanggal posting.
5. URL lowongan pekerjaan.

**Website Sumber:** https://realpython.github.io/fake-jobs/

## 📂 5. Struktur Folder

<img width="267" height="486" alt="Screenshot 2026-11-09 200943" src="https://github.com/user-attachments/assets/4b0fad09-f0e3-4ab6-b236-39eef400f1cc" />

## 📈 6. Hasil Implementasi
Berdasarkan pengujian, aplikasi berhasil:

1. Mengambil 30 data lowongan pekerjaan.
2. Mengekstrak informasi pekerjaan dari website.
3. Membersihkan lokasi dan memvalidasi tanggal menggunakan Regex.
4. Menyimpan hasil scraping ke dalam CSV dan TXT.
5. Membuat folder penyimpanan secara otomatis.
6. Membuat file backup dalam format ZIP.
---


<p align="center">
  <b>🎯 UNIVERSITAS PELITA BANGSA</b>
  <br>
  Program Studi Teknik Informatika
  <br>
  © 2025–2026
</p>
