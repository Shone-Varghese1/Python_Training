# 26. Create a class Book with title, author, pages. Add method to check if pages > 300.
class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def check_pages(self):
        if self.pages>300:
            print("pages more than 300")
        else:
            print("pages less than 300")
b1=Book("Alchemist","paulo",325)
b1.check_pages()
b2=Book("placeholder","placeholder2",250)
b2.check_pages()