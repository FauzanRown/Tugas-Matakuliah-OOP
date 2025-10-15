# Edcorner Learning Python OOPS

class Human:
    species = "Homo Sapiens"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


# x and y are instances of class Human
x = Human("Edcorner", 30, "male")
y = Human("Learning", 32, "female")

print(x.species)  # species are class attributes, same value for all instances
print(y.species)

print(f"Hi! My name is {x.name}. I am a {x.gender}, and I am {x.age} years old")
print(f"Hi! My name is {y.name}. I am a {y.gender}, and I am {y.age} years old")
