input_list = [2,4,5,6,5]
def evenodd(list):
    output_list = []
    for num in list:
        if(num==237):
            return output_list
        elif(num%2==0):
            output_list.append(num)
    return output_list
 
            
print (evenodd(input_list))