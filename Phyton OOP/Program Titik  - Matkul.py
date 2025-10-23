import math

class Titik:
    def __init__(self, x = 0 , y = 0):   # ✅ pakai double underscore
        self.x = x
        self.y = y

    def jarak(self, titik_lain):
        # ✅ gunakan **2 untuk pangkat dua
        return math.sqrt((self.x - titik_lain.x)**2 + (self.y - titik_lain.y)**2)

    def geser(self, dx, dy):
        self.x += dx
        self.y += dy

    def cermin_sumbuX(self):
        self.y = -self.y

    def cermin_sumbuY(self):
        self.x = -self.x

    def cermin_titikO(self):
        self.x = -self.x
        self.y = -self.y

    def skala(self, k):
        self.x *= k
        self.y *= k

    def __str__(self):   # ✅ pakai double underscore
        return f"({self.x}, {self.y})"

# Contoh penggunaan
A = Titik(3, 4)
B = Titik(0, 0)

print("Titik A:", A)
print("Jarak A ke B:", A.jarak(B))
A.geser(2, -1)
print("Setelah digeser:", A)
A.cermin_sumbuX()
print("Cermin sumbu X:", A)
A.skala(2)
print("Setelah diskalakan:", A)
