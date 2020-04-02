def findamount(principle, interest, years):
    interest = 1 + interest/100
    return  (principle)*(interest**years)

print (findamount(1000,5,2))