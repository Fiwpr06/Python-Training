# Basic catching 
l = [1, 2, 3]

try:
    print(l[5])
except IndexError as e:
    print("Caught an exception:", e, end="\n\n")
    
# Manual raising
try:
    raise ValueError("This is a manually raised exception.")
except ValueError as e:
    print("Caught an exception:", e, end="\n\n")
    
# User-defined exceptions
class CustomError(Exception):
    def __str__(self):
        return "This is a custom error message."
    
try:
    raise CustomError()
except CustomError as e:
    print("Caught an exception:", e, end="\n\n")
    
# Termination Actions
try:
    print("This will execute.")
    f = open("file.txt", "w")
    f.write("Hello, World!")
except IOError as e:
    print("Caught an exception:", e)
finally:
    f.close()
    print("File closed in finally block.", end="\n\n")