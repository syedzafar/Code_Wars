# Write a reverseWords function that accepts a string a parameter, and reverses each word in the string. Every space should stay, so you cannot use words from Prelude.
def reverse_words(word):
    new_word = word.split(' ')
    x = new_word[::-1]

    for char in x:
        b = ' '.join(x[::1])
        y = b[::-1]
        return y
