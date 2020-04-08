list1= [1,2,3]
list2=[2,5,4]




def union(list1, list2):
    list3 = []
    for num in list1:
        list3.append(num)
    for num in list2:
        if(num not in list3):    
            list3.append(num)
    return list3

def findintersection(list1,list2):
    intersection = []
    for num in list1:
        if(num in list2):
            intersection.append(num)
    return intersection


def subtract(list1,list2):
    subtract1=[]
    for num in list1:
        if(num not in list2):
            subtract1.append(num)
    return subtract1


print (union(list1,list2))
print (findintersection(list1,list2))
print (subtract(list1,list2))
print (subtract(list2,list1))
print (subtract(list2,list1))



print 
