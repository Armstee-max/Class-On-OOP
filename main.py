class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def display(self):
        print(f"Player name: {self.name} and Player Level: {self.level}") 




player1 = Player("Gabriel", "TT")
player2 = Player("John", "RR")

player1.display()
player2.display()


# LIBRARY
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


class Library:
    def __init__(self, name):
        self.name = name
        self.book = []

    def add_book(self, book):
        self.book.append(book)

    def show_book(self):
        print(f"Book in: {self.name}")
        for book in self.book:
            print(f"Book Title: {book.title} by {book.author}")


library = Library("My Library")

book1 = Book("Othello", "Williams Shakespear")
book2 = Book("Things Fall Apart", "Gabriel")

library.add_book(book1)
library.add_book(book2)

library.show_book()

        