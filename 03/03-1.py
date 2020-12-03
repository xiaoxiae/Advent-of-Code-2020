import sys
sys.path.insert(0, "../")
from utilities import success, get_input

input = get_input()

x, y = 0, 0
trees = 0

for y in range(1, len(input)):
    line = input[y]
    x = (x + 3) % len(line)

    if input[y][x] == "#":
        trees += 1

print(trees)
