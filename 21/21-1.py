import sys

sys.path.insert(0, "../")
from utilities import success, get_input
from typing import *

from itertools import product

input = get_input()

pairings = []

foods = set()
alergens = set()


for line in input:
    ingredients, alg = line.split(" (contains ")
    pairings.append((ingredients.split(), alg.strip(")").split(", ")))
    foods = foods.union(set(pairings[-1][0]))
    alergens = alergens.union(set(pairings[-1][1]))

impossible_foods = set(foods)
for alergen in alergens:
    possible_foods = set(foods)

    for f, a in pairings:
        if alergen in a:
            for food in foods:
                if food not in f:
                    possible_foods -= {food}

    impossible_foods -= possible_foods

total = 0
for food in impossible_foods:
    for f, _ in pairings:
        total += f.count(food)

success(total)
