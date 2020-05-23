from urllib.request import urlopen
story = urlopen("http://sixty-north.com/c/t.txt")
filehandle = open("Website.txt","w")
for line in story:
    line = line.decode("utf-8")
    filehandle.write(line)
filehandle.close()