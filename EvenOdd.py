number = input("Enter an integer : ")
if(number.isnumeric() == True):
    print ()
else:
    print ("Please enter an integer")
    exit()
    
input = int(number)

if(input%2==0):
    print ("This number is even")
else:
    print ("This number is odd")