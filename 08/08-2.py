import sys

sys.path.insert(0, "../")
from utilities import success, get_input

instructions = get_input()


for i in range(len(instructions)):
    acc = 0
    ptr = 0

    visited = set()

    while True:
        if ptr == len(instructions):
            success(acc)

        if ptr in visited:
            break

        visited.add(ptr)

        opt, arg = instructions[ptr].split(" ")

        if i == ptr:
            if opt == "jmp":
                opt = "nop"
            else:
                opt = "jmp"


        if opt == "acc":
            acc += int(arg)
        elif opt == "jmp":
            ptr += int(arg)
            continue

        ptr += 1


