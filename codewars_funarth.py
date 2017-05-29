# Given two numbers and an arithmetic operator (the name of it, as a string), return the result of the two numbers having that operator used on them.
#
# a and b will both be positive integers, and a will always be the first number in the operation, and b always the second.
#


def arithmetic(a, b, op):

    if op == "add":
        return a+b
    if op == 'subtract':
        return a-b
    if op == 'divide':
        return a/b
    if op == 'multiply':
        return a*b
