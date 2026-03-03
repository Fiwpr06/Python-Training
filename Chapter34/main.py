# try/except/else/finally structure
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print("Caught an exception:", e)
        return None
    else:
        print("Division successful.")
        return result
    finally:
        print("This will always execute.", end="\n\n")

divide(10, 2)
divide(10, 0)

# catching multiple exceptions
try:
    x = int("not a number")
except (ValueError, TypeError) as e:
    print("Caught an exception:", e, end="\n\n")
    
# try/finally for cleanup
try:
    f = open("file.txt", "w")
    f.write("Hello, World!")
except IOError as e:
    print("Caught an exception:", e)

# try/else to separate 
try:
    x = int("123")
except ValueError as e:
    print("Caught an exception:", e)
else:
    print("Conversion successful, x =", x, end="\n\n")