import sys

sys.path.insert(0, "../")
from utilities import success, get_input
from typing import *

from itertools import product

input = get_input(whole=True)

images = set()

for image in input.split("\n\n"):
    id = int(image.split("\n")[0].split(" ")[1].strip(":"))

    images.add((id, tuple(image.split("\n")[1:])))


def yield_symmetric_images(image):
    """Yield the possible rotations of the image."""
    for h in (True, False):  # horizontal
        for v in (True, False):  # vertical
            for d in (True, False):  # diagonal
                new_image = list(image)

                if v:
                    new_image = list(reversed(new_image))

                if h:
                    new_image = [row[::-1] for row in new_image]

                if d:
                    new_image = [
                        "".join([new_image[c][r] for c in range(len(new_image))])
                        for r in range(len(new_image))
                    ]

                yield tuple(new_image)


def down(i1, i2):
    """Return True if the image i2 can be below i1."""
    return i1[-1] == i2[0]


def right(i1, i2):
    """Return True if the image i2 can be to the right of i1."""
    return "".join([i1[row][-1] for row in range(len(i1))]) == "".join(
        [i2[row][0] for row in range(len(i2))]
    )


def fill(square, images, current: int):
    if current == len(square) ** 2:
        return square

    x, y = current % len(square), current // len(square)

    for id, image in images:

        for symmetric_image in yield_symmetric_images(image):

            # if we can add it
            if (y == 0 or down(square[y - 1][x][1], symmetric_image)) and (
                x == 0 or right(square[y][x - 1][1], symmetric_image)
            ):

                # if square[0][0] is not None and square[0][0][0] == 1951:
                #    print(symmetric_image)

                square[y][x] = (id, symmetric_image)
                res = fill(square, images - {(id, image)}, current + 1)

                if res != None:
                    return res

                square[y][x] = None


def contains_monster(waters, x, y, monster):
    for yd, row in enumerate(monster):
        for xd, char in enumerate(row):
            if char == " ":
                continue

            if waters[y + yd][x + xd] != "#":
                return False
    return True


def count_monsters(waters):
    monster = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]

    w, h = len(monster[0]), len(monster)

    total = 0
    for y in range(len(waters) - h):
        for x in range(len(waters[0]) - w):
            if contains_monster(waters, x, y, monster):
                total += 1

    return total


side = int(len(images) ** (1 / 2))

result = fill([[None] * side for _ in range(side)], images, 0)

water_side = side * (len(result[0][0][1]) - 2)

waters = ["" for _ in range(water_side)]

for i, a in enumerate(result):
    for id, b in a:
        for j, row in enumerate(b[1:-1]):
            waters[i * (len(result[0][0][1]) - 2) + j] += row[1:-1]

for i in yield_symmetric_images(waters):
    result = count_monsters(i)

    if result != 0:
        total = 0
        for row in waters:
            for c in row:
                if c == "#":
                    total += 1

        # assume they don't overlap
        success(total - 15 * result)

