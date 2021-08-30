#Class Dog - Sample

class Dog:
    # Class attributes
    species = 'Canis familiaris'
    numbersPaws = 4

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def printName(self):
        print(self.name)
    

    # Other Instane method

    def speak(self, sound):
        return f"{self.name} says {sound}"



    







