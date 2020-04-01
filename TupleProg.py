sample = input("Enter a comma seperated string")
def makelist(sample):
    output = "['"
    outputtuple = "('"
    count = 0
    while(count < len(sample)):
        if(sample[count]==  ","):
            output = output + "','"
            outputtuple = outputtuple + "','"
        else:
            output = output + sample[count]
            outputtuple = outputtuple + sample[count]
        count = count + 1
    output = output +"']"
    outputtuple = outputtuple + "')"
    print  (output)
    return  outputtuple
    
        

   

    

