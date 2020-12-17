import sys

sys.path.insert(0, "../")
from utilities import success, get_input

numbers = list(map(int, get_input(whole=True).split(",")))

def rfind(numbers, n):
    for i in reversed(range(len(numbers))):
        if numbers[i] == n:
            return i
    return len(numbers)


while len(numbers) < 2020:
    numbers.append(len(numbers) - 1 - rfind(numbers[:-1], numbers[-1]))

success(numbers[-1])
