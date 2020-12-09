import sys

sys.path.insert(0, "../")
from utilities import success, get_input

instructions = get_input(as_int = True)

numbers = []
preamble = 25

def adds_up_to(target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return True
    return False

for n in instructions[:preamble]:
    numbers.append(n)

for n in instructions[preamble:]:
    if not adds_up_to(n):
        success(n)

    numbers.pop(0)
    numbers.append(n)
