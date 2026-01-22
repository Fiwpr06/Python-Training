print("time", "set", "day", sep ="--->", end="!!!\n")
print("Hello", end=" ")
print("World")

print("Python", "is", "fun", sep="_", end=".\n", file=open('output.txt', 'a'))

import sys
print("Failure", file=sys.stderr) 