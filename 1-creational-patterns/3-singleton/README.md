# Name
Singleton Pattern

# Pattern
* Need to allow only one instance of a class.
* Sometimes used to create a global variable in an object oriented way.

# Scenario
* An information cache shared by multiple objects.

# Solution
* Modules in Python act as singletons
* We'll use the Borg Design pattern to implement the above scenario.
    * Borg Design pattern allows for multiple instances that all share the same state.
    * Technically, Singleton should have only one instance. But usually what we care about is the shared/singular state.
    * Borg is a Star Trek reference for a Collective alien species (https://en.wikipedia.org/wiki/Borg)
