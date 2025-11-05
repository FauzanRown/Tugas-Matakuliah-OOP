# Superclass
class Kendaraan:
    def __init__(self, nama):
        self.nama = nama

    def jalan(self):
        print(f"{self.nama} sedang berjalan.")

# Subclass dari Kendaraan
class Mobil(Kendaraan):
    def klakson(self):
        print(f"{self.nama} membunyikan klakson!")

# Subclass dari Mobil
class MobilListrik(Mobil):
    def isiDaya(self):
        print(f"{self.nama} sedang mengisi daya listrik...")

# === Contoh penggunaan ===
mobil_listrik = MobilListrik("Tesla")
mobil_listrik.jalan()       # diwarisi dari Kendaraan
mobil_listrik.klakson()     # diwarisi dari Mobil
mobil_listrik.isiDaya()     # milik sendiri

# === Coba dari superclass ===
kendaraan = Kendaraan("Kendaraan Umum")
kendaraan.jalan()
# kendaraan.isiDaya()  # ❌ ERROR: Kendaraan tidak memiliki metode isiDaya()
