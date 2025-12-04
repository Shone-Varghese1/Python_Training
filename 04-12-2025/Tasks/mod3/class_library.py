# 22. Create a Library class to store books and a method to search by title or author.

class Library:
    def __init__(self):
        self.books=[]
    def add_book(self,title,author):
        self.books.append((title,author))
        print("added book")
    def find_book_title(self,title):
        for book in self.books:
            if book[0]==title:
                return f"{book[1]} - {book[2]}"
        return None
    def find_book_author(self,author):
        book1=[]
        for book in self.books:
            if book[1]==author:
                book1.append((book[0]))
        return book1 if len(book1)>0 else None
    def print_books(self):
        for book in self.books:
            print(f"{book[0]} - {book[1]}")
b1=Library()
b1.add_book("alchemist","paulo coehlo")
b1.add_book("murder in the orient express","agatha christie")
b1.add_book("wings of fire","APJ abdul kalam")
b1.add_book("and then there were none","agatha christie")
b1.print_books()
print(b1.find_book_author("paulo coehlo"))
print(b1.find_book_author("agatha christie"))
