from statistics import mean
import os
import re

def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def welcome():
    clearScreen()
    print("|-------------------------------------------------------------------------|")
    print("|--------------------Selamat Datang Di Dika Hospital----------------------|")
    print("|-----------------------INI ADALAH TAMPILAN ADMIN-------------------------|")
    print("|-------------------------------------------------------------------------|")
    input("Tekan ENTER untuk melanjutkan...")
    clearScreen()

# Data awal pasien
# PRIMARY KEY = idPasien
pasien = {
    "P001": {"nama": "Andi", "umur": 25, "alamat": "Jakarta", "jenisKelamin": "Laki-laki", "golonganDarah": "O"},
    "P002": {"nama": "Budi", "umur": 30, "alamat": "Bandung", "jenisKelamin": "Laki-laki", "golonganDarah": "A"},
    "P003": {"nama": "Citra", "umur": 22, "alamat": "Surabaya", "jenisKelamin": "Perempuan", "golonganDarah": "B"},
}

# ----------------------------- FUNGSI EXTRA -----------------------------
def inputJenisKelamin():
    while True:
        jk = input("Masukan Jenis Kelamin Anda (L = Laki-Laki /P = Perempuan): ").upper()
        if jk == "L":
            return "Laki-Laki"
        elif jk == "P":
            return "Perempuan"
        else:
            print("Input Tidak Valid Silahkan Pilih L atau P")

def inputGolonganDarah():
    validGolongan = ["A", "B", "AB", "O"]
    while True:
        gd = input("Masukan golongan darah (A/B/AB/O): ").upper()
        if gd in validGolongan:
            return gd
        else:
            print("Golongan Darah TIdak Valid")

def inputTambahPasien():
    while True:
        idPasien = input("Masukkan ID Pasien (format PXXX, contoh: P001): ").upper()
        if not re.match(r"^P\d{3}$", idPasien):   #buat validasi format
            print("Format ID tidak valid! Gunakan format PXXX (contoh: P001, P123).")
            continue
        if idPasien in pasien:
            print("ID pasien sudah ada, gunakan ID lain.")
            continue
        break

# ----------------------------- FUNGSI LIHAT -----------------------------
def lihatSemua():
    if not pasien:
        print("Tidak ada data pasien.")
    else:
        print("\n-------------------------[Daftar Pasien]---------------------------- ")
        for id, data in pasien.items():
            print(f"ID: {id}, Nama: {data['nama']}, Umur: {data['umur']}, "f"Alamat: {data['alamat']}, Gender: {data['jenisKelamin']}, "f"Golongan Darah: {data['golonganDarah']}")

def cariPasien():
    idPasien = input("Masukan ID Pasien: ").upper()
    if idPasien in pasien:
        data = pasien[idPasien]
        print("\nPasien ditemukan:")
        print(f"- ID: {idPasien}")
        print(f"- Nama: {data['nama']}")
        print(f"- Umur: {data['umur']}")
        print(f"- Alamat: {data['alamat']}")
        print(f"- Gender: {data['jenisKelamin']}")
        print(f"- Golongan Darah: {data['golonganDarah']}")
    else:
        print("\nPasien dengan ID tersebut tidak ditemukan.")

def cariPasienNama():
    namaCari = input("Masukkan nama pasien yang dicari: ").lower()
    hasil = []
    for idPasien, data in pasien.items():
        if namaCari in data['nama'].lower():
            hasil.append((idPasien, data))
    if hasil:
        print("\nPasien ditemukan:")
        for idPasien, data in hasil:
            print(f"- ID: {idPasien}")
            print(f"- Nama: {data['nama']}")
            print(f"- Umur: {data['umur']}")
            print(f"- Alamat: {data['alamat']}")
            print(f"- Gender: {data['jenisKelamin']}")
            print(f"- Golongan Darah: {data['golonganDarah']}\n")
    else:
        print("\nPasien dengan nama tersebut tidak ditemukan.")


# ----------------------------- FUNGSI TAMBAH -----------------------------
def tambahData():
    idPasien = inputTambahPasien()
    nama = input("Masukkan nama pasien: ").capitalize()
    try:
        umur = int(input("Masukkan umur pasien: "))
    except ValueError:
        print("Umur harus berupa angka!")
        return
    alamat = input("Masukkan alamat pasien: ").capitalize()
    jenisKelamin = inputJenisKelamin()
    golonganDarah = inputGolonganDarah()
    
    # tampilkan preview data
    clearScreen()
    print("\n----------------------------- Preview Data -----------------------------")
    print(f"ID: {idPasien}")
    print(f"Nama: {nama}")
    print(f"Umur: {umur}")
    print(f"Alamat: {alamat}")
    print(f"Jenis Kelamin: {jenisKelamin}")
    print(f"Golongan Darah: {golonganDarah}")
    
    konfirmasi = input("Apakah data sudah benar? (y/n): ").lower()
    if konfirmasi == 'y':
        pasien[idPasien] = {
            "nama": nama,
            "umur": umur,
            "alamat": alamat,
            "jenisKelamin": jenisKelamin,
            "golonganDarah": golonganDarah
        }
        clearScreen()
        print(f"\n================ Data pasien {nama} berhasil ditambahkan =================")
        input("Tekan ENTER untuk kembali..")
    else:
        clearScreen()
        print("Penambahan data dibatalkan.")
        input("Tekan ENTER untuk kembali..")


