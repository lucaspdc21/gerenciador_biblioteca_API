#TODO: função de linkar//deslinkar livro com autor
class Book:
    def __init__(self, title, **kwargs):
        self.title = title
        self.genre = kwargs.get("genre", None)
        self.year = kwargs.get("year", None)
        self.author_id = kwargs.get("author_id", None)
    
    def to_dict(self):
        return {
            title: self.title,
            genre: self.genre,
            year: self.year,
            author_id: self.author_id,
        }
    

# TODO: função de linkar//deslinkar artista com livro
class Author:
    def __init__(self, name, **kwargs):
        self.name = name
        self.books = kwargs.get("books", [])
        self.birthday = kwargs.get("birthday", None)
        self.nationality = kwargs.get("nationality", None)
    
    def to_dict(self):
        return {
            name: self.name,
            books: self.books,
            birthday: self.birthday,
            nationality: self.nationality,
        }