import sys

sys.path.insert(0, "../")
from utilities import success, get_input

from itertools import product

input = get_input()

state = set()

def neighbours(cell):
    total = 0
    for neighbour in neighbouring_cells(cell):
        if neighbour in state:
            total += 1
    return total


def neighbouring_cells(cell, yield_itself=False):
    x, y, z = cell
    for xd, yd, zd in product((0, 1, -1), repeat=3):
        # skip zero delta
        if xd == yd == zd == 0:
            continue

        yield (x + xd, y + yd, z + zd)
    if yield_itself:
        yield cell


for i in range(len(input)):
    for j in range(len(input[0])):
        if input[i][j] == "#":
            state.add((i, j, 0))

for i in range(6):
    new_state = set()

    for cell in state:
        for c in neighbouring_cells(cell, yield_itself=True):
            # if the cell is alive
            if c in state:
                if 2 <= neighbours(c) <= 3:
                    new_state.add(c)
            else:
                if neighbours(c) == 3:
                    new_state.add(c)

    state = new_state

success(len(state))
