import sys
sys.path.insert(0, "../")
from utilities import success, get_input

input = get_input(as_int=True)

target = 2020
saw = set()
for i, v1 in enumerate(input):
    for v2 in input[i + 1:]:
        if target - v1 - v2 in saw:
            success(v1 * v2 * (target - v1 - v2))
    saw.add(v1)
