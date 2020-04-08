import random
guess = int(input("Guess Rock, Paper, Scissors; Rock =0, Paper = 1 Scissors = 2"))
if(guess != 0 and guess != 1 and guess != 2):
    print ("Guess a number between 0-2")
computerguess = random.randint(0,2)
print ("The computer's guess is %d" % (computerguess))
if(guess == computerguess):
    print("It is a draw, click the play button again")
    
if(guess==0 and computerguess==1):
    print("Computer wins")
elif(guess==1 and computerguess==2):
    print("Computer wins!")
elif(guess==2 and computerguess==0):
    print("Computer wins!")
else:
    print("You win")







