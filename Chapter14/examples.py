# Iterator

l = [1, 2, 3]
it = iter(l)
print(f"Iterator next(): {next(it)}")
print(f"Iterator next(): {next(it)}")
print(f"Iterator next(): {next(it)}", end="\n\n")

it = iter(l)
while True:
    try:
        item = next(it)
        print(item)
    except StopIteration:
        print("StopIteration encountered, ending loop.")
        break

for item in it:
    print(item)
else:
    print("Iterator exhausted, loop ended.", end="\n\n")
    
# Generator
def countdown(n):
    print("Countdown started!")
    while n > 0:
        yield n
        n -= 1
    print("Countdown ended!")
    
countdown_gen = countdown(3)
print(f"Generator next(): {next(countdown_gen)}")
print(f"Generator next(): {next(countdown_gen)}")
print(f"Generator next(): {next(countdown_gen)}", end="\n\n")

# Comprehensions
squares = (x*x for x in range(0, 10))
for square in squares:
    print(f"Square: {square}")
print()

# Comprehension with condition
odd_squares = (x*x for x in range(0, 10) if x % 2 != 0)
for odd_square in odd_squares:
    print(f"Odd Square: {odd_square}")
print()

# Advanced
r = range(10)
print(r)
list(r)
print(f"Range as list: {list(r)}", end="\n\n")
m = filter(lambda x: x % 2 == 0, range(10))
print(f"Filter even numbers: {list(m)}", end="\n\n")

# Single vs Multiple pass iterators
data = [1, 2, 3]
it1, it2 = iter(data), iter(data)
# Multiple pass
print("Multiple pass iterator:")
print(f"Data: {data}")
print(f"it1 next(): {next(it1)}, it2 next(): {next(it2)}")
print(f"it1 next(): {next(it1)}, it2 next(): {next(it2)}")
print("Check if iter(data) is data:", iter(data) is data, end="\n\n")

# Single pass
print("Single pass iterator:")
z = zip((1, 2), (3, 4))
print(f"zip object: {list(z)}")
z = zip((1, 2), (3, 4))
it3, it4 = iter(z), iter(z)
print(f"it3 next(): {next(it3)}\nit4 next(): {next(it4)}")
print("Check if iter(z) is z:", iter(z) is z)
