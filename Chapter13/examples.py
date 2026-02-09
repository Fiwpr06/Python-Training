# While Loop

def checkPrime(x):
    if x < 2:
        return "Non-Prime"
    i = 2
    while i*i <= x:
        if x % i == 0:
            break
        i += 1  
    else:
        return "Prime"
    return "Non-Prime"

print(f"Prime Check: {checkPrime(7)}", end="\n\n")  

# For Loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")
else:
    print("All fruits have been listed.")    
print()

# Using range()
for i in range(1, 6):
    print(f"Number: {i}")
print()

# Using zip()
names = ["ZywOo", "m0NESY", "s1mple"]
ages = [25, 20, 28]
for name, age in zip(names, ages):
    print(f"Player: {name}, Age: {age}")
print()

# Using enumerate()
for ofset, char in enumerate(names[0], start=1):
    print(f"Character {ofset}: {char}")
print()

# Comprehensions
list = [x for x in range(1, 11)]
print(f"List Comprehension: {list}", end="\n\n")