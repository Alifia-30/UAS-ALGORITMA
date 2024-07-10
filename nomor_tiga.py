class AntrianRestoran:
    def __init__(self):
        self.antrian = []

    def enqueue(self, pesanan):
        self.antrian.append(pesanan)
        print(f"Pesanan '{pesanan}' telah ditambahkan ke dalam antrian.")

    def dequeue(self):
        if len(self.antrian) == 0:
            print("Antrian kosong, tidak ada pesanan untuk dihapus.")
        else:
            pesanan = self.antrian.pop(0)
            print(f"Pesanan '{pesanan}' telah dihapus dari antrian.")

    def tampilkan_antrian(self):
        if len(self.antrian) == 0:
            print("Antrian kosong.")
        else:
            print("Antrian saat ini:")
            for idx, pesanan in enumerate(self.antrian):
                print(f"{idx + 1}. {pesanan}")

if __name__ == "__main__":
    antrian = AntrianRestoran()
    antrian.enqueue("Pesanan 1")
    antrian.enqueue("Pesanan 2")
    antrian.enqueue("Pesanan 3")
    antrian.tampilkan_antrian()
    antrian.dequeue()
    antrian.tampilkan_antrian()
    antrian.dequeue()
    antrian.dequeue()
    antrian.dequeue()

