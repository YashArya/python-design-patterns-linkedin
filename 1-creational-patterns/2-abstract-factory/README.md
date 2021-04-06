# Name
Abstract Factory Pattern

# Context
* Builds on top of the Factory Pattern.

# Problem
Used when
* There are uncertainities in types of Factory to be used at runtime
* Decisisions need to be made at runtime regarding what classes to use spanning across different factories that are logically related

# Scenario
* Build a Pet Factory that consists of a Dog Factory and a Cat Factory.
* Dog and Cat Factory produce Dog and Cat Food.

# Solution
* Abstract Factory: Pet Factory
* Concrete Factory: Dog Factory, Cat Factory
* Abstract Product: Pet and Pet Food
* Concrete Products: Dog and Dog Food, Cat and Cat Food

# Related Patterns
* Factory Pattern