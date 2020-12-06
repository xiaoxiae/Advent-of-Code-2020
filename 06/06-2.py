import sys

sys.path.insert(0, "../")
from utilities import success, get_input

from string import ascii_lowercase

input = get_input(whole=True)

total = 0
for group in input.split("\n\n"):
    all_yes = set(c for c in ascii_lowercase)
    for line in group.split("\n"):
        all_yes = all_yes.intersection(set(c for c in line if c not in (" ")))
    total += len(all_yes)

success(total)
