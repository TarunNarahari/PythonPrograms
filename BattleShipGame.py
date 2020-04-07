import random
board = [["O","O","O","O","O"],["O","O","O","O","O"],["O","O","O","O","O"],["O","O","O","O","O"],["O","O","O","O","O"]]
def printboard(board):
    for row in board:
        row = " ".join(row)
        print (row)
printboard(board)
battlerow = random.randint(0,5)
battlecol = random.randint(0,5)
print (battlerow)
print (battlecol)


guess = 1
while(guess<6):
    guess = guess + 1
    guessrow = int(input("Guess a row"))
    guesscol = int(input("Guess a colomn"))
    if(guessrow==battlerow and guesscol==battlecol):
        print("You sank the ship")
        break
    elif(guessrow>=5 or guesscol>=5):
        print ("That's outside the map")
    elif(board[guessrow][guesscol]=="X"):
        print ("You've already guessed here")
    else:
        board[guessrow][guesscol]= "X"
        printboard(board)
else:
    print("You have lost the game")
        
        