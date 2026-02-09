import sys

s = "Hello, World!"
# List all attributes and methods
attribute = dir(s)
print(attribute)
# Filter out private attributes
public_attrs = [a for a in attribute if not a.startswith('_')]
print(f"Public attributes of str: {public_attrs}", end="\n\n")

"""
Module documentation
"""

def add(x, y):
    """Add two numbers and return the result."""
    return x + y
print("Function add() docstring:", add.__doc__, end="\n\n")

help(add)