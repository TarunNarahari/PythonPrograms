pi = 3.14
inputradius = input("Enter the radius: ")
if(inputradius.isnumeric() == True):
    print ("Radius : " + inputradius)
else:
    print ("Please enter a year")
    exit()
    
inputradius = int(inputradius)

def circumference(radius):
    return radius*2*pi

print ("Circumference: %d" % circumference(inputradius))

def volume(radius):
    return (radius**3)*(4/3*pi)

print ("Volume: %d" % volume(inputradius))

    
def area(radius):
    return (radius**2)*(pi)

print ("Area: %d" % (area(inputradius)))







    
