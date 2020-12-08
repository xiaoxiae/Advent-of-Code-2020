import sys

sys.path.insert(0, "../")
from utilities import success, get_input

input = get_input()

ids = list()
for line in input:
    row = 0
    col = 0
    lo = 0
    hi = 128
    for c in line[:7]:
        avg = (lo + hi) // 2
        if c == "F":
            hi = avg
        else:
            lo = avg
    row = lo

    lo = 0
    hi = 8
    for c in line[7:]:
        avg = (lo + hi) // 2
        if c == "L":
            hi = avg
        else:
            lo = avg
    col = lo

    ids.append(row * 8 + col)

ids = sorted(ids)
for i in range(len(ids) - 1):
    if ids[i] != ids[i + 1] - 1:
        success(ids[i] + 1)
