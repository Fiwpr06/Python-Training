# Object to represent boolean values

print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(None))

# Example usage in conditionals
l = []
if not l:
    print("The list is empty")
    