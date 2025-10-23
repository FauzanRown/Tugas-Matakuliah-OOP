from math import gcd

class Pecahan:
    def __init__(self, pembilang, penyebut):
        self.pembilang = pembilang
        self.penyebut = penyebut
        self.sederhanakan()

    # Menyederhanakan pecahan
    def sederhanakan(self):
        pembagi = gcd(self.pembilang, self.penyebut)
        if pembagi != 0:
            self.pembilang //= pembagi
            self.penyebut //= pembagi

    # Menampilkan pecahan
    def tampilkan(self, operasi=""):
        if operasi:
            print(f"Hasil {operasi:<6}: {self.pembilang}/{self.penyebut}")
        else:
            print(f"{self.pembilang}/{self.penyebut}")


class OperasiPecahan:
    def tambah(self, a, b):
        pembilang_baru = (a.pembilang * b.penyebut) + (b.pembilang * a.penyebut)
        penyebut_baru = a.penyebut * b.penyebut
        return Pecahan(pembilang_baru, penyebut_baru)

    def kurang(self, a, b):
        pembilang_baru = (a.pembilang * b.penyebut) - (b.pembilang * a.penyebut)
        penyebut_baru = a.penyebut * b.penyebut
        return Pecahan(pembilang_baru, penyebut_baru)

    def kali(self, a, b):
        pembilang_baru = a.pembilang * b.pembilang
        penyebut_baru = a.penyebut * b.penyebut
        return Pecahan(pembilang_baru, penyebut_baru)

    def bagi(self, a, b):
        pembilang_baru = a.pembilang * b.penyebut
        penyebut_baru = a.penyebut * b.pembilang
        return Pecahan(pembilang_baru, penyebut_baru)


# Program utama
if __name__ == "__main__":
    p1 = Pecahan(1, 2)
    p2 = Pecahan(3, 4)
    op = OperasiPecahan()

    print("=== Operasi Pecahan ===")
    print(f"P1 = {p1.pembilang}/{p1.penyebut}")
    print(f"P2 = {p2.pembilang}/{p2.penyebut}")
    print("\nHasil Operasi:")

    op.tambah(p1, p2).tampilkan("tambah")
    op.kurang(p1, p2).tampilkan("kurang")
    op.kali(p1, p2).tampilkan("kali")
    op.bagi(p1, p2).tampilkan("bagi")
