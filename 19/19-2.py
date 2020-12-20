import sys

sys.path.insert(0, "../")
from utilities import success, get_input
from typing import *

from itertools import product

input = get_input()

rules = {}


def matches_rule(string: str, rule: int):
    """Return the remainder of the string if it starts to match a rule, else None."""
    if isinstance(rules[rule], str):
        if string.startswith(rules[rule]):
            yield [string[len(rules[rule]) :]]
        else:
            yield [None]
    else:
        # one of those has to match
        s_total = []
        for option in rules[rule]:
            s = [string]  # the initial string

            # these have to match in this order
            for subrule in option:
                new_s = []  # new possible string endings

                for st in s:
                    for continuation in matches_rule(st, subrule):
                        new_s += [r for r in continuation if r is not None]

                s = new_s

            s_total += new_s

        yield s_total


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

rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]

total = 0
for line in input[i + 1 :]:
    for item in list(matches_rule(line, 0))[0]:
        if item == "":
            total += 1
            break

success(total)
