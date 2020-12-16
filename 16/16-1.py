import sys

sys.path.insert(0, "../")
from utilities import success, get_input


input = get_input()

rules = {}

i = 0
while input[i] != "":
    rule, values = input[i].split(": ")
    rules[rule] = []

    for value in values.split(" or "):
        lo, hi = value.split("-")

        rules[rule].append((int(lo), int(hi)))

    i += 1

my_ticket = input[i + 2]
tickets = []

for ticket in input[i + 5 :]:
    tickets.append(list(map(int, ticket.split(","))))


def is_valid(ticket):
    for rule in rules:
        for lo, hi in rules[rule]:
            if lo <= value <= hi:
                return True
    return False


error = 0
for ticket in tickets:
    for value in ticket:
        if not is_valid(value):
            error += value

success(error)
