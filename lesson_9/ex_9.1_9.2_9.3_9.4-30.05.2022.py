class BookLibrary:
    def __init__(self, name, color, author, page):
        self.name = name
        self.color = color
        self.author = author
        self.page = page


    def pages(self):
        return ((self.page))


    def books(self):
        return "It's a cool book"


x = BookLibrary('bad', 'red', 'Remark', 11)

print(x.pages())
x.pages()