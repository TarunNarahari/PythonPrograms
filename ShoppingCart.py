class ShoppingCart:
    cart = {}
    def __init__(self,name):
        self.name = name
    def add(self,product,price):
        if(product not in self.cart):
            self.cart[product]=price
        else:
            print("%s is already in the cart" % (product))
    def remove(self,product):
        if(product in self.cart):
            del self.cart[product]
        else:
            print("%s is not in the cart" % (product))
            
    def total(self):
        count = len(self.cart)
        print ("The number of items in the cart are %d" % (count))
        sum = 0
        for item in self.cart:
            sum = sum + self.cart[item]
        print ("The total is $%d" % (sum))
    
my_cart = ShoppingCart("Tarun's Cart")
my_cart.add("Potato",1.00)
my_cart.add("Tomato",3.00)
my_cart.add("Tomato",3.00)
my_cart.remove("Tomato")
my_cart.add("chocolate chips",56)
print (my_cart.cart)
my_cart.total()

        
        