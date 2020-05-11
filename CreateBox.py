row = int(input("How many rows of boxes should your board have"))
column = int(input("How many columns of boxes should your board have"))
def createboard(row,col):
    count = 1
    number = 1
    
        
    for num in range(row):
        #first print the dahes
        for dash in range(col-1):
            print (" ---",end =" ")
        else:
            print(" ---")
        
        #Next print the Vertical lines
        for dash in range(col):
            print ("|   ",end =" ")
        else:
            print("|")
    for dash in range(col-1):
        print (" ---",end =" ")
    else:
        print(" ---")
           
            
            
                
        
createboard(row,column)
            