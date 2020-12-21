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

canonical = []

while len(alergens) != 0:
    for alergen in alergens:
        possible_foods = set(foods)

        for f, a in pairings:
            if alergen in a:
                for food in foods:
                    if food not in f:
                        possible_foods -= {food}

        if len(possible_foods) == 1:
            canonical.append((list(possible_foods)[0], alergen))
            alergens -= set([alergen])
            foods -= possible_foods
            break

success(",".join(a for a, b in sorted(canonical, key=lambda x:x[1])))
