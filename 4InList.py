def count_four(list):
    count =0
    for number in list:
        if(number==4):
            count = count +1
    return count
        
    
print (count_four([1,23,3,5,4,4]))
print (count_four([4,23,3,5,4,4]))

