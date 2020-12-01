import sys
sys.path.insert(0, "../")
from utilities import success, get_input

input = get_input(as_int=True)

target = 2020
saw = set()
for value in input:
    if target - value in saw:
        success(value * (target - value))
    saw.add(value)
