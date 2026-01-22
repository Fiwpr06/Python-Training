x = True

if x:
    y = False
    if not y:
        print("Level 2 reached")
    print("Level 1 reached")
print("Outside if block", end="\n\n")

list = 'hello', 'my', 'friend'
for item in list:
    print(item)
    
list2 = [
    'hello', 
    'my', 
    'friend'
]
for item in list2:
    print(item)
    
if (list != list2 or
    list is not list2):
    print("list1 and list2 are different")
    
S = "This is a very long string " \
    "continued on the next line."
    
print(S, end="\n\n")
    
while True:
    rep = input("Enter 'exit' to quit: ")
    if rep == 'exit':
        break
    print("You entered:", rep)
        