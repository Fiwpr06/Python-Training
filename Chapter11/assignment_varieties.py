n, m = 10, 5
print(f"n: {n}, m: {m}")

[a, b] = [3, 40]
print(f"a: {a}, b: {b}")

x, y, z = 'abc'
print(f"x: {x}, y: {y}, z: {z}")

first, *middle, last = [1, 2, 3, 4, 5]

print(f"first: {first}, middle: {middle}, last: {last}") 

*head, tail = [1, 2, 3, 4, 5]

print(f"head: {head}, tail: {tail}")

k = l = j = 0

if k is l is j:
    print("All variables point to the same object")
    
s = 0;
s += 1;
s *= 2;
print(f"s: {s}")