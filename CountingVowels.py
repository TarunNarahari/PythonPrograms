word = input("Please enter a word")
vowels = ["a","e","i","o","u"]
def count(x):
    amount = 0
    for letter in x:
        if(letter.lower() in vowels):
            amount = amount + 1
    return amount
print ("The number of vowels are %d" % (count(word)))