# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 integers.
# No floats or empty arrays will be passed.
#
# For example, when an array is passed like [19,5,42,2,77], the output should be 7.
def sum_two_smallest_numbers(numbers):
    num = sorted(numbers)
    y = num[0]
    z = num[1]
    x = y+z

    return x
