a = 4
b = 25
print(a + b)
print(a - b)
print(a * b)
print(a ** b)

print(a / b)
print(a // b)
print(a % b)

import math
import random

print(math.pi)
print(math.e)
print(math.sqrt(b))
print(random.random())
print(random.randint(1, 10))

print("\nSet operations:")
x = {1, 2, 3, 4, 5}
y = {4, 5, 6, 7, 8}

print(x & y)
print(x | y)
print(x - y)
print(x ^ y)

print(x.intersection(y))
print(x.union(y))
print(x.difference(y))
print(x.symmetric_difference(y))

from decimal import Decimal
from fractions import Fraction

print("\nDecimal and Fraction operations:", Decimal('0.1') + Decimal('0.2'), "and", Fraction(1, 3) + Fraction(1, 6))