# Your goal in this kata is to implement an difference function, which subtracts one list from another.
#
# It should remove all values from list a, which are present in list b.


def array_diff(a, b):
    x = []
    for diff in a:
        if diff not in b:
            x.append(diff)
    return x
