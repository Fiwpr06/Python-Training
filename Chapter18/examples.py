# Positional and Keyword Arguments
print("Positional and keyword arguments demonstration:")
def func(a, b, c):
    print(f"a={a}, b={b}, c={c}")
    
func(1, 2, 3) # Positional
func(a=1, b=2, c=3) # Keyword 

# Positional, Default arguments, *args (extra positional), keyword-only (c), **kwargs (extra keywords)
print("\nDefault values and starred collectors demonstration:")
def func2(a, b= 10, *args, c = 20, **kwargs):
    print(f"a={a}, b={b}, args={args}, c={c}, kwargs={kwargs}")
    
func2(1)
func2(1, 2, 3, 4, c=30, d=40, e=50) 
func2(1, c =4, d=40, e=50)

# Unpacking using * and **
print("\nUnpacking demonstration:")
args = (3, 4)
kwargs = {'c': 30, 'd': 40, 'e': 50}
func2(1, *args, **kwargs)

# Positional-only (/) and keyword-only (*) arguments
def func3(a, /, b, *, c):
    print(f"a={a}, b={b}, c={c}")
print("\nPositional-only and keyword-only demonstration:")
func3(1, 2, c=3)
func3(1, b=2, c=3)