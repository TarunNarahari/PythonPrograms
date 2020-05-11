filehandle = open('Sales.txt','w')


def write(order):
    
    total = 0.00
    for item,price in order.items():
        filehandle.write(item + format(price, ".2f")+ "\n")
        total = total + price
    filehandle.write("total is %d " % (total) + "\n")

    




write({'Lettuce' : 1.00, 'Tomato' : 2.00})
write({'Olives' : 1.00, 'potato' : 2.00})
filehandle.close()




        