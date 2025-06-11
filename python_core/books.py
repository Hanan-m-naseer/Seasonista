class book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
    
    def getBookInfo(self):
        print("The details of the book are:")
        print(f"Title:[{self.title}], Author:[{self.author}],Year:[{self.year}]")
        
book = book("Angry River","Ruskin Bond",1972)
book.getBookInfo()