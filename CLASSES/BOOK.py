class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f"Book: {self.title}, Author: {self.author}")

# Usage
my_book = Book("Python Basics", "John Doe")
my_book.display()
