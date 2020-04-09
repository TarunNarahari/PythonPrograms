board = [["_","_","_"],["_","_","_"],["_","_","_"]]
def displayboard(board):
    for row in board:
        print (" ".join(row))
displayboard(board)
def whowon():
    gameover = True
    if(board[0]== ["O","O","O"]):
        print("Player 1 wins")
    elif(board[0]== ["X","X","X"]):
        print("Player 2 wins")
    elif(board[1]== ["O","O","O"]):
        print("Player 1 wins")
    elif(board[1]== ["X","X","X"]):
        print("Player 2 wins")
    elif(board[2]== ["O","O","O"]):
        print("Player 1 wins")
    elif(board[2]== ["X","X","X"]):
        print("Player 2 wins")
    elif(board[0][0]=="O" and board[1][0]=="O" and board[2][0]=="O"):
        print("Player 1 wins")
    elif(board[0][0]=="X" and board[1][0]=="X" and board[2][0]=="X"):
        print("Player 2 wins")
    elif(board[0][1]=="O" and board[1][1]=="O" and board[2][1]=="O"):
        print("Player 1 wins")
    elif(board[0][1]=="X" and board[1][1]=="X" and board[2][1]=="X"):
        print("Player 2 wins")
    elif(board[0][2]=="O" and board[1][2]=="O" and board[2][2]=="O"):
        print("Player 1 wins")
    elif(board[0][2]=="X" and board[1][2]=="X" and board[2][2]=="X"):
        print("Player 2 wins")
    elif(board[0][0]== "O" and board[1][1]=="O" and board[2][2]== "O"):
        print("Player 1 wins")
    elif(board[0][0]== "X" and board[1][1]=="X" and board[2][2]== "X"):
        print("Player 2 wins")
    elif(board[0][2]== "O" and board[1][1]=="O" and board[2][0]== "O"):
        print("Player 1 wins")
    elif(board[0][2]== "X" and board[1][1]=="X" and board[2][0]== "X"):
        print("Player 2 wins")
    else:
        gameover=False
    return gameover

def pickaspot(playernumber):
    spacetaken=0
    while (spacetaken ==0):
        pickedrow = int(input("Player %d, guess a row between 0-2  " % playernumber))
        pickedcol = int(input("Player %d, guess a col between 0-2  " % playernumber))
        if(pickedrow >2 or pickedcol >2):
            print("Out of range, pick again")
        elif(board[pickedrow][pickedcol]!= "_"):
            print("This space is taken")
        else:
            if(playernumber== 1):
                board[pickedrow][pickedcol]= "O"
            else:
                board[pickedrow][pickedcol]= "X"
            spacetaken = 1
        displayboard(board)
    
def playgame():
    turn=0
    while(turn<9):
        pickaspot(turn%2+1)
        if(whowon()==True):
            break
        turn = turn + 1
    else:
        print("The game is a draw")
playgame()

        
        
        