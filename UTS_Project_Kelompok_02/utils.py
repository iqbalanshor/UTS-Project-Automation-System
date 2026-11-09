import csv
import zipfile
from pathlib import Path

def buat_folder(nama_folder):
    Path(nama_folder).mkdir(parents=True, exist_ok=True)

def simpan_csv(data, path_file, fieldnames):
    with open(path_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def buat_laporan(data, path_file):
    with open(path_file, "w", encoding="utf-8") as f:
        f.write(f"=== LAPORAN HASIL SCRAPING ===\n")
        f.write(f"Total record ditemukan: {len(data)}\n\n")
        for item in data:
            f.write(str(item) + "\n")

def buat_backup_zip(folder_output, path_zip):
    with zipfile.ZipFile(path_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        for file in Path(folder_output).rglob("*"):
            if file.is_file():
                zf.write(file, file.relative_to(folder_output))