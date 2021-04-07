#!/usr/bin/env python3

'''
# Scenario
* Korean and British objects have different methods for speaking: speak_korean() and speak_english()
* Client would ike to use a uniform interface: speak()
'''

class Korean():
    def __init__(self):
        self.name = "Korean"
    
    def speak_korean(self):
        return "An-neyong?"


class British():
    def __init__(self):
        self.name = "British"

    def speak_english(self):
        return "Hello!"

class Adapter():
    def __init__(self, object, **adapted_method):
        self._object = object

        # Add a new dict item tht establishes the meapping between the generic method speak() and the concrete methods
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        return getattr(self._object, attr)

speakers = list()
korean = Korean()
british = British()

speakers.append(Adapter(korean, speak=korean.speak_korean))
speakers.append(Adapter(british, speak=british.speak_english))

for speaker in speakers:
    print("{} says '{}'\n".format(speaker.name, speaker.speak()))

