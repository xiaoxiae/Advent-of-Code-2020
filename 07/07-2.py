import sys

sys.path.insert(0, "../")
from utilities import success, get_input

input = get_input()

bags = {}
for line in input:
    bag, spec = line.split(" bags contain ")

    for other in spec.split(", "):
        other = other.strip(".").strip("bag").strip("bags").strip()

        if other == "no other":
            bags[bag] = {}
        else:
            if bag not in bags:
                bags[bag] = {}

            count, o = other.split(" ", 1)

            bags[bag][o] = count


def recursive_sum(bag):
    if len(bags[bag]) == 0:
        return 0

    total = 0
    for b, i in bags[bag].items():
        total += recursive_sum(b) * int(i) + int(i)
    return total


success(recursive_sum("shiny gold"))
