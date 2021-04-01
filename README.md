# python-design-patterns-linkedin
https://www.linkedin.com/learning/python-design-patterns

# Creational Patterns
## Definition
Used to create objects in a systematic way

## Benefits 
Flexiblity.

Example: Different subtypes of objects from the same class at runtime.

## Object-Oriented Mechanisms Used
Polymorphism, Interfaces

# Structural Patterns
## Definition
Establishes useful relationships between software components in certain configurations. 

The goal is to satisfy both functional and non-functional requirements. 
Different goals yield different structural patterns.

## Object-Oriented Mechanisms Used
Inheritance, Interfaces

# Behavioral Patterns
## Definition
Provide best practices for how objects interact with each other.

## Focus
Define the protocol used for interaction between these objects to accomplish a common goal.

## Object-Oriented Mechanisms Used
Methods and their signatures, interfaces

# Pattern Context
To use a design pattern effectively, you need to know the context in which it works best.

A pattern context consists of the following.
* Participants
* Quality Attributes
* Forces
* Consequences

## Participants
* Refers to the classes involved to form a design pattern.
* These classes play different roles in the pattern

## Quality Attributes
* Refer to non-functional requirements such as 
    * usability, modifiability, reliability, performance, security, etc.

* They have an effect on the entire software
    * Typically addressed by architectural solutions

## Forces
* Refer to the various factors or trade-offs to consider
* Typically manifests in the quality attributes
* If you don't reason about these forces well, you could end up with unintended consequences

## Consequences
* Refers to the side effects of using a pattern.
    * Eg: Better security but worse performance.
* Look at the benefits (problem solved by the pattern) as well as the costs (including unintended consequences) in order to decide whether to use the pattern.

## Pattern Language
A pattern language provides a framework within which to talk about the different aspects of a pattern.

It consists of 
* Name: Captures the gist of the pattern. Should be meaningful and memorable.
* Context: Provides the information regarding when to use a pattern and when not to use a pattern.
* Problem: Describes a design challenge to be addressed.
* Solution: Specifies the pattern itself. 
    * Patterns are specified in terms of their structure and behavior
        * Structure: Relationship among elements
        * Behavior: Interaction between elements
* Related patterns: 
    * Other patterns either used together with the pattern being described, or similar but different
    * It's helpful to describe the subtle differences between these patterns
