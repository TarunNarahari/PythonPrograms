filehandle = open("Sales2.txt","w")
def convert(filename):
    items = []
    menuitems = {}
    filehandle = open(filename,"r")
    for line in filehandle.readlines():
        items= line.split(" - ")
        menuitems[items[0]]=items[1].replace("\n","")
    return menuitems
    
def getorder(filename):
    items = []
    filehandle = open(filename,"r")
    for line in filehandle.readlines():
        line = line.replace("\n","")
        items.append(line)
        
    return items

def total():
    order = getorder("Orders.txt")
    menu = convert("Menu.txt")
    subtotal = 0.00
    for items in order:
        subtotal = subtotal + float(menu[items])
    return subtotal 
        
    
    
    
    
    
print(total())