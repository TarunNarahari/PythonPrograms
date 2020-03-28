def findlcm(x,y):
    times = 0
    while(times>=0):
        times = times  + 1
        if(y==0 or x==0):
            return "invalid"
        elif((x*times)%y==0):
            return (x*times)
            

print (findlcm(0,6))

    