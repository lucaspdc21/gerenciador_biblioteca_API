class Author:
    def __init__(self, name, birthday=None, nationality=None):
        self.name = name
        self.books = {}
        self.birthday = birthday
        self.nationality = nationality

    def to_dict(self):
        books = {}
        for book_id, book in self.books.items():
            books[book_id] = book.to_dict()
        return {
            'name': self.name,
            'books': books,
            'birthday': self.birthday,
            'nationality': self.nationality
        }
