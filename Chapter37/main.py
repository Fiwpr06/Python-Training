# Encoding and decoding 
s = 'Hello, World!'
s1 = s.encode('utf-8')
print(s1)
s2 = s1.decode('utf-8')
print(s2, end="\n\n")

# Different in indexing
print("Default:",s[0])
print("Encoded:",s1[0])
print("Decoded:",s2[0], end="\n\n")

# Mutable bytearray
bs = bytearray(b'Hello, World!')
bs.append(ord('?'))
print(bs)
bs[-1] = ord('!')
print(bs)

# File I/O with bytes
with open('data.txt', 'w', encoding='utf-8') as f:
    f.write("Xin chào")
    
with open('data.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content, end="\n\n")

with open('data.txt', 'rb') as f:
    data = f.read()
    print(data)