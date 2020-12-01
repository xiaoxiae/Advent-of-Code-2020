"""Various utility function for getting input/printing the solution/..."""
import sys


def success(text):
    color = 2
    print(f"\u001b[38;5;{color}mResult: \u001b[0m{text}")
    sys.exit()


def get_input(as_int=False):
    result = open("input", "r").read().strip().splitlines()

    if as_int:
        return list(map(int, result))
