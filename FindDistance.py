def distance(pointa, pointb):
    length = ((pointb[0]-pointa[0])**2 + (pointb[1]-pointa[1])**2)**0.5
    return length
print (distance([3,4], [3,6]))