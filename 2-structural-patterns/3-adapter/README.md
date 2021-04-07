# Adapter Pattern
Converts the interface of a class into another one that the client is expecting

# Problem
* Incompatible interfaces between client/server

# Scenario
* Korean and British objects have different methods for speaking: speak_korean() and speak_english()
* Client would ike to use a uniform interface: speak()

# Solution
* Use the adapter pattern to translate the method name between the client and server code

# Related Patterns
* Bridges, Decorators