def multiply(x):
    total = 0
    count  = 0
    while(count<3):
        count = count +1
        total = total + (x**count)
    return total
print (multiply(5))