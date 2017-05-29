# Who remembers back to their time in the schoolyard, when girls would take a flower and tear its petals, saying each of the following phrases each time a petal was torn:
#
# I love you
# a little
# a lot
# passionately
# madly
# not at all

def how_much_i_love_you(nb_petals):
    n = nb_petals % 6
    if n == 1:
        return "I love you"
    if n == 2:
        return "a little"
    if n == 3:
        return "a lot"
    if n == 4:
        return "passionately"
    if n == 5:
        return "madly"
    if n == 0:
        return "not at all"


        
