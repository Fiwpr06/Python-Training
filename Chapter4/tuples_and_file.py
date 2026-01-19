t = (1, 2, 3, 4)

f = open("output.txt", "w")
f.write(str(t))

print("\nTuple written to output.txt", t, file=f)

f = open("output.txt", "r")

for line in f:
    print("Read from file:", line)