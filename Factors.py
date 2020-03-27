def findfactor(x,y):
    count = 0
    Factor_list=[]
    if(x<y):
        smallnum=x
    else:
        smallnum=y
    while(count<=smallnum):
        count = count + 1
        if(x%count==0 and y%count==0):
            Factor_list.append(count)
    return Factor_list    
            
abc = findfactor(10,20)
print (abc)

    