# LEGB
x = 100 # Global(G)

def outer():
    x = 200 # Enclosing(E)
    
    def inner():
        x = 300 # Local(L)
        print("Inner x:", x)
    
    inner()
    print("Outer x:", x)

outer()
print("Global x:", x, end="")
print() # Build-in(B)

# The nonlocal statement and closure
def name(st):
    """Return a function that greets the given name st n times."""
    def hello(n):
        return (f"Hello, {st}!\n") * n
    return hello

f = name("Phi")
print(f(3))