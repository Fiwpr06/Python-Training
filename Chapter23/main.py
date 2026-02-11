import module

L = [1, 2, [3, 4], 5, [6, [7, 8]], 9]
print("Nested list L:", L)
print("Sum of nested list L:", module.sum_tree(L), end="\n\n")

# REPL 
from share import x, y
print("Before modification:")
print("Value of x:", x)
print("Value of y:", y)

x = 99
y.append([9, 9, 9, 9, 9, 9, 9, 9, 9, 9])

import share
print("\nAfter modification:")
print("Value of x in share module:", share.x)
print("Value of y in share module:", share.y)

from importlib import reload
reload(share)
