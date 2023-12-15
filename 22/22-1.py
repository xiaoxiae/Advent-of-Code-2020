import sys

sys.path.insert(0, "../")
from utilities import success, get_input
from typing import *

from itertools import product

input = get_input(whole=True)

players = list(map(lambda x: list(map(int, x.split("\n")[1:])), input.split("\n\n")))

while len(players[0]) != 0 and len(players[1]) != 0:
    c1 = players[0].pop(0)
    c2 = players[1].pop(0)

    if c1 > c2:
        players[0].append(c1)
        players[0].append(c2)
    else:
        players[1].append(c2)
        players[1].append(c1)

deck = players[0] or players[1]

total = 0
for i in range(1, len(deck) + 1):
    total += deck[-i] * i

success(total)
