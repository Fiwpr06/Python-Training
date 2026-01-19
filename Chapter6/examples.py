a = 5
b = a
a += 2
print("a:", a, "b:", b)

print("\nList assignment and copying:")
l = [1, 2, 3]
l2 = l
l2[0] = 10
print("l:", l, "l2:", l2)

print("\nProper list copying:")
l = [1, 2, 3]
l2 = l.copy()
l3 = l[:]

l2[0] = 10
l3[1] = 20
print("l:", l, "l2:", l2, "l3:", l3)

print("Comparing lists:")
l = [1, 2, 3, 4, 5]
l2 = [1, 2, 3, 4, 5]
print("\nList comparisons:", l == l2, l is l2)

import sys

x = [1, 2, 3, 4, 5]
print("\nReference count for x:", sys.getrefcount(x))
