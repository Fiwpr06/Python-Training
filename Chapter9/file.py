# Writing 
f = open("data.txt", "w")

f.write("Hello, World!\n")
f.writelines(["Welcome to file handling in Python", ", Enjoy your stay!\n"])
print("This is a sample file.", "Goodbye!", file=f, sep="\n", end="\n")
f.close()

# Reading
f = open("data.txt", "r")
print("Reading file by readline(): ", f.readline())
print("Reading file by readlines(): ", f.readlines(), end='\n\n')
f.close()

# Appending
f = open("data.txt", "a")
f.write("Appending a new line to the file.\n")
f.close()

# Reading full file
f = open("data.txt", "r")
print("Reading file by read():", f.read(), sep = "\n")
f.close()