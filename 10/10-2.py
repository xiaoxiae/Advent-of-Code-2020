import sys

sys.path.insert(0, "../")
from utilities import success, get_input


def fill_ones(ones):
    """Too lazy to do a proper function :)."""
    if ones in (0, 1):
        return 1
    elif ones == 2:
        return 2
    elif ones == 3:
        return 4
    elif ones == 4:
        return 7


inst = sorted(get_input(as_int=True))

deltas = [1]

for i in range(len(inst) - 1):
    deltas.append(inst[i + 1] - inst[i])

deltas.append(3)

total = 1
ones = 0
for i in range(len(deltas)):
    if deltas[i] == 1:
        ones += 1
    else:
        total *= fill_ones(ones)
        ones = 0

success(total)
