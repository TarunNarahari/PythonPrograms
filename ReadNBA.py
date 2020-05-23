from urllib.request import urlopen
story = urlopen("http://sixty-north.com/c/t.txt")
for line in story:
    print (line)
    
story.close()