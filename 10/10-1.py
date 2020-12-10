import sys

sys.path.insert(0, "../")
from utilities import success, get_input

inst = sorted(get_input(as_int = True))

one_jolt = 1
three_jolt = 1

for i in range(len(inst) - 1):
    if inst[i + 1] - inst[i] == 1:
        one_jolt += 1
    else:
        three_jolt += 1

success(one_jolt * three_jolt)

