# initialization and basic operations
d = {'item': "pickaxe", 'enchantment': "sharpness", 'level': 5, 'durability': "unbreaking"}

print("Original dictionary:", d)
print("Length of the dictionary:", len(d))
print("Accessing 'item':", d['item'])
print("Accessing 'level':", d.get('level'))

d["level"] -= 1
print("After decreasing 'level' by 1:", d, end='\n\n')

# adding and removing items
d['owner'] = "Steve"
print("After adding 'owner':", d)
d['enchantment'] = ["efficiency", "fortune", "mending"]
print("After changing 'enchantment' to a list:", d)

removed_item = d.pop('durability')
print("After removing 'durability':", d)
print("Removed 'durability':", removed_item)

# accessing keys, values, and items
keys = d.keys()
values = d.values()
items = d.items()
print("\nDictionary keys:", keys)
print("Dictionary values:", values)
print("Dictionary items:", items, end='\n\n')

# access and key verification
print("item" in d)
print(d.get('nonexistent', 0)) # default value if key not found

d2 = {'item': "bow", 'enchantment': "power", 'level': 3}
d3 = d | d2
print("\nMerged dictionary d3 (d | d2):", d3)

d4 = {**d, **d2}
print("Merged dictionary d4 ({**d, **d2}):", d4)