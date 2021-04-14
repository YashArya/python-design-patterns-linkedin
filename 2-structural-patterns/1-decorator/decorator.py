#!/usr/bin/env python3

'''
Goal
* Start with a function that displays "hello world"
* Then make the message fancier by decorating it with additional text
'''

from functools import wraps

def make_blink(function):
    
    # This helps retain the name and docstring of the function being decorated.
    @wraps(function)

    # Define the inner function
    def decorator():
        """Decorator Function!"""
        ret = function()
        return "<blink>" + ret + "</blink>"
    
    return decorator

# Apply decorator using annotation
@make_blink
def hello_world():
    """Original function!"""
    return "Hello, World!"

if __name__ == "__main__":
    # Check the result of decorating
    print(hello_world())

    # Check if the function name is still the same as before
    print(hello_world.__name__)

    # Check if the docscring is still the same as before
    print(hello_world.__doc__)


