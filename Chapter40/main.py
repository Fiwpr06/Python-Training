# Basic Metaclass
class Meta(type):
    def __new__(meta, classname, supers, classdict):
        """Create a new class with the given name, bases, and attributes."""
        print(f"Creating class: {classname}")
        classdict['generated_by'] = 'Python Metaclass'
        return type.__new__(meta, classname, supers, classdict)

    def meta_method(self):
        return "I am a metaclass method!"

# Using Metaclass
class MyClass(metaclass=Meta):
    def normal_method(self):
        """Return a message indicating this is a normal method."""
        return "I am a normal method."

# 3. Testing Search Rules
obj = MyClass()
print(MyClass.generated_by)
print(MyClass.meta_method())

try:
    print(obj.meta_method())
except AttributeError:
    print("Instance cannot see metaclass methods.", end="\n\n")

# 4.Auto-decorating methods
from types import FunctionType

def debug(func):
    def wrapper(*args, **kwargs):
        """Print the function name and call it."""
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

class AutoDebug(type):
    def __new__(meta, name, bases, dct):
        """Automatically decorate all methods with the debug decorator."""
        for attr, value in dct.items():
            if isinstance(value, FunctionType):
                dct[attr] = debug(value)
        return type.__new__(meta, name, bases, dct)

class Person(metaclass=AutoDebug):
    def __init__(self, name):
        self.name = name
    def work(self):
        """Print a message indicating that the person is working."""
        print(f"{self.name} is working.", end="\n\n")

p = Person("Alice")
p.work()           