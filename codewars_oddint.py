# Given an array, find the int that appears an odd number of times.
#
# There will always be only one integer that appears an odd number of times.

def find_it(seq):
  for char in seq:
        if seq.count(char)%2!=0:
            return char
