import sys

sys.path.insert(0, "../")
from utilities import success, get_input

numbers = list(map(int, get_input(whole=True).split(",")))

positions = {}

for i, n in enumerate(numbers):
    positions[n] = [i]

n = 0
i = len(numbers)

while i < 30000000 - 1:
    if n not in positions:
        positions[n] = [i]
    else:
        positions[n].append(i)

    if len(positions[n]) == 1:
        n = 0
    else:
        n = positions[n][-1] - positions[n][-2]

    i += 1

success(n)
