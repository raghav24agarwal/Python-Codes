import copy

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print(f"I am {self.name} the {self.species}.")

# Create a prototype animal
prototype_animal = Animal("Fido", "Dog")

# Create a new animal by cloning the prototype
shallow_animal = copy.copy(prototype_animal)

# Set the name of the new animal
shallow_animal.name = "Spot"

# Speak to the new animal
prototype_animal.speak()
shallow_animal.speak()

deep_animal = copy.deepcopy(prototype_animal)

# deep_animal.name = "Rustom"

# shallow_animal.speak()
# deep_animal.speak()



