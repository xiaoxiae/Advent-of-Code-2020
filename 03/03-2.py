import sys
sys.path.insert(0, "../")
from utilities import success, get_input

input = get_input()

slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
product = 1

for xd, yd in slopes:
    x, y = 0, 0
    trees = 0
    for y in range(yd, len(input), yd):
        line = input[y]
        x = (x + xd) % len(line)

        if input[y][x] == "#":
            trees += 1
    product *= trees

success(product)
