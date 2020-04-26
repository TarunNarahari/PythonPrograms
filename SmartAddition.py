def smartaddition(x,y):
    if(type(x) == int and type(y)== int):
        return x+y
    elif(type(x) == str and type(y)== str):
        return x + y
    else:
        return "none"
print(smartaddition("5",6))