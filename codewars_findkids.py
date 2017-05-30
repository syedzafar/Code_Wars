# Where is my parent!?(cry)
#
# Mothers arranged dance party for children in school.On that party there are only mothers and their children.All are having great fun on dancing floor when suddenly all lights went out.Its dark night and no one can see eachother.But you were flying nearby and you can see in the dark and have ability to teleport people anywhere you want.
#
# Legend:
#
# -Uppercase letters stands for mothers,lowercase stand for their children. I.E "A" mothers children are "aaaa".
# -Function input:String contain only letters,Uppercase letters are unique.
# Task:
#
# Place all people in alphabetical order where Mothers are followed by their children.I.E "aAbaBb" => "AaaBbb".
#

def find_children(dancing):


    # x = sorted(dancing, key=lambda L: (L.upper(), L))
    # print ''.join(x)
    #

    x = sorted(dancing)    #['A', 'B', 'a', 'b']
    arr = []
    for u in x:
        if u.isupper() == True:
            arr.append(u)
            print arr
            for l in x:
                if l == u.lower():
                    arr.append(l)
                    print arr
    return ''.join(arr)






print find_children("aAbaBb")
