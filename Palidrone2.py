word = input("Enter your word")
def reverseword(x):
    newword= x[::-1]
    if(newword==x):
        print ("It is a palidrone")
    else:
        print ("It is not a palidrone")
        
reverseword(word)
    
