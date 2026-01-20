s1 = "hehe'S"

s2 = 'hehe"S'

s3 = "\tLorem ipsum dolor sit amet,\n \tconsectetur adipiscing elit,\n sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

s4 = r"C:\hehe\Main\file.txt"

s5 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."""

print(s1, s2, s3, s4, s5, sep="\n\n")

# Indexing and slicing

s = "Hello, World!"
print("\nString for indexing and slicing:", s)

print("Index: s[4]:", s[4], "s[-2]:", s[-2])

print("Slicing: s[0:5]:", s[0:5], "\ns[:]:", s[:], "\ns[7:12]:", s[7:12], "\ns[-6:-1]:", s[-6:-1], "\ns[:5]:", s[:5], "\ns[7:]:", s[7:], "\ns[::2]:", s[::2], "\ns[1::2]:", s[1::2])

# immutability

s = "Hello"
print("\nOriginal string s:", s)
# s[0] = "h"  This will raise an error

s2 = s.replace("H", "h")
print("After replacing H with h in s:", s2)

s2 = 'h' + s[1:]
print("After concatenating 'h' with s[1:]:", s2)

# methods

s = "  Hello, World!  "
print("\nOriginal string with spaces:", repr(s))

s_stripped = s.strip()
print("After strip():", repr(s_stripped))

s_upper = s.upper()
print("After upper():", repr(s_upper))

s_lower = s.lower()
print("After lower():", repr(s_lower))

s_isAlpha = s.isalpha()
print("s.isalpha():", s_isAlpha)

print("'abc'.isalpha():", 'abc'.isalpha())

s_isDigit = s.isdigit()
print("s.isdigit():", s_isDigit)

print("'1234'.isdigit():", '1234'.isdigit())

print("s.find(\"World\"):", s.find("World"))

print("s.replace(\"World\", \"There\"):", s.replace("World", "There"))

print("\nSplitting and joining strings:")
s = s_stripped + " Welcome to Python."
result = s.split(" ")
print("After splitting the string into a list:", result)

st = ""
for i in result:
    st += i + " "
print("After concatenating each word with an underscore:", st)
    
print("Joining the list back into a string:", " ".join(result))

name = "VScode"
greeting = f"Hello, {name}!"
print("\nUsing f-string for formatting:", greeting)

print("Using format() method for formatting: Hello, {}!".format(name))

print("Using %% operator for formatting: Hello, %s!" % name)

pi = 3.14159
print(f"Using f-string for formatting pi: {pi:.2f}")
print("Using format() method for formatting pi: {:.2f}".format(pi))
print("Using %% operator for formatting pi: %.2f" % pi)
