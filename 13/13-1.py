import sys

sys.path.insert(0, "../")
from utilities import success, get_input

wait = int(get_input()[0])
times = get_input()[1].split(",")

minimum_time = float("+inf")
minimum_bus = 0

for time in times:
    if time == "x":
        continue

    time = int(time)

    if time - wait % time < minimum_time:
        minimum_time = time - wait % time
        minimum_bus = time

success(minimum_time * minimum_bus)

