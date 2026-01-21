# initialization
T = (2, 3, 4, 5, 6)

print("Original tuple:", T)
print("Length of the tuple:", len(T))
# concatenation, accessing elements, slicing
T += (7, 8, 7, 7)
print("Tuple after concatenation:", T)

print("First element (T[0]):", T[0])
print("Last element (T[2:-2]):", T[2:-2], end='\n\n')

# methods: index and count
print("Index of element 5 in tuple T:", T.index(5))
print("Count of element 7 in tuple T:", T.count(7), end='\n\n')

# attention to single-element tuples
T1 = (10) 
T2 = (10,)
print("Type of T1 (10):", type(T1))
print("Type of T2 (10,):", type(T2), end='\n\n')