# ----------------------------- FUNGSI HAPUS -----------------------------
def hapusData():
    idPasien = input("Masukkan ID Pasien yang ingin dihapus (Format: P00X): ").upper()
    if idPasien in pasien:
        konfirmasi = input(f"Apakah yakin ingin menghapus pasien {pasien[idPasien]['nama']}? (y/n): ").lower()
        if konfirmasi == 'y':
            del pasien[idPasien]
            print("Data pasien berhasil dihapus.")
        else:
            print("Dibatalkan.")
    else:
        print("Pasien tidak ditemukan.")

# ----------------------------- FUNGSI UPDATE -----------------------------
def ubahData():
    idPasien = input("Masukkan ID Pasien yang ingin diupdate (Format: P00X): ").upper()
    if idPasien in pasien:
        print(f"Data lama: {pasien[idPasien]}")
        nama = input("Masukkan nama baru: ").capitalize()
        try:
            umur = int(input("Masukkan umur baru: "))
        except ValueError:
            print("Umur harus angka!")
            return
        alamat = input("Masukkan alamat baru: ").capitalize()
        jenisKelamin = inputJenisKelamin()
        golonganDarah = inputGolonganDarah()
        
    # tampilkan preview data
    clearScreen()
    print("\n----------------------------- Preview Data -----------------------------")
    print(f"ID: {idPasien}")
    print(f"Nama: {nama}")
    print(f"Umur: {umur}")
    print(f"Alamat: {alamat}")
    print(f"Jenis Kelamin: {jenisKelamin}")
    print(f"Golongan Darah: {golonganDarah}")
    
    konfirmasi = input("Apakah data sudah benar dan ingin diupdate? (y/n): ").lower()
    if konfirmasi == 'y':
        pasien[idPasien] = {
            "nama": nama,
            "umur": umur,
            "alamat": alamat,
            "jenisKelamin": jenisKelamin,
            "golonganDarah": golonganDarah
        }
        clearScreen()
        print(f"\n============= Data pasien {nama} berhasil diperbarui ===============")
    else:
        clearScreen()
        print("Pembaruan data dibatalkan.")

# ----------------------------- FUNGSI RATA-RATA -----------------------------
def hitungRataRata():
    if not pasien:
        print("Data kosong, tidak bisa menghitung rata-rata.")
    else:
        avg = mean([data['umur'] for data in pasien.values()])
        clearScreen()
        print(f"Rata-rata umur pasien: {avg:.2f} tahun")

# ----------------------------- FUNGSI GRAFIK -----------------------------
def grafikGolonganDarah():
    clearScreen()
    if not pasien:
        print("Tidak ada data pasien.")
        return
    
    print("\nGrafik Jumlah Pasien Berdasarkan Golongan Darah")
    print("------------------------------------------------")
    golDarahCount = {}
    for data in pasien.values():
        gol = data['golonganDarah']
        golDarahCount[gol] = golDarahCount.get(gol, 0) + 1

    for gol, jumlah in golDarahCount.items():
        print(f"{gol}: {'#' * jumlah} ({jumlah})")


def grafikJenisKelamin():
    clearScreen()
    if not pasien:
        print("Tidak ada data pasien.")
        return
    
    print("\nGrafik Jumlah Pasien Berdasarkan Jenis Kelamin")
    print("------------------------------------------------")
    genderCount = {"L": 0, "P": 0}
    
    for data in pasien.values():
        gender = data['jenisKelamin'].lower()  
        if gender in ["l", "laki-laki", "laki"]:  
            genderCount["L"] += 1
        elif gender in ["p", "perempuan", "wanita"]:  
            genderCount["P"] += 1
    
    print(f"Laki-laki : {'#' * genderCount['L']} ({genderCount['L']})")
    print(f"Perempuan : {'#' * genderCount['P']} ({genderCount['P']})")



