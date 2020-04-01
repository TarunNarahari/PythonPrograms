def findname(filename):
    count = 0
    while(count>=0):
        count = count + 1
        if(filename[count]== "."):
            return (filename[:count])
print (findname("kldsfs.py"))