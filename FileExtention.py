def findname(filename):
    count = 0
    while(count<len(filename)):
        if(filename[count]=="."):
          return (filename[count+1:])
        count = count + 1
        


print (findname("a.java"))
        