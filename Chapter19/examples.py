# Recursive Function
def sum_tree(L):
    total = 0
    for x in L:
        if not isinstance(x, list):
            total += x
        else:
            total += sum_tree(x)  
    return total

L = [1, [2, [3, [4, 5]]], [6, 7], 8]
print("Nested list L:", L)
sum = sum_tree(L)
print("Sum of L:", sum)

# Interaction Alternatives
def sum_tree_iter(L):
    total = 0
    stack = [L]
    while stack:
        current = stack.pop()
        for x in current:
            if not isinstance(x, list):
                total += x
            else:
                stack.append(x)
    return total

print("Sum of L using iterative approach:", sum_tree_iter(L), end="\n\n")

# Function Attributes
def countdown():
    countdown.call -= 1
    print(f"Countdown: {countdown.call}")

countdown.call = 10
for _ in range(10):
    countdown()
    
# Function Annotations
def func(a: int, b: int = 5) -> int:
    """Return the sum of a and b."""
    return a + b

print("\nFunction Annotations:")
print("Annotations:", func.__annotations__)


# Lambda Functions
print("\nLambda Functions:")
cal = {'add': lambda x, y: x + y, 'sub': lambda x, y: x - y, 'mul': lambda x, y: x * y, 'div': lambda x, y: x / y}
print("Addition:", cal['add'](10, 5))
print("Subtraction:", cal['sub'](10, 5))
print("Multiplication:", cal['mul'](10, 5))
print("Division:", cal['div'](10, 5), end="\n\n")