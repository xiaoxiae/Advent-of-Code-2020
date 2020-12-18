import sys

sys.path.insert(0, "../")
from utilities import success, get_input

from itertools import product

input = get_input()


def evaluate(expression):
    operators = {
        "+": [lambda a, b: a + b, 1],
        "*": [lambda a, b: a * b, 1],
    }

    number_stack = []
    operator_stack = []

    for term in expression:
        if term.isdigit():
            number_stack.append(int(term))

        elif term == "(":
            operator_stack.append("(")

        elif term == ")":
            while operator_stack[-1] in operators:
                operator = operators[operator_stack.pop()][0]

                b, a = number_stack.pop(), number_stack.pop()
                number_stack.append(operator(a, b))

            operator_stack.pop()

        elif term in operators:
            operator = operators[term]

            while len(operator_stack) > 0 and operator_stack[-1] in operators:
                if operators[operator_stack[-1]][1] >= operator[1]:
                    operator = operators[operator_stack.pop()][0]

                    b, a = number_stack.pop(), number_stack.pop()
                    number_stack.append(operator(a, b))
                else:
                    break

            operator_stack.append(term)

    while len(operator_stack) != 0:
        operator = operators[operator_stack.pop()][0]

        b, a = number_stack.pop(), number_stack.pop()
        number_stack.append(operator(a, b))

    return number_stack[0]

def tokenize(line):
    return " ( ".join(((" ) ".join(line.split(")"))).split("("))).split()

success(sum(evaluate(tokenize(line)) for line in input))
