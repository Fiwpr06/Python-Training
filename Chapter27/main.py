# Create Instances and Method 
class Father:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        """Method to print a greeting message including the father's name"""
        print(f"Hello, I am {self.name}, the father.\n")
        
a = Father("Huy")
a.say_hello()

# Inheritance and Method Overriding
class Son(Father):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def say_hello(self):
        """Override the say_hello method to include the son's name and age"""
        print(f"Hello, I am {self.name}, the son. I am {self.age} years old.\n")
        
b = Son("Hieu", 20)
b.say_hello()

# Operator Overloading and String Representation
class Daughter(Father):
    def __init__(self, name, hobby):
        super().__init__(name)
        self.hobby = hobby
        
    def __add__(self, other):
        """Overload the + operator to return a message about the relationship"""
        if isinstance(other, Son):
            return f"{self.name} and {other.name} are siblings."
        return NotImplemented
    
    def __str__(self):
        """Return a string representation of the daughter"""
        return f"{self.name} is the daughter with a hobby of {self.hobby}."

    def say_hello(self):
        """Override the say_hello method to include the daughter's name and hobby"""
        print(f"Hello, I am {self.name}, the daughter. My hobby is {self.hobby}.")

c = Daughter("Lan", "painting")
c.say_hello()
print(c)

d = Daughter("Mai", "dancing")
d.say_hello()
print(c + b)    