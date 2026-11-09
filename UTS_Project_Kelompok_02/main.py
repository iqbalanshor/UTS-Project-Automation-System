import argparse
import sys
from pathlib import Path
import requests
from scraper import scrape_lowongan
from utils import buat_folder, simpan_csv, buat_laporan, buat_backup_zip

def main():
    parser = argparse.ArgumentParser(description="Aplikasi Scraping Lowongan Kerja (UTS Automation Systems)")
    parser.add_argument("--url", required=True, help="URL sumber data (contoh: https://realpython.github.io/fake-jobs/)")
    parser.add_argument("--keyword", default="", help="Kata kunci untuk memfilter judul lowongan")
    parser.add_argument("--limit", type=int, default=30, help="Jumlah maksimal data yang diambil")
    parser.add_argument("--output", default="output", help="Nama folder untuk menyimpan hasil")
    parser.add_argument("--backup", action="store_true", help="Tambahkan flag ini untuk membuat file ZIP backup")
    
    args = parser.parse_args()

    print("\n" + "="*50)
    print(" 💼 APLIKASI SCRAPING LOWONGAN KERJA - KELOMPOK 2")
    print("="*50)

    print("[*] Menyiapkan folder...")
    buat_folder("data")
    buat_folder(args.output)
    buat_folder("backup")

    url_bersih = args.url.rstrip('/')

    print(f"[*] Memulai proses scraping (Limit: {args.limit}, Keyword: '{args.keyword}')...")
    try:
        data_hasil = scrape_lowongan(url_bersih, keyword=args.keyword, limit=args.limit)
    except Exception as e:
        print(f"\n[❌] ERROR tidak terduga: {e}")
        sys.exit(1)

    if not data_hasil:
        print("\n" + "!"*50)
        print(" ⚠️ PERINGATAN: DATA KOSONG")
        print(" Tidak ada lowongan yang cocok dengan kriteria.")
        print("!"*50 + "\n")
        sys.exit(1)

    print(f"[*] Menyimpan {len(data_hasil)} data...")
    path_csv = Path(args.output) / "hasil_scraping.csv"
    path_txt = Path(args.output) / "laporan.txt"
    
    fieldnames = ["judul_pekerjaan", "perusahaan", "lokasi", "tanggal_posting", "url"]
    simpan_csv(data_hasil, path_csv, fieldnames)
    buat_laporan(data_hasil, path_txt)
    
    with open("data/raw_data.txt", "w", encoding="utf-8") as f:
        for item in data_hasil:
            f.write(str(item) + "\n")

    if args.backup:
        print("[*] Membuat backup ZIP...")
        path_zip = Path("backup") / "backup_data.zip"
        buat_backup_zip(args.output, path_zip)
        print(f"    -> Tersimpan di: {path_zip}")

    print("\n" + "="*50)
    print(" ✅ RINGKASAN PEMROSESAN")
    print("="*50)
    print(f" 📊 Total Data   : {len(data_hasil)} lowongan")
    print(f" 📁 File CSV     : {path_csv}")
    print(f" 📄 File Laporan : {path_txt}")
    if args.backup:
        print(f" 📦 File Backup  : backup/backup_data.zip")
    print("="*50)
    print(" 🎉 PROSES SELESAI DENGAN SUKSES!\n")

if __name__ == "__main__":
    main()