# Builder Pattern

# Problem
* Antipattern: Telescoping constructors
    * Excessive number of constructors

# Scenario
* Building cars: First need to build the components and subcomponents
    * Tires, engine, etc

# Solution
* Partions the process of building a complex object into 4 different roles
    1. Director: In charge of building a product using the builder object
    2. Abstract Builder: Interfaces 
    3. Concrete Builder: implements the interfaces
    4. Product: Object being built
* Unlike the Factory/Abstract Factory, this pattern does not rely on polymorphism
    * Focus is on reducing the complexity through a divide and conquer strategy.