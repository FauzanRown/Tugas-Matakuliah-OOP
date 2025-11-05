class NovelDetektif:
    def __init__(self, judul, pengarang, tahun_terbit, harga_beli):
        # atribut privat (enkapsulasi)
        self.__judul = judul
        self.__pengarang = pengarang
        self.__tahun_terbit = tahun_terbit
        self.__harga_beli = harga_beli

    # getter dan setter
    def get_judul(self):
        return self.__judul

    def set_judul(self, judul):
        self.__judul = judul

    def get_pengarang(self):
        return self.__pengarang

    def set_pengarang(self, pengarang):
        self.__pengarang = pengarang

    def get_tahun_terbit(self):
        return self.__tahun_terbit

    def set_tahun_terbit(self, tahun_terbit):
        self.__tahun_terbit = tahun_terbit

    def get_harga_beli(self):
        return self.__harga_beli

    def set_harga_beli(self, harga_beli):
        self.__harga_beli = harga_beli

    # method untuk menghitung harga jual
    def hitung_harga_jual(self):
        return self.__harga_beli - (0.2 * self.__harga_beli)

    # method untuk menampilkan informasi
    def tampilkan_info(self):
        print(f"Judul       : {self.__judul}")
        print(f"Pengarang   : {self.__pengarang}")
        print(f"Tahun Terbit: {self.__tahun_terbit}")
        print(f"Harga Beli  : Rp{self.__harga_beli:,.0f}")
        print(f"Harga Jual  : Rp{self.hitung_harga_jual():,.0f}")
        print("-" * 40)


# Membuat 3 objek
novel1 = NovelDetektif("Pembunuhan di Orient Express", "Agatha Christie", 1934, 120000)
novel2 = NovelDetektif("Sherlock Holmes: A Study in Scarlet", "Arthur Conan Doyle", 1887, 95000)
novel3 = NovelDetektif("Detective Conan Vol.1", "Gosho Aoyama", 1994, 70000)

# Menampilkan informasi setiap novel
novel1.tampilkan_info()
novel2.tampilkan_info()
novel3.tampilkan_info()

# Menghitung total harga beli dan harga jual semua novel
total_beli = novel1.get_harga_beli() + novel2.get_harga_beli() + novel3.get_harga_beli()
total_jual = novel1.hitung_harga_jual() + novel2.hitung_harga_jual() + novel3.hitung_harga_jual()

print(f"Total Harga Beli Semua Buku: Rp{total_beli:,.0f}")
print(f"Total Harga Jual Semua Buku: Rp{total_jual:,.0f}")
