class Library:
    shelves = []
    books = []
    bookpatron = {}
    
    def __init__(self,name,phonenumber):
        self.name = name
        self.phonenumber = phonenumber
    def addshelf(self,shelf):
        self.shelves.append(shelf)
        print (self.shelves)
        
    def addbook(self,book):
        self.books.append(book)
        print (self.books)
        
    def associateBookToPatron(self,book,patronname):
        
        if(book not in self.books):
            print ("We don't have the book")
        elif(book in self.bookpatron.keys()):
            print ("This book is already checked out")
        else:
            print ("You can check out the book")
            self.bookpatron[book]=patronname
            print (self.bookpatron)
    
    def mybooks(self,patronname):
        count =0
        for key in self.bookpatron.keys():
            if(patronname==self.bookpatron[key]):
                count = count+1
        print ("The number of books you have checked out is %d" % (count))
            
class Book:
    def __init__(self,title,author,genre,ID):
        self.title =title
        self.author = author
        self.genre = genre
        self.ISBN= ISBN
  
class Shelf:
    books = []
    def __init__(self,name):
        self.name = name
    def addbook(self,book):
        return 0
    def removebook(self,book):
        return 0
        
class Patron:
    def __init__(self,name):
        self.name = name
    def returnbook(self,book):
        return 0
    

bethany= Library("Bethany Library", 5036458889)
bethany.addshelf("a")
bethany.addshelf("b")
bethany.addshelf("c")
bethany.addbook("Harry Potter")
bethany.addbook("Lightening Thief")
bethany.addbook("Frankenstein")
tarun = Patron("Tarun Narahari")
murali = Patron("Murali Narahari")
bethany.associateBookToPatron("Harry Potter","Tarun Narahari")
bethany.associateBookToPatron("Harry Potter","Murali Narahari")
bethany.mybooks("Tarun Narahari")
bethany.mybooks("Murali Narahari")
