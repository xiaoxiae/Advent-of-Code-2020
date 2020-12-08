import sys
sys.path.insert(0, "../")
from utilities import success, get_input

input = get_input()
total = 0

for value in input:
    a, b, password = value.split()
    lo, hi = map(int, a.split("-"))
    policy = b.strip(":")

    if lo <= password.count(policy) <= hi:
        total += 1

success(total)
