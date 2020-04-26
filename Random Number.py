import random
number = random.randint(1,10)
print(number)
guessnumber = int(input("Guess a number between 1-9"))
def check(realnum,hyponum):
    if(hyponum<realnum):
        print("You are low")
    elif(hyponum>realnum):
        print("You are high")
    else:
        print("You guessed the number correctly")
check(number,guessnumber)
