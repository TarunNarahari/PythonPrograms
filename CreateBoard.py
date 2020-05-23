def createboard(row,col):
    counter= 1
    for number in range(row):
        for dashes in range(col-1):
            print(" ---",end= " ")
        else:
            print (" ---")
     
        for num in range(col):
            print("| %d "%(counter) ,end = " ")
            counter = counter + 1
        else:
            print("|")
    
    
    
    for dashes in range(col):
        print(" ---", end = " ")
            
createboard(3,3)