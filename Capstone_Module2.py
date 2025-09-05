from statistics import mean
import os

def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def welcome():
    clearScreen()
    print("|-------------------------------------------------------------------------|")
    print("|-------------Selamat Datang Di Rumah Sakit Dika Hospital-----------------|")
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
            print("Input Tidak Valid Dan Golongan Darah TIdak Exist")

# ----------------------------- FUNGSI LIHAT -----------------------------
def lihatSemua():
    if not pasien:
        print("Tidak ada data pasien.")
    else:
        print("\n-------------------------[Daftar Pasien]---------------------------- ")
        for id, data in pasien.items():
            print(f"ID: {id}, Nama: {data['nama']}, Umur: {data['umur']}, "f"Alamat: {data['alamat']}, Gender: {data['jenisKelamin']}, "f"Golongan Darah: {data['golonganDarah']}")

def cariPasien():
    idPasien = input("Masukkan ID Pasien: ")
    found = None
    for key in pasien.keys():
        if key.lower() == idPasien.lower():
            found = key
            break
    if found:
        data = pasien[found]
        print(f"Pasien Ditemukan -> {found} | {data}")
    else:
        print("Pasien Tidak Ditemukan")
    

# ----------------------------- FUNGSI TAMBAH -----------------------------
def tambahData():
    idPasien = input("Masukkan ID Pasien baru: ").upper()
    for key in pasien.keys():
        if key.lower() == idPasien.lower():
            print("ID sudah terdaftar")
            return
    
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
        print(f"Data pasien {nama} berhasil ditambahkan.")
    else:
        print("Penambahan data dibatalkan.")


# ----------------------------- FUNGSI HAPUS -----------------------------
def hapusData():
    idPasien = input("Masukkan ID Pasien yang ingin dihapus: ")
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
    idPasien = input("Masukkan ID Pasien yang ingin diupdate: ")
    if idPasien in pasien:
        print(f"Data lama: {pasien[idPasien]}")
        nama = input("Masukkan nama baru: ")
        try:
            umur = int(input("Masukkan umur baru: "))
        except ValueError:
            print("Umur harus angka!")
            return
        alamat = input("Masukkan alamat baru: ")
        jenisKelamin = input("Masukkan jenis kelamin baru: ")
        golonganDarah = input("Masukkan golongan darah baru: ")
        
        pasien[idPasien] = {
            "nama": nama,
            "umur": umur,
            "alamat": alamat,
            "jenisKelamin": jenisKelamin,
            "golonganDarah": golonganDarah
        }
        print("Data pasien berhasil diperbarui.")
    else:
        print("Pasien tidak ditemukan.")

# ----------------------------- FUNGSI RATA-RATA -----------------------------
def hitungRataRata():
    if not pasien:
        print("Data kosong, tidak bisa menghitung rata-rata.")
    else:
        avg = mean([data['umur'] for data in pasien.values()])
        print(f"Rata-rata umur pasien: {avg:.2f} tahun")

# ----------------------------- SUB MENU -----------------------------
def subMenuLihat():
    while True:
        print("\n-------------------------[Lihat Data Pasien]---------------------------- ")
        print("1. Lihat semua pasien")
        print("2. Cari pasien berdasarkan ID")
        print("3. Kembali ke menu utama")
        pilih = input("Pilih (1-3): ")
        clearScreen()
        if pilih == '1':
            lihatSemua()
            input("\nTekan Enter untuk kembali...")
        elif pilih == '2':
            cariPasien()
            input("\nTekan Enter untuk kembali...")
        elif pilih == '3':
            break
        else:
            print("Pilihan tidak valid.")

def subMenuTambah():
    while True:
        print("\n-------------------------[Tambah Data Pasien]---------------------------- ")
        print("1. Tambah pasien")
        print("2. Kembali ke menu utama")
        pilih = input("Pilih (1-2): ")
        clearScreen()
        if pilih == '1':
            tambahData()
        elif pilih == '2':
            break
        else:
            print("Pilihan tidak valid.")

def subMenuHapus():
    while True:
        print(print("\n-------------------------[Hapus Data Pasien]---------------------------- "))
        print("1. Hapus pasien berdasarkan ID")
        print("2. Kembali ke menu utama")
        pilih = input("Pilih (1-2): ")
        clearScreen()
        if pilih == '1':
            hapusData()
        elif pilih == '2':
            break
        else:
            print("Pilihan tidak valid.")

def subMenuUpdate():
    while True:
        print(print("\n-------------------------[Update Data Pasien]---------------------------- "))
        print("1. Update pasien berdasarkan ID")
        print("2. Kembali ke menu utama")
        pilih = input("Pilih (1-2): ")
        clearScreen()
        if pilih == '1':
            ubahData()
            input("\nTekan Enter untuk kembali...")
        elif pilih == '2':
            break
        else:
            print("Pilihan tidak valid.")

# ----------------------------- MENU UTAMA -----------------------------
def displayMenu():
    print("\n------------------------------[Menu Utama]--------------------------------")
    print("1. Lihat Data Pasien")
    print("2. Tambah Data Pasien")
    print("3. Hapus Data Pasien")
    print("4. Update Data Pasien")
    print("5. Hitung Rata-rata Umur Pasien")
    print("6. Keluar")
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
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    welcome()
    main()
