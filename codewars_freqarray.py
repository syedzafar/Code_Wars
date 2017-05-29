# Write a program to find count of the most frequent item of an array.
#
# Assume that input is array of integers.
def most_frequent_item_count(collection):
    l = 0
    for x in list(collection):
        count = collection.count(x)
        if count > l:
            l = count
    return l
