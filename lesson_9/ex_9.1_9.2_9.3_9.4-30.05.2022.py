class BookLibrary:
    def __init__(self, name, color, author, page):
        self.name = name
        self.color = color
        self.author = author
        self.page = page

    @staticmethod
    def good_book():
        print("It's a cool book")


    @classmethod
    def type_of_book(cls, name, color, author, page):
        return cls(name, color, author, page)




book1 = BookLibrary("ray", 'black', 'tolstoj', 150)

print(book1.name)
book1.good_book()




