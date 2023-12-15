import sys

sys.path.insert(0, "../")
from utilities import success, get_input
from typing import *


def recursive_combat(h1, h2):
    seen = set()
    seen.add((tuple(h1), tuple(h2)))

    i = 0
    while len(h1) != 0 and len(h2) != 0:
        i += 1
        c1 = h1.pop(0)
        c2 = h2.pop(0)

        if c1 <= len(h1) and c2 <= len(h2):
            winner, _ = recursive_combat(list(h1[:c1]), list(h2[:c2]))
        else:
            winner = 0 if c1 > c2 else 1

        if winner == 0:
            h1.append(c1)
            h1.append(c2)
        else:
            h2.append(c2)
            h2.append(c1)

        h = (tuple(h1), tuple(h2))

        if h in seen:
            return 0, (h1, h2)

        seen.add(h)

    return (0 if len(h1) != 0 else 1), (h1, h2)

input = get_input(whole=True)

players = list(map(lambda x: list(map(int, x.split("\n")[1:])), input.split("\n\n")))

_, players = recursive_combat(*players)
deck = players[0] or players[1]

print(players)

total = 0
for i in range(1, len(deck) + 1):
    total += deck[-i] * i

success(total)
