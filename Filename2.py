def beforedot(filename):
    count = 0
    while(count>=0):
        count = count + 1
        if(filename[count]== "."):
            return ("The filename is %s" % filename[:count])
def afterdot(filename):
    count = 0
    while(count>=0):
        count = count + 1
        if(filename[count]== "."):
            return ("The file index is %s" % (filename[count+1:]))

print (beforedot("java.ppt"))
print (afterdot("java.ppt"))