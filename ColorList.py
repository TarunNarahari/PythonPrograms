color_list_1 = ["blue","black"]
color_list_2 = ["black"]
output_list = []

for color in color_list_1:
    if(color  in color_list_2):
        a=1
    else:
        output_list.append(color)

print (output_list)
