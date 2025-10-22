# Edcorner Learning Python OOPS

class Human:

    species = "Homo Sapiens" # ? ini adalah variabel class 

    def __init__(self, name, age, gender): # Untuk menginisiasi deklarasi atribut
        self.name = name
        self.age = age  #! self mengacu pada objek ini, | klo di java namnaya this 
        self.gender = gender


# membuat objek
x = Human("Edcorner", 32, "Male")
y = Human("Learning", 30, "Female")

# menampilkan hasil
print(x.name, x.age, x.gender)
print(y.name, y.age, y.gender)
print(x.species)
