import sys

sys.path.insert(0, "../")
from utilities import success, get_input

instructions = get_input()

acc = 0
ptr = 0

visited = set()

while True:
    if ptr in visited:
        success(acc)
    visited.add(ptr)

    opt, arg = instructions[ptr].split(" ")

    if opt == "acc":
        acc += int(arg)
    elif opt == "jmp":
        ptr += int(arg)
        continue

    ptr += 1