def grafikUmur():
    clearScreen()
    if not pasien:
        print("Tidak ada data pasien.")
        return
    
    print("\nGrafik Umur Pasien")
    print("------------------------------------------------")
    umurCount = {}
    for data in pasien.values():
        try:
            umur = int(data['umur'])
            umurCount[umur] = umurCount.get(umur, 0) + 1
        except:
            continue

    for umur, jumlah in sorted(umurCount.items()):
        print(f"Umur {umur}: {'#' * jumlah} ({jumlah})")

# ----------------------------- SUB MENU --------------------------------------
def subMenuLihat():
    while True:
        clearScreen()
        print("\n-------------------------[Lihat Data Pasien]---------------------------- ")
        print("1. Lihat semua pasien")
        print("2. Cari pasien berdasarkan ID")
        print("3. Cari pasien berdasarkan Nama")
        print("4. Kembali ke menu utama")
        pilih = input("Pilih (1-4): ")
        clearScreen()
        if pilih == '1':
            lihatSemua()
            input("\nTekan Enter untuk kembali...")
        elif pilih == '2':
            cariPasien()
            input("\nTekan Enter untuk kembali...")
        elif pilih == '3':
            cariPasienNama()
            input("\nTekan Enter untuk kembali...")
        elif pilih == '4':
            break
        else:
            print("Pilihan tidak valid.")

def subMenuTambah():
    while True:
        clearScreen()
        print("\n-------------------------[Tambah Data Pasien]---------------------------- ")
        print("1. Tambah pasien")
        print("2. Lihat semua pasien")
        print("3. Kembali ke menu utama")
        pilih = input("Pilih (1-3): ")
        clearScreen()
        if pilih == '1':
            tambahData()
        elif pilih == '2':
            lihatSemua()
            input("\nTekan Enter untuk kembali...")
            clearScreen()
        elif pilih == '3':
            break
        else:
            print("Pilihan tidak valid.")

def subMenuHapus():
    while True:
        clearScreen()
        print("\n-------------------------[Hapus Data Pasien]---------------------------- ")
        print("1. Hapus pasien berdasarkan ID")
        print("2. Lihat semua pasien")
        print("3. Kembali ke menu utama")
        pilih = input("Pilih (1-3): ")
        clearScreen()
        if pilih == '1':
            hapusData()
        elif pilih == '2':
            lihatSemua()
            input("\nTekan Enter untuk kembali...")
            clearScreen()
        elif pilih == '3':
            break
        else:
            print("Pilihan tidak valid.")

def subMenuUpdate():
    while True:
        clearScreen()
        print("\n-------------------------[Update Data Pasien]---------------------------- ")
        print("1. Update pasien berdasarkan ID")
        print("2. Lihat semua data")
        print("3. Kembali ke menu utama")
        pilih = input("Pilih (1-3): ")
        clearScreen()
        if pilih == '1':
            ubahData()
            input("\nTekan Enter untuk kembali...")
        elif pilih == '2':
            lihatSemua()
            input("\nTekan Enter untuk kembali...")
            clearScreen()
        elif pilih == '3':
            break
        else:
            print("Pilihan tidak valid.")

def subMenuStatistik():
    while True:
        print("\n-------------------------[Menu Statistik Pasien]---------------------------- ")
        print("1. Grafik Jumlah Pasien per Golongan Darah ")
        print("2. Grafik Jumlah Pasien per Jenis Kelamin ")
        print("3. Grafik Umur Pasien")
        print("4. Kembali ke Menu Utama")
        
        choice = input("Pilih menu (1-4): ")
        if choice == "1":
            grafikGolonganDarah()
        elif choice == "2":
            grafikJenisKelamin()
        elif choice == "3":
            grafikUmur()
        elif choice == "4":
            break
        else:
            print("Pilihan tidak valid.")



# ----------------------------- MENU UTAMA -----------------------------
def displayMenu():
    clearScreen()
    print("\n------------------------------[Menu Utama]--------------------------------")
    print("1. Lihat Data Pasien")
    print("2. Tambah Data Pasien")
    print("3. Hapus Data Pasien")
    print("4. Update Data Pasien")
    print("5. Hitung Rata-rata Umur Pasien")
    print("6. Statistik")
    print("7. Keluar")
    print("----------------------------------------------------------------------------")

def main():
    while True:
        displayMenu()
        choice = input("Pilih menu (1-6): ")
        clearScreen()
        if choice == '1':
            subMenuLihat()
        elif choice == '2':
            subMenuTambah()
        elif choice == '3':
            subMenuHapus()
        elif choice == '4':
            subMenuUpdate()
        elif choice == '5':
            hitungRataRata()
            input("\nTekan Enter untuk kembali...")
        elif choice == '6':
            subMenuStatistik()
        elif choice == '7':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    welcome()
    main()
