number = input("Enter an integer : ")
number = int(number)
if(number>0 and number<=100):
    print("The number is between 0 and 100")
elif(number>= 101 and number<=999):
    print("The number is between 101 and 999")
elif(number >=1000 and number<=1999):
    print("The number is between 1000 and 1999")
else:
    print("The number is between 2000 and infinity")
    
