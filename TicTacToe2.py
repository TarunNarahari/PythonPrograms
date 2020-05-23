tictactoe= [["_","_","_"],["_","_","_"],["_","_","_"]]
def showboard(board):
    for row in board:
        print(" ".join(row))
        
showboard(tictactoe)
        
def winner():
    champion = True
    if(tictactoe[0]== ["O","O","O"]):
        print("Player 1 wins")
    elif(tictactoe[0]== ["X","X","X"]):
        print("Player 2 wins")
    elif(tictactoe[1]== ["O","O","O"]):
        print("Player 1 wins")
    elif(tictactoe[1]== ["X","X","X"]):
        print("Player 2 wins")
    elif(tictactoe[2]== ["O","O","O"]):
        print("Player 1 wins")
    elif(tictactoe[2]== ["X","X","X"]):
        print("Player 2 wins")
    elif(tictactoe[0][0]== "O" and tictactoe[1][0]=="O" and tictactoe[2][0] == "O"):
        print("Player 1 wins")
    elif(tictactoe[0][0]== "X" and tictactoe[1][0]=="X" and tictactoe[2][0] == "X"):
        print("Player 2 wins")
    elif(tictactoe[0][1]== "O" and tictactoe[1][1]=="O" and tictactoe[2][1] == "O"):
        print("Player 1 wins")
    elif(tictactoe[0][1]== "X" and tictactoe[1][1]=="X" and tictactoe[2][1] == "X"):
        print("Player 2 wins")
    elif(tictactoe[0][2]== "O" and tictactoe[1][2]=="O" and tictactoe[2][2] == "O"):
        print("Player 1 wins")
    elif(tictactoe[0][2]== "X" and tictactoe[1][2]=="X" and tictactoe[2][2] == "X"):
        print("Player 2 wins")
    elif(tictactoe[0][0]== "O" and tictactoe[1][1]=="O" and tictactoe[2][2]== "O"):
        print("Player 1 wins")
    elif(tictactoe[0][0]== "X" and tictactoe[1][1]=="X" and tictactoe[2][2]== "X"):
        print("Player 2 wins")
    elif(tictactoe[0][2]== "O" and tictactoe[1][1]=="O" and tictactoe[2][0]== "O"):
        print("Player 1 wins")
    elif(tictactoe[0][2]== "X" and tictactoe[1][1]=="X" and tictactoe[2][0]== "X"):
        print("Player 2 wins")
    else:
        champion=False
    return champion

def play(playernumber):
    spacetaken=0
    while (spacetaken ==0):
        pickedrow = int(input("Player %d, guess a row between 0-2  " % playernumber))
        pickedcol = int(input("Player %d, guess a col between 0-2  " % playernumber))
        if(tictactoe[pickedrow][pickedcol]!= "_"):
            print("This space is taken")
        else:
            if(playernumber== 1):
                tictactoe[pickedrow][pickedcol]= "O"
            else:
                tictactoe[pickedrow][pickedcol]= "X"
            spacetaken = 1
        showboard(tictactoe)
        
def gameplay():
    turn=0
    while(turn<9):
        play(turn%2+1)
        if(winner()==True):
            break
        turn = turn + 1
    else:
        print("The game is a draw")



gameplay()
showboard(tictactoe)