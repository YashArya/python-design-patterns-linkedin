#!/usr/bin/env python3

'''
Use the following scenario for the coding challenge.
* Your pet shop only sold dogs before. Now you sell cats too. You might sell other pets in the future.
* Your system should show how each of the pets speak.
'''

class Dog():
    def __init__(self, name):
        self._name = name 

    def speak(self):
        return "Woof!"

class Cat():
    def __init__(self, name):
        self._name = name
    
    def speak(self):
        return "Meow!"

# Factory method
def get_pet(pet):
    
    # Factory has information regarding how to instantiate objects of different types.
    pets = dict(dog=Dog("Ruffy"), cat=Cat("Kitty"))
    
    return pets[pet]

if __name__ == "__main__":
    dog = get_pet("dog")
    print(dog.speak())

    cat = get_pet("cat")
    print(cat.speak())