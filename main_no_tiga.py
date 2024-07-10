from nomor_tiga import AntrianRestoran

def main():
    antrian = AntrianRestoran()

    while True:
        print("\nMenu:")
        print("1. Tambahkan Pesanan (Enqueue)")
        print("2. Hapus Pesanan (Dequeue)")
        print("3. Tampilkan Antrian")
        print("4. Keluar")

        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == '1':
            pesanan = input("Masukkan nama pesanan: ")
            antrian.enqueue(pesanan)
        elif pilihan == '2':
            antrian.dequeue()
        elif pilihan == '3':
            antrian.tampilkan_antrian()
        elif pilihan == '4':
            print("Terima kasih telah menggunakan sistem antrian restoran.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
