# Data Hiding
print("Data Hiding Example:")
from module.secrect import *

print(secret_function())
print(_internal_accessible())
# print(_private_function()) Error _private_function is not defined

# Import module and access private function
print("\nAccessing Private Function:")
from module import secrect

print(secrect._private_function()) # This will work

# Dual usage 
print("\nDual Usage:")
from module import tool

print("Sum of 10 and 20 is:", tool.sum(10, 20))

# Dynamic imports
print("\nDynamic Imports:")
from module import dynamic as dyn

print(dyn.name)
print(dyn.version)

# Introspect module attributes
print("\nIntrospecting:")
print("Attributes of dynamic module:", dir(dyn))
print("getattr for 'description':", getattr(dyn, 'description', "Attribute not found"))
print("getattr for 'description':", getattr(dyn, 'des', "Attribute not found"))
print("Namespace of dynamic module:", dyn.__dict__.keys())
