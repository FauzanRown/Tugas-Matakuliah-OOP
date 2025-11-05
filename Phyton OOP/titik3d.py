class Titik:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Titik(x={self.x}, y={self.y})"


class Titik3D(Titik):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)  # panggil constructor Titik
        self.z = z

    # Geser titik (translasi)
    def geser(self, dx, dy, dz):
        self.x += dx
        self.y += dy
        self.z += dz

    # Cermin terhadap sumbu x
    def cermin_x(self):
        self.x = -self.x

    # Cermin terhadap sumbu y
    def cermin_y(self):
        self.y = -self.y

    # Cermin terhadap sumbu z
    def cermin_z(self):
        self.z = -self.z

    # Skala (perkalian koordinat)
    def skala(self, kx, ky, kz):
        self.x *= kx
        self.y *= ky
        self.z *= kz

    def __repr__(self):
        return f"Titik3D(x={self.x}, y={self.y}, z={self.z})"


# === Contoh penggunaan ===
t = Titik3D(2, 3, 4)
print("Awal:", t)

t.geser(1, -2, 3)
print("Setelah geser:", t)

t.cermin_x()
print("Setelah cermin X:", t)

t.cermin_y()
print("Setelah cermin Y:", t)

t.cermin_z()
print("Setelah cermin Z:", t)

t.skala(2, 0.5, 3)
print("Setelah skala:", t)
