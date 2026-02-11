from timeit import timeit

def list_comprehension():
    return [x for x in range(10000)]

def list_map():
    return list(map(int, range(10000)))

def list_loop():
    result = []
    for x in range(10000):
        result.append(x)
    return result

def list_generator():
    return list(x for x in range(10000))

time_comprehension = timeit(list_comprehension, number=1000)
time_map = timeit(list_map, number=1000)
time_loop = timeit(list_loop, number=1000)
time_generator = timeit(list_generator, number=1000)

print(f"List comprehension time: {time_comprehension:.6f} seconds")
print(f"List map time: {time_map:.6f} seconds")
print(f"List loop time: {time_loop:.6f} seconds")
print(f"List generator time: {time_generator:.6f} seconds")