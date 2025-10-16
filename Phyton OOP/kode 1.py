# Edcorner Learning Python OOPS

class Human:

    species = "Homo Sapiens" # ? ini adalah variabel class 

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


# membuat objek
x = Human("Edcorner", 32, "Male")
y = Human("Learning", 30, "Female")

# menampilkan hasil
print(x.name, x.age, x.gender)
print(y.name, y.age, y.gender)
print(x.species)
