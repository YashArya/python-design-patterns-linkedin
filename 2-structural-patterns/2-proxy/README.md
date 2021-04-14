# Proxy Pattern

# Problem
* Proxy pattern is handy when creating a resource incentive object
* Postpone object creation until absolutely necessary, due to its resource intensive nature
* Thus we need a placeholder which will in turn create the object when necessary (this is the "proxy")

# Scenario
* Producer - resource intensive object
    * Only a fixed number of Producer objects can exist at a time
* Artist - Proxy; Checks to see if a producer becomes available for a Guest
* Guest

# Solution
* Clients interact with Proxy until the resource intensive object is available
* Proxy object is incharge of creating the resource intensive object