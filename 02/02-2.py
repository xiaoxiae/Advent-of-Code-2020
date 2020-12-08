import sys

sys.path.insert(0, "../")
from utilities import success, get_input

input = get_input()
total = 0

for value in input:
    a, b, password = value.split()
    i, j = map(int, a.split("-"))
    i -= 1
    j -= 1
    policy = b.strip(":")

    if (password[i] == policy or password[j] == policy) and password[i] != password[j]:
        total += 1

success(total)
