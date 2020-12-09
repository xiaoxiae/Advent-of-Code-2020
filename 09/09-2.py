import sys

sys.path.insert(0, "../")
from utilities import success, get_input

instructions = get_input(as_int=True)

numbers = []
preamble = 25


def adds_up_to(target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return True
    return False


def find_continuous_sum(target):
    for i in range(len(instructions)):
        for j in range(i + 1, len(instructions)):
            if sum(instructions[i:j]) == target:
                success(min(instructions[i:j]) + max(instructions[i:j]))


for n in instructions[:preamble]:
    numbers.append(n)

for n in instructions[preamble:]:
    if not adds_up_to(n):
        find_continuous_sum(n)

    numbers.pop(0)
    numbers.append(n)
