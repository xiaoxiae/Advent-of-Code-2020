import sys

sys.path.insert(0, "../")
from utilities import success, get_input
from typing import *

from itertools import product

input = get_input()

rules = {}


def matches_rule(string: str, rule: int) -> Optional[str]:
    """Return the remainder of the string if it starts to match a rule, else None."""
    if isinstance(rules[rule], str):
        if string.startswith(rules[rule]):
            return string[len(rules[rule]) :]
        return None

    # one of those has to match
    for option in rules[rule]:
        s = string

        # these have to match in this order
        for subrule in option:
            s = matches_rule(s, subrule)

            if s is None:
                break
        else:
            return s

    return None


i = 0
while input[i] != "":
    line = input[i]

    rule, content = line.split(": ")

    if '"' in content:
        rules[int(rule)] = content.strip('"')
    else:
        rules[int(rule)] = list(
            map(lambda l: list(map(int, l.split())), content.split(" | "))
        )

    i += 1

total = 0
for line in input[i + 1 :]:
    if matches_rule(line, 0) == "":
        total += 1

success(total)
