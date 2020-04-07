word = input("Enter word here")
def ispalidrone(string):
    string1= ""
    count = len(string)
    while(count > 0):
        count = count - 1
        string1 = string1 + string[count]
    print (string1)
    if(string1 == string):
        return "This is a palidrone"
    else:
        return "This is not a palidrone"
print (ispalidrone(word))