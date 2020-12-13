import sys

sys.path.insert(0, "../")
from utilities import success, get_input

wait = int(get_input()[0])
times = get_input()[1].split(",")


def get_extended_gcd(a, b):
    """https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm"""
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


def get_lcm(a, b):
    gcd, _, _ = get_extended_gcd(a, b)
    return abs((a * b) // gcd)


equations = []
base = int(times[0])
for i in range(1, len(times)):
    time = times[i]

    if time == "x":
        continue

    time = int(time)

    _, x, y = get_extended_gcd(base, time)
    lcm = get_lcm(base, time)

    equations.append((lcm, -base * x * i))

while len(equations) != 1:
    e2, e1 = equations.pop(), equations.pop()

    a, b, s = e1[0], -e2[0], -(e1[1] - e2[1])

    gcd, x, y = get_extended_gcd(a, b)

    a //= gcd
    b //= gcd
    s //= gcd

    j = -1
    while True:
        if (b * j + s) % a == 0 and (b * j + s) // a > 0:
            break

        j -= 1

    i = (b * j + s) // a

    lcm = get_lcm(a, b)

    equations.append((lcm, gcd * a * i + e1[1]))

success(equations[0][1])
