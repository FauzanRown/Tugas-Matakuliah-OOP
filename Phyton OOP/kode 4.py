# Edcorner Learning Python OOPS

class Human:
    # class attribute
    species = "Homo Sapiens"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

# ubah nilai class attribute
Human.species = "Sapiens"

# membuat objek dari class Human
obj = Human("Edcorner", 32, "male")

# menampilkan nilai species dari objek
print(obj.species)
