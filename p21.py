import re
from collections import Counter
from itertools import cycle

from aocd import data as foods


p = re.compile(r'(.+) \(.+? (.+)\)')

food = {}
seen_ingredients = set()
seen_allergens = set()
frequency = Counter()

for line in foods.splitlines():
    ingredients, allergens = p.search(line).groups()
    ingredients = tuple(ingredients.split())
    frequency.update(ingredients)
    allergens = set(allergens.split(', '))

    food[ingredients] = allergens
    seen_ingredients.update(set(ingredients))
    seen_allergens.update(allergens)

definite_allergens = {}
found_allergens = set()
for allergen in cycle(seen_allergens):
    if allergen in found_allergens:
        continue
    i = set()
    for ingredients, allergens in food.items():
        if allergen in allergens:
            if i:
                i &= set(ingredients) - definite_allergens.keys()
            else:
                i = set(ingredients) - definite_allergens.keys()

    if len(i) == 1:
        definite_allergens[i.pop()] = allergen
        found_allergens.add(allergen)

    if found_allergens == seen_allergens:
        break

non_allergens = seen_ingredients - definite_allergens.keys()
occurences = sum(frequency[item] for item in non_allergens)
print('Part 1:', occurences)
print('Part 2:', ','.join(sorted(definite_allergens, key=lambda i: definite_allergens[i])))
