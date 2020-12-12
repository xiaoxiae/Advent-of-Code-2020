import sys

sys.path.insert(0, "../")
from utilities import success, get_input

d, x, y = 0, 0, 0
delta = ((1, 0), (0, 1), (-1, 0), (0, -1))

for inst in get_input():
    by = int(inst[1:])

    if inst[0] == "E":
        x += by
    if inst[0] == "N":
        y += by
    if inst[0] == "S":
        y -= by
    if inst[0] == "W":
        x -= by

    if inst[0] == "R":
        by //= 90
        d = (d - by) % 4
    if inst[0] == "L":
        by //= 90
        d = (d + by) % 4

    if inst[0] == "F":
        x += delta[d][0] * by
        y += delta[d][1] * by

success(abs(x) + abs(y))
