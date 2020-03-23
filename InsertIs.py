def insertis(word):
    if(word[:2].lower()== "is"):
        return word
    else:
        return ("is"+ word)

print (insertis("Isael")) 
    