performances = {'Ventriloquism':'9:00am', 
                'Snake Charmer': '12:00pm', 
                'Amazing Acrobatics': '2:00pm', 
                'Enchanted Elephants':'5:00pm'}
for show, time in performances.items():
    print (show + ":" + time,sep='::')