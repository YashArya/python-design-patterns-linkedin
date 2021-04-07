#!/usr/bin/env python3

'''
Goal: Create a prototype car object and clone other car objects using that prototype.
'''

import copy

# Stores a dict of prototypes
class Prototype():
    def __init__(self):
        self._objects = dict()

    def register_object(self, name, obj):
        self._objects[name] = obj
    
    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attr):
        obj = copy.deepcopy(self._objects.get(name))

        # In case you want to clone the object but modify specific attributes (key/values)
        obj.__dict__.update(attr)
        return obj


class Car():
    def __init__(self):
        self.name = "Honda"
        self.color = "Red"
        self.options = "Ex"

    def __str__(self):
        return "{} | {} | {} ".format(self.name, self.color, self.options)
    
c = Car()
prototype = Prototype()
prototype.register_object("Honda", c)
c1 = prototype.clone("Honda", type="Sedan")
print(c1)