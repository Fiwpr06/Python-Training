# Breaking out of nested loops 
import sys
import traceback

class Exitloop(Exception):
    pass

try:
    for i in range(5):
        for j in range(5):
            if i == 2 and j == 3:
                raise Exitloop
            print(f"i: {i}, j: {j}")
except Exitloop:
    print("Exited the loop at i=2, j=3.", end="\n\n")
    
# Signaling non-error conditions
def check_value(x):
    """Check if x is prime."""
    class FoundValue(Exception):
        pass
    
    try:
        if x < 2:
            raise FoundValue
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                raise FoundValue
    except FoundValue:
        return False
    return True

print(check_value(1))
print(check_value(2), end="\n\n")

# Accessing exception information
try:
    1 / 0
except:
    type, value, ex_traceback = sys.exc_info()
    print(f"Exception type: {type}, value: {value}, traceback: {ex_traceback}", end="\n\n")
    print("Type name:", type.__name__)
    
    if hasattr(sys, "exception"):
        print("Instance:", sys.exception())
    
    with open("error_log.txt", "w") as f:
        traceback.print_exc(file=f)