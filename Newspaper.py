filehandle = open("newspaper.txt","w")
filehandle.write("Big ETF\n")
filehandle.write("First Aim\n")
filehandle.write("For Strict\n")
filehandle.write("Labeling\n")
filehandle.close()

filehandle1= open("newspaper.txt","r")
numline = 0
words = []
character = 0
for line in filehandle1.readlines():
    for char in line:
        character = character +1
        line = line.replace("\n","")
    words= words + line.split(" ")
    numline = numline + 1
print ("The number of lines are: %d" % (numline))
print ("The number of words are: %d" % (len(words)))
print ("The number of characters are: %d" % (character))