# Initialization and basic operations
l = [43, 'hello', 3.14, True]
print("Original list:", l)
print("Length of the list:", len(l))
print("First element (l[0]):", l[0])
print("Last element (l[-1]):", l[-1], end='\n\n')

# Mutability
l[1] += ', world!'
print("After modifying second element (l[1] = 'world'):", l)
l.append('new item')
l.pop(2)
print("After appending 'new item' and popping index 2:", l, end='\n\n')

# Sorting and reversing
l2 = [1, 9, 3, 7, 5, 6, 2, 8, 6, 1]
l2.sort()

print("List l2:", l2)
print("Sorted list l2:", l2)
print("Reversed list l2:", list(reversed(l2)), end='\n\n')

# List comprehensions
squares = [x**2 for x in range(10)]
print("List of squares from 0 to 9:", squares)

matrix = [[j*i for j in range(5)] for i in range(1, 4)]
print("3x5 matrix using list comprehension:", matrix)

first_column = [row[1] for row in matrix]
print("First column of the matrix:", first_column, end='\n\n')