import sys

sys.path.insert(0, "../")
from utilities import success, get_input

from itertools import product

memory = {}

mask = "X" * 36
ones = (1 << 36) - 1

for inst in get_input():
    opt, val = inst.split(" = ")

    if opt == "mask":
        mask = val
    else:
        index = int(opt.split("[")[1].strip("]"))
        number = int(val)
        floats = []

        for i, c in enumerate(reversed(mask)):
            if c != "X":
                if c == "1":
                    index = index & (ones ^ (1 << i)) | 1 << i
            else:
                floats.append(i)

        for p in product((0, 1), repeat=len(floats)):
            v = index

            for f, b in zip(floats, p):
                v = v & (ones ^ (1 << f)) | b << f

            memory[v] = number

total = 0
for i in memory:
    total += memory[i]

success(total)
