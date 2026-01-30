class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f"Название: {self.title}, Автор: {self.author}, Год выпыска: {self.year}")
book1 = Book("Save the world", "Homeless", 1999)
book1.display_info()
book2 = Book("Save the world", "Homeless", 2005)
book2.display_info()