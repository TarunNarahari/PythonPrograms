letter = input("Enter a letter")
print (letter)
letter = letter.lower()
print (letter)
#if(letter == "a" or letter == "e" or letter == "i" or letter =="o" or letter=="u"):
if(letter in ["a","e","i","o","u"]):
    print("This letter is a vowel")
else:
    print("This letter is not a vowel")