def add(a, b):
    """Return the sum of two values"""
    return a + b

print("Sum of 5 and 3 is:", add(5, 3), end="\n\n")

# Demonstrating that `def` is executed at runtime
n = int(input("Enter a number: "))

if n >= 2:
    def check_prime(num):
        """Return True if num is a prime number, otherwise False."""
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    # Function names are references to function objects
    f = check_prime
    print("Is 7 prime?", f(7), end="\n\n")
else:
    print("Number is less than 2, skipping prime check.\n")
    
    
# Demonstrating local scope with an immutable object
print("Immutable object and local variable demonstration:")
def immutable(x):
    """Rebinds a local name to a new immutable object."""
    x = 10
    print("Inside function, x =", x)

x = 100    
immutable(x)
print("Outside function, x =", x, end="\n\n")

print("Mutable variable demonstration:")
def mutable(lst):
    """Mutates the original list object passed into the function."""
    lst.append(4)
    print("Inside function, lst =", lst)
    
lst = [1, 2, 3]
mutable(lst)
print("Outside function, lst =", lst, end="\n\n")

print("Global name with immutable object demonstration:")
y = 10
def immutable_global():
    """Modifies a global name by rebinding it to a new object."""
    global y
    y = 20
    print("Inside function, y =", y)
    
immutable_global()
print("Outside function, y =", y, end="\n\n")

# Demonstrating that functions are first-class objects
print("Functions as first-class objects demonstration:")
def run(func):
    """Accepts a function object and executes it."""
    result = func()
    print("Result of the function:", result)

def hello():
    """Return a greeting string."""
    return "Hello, World!"

run(hello)