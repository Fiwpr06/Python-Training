# List Comprehension and Generator Expressions
L = [x ** 2 for x in range(1000)]
G = (x ** 2 for x in range(1000))

print("List comprehension output:")
print(L[:10], "...", L[-10:], end="\n\n")
print("Generator expression output:")
print(next(G))
print(next(G))
print(next(G))
print(next(G), end="\n\n")

# Generator Function
def gen():  
    for x in range(100):
        yield x ** 2

print("Generator function output:")   
for i in gen():
    print(i, end=" ")
print(end="\n\n")

# Asynchronous Programming
import asyncio

print("Asynchronous programming demonstration:")
async def A():
    print("A start")
    await asyncio.sleep(1)
    print("A resume")

async def B():
    print("B start")
    await asyncio.sleep(7)
    print("B resume")

async def main():
    asyncio.create_task(A())
    asyncio.create_task(B())
    
    # main() only wait 2 seconds, so B() will not complete before main() finishes
    await asyncio.sleep(2)

asyncio.run(main())
