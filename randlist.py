import random
def randomlist():
    newlist = []
    for i in range(5):
        newlist.append(random.randint(1,5))
    return(newlist)
