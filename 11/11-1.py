import sys

sys.path.insert(0, "../")
from utilities import success, get_input

lines = get_input()
for i in range(len(lines)):
    lines[i] = list(lines[i])


def neighbours(x, y):
    empty = 0
    occupied = 0
    for xd, yd in (
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
    ):
        xn, yn = x + xd, y + yd

        if not (0 <= xn < len(lines[0]) and 0 <= yn < len(lines)):
            continue

        if lines[yn][xn] == "L":
            empty += 1

        if lines[yn][xn] == "#":
            occupied += 1

    return empty, occupied


def pprint(lines):
    for line in lines:
        print("".join(line))
    print()


while True:
    new_lines = [[c for c in line] for line in lines]

    for y in range(len(new_lines)):
        for x in range(len(new_lines[0])):
            _, occupied = neighbours(x, y)

            if lines[y][x] == "L" and occupied == 0:
                new_lines[y][x] = "#"

            if lines[y][x] == "#" and occupied >= 4:
                new_lines[y][x] = "L"

    if lines == new_lines:
        break

    lines = new_lines

count = 0
for y in range(len(new_lines)):
    for x in range(len(new_lines[0])):
        if lines[y][x] == "#":
            count += 1
success(count)
