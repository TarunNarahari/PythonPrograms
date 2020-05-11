filehandle = open("books.txt","r")
readlines = filehandle.readlines()
print (readlines)

filehandle.close()

newfile = open("newfile.txt","w")
readlines = (readlines[::-1])
for lines in readlines:
    newfile.write(lines )
newfile.close()