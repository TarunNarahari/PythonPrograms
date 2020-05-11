filehandle = open("books.txt","r")
count = 0
wcount = 0
for line in filehandle.readlines():
    count = count + 1
    for word in line.split():
        wcount = wcount + 1
print (count)
print (wcount)

filehandle.close()

total = open("total.txt","w")
total.write("The number of lines is: %d. \n" % (count))
total.write("The number of words is: %d .\n" % (wcount))
total.close()