# Edcorner Learning Python OOPS

class Human:
    # class attribute
    species = "Homo Sapiens"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


x = Human("Edcorner", 32, "Male")
y = Human("Learning", 30, "Female")

print(x.name)
print(y.name)
