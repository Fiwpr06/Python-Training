items = [{'item': 'sword', 'damage': 10, 'durability': 250, 'enchantments': ['sharpness', 'unbreaking']},
         {'item': 'bow', 'damage': 7, 'durability': 384, 'enchantments': ['power', 'punch']},
         {'item': 'axe', 'damage': 9, 'durability': 200, 'enchantments': ['efficiency', 'fortune']}]

print(items[0]['enchantments'][0])
items[1]['enchantments'].append('flame')
print(items[1])


