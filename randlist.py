import random
def randomlist():
    newlist = []
    count = 0
    for i in range(5):
        newlist.append(random.randint(1,5))
        count +=1
    return(newlist,count)
