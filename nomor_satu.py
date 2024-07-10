def main():
    mahasiswa_list = []

    while True:
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        mahasiswa_list.append({"nim": nim, "nama": nama})

        tambah_lagi = input("Ingin tambah lagi? (ya/tidak): ").strip().lower()
        if tambah_lagi != 'ya':
            break

    print("\nData Mahasiswa:")
    for mahasiswa in mahasiswa_list:
        print(f"NIM: {mahasiswa['nim']}, Nama: {mahasiswa['nama']}")

if __name__ == "__main__":
    main()

