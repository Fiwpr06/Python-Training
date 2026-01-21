# Problem 1: Shared Reference

A = [1, 2, 3, 4]
B = A

A[0] = "Changed"
print("B: ", B)

# Solution 1:

a = [1, 2, 3, 4]
b = a[:]
c = a.copy()

a[0] = "Safe"
print("b: ", b)
print("c: ", c)

# Problem 2: Nested Structure
import copy

X = [[1, 2, 3], [4, 5, 6]]
Y = X[:]
Z = copy.deepcopy(X)

X[0][0] = "Modified"
print("Y: ", Y)
print("Z: ", Z)