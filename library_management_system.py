class Library:
    def __init__(self):
       self.noBooks=0
       self.books=[]
    def addBook(self,book):
        self.books.append(book)
        self.noBooks=len(self.books)
    def showInfo(self):
        print(f"The Library has {self.noBooks} books, and the books are: ")
        for book in self.books:
            print(book)
l1=Library()
l1.addBook("Harry Potter")
l1.addBook("The Alchemist")
l1.addBook("Rich Dad Poor Dad")
l1.addBook("Atomic Habits")
l1.addBook("Wings of Fire")
l1.showInfo()


