import sys

sys.path.insert(0, "../")
from utilities import success, get_input

d, xw, yw, xs, ys = 0, 10, 1, 0, 0

for inst in get_input():
    by = int(inst[1:])

    if inst[0] == "E":
        xw += by
    if inst[0] == "N":
        yw += by
    if inst[0] == "S":
        yw -= by
    if inst[0] == "W":
        xw -= by

    if inst[0] == "R":
        for i in range(by // 90):
            xw, yw = yw, -xw
    if inst[0] == "L":
        for i in range(by // 90):
            xw, yw = -yw, xw

    if inst[0] == "F":
        xs += xw * by
        ys += yw * by

success(abs(xs) + abs(ys))
