#Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
# They are automatically called by many of Python's built-in operations.
# They allow developers to define or customize the behavior of objects

#def __init__ method is called when an object is created from a class (similar to constructor in other languages)

class Book:
    
    def __init__(self, title, author, num_pages):
      self.title = title
      self.author = author
      self.num_pages = num_pages

    def __str__(self):
       return f"{self.title} by {self.author}"
    
    def __eq__(self, other):
       return self.title == other.title and self.author == other.author
    def __lt__(self, other):
       return self.num_pages < other.num_pages
    def __gt__(self, other):
       return self.num_pages > other.num_pages
    
    def __add__(self, other):
       return f"{self.num_pages + other.num_pages} pages"
    
    def __contains__(self, keyword):
       return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
       if key == "title":
          return self.title
       elif key == "author":
          return self.author
       elif key == "num_pages":
          return self.num_pages

book1 = Book("The Hobbit", "J.R.R Tolkien", 310)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 296)
book3 = Book("1984", "George Orwell", 328)

print(book1['num_pages'])