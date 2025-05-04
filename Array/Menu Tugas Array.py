class Mahasiswa:
    def __init__(self, nama, nim, nilai):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai

def input_data_mahasiswa():
    nama = input("Masukkan nama mahasiswa: ")
    nim = input("Masukkan NIM mahasiswa: ")
    nilai = float(input("Masukkan nilai mahasiswa: "))
    return Mahasiswa(nama, nim, nilai)

def tampilkan_data_mahasiswa(mahasiswa_list):
    print("\nData Mahasiswa:")
    for mahasiswa in mahasiswa_list:
        print(f"Nama: {mahasiswa.nama}, NIM: {mahasiswa.nim}, Nilai: {mahasiswa.nilai}")

def hitung_rata_rata_nilai(mahasiswa_list):
    total_nilai = sum(mahasiswa.nilai for mahasiswa in mahasiswa_list)
    rata_rata = total_nilai / len(mahasiswa_list)
    print(f"\nRata-rata nilai mahasiswa: {rata_rata:.2f}")

def cari_nilai_tertinggi_terendah(mahasiswa_list):
    nilai_tertinggi = max(mahasiswa_list, key=lambda x: x.nilai)
    nilai_terendah = min(mahasiswa_list, key=lambda x: x.nilai)
    print("\nMahasiswa dengan nilai tertinggi:")
    print(f"Nama: {nilai_tertinggi.nama}, NIM: {nilai_tertinggi.nim}, Nilai: {nilai_tertinggi.nilai}")
    print("\nMahasiswa dengan nilai terendah:")
    print(f"Nama: {nilai_terendah.nama}, NIM: {nilai_terendah.nim}, Nilai: {nilai_terendah.nilai}")

def tugas1():
    mahasiswa_list = []

    # Input data mahasiswa
    jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))
    for _ in range(jumlah_mahasiswa):
        mahasiswa_list.append(input_data_mahasiswa())

    # Tampilkan data mahasiswa
    tampilkan_data_mahasiswa(mahasiswa_list)

    # Hitung rata-rata nilai mahasiswa
    hitung_rata_rata_nilai(mahasiswa_list)

    # Cari nilai tertinggi dan terendah
    cari_nilai_tertinggi_terendah(mahasiswa_list)

    print("Program Data Mahasiswa selesai.")
    input("Tekan Enter untuk kembali ke menu utama.")

class Barang:
    def __init__(self, nama, kode, jumlah):
        self.nama = nama
        self.kode = kode
        self.jumlah = jumlah

def input_data_barang():
    nama = input("Masukkan nama barang: ")
    kode = input("Masukkan kode barang: ")
    jumlah = int(input("Masukkan jumlah barang: "))
    return Barang(nama, kode, jumlah) 

def tampilkan_semua_barang(barang_list):
    print("\nDaftar Barang:")
    for barang in barang_list:
        print(f"Nama: {barang.nama}, Kode: {barang.kode}, Jumlah: {barang.jumlah}")

def cari_barang_berdasarkan_kode(barang_list, kode):
    for barang in barang_list:
        if barang.kode == kode:
            print("\nBarang ditemukan:")
            print(f"Nama: {barang.nama}, Kode: {barang.kode}, Jumlah: {barang.jumlah}")
            return barang
    print("\nBarang tidak ditemukan.")
    return None

def hapus_barang_berdasarkan_kode(barang_list, kode):
    for i, barang in enumerate(barang_list):
        if barang.kode == kode:
            del barang_list[i]
            print("\nBarang berhasil dihapus.")
            return
    print("\nBarang tidak ditemukan.")

def tugas2():
    barang_list = []

    while True:
        print("\nMenu:")
        print("1. Tambah Barang")
        print("2. Tampilkan Semua Barang")
        print("3. Cari Barang berdasarkan Kode")
        print("4. Hapus Barang berdasarkan Kode")
        print("5. Kembali ke menu utama")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            barang_list.append(input_data_barang())
        elif pilihan == "2":
            tampilkan_semua_barang(barang_list)
        elif pilihan == "3":
            kode_cari = input("Masukkan kode barang yang ingin dicari: ")
            cari_barang_berdasarkan_kode(barang_list, kode_cari)
        elif pilihan == "4":
            kode_hapus = input("Masukkan kode barang yang ingin dihapus: ")
            hapus_barang_berdasarkan_kode(barang_list, kode_hapus)
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

    print("Program Inventaris Barang selesai.")
    input("Tekan Enter untuk kembali ke menu utama.")

class Transaksi:
    def __init__(self, jenis, jumlah):
        self.jenis = jenis
        self.jumlah = jumlah

def input_transaksi():
    jenis = input("Masukkan jenis transaksi (pemasukan/pengeluaran): ").lower()
    if jenis not in ['pemasukan', 'pengeluaran']:
        print("Jenis transaksi tidak valid.")
        return None
    jumlah = float(input("Masukkan jumlah transaksi: "))
    return Transaksi(jenis, jumlah)

def tampilkan_semua_transaksi(transaksi_list):
    print("\nDaftar Transaksi:")
    for idx, transaksi in enumerate(transaksi_list, start=1):
        print(f"{idx}. Jenis: {transaksi.jenis}, Jumlah: {transaksi.jumlah}")

def hitung_total_pemasukan(transaksi_list):
    total_pemasukan = sum(transaksi.jumlah for transaksi in transaksi_list if transaksi.jenis == 'pemasukan')
    print(f"\nTotal pemasukan: {total_pemasukan:.2f}")

def hitung_total_pengeluaran(transaksi_list):
    total_pengeluaran = sum(transaksi.jumlah for transaksi in transaksi_list if transaksi.jenis == 'pengeluaran')
    print(f"\nTotal pengeluaran: {total_pengeluaran:.2f}")

def hitung_saldo_akhir(transaksi_list):
    total_pemasukan = sum(transaksi.jumlah for transaksi in transaksi_list if transaksi.jenis == 'pemasukan')
    total_pengeluaran = sum(transaksi.jumlah for transaksi in transaksi_list if transaksi.jenis == 'pengeluaran')
    saldo_akhir = total_pemasukan - total_pengeluaran
    print(f"\nSaldo akhir: {saldo_akhir:.2f}")

def tugas3():
    transaksi_list = []

    while True:
        print("\nMenu:")
        print("1. Tambah Transaksi")
        print("2. Tampilkan Semua Transaksi")
        print("3. Hitung Total Pemasukan")
        print("4. Hitung Total Pengeluaran")
        print("5. Hitung Saldo Akhir")
        print("6. Kembali ke menu utama")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            transaksi = input_transaksi()
            if transaksi:
                transaksi_list.append(transaksi)
        elif pilihan == "2":
            tampilkan_semua_transaksi(transaksi_list)
        elif pilihan == "3":
            hitung_total_pemasukan(transaksi_list)
        elif pilihan == "4":
            hitung_total_pengeluaran(transaksi_list)
        elif pilihan == "5":
            hitung_saldo_akhir(transaksi_list)
        elif pilihan == "6":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

    print("Program Pengelolaan Barang Pribadi selesai.")
    input("Tekan Enter untuk kembali ke menu utama.")

def main():
    while True:
        print("\nMenu Utama:")
        print("1. Program Data Mahasiswa")
        print("2. Program Inventaris Barang")
        print("3. Program Pengelolaan Barang Pribadi")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tugas1()
        elif pilihan == "2":
            tugas2()
        elif pilihan == "3":
            tugas3()
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()