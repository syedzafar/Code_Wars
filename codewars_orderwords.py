# Given a string, you need to write a method that order every letter in this string in ascending order.
#
# Also, you should validate that the given string is not empty or null. If so, the method should return:

def order_word(s):
    if s =='':
        return 'Invalid String!'
    elif s == None:
        return 'Invalid String!'
    return "".join(sorted(s))
