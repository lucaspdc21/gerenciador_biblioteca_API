from author import Author
from book import Book

class LibraryController:
    def __init__(self):
        self.books = {}
        self.authors = {}
        self.book_id_counter = 1
        self.author_id_counter = 1

    # Métodos GET
    # Retorna um dicionário com todos os livros da biblioteca
    # (convertendo os objetos dos livros para dicionários)
    def list_books(self) -> dict:
        books = {}
        for id, book in self.books.items():
            books[id] = book.to_dict() # Converte o objeto do livro pra dicionário
        return books

    # Retorna um livro com id específico em forma de dicionário (null se não existe)
    def get_book(self, id: int) -> dict:
        book = self.books.get(id).to_dict()
        if book != None:
            return book.to_dict()
        else:
            return None; # o livro não existe
    
    # TODO: Retorna um dicionário com todos os autores da biblioteca
    # (convertendo os objetos dos autores para dicionários)
    def list_authors(self) -> dict:
        pass
    
    # TODO: Retorna um autor com id específico em forma de dicionário (null se não existe)
    def get_author(self, id: int) -> dict:
        pass

    # TODO: Retorna um dicionário com todos os livros de um autor específico
    def get_author_books(self, id: int) -> dict:
        pass


    # Métodos POST
    # Adiciona um livro na biblioteca
    def create_book(self, data: dict) -> None:
        book = Book(data.get("title"), data.get("genre"), data.get("year"), data.get("author_id"))
        self.books[self.book_id_counter] = book
        
        # Se o livro tem um author_id, linka ele com o autor
        if data.get("author_id") != None:
            self.create_association(book, self.authors[data["author_id"]])

        self.book_id_counter += 1
    
    # Associa um autor com um livro
    def create_association(self, author_id: int, book_id: int) -> None:
        author = self.authors[author_id]
        book = self.books[book_id]

        author.books[book_id] = book
        book[author_id] = author

    # TODO: Adiciona um autor na biblioteca
    def create_author(self, data: dict) -> None:
        pass


    # Métodos PUT
    # Atualiza um livro específico
    def update_book(self, id: int, data: dict) -> None:
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


    # Métodos DELETE
    # Deleta um livro específico
    def delete_book(self, id: int) -> None:
        # remove o livro da database
        book = self.books.pop(id)
        # Deleta a associação entre o livro e o autor, se ele tiver author_id
        if book != None and book["author_id"] != None:
            self.delete_association(book["author_id"], id)
        
    # Desassocia um autor com um livro
    def delete_association(self, author_id: int, book_id: int) -> None:
        author = self.authors[author_id]
        book = self.books[book_id]

        author.books.pop(book_id)
        book[author_id] = None
