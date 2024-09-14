class Author:
    def __init__(self, name, birthday=None, nationality=None):
        self.name = name
        self.books = {}
        self.birthday = birthday
        self.nationality = nationality

    def to_dict(self):
        return {
            'name': self.name,
            'books': self.books,
            'birthday': self.birthday,
            'nationality': self.nationality
        }
