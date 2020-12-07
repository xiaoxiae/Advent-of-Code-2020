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

target = "shiny gold"

def contains_target(bag):
    if target in bags[bag]:
        return True

    return any(contains_target(b) for b in bags[bag])

count = 0
for bag in bags:
    if contains_target(bag):
        count += 1

success(count)
