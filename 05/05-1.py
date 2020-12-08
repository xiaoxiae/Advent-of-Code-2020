import sys

sys.path.insert(0, "../")
from utilities import success, get_input

input = get_input()

m = 0

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

    m = max(m, row * 8 + col)

success(m)
