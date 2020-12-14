import sys

sys.path.insert(0, "../")
from utilities import success, get_input

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

        for i, c in enumerate(reversed(mask)):
            if c != "X":
                number = number & (ones ^ (1 << i)) | int(c) << i

        memory[index] = number

total = 0
for i in memory:
    total += memory[i]

success(total)
