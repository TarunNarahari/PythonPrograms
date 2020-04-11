number = int(input("Enter a number"))
def findfactors(principle):
    factors = []
    count = 1
    while(count<=(principle*0.5)):
        if(principle%count==0):
            factors.append(count)
        count = count + 1
    return factors
print(findfactors(number))
            
        