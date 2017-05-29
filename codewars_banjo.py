# Create a function which answers the question "Are you playing Banjo?". If your name starts with the letter "R" or lower case "r", you are playing Banjo!

#The function takes a name as its only argument, and returns one of the following strings:

def areYouPlayingBanjo(name):
    for i in name:
        if i =='R' or i=='r':
            return name+ " "+"plays banjo"
        else:
            return name+" does not play banjo"
