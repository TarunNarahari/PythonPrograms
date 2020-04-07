word = input("Please enter a word")
vowels = ["a","e","i","o","u"]
def count(x):
    num = 0
    for letter in x:
        if(letter.lower() in vowels):
            num = num + 1
    return num
print (count(word))
        