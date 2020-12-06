import sys

sys.path.insert(0, "../")
from utilities import success, get_input

input = get_input(whole=True)

total = 0
for line in input.split("\n\n"):
    total += len(set(c for c in line if c not in (" ", "\n")))

success(total)
