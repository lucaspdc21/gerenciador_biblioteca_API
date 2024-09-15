from author import Author
from book import Book

class LibraryController:
    def __init__(self):
        self.books = {}
        self.authors = {}
        self.book_id_counter = 1
        self.author_id_counter = 1

    # Métodos GET
    # Retorna um dicionário com os dicionários de livros autores da biblioteca
    def list_root(self) -> dict:
        return {"books": self.list_books(), "authors": self.list_authors()}

    # Retorna um dicionário com todos os livros da biblioteca
    # (convertendo os objetos dos livros para dicionários)
    def list_books(self) -> dict:
        books = {}
        for id, book in self.books.items():
            books[id] = book.to_dict() # Converte o objeto do livro pra dicionário
        return books

    # Retorna um livro com id específico em forma de dicionário (null se não existe)
    def get_book(self, id: str) -> dict:
        book = self.books.get(id)
        if book is not None:
            return book.to_dict()
        else:
            return None; # o livro não existe
    
    # Retorna um dicionário com todos os autores da biblioteca
    # (convertendo os objetos dos autores para dicionários)
    def list_authors(self) -> dict:
        authors = {}
        for id, author in self.authors.items():
            authors[id] = author.to_dict()
        return authors
        
    
    # Retorna um autor com id específico em forma de dicionário (null se não existe)
    def get_author(self, id: str) -> dict:
        author = self.authors.get(id)
        if author != None:
            return author.to_dict()
        else:
            return None;

    # Retorna um dicionário com todos os livros de um autor específico
    def get_author_books(self, id: str) -> dict:
        if self.authors.get(id) is None:
            return None # se o autor não existir, ele retorna None
        
        authors_books = {}
        for book_id, book in self.authors[id].books.items():
            authors_books[book_id] = book.to_dict()
        return authors_books


    # Métodos POST
    # Adiciona um livro na biblioteca
    def create_book(self, data: dict) -> None:
        book = Book(data.get("title"), data.get("genre"), data.get("year"), data.get("author_id"))
        self.books[str(self.book_id_counter)] = book
        
        # Se o livro tem um author_id, linka ele com o autor
        if data.get("author_id") is not None:
            self.create_association(book, self.authors[data["author_id"]])

        self.book_id_counter += 1
    
    # Associa um autor com um livro
    def create_association(self, author_id: str, book_id: str) -> None:
        author = self.authors[author_id]
        book = self.books[book_id]

        author.books[book_id] = book
        book.author_id = author_id


    def create_author(self, data: dict) -> None:
        author = Author(data.get("name"), data.get("birthday"), data.get("nationality"))
        self.authors[str(self.author_id_counter)] = author
        
        self.author_id_counter += 1

    # Métodos PUT
    # Atualiza um livro específico
    def update_book(self, id: str, data: dict) -> None:
        livro = self.books.get(id)

        # Isso impede de sobscrever dados acidentalmente com None
        try: livro.title = data["title"]
        except: pass
        try: livro.genre = data["genre"]
        except: pass
        try: livro.year = data["year"]
        except: pass
        try:
            livro.author_id = data["author_id"]
            # Deleta a associação entre o autor e o livro se o novo author_id for None
            if data["author_id"] == None:
                self.delete_association(data["author_id"], id)
        except: pass

    def update_author(self, id: str, data: dict) -> None:
        author = self.authors.get(id)
        if author is None:
            return None # está tentando atualizar um autor inexistente
        
        author = self.authors.get(id)
        try: author.name = data["name"]
        except: pass
        try: author.birthday = data["birthday"]
        except: pass
        try: author.nationality = data["nationality"]
        except: pass
        

    # Métodos DELETE
    # Deleta um livro específico
    def delete_book(self, id: str) -> None:
        # remove o livro da database
        book = self.books.pop(id)
        # Deleta a associação entre o livro e o autor, se ele tiver author_id
        if book["author_id"] is not None:
            self.delete_association(book["author_id"], id)

    # Desassocia um autor com um livro
    def delete_association(self, author_id: str, book_id: str) -> None:
        author = self.authors[author_id]
        book = self.books[book_id]

        author.books.pop(book_id)
        book.author_id = None
    
    # Deleta um autor específico
    def delete_author(self, id: str) -> None:
        author = self.authors.pop(id)
        
        for book_id, book in author.books.items():
            delete_association(author, book_id)
