#!/usr/bin/env python3

class AcronymDict():
    _shared_state = dict()

    def __init__(self):
        self.__dict__ = self._shared_state

class Singleton(AcronymDict):
    def __init__(self, **kwargs):
        AcronymDict.__init__(self)
        self._shared_state.update(kwargs)

    def __str__(self):
        return str(self._shared_state)

x = Singleton(HTTP = "Hyper Text Transfer Protocol")
print(x)

y = Singleton(SNMP = "Simple Network Management Protocol")
print(y)

