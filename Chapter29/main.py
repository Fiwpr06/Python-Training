# Class and Instance attributes
class SharedData:
    value = 65
    def __init__(self, val):
        self.data = val

a = SharedData(10)
b = SharedData(20)
print(a.value, b.value, SharedData.value)
SharedData.value = 75
print(a.value, b.value, SharedData.value)
a.value = 85
print(a.value, b.value, SharedData.value)

# Multiple Inheritance and Method Resolution Order
class A:
    def method(self):
        print("Method from class A")
class B():
    def method(self):
        print("Method from class B")

class sub(A, B):
    pass 

s = sub()
s.method()
print(sub.__mro__)

# Bound Methods and Unbound Methods
class MyClass:
    def display(self, msg):
        print(f"MyClass says: {msg}")

obj = MyClass()

bound_method = obj.display
bound_method("Hello, World!")

unbound_method = MyClass.display
unbound_method(obj, "Hello again!")

print(a.__dict__)
print(a.__class__)
print(sub.__bases__)