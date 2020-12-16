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

my_ticket = list(map(int, input[i + 2].split(",")))
tickets = []

for ticket in input[i + 5 :]:
    tickets.append(list(map(int, ticket.split(","))))


def is_valid(value, r=None):
    # possibly restrict only to a single rule
    for rule in rules if r is None else [r]:
        for lo, hi in rules[rule]:
            if lo <= value <= hi:
                return True
    return False


i = 0
while i < len(tickets):
    ticket = tickets[i]

    for value in ticket:
        if not is_valid(value):
            del tickets[i]
            break
    else:
        i += 1

# for the number of rules
assigned_rules = [None] * len(tickets[0])
for _ in tickets[0]:
    # examine each row, whether we can place it there
    for column in range(len(tickets[0])):
        possible = set(rule for rule in rules if rule not in assigned_rules)
        for row in range(len(tickets)):
            for rule in rules:
                if not is_valid(tickets[row][column], rule):
                    possible -= {rule}

        if len(possible) == 1:
            assigned_rules[column] = list(possible)[0]

prod = 1
for i, rule in enumerate(assigned_rules):
    if rule.startswith("departure"):
        prod *= my_ticket[i]

success(prod)
