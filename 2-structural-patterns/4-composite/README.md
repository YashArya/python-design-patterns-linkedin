# Composite Pattern
Maintains a tree data structure to represent part-whole relationships 

# Problem
* Build a recursive tree data structure
* Elements have sub-elements

# Scenario
* Menu > submenu > sub-submenu...
* Display Menu and Sub-Menu items using Composite pattern.

# Solution
* Component: Abstract Class
* Child: Concrete class inheriting from Component
* Composite: Also a concrete class inheriting from Component
    * Composite child maintains child objects by adding/removing them to/from the tree data structure

# Related Patterns
* Decorator, Iterator, Visitor patterns
