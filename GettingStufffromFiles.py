filehandle = open("Sales3.txt","w")
def convertfromfiletodict(filename):
    items = []
    menuitems = {}
    filehandle = open(filename,"r")
    for food in filehandle.readlines():
        items= food.split(" - ")
        menuitems[items[0]]=items[1].replace("\n","")
    return menuitems
def getorder(filename):
    items = []
    filehandle = open(filename,"r")
    for line in filehandle.readlines():
        line = line.replace("\n","")
        items.append(line)
    return items
        
def subtotal():
    order = getorder("Orders.txt")
    menu = convertfromfiletodict("Menu.txt")
    total = 0.00
    for items in order:
        filehandle.write(items + ": " + (menu[items]) + ("\n") )
        total = total + float(menu[items])
    return total
filehandle.write("Your order comes out to $%d" % (subtotal()))
filehandle.close()

            
