import re
import requests
from bs4 import BeautifulSoup

def ekstrak_lokasi(teks_lokasi):
    # REGEX 1: Mengambil format "Kota, Negara Bagian" (contoh: "Stewartbury, AA")
    pola = r"([A-Za-z\s]+),\s*([A-Z]{2})"
    hasil = re.search(pola, teks_lokasi)
    if hasil:
        return hasil.group(0).strip()
    return teks_lokasi.strip()

def validasi_tanggal(teks_tanggal):
    # REGEX 2: Memastikan format tanggal YYYY-MM-DD
    pola = r"^\d{4}-\d{2}-\d{2}$"
    if re.fullmatch(pola, teks_tanggal.strip()):
        return teks_tanggal.strip()
    return "Tanggal tidak valid"

def scrape_lowongan(url_dasar, keyword="", limit=30):
    hasil_data = []
    print(f"Mulai scraping lowongan dari: {url_dasar}")
    
    try:
        response = requests.get(url_dasar, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"[!] Gagal koneksi: {e}")
        return hasil_data
        
    soup = BeautifulSoup(response.text, "html.parser")
    semua_kartu = soup.select("div.card-content")
    
    for kartu in semua_kartu:
        judul = kartu.select_one("h2.title").text.strip()
        
        # Filter keyword
        if keyword and keyword.lower() not in judul.lower():
            continue
            
        perusahaan = kartu.select_one("h3.company").text.strip()
        lokasi_mentah = kartu.select_one("p.location").text
        lokasi_bersih = ekstrak_lokasi(lokasi_mentah)
        
        tanggal_mentah = kartu.select_one("time")["datetime"]
        tanggal_valid = validasi_tanggal(tanggal_mentah)
        
        # Ambil link apply (link terakhir di dalam kartu)
        link = kartu.find_all("a")[-1]["href"]
        
        data_lowongan = {
            "judul_pekerjaan": judul,
            "perusahaan": perusahaan,
            "lokasi": lokasi_bersih,
            "tanggal_posting": tanggal_valid,
            "url": link
        }
        hasil_data.append(data_lowongan)
        
        if len(hasil_data) >= limit:
            break
            
    return hasil_data