# Create a function that returns the average of an array of numbers ("scores"), rounded to the nearest whole number. You are not allowed to use any loops (including for, for/in, while, and do/while loops).

def average(x):
    b = x
    a = len(b)


    y = sum(b)

    x = y/a
    return int(round(x))
