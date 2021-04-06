#!/usr/bin/env python3
'''
# Scenario
    * Build a Pet Factory that consists of a Dog Factory and a Cat Factory.
    * Dog and Cat Factory produce Dog and Cat Food.
'''

class Dog():
    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"

class DogFactory():
    def get_pet(self):
        return Dog()
    
    def get_food(self):
        return "Dog Food!"

class Cat():
    def speak(self):
        return "Meow!"

    def __str__(self):
        return "Cat"

class CatFactory():
    def get_pet(self):
        return Cat()
    
    def get_food(self):
        return "Cat Food!"

class PetStore:
    def __init__(self, pet_factory=None):
        self._pet_factory = pet_factory
    
    def show_pet(self):
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print("Our pet is {}".format(pet))
        print("Our pet says {}".format(pet.speak()))
        print("Our pet eats {}".format(pet_food))

# Create a concrete factory
dog_factory = DogFactory()

# Create a pet store containing the Abstract Factory
shop = PetStore(dog_factory)

# Print the details of the pet
shop.show_pet()

cat_factory = CatFactory()
shop = PetStore(cat_factory)
shop.show_pet()
