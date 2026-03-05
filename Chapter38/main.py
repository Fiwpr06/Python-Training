# Properties
class Group:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        """Get the name of the group."""
        print("Getting name...")
        return self._name
    
    @name.setter
    def name(self, value):
        """Set the name of the group."""
        print("Setting name...")
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        self._name = value

g = Group("Admins")
print(g.name, end="\n\n")
g.name = "Users"
print(g.name, end="\n\n")

# Descriptor
class Descriptor:
    def __init__(self, value):
        self.default = value
        
    def __get__(self, instance, owner):
        """Get the value from the instance."""
        if instance is None:
            return self
        return instance.__dict__.get("value", self.default)

    def __set__(self, instance, value):
        """Set the value on the instance."""
        if not isinstance(value, int):
            raise ValueError("Value must be an integer.")
        instance.__dict__["value"] = value
class MyClass:
    value = Descriptor(23)
    
print("Descriptor created.")
obj = MyClass()
obj.value = 42
print(obj.value, end="\n\n")

# __getattr__ and __setattr__
class User:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        """Return a greeting message."""
        return f"Hello, I'm {self.name}!"
    
class Proxy:
    def __init__(self, obj):
        self.wrapped  = obj
        
    def __getattr__(self, name):
        """Get an attribute from the wrapped object."""
        return getattr(self.wrapped, name)
    
    def __setattr__(self, name, value):
        """Set an attribute in the wrapped object."""
        if name == "wrapped":
            super().__setattr__(name, value)
        else:
            setattr(self.wrapped, name, value)

obj = Proxy(User("Phi"))
print(obj.name)
obj.name = "Pha"
print(obj.name)
print(obj.greet())