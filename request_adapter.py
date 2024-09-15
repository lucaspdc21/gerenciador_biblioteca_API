import json
from controller import LibraryController
# TODO: mover as mensagens de erro do status_message pra um content. do jeito que tá é bem paia.

class RequestAdapter():
    def __init__(self):
        self.controller: LibraryController = LibraryController()


    def validate_book(self, data: dict) -> dict:
        title = data.get("title")
        genre = data.get("genre")
        year = data.get("year")
        author_id = data.get("author_id")

        if type(title) != str or title is None:
            return {"status_code": 400, "status_message": "Título é obrigatório e deve ser uma string."}
        if type(genre) != str and genre is not None:
            return {"status_code": 400, "status_message": "Gênero deve ser uma string."}
        if type(year) != int and year is not None:
            return {"status_code": 400, "status_message": "Ano deve ser um número inteiro."}
        if author_id is not None:
            if type(author_id) != str:
                return {"status_code": 400, "status_message": "author_id deve ser uma string."}
            elif self.controller.get_author(author_id):
                return {"status_code": 400, "status_message": f"Não existe um autor com id {author_id}."}
        
        return {"status_code": 200}
    
    def validate_author(self, data: dict) -> dict:
        name = data.get("name")
        birthday = data.get("birthday")
        nationality = data.get("nationality")

        if type(name) != str or name is None:
            return {"status_code": 400, "status_message": "Nome é obrigatório e deve ser uma string."}
        if type(birthday) != int and birthday is not None:
            return {"status_code": 400, "status_message": "Data de nascimento deve ser um número inteiro."}
        if type(nationality) != str and nationality is not None:
            return {"status_code": 400, "status_message": "Nacionalidade deve ser uma string."}
        
        return {"status_code": 200}


    
    def get(self, path: list, data: any = None) -> dict:
        match (path[0], len(path)):
            # Pasta raíz
            case ("", 1): # GET /
                return {
                    "status_code": 200,
                    "content_type": "application/json",
                    "content": json.dumps(self.controller.list_root()),
                }
            
            # Livros
            case ("books", 1): # GET /books
                return {
                    "status_code": 200,
                    "content_type": "application/json",
                    "content": json.dumps(self.controller.list_books()),
                }    
            case ("books", 2): # GET /books/{id}
                book = self.controller.get_book(path[1])
                if book is not None:
                    return {
                        "status_code": 200,
                        "content_type": "application/json",
                        "content": json.dumps(book),
                    }
                    
            
            # Autores
            case ("authors", 1): # GET /authors
                return {
                    "status_code": 200,
                    "content_type": "application/json",
                    "content": json.dumps(self.controller.list_authors()),
                }
            case ("authors", 2): # GET /authors/{id}
                author = self.controller.get_author(path[1])
                if author is not None:
                    return {
                        "status_code": 200,
                        "content_type": "application/json",
                        "content": json.dumps(self.controller.list_authors()),
                    }
            case ("authors", 3) if path[2] == "books": # GET /authors/{id}/books
                author = self.controller.get_author(path[1])
                if author is not None:
                    return {
                        "status_code": 200,
                        "content_type": "application/json",
                        "content": json.dumps(self.controller.get_author_books(path[3])),
                    }

        # Retorna 404 Not Found se o request não for encontrado no match case
        return {"status_code": 404}
    

    # Adapta os requests POST pro controller
    def post(self, path: list, data: any) -> dict:
        if path[0] == "": # POST na pasta raiz
            return {"status_code": 403}

        p0 = path[0]
        match (p0, len(path)):
            # Requests post válidos
            case ("books", 1): # POST /books
                response = self.validate_book(data)
                if response["status_code"] != 200:
                    return response
                self.controller.create_book(data)
                return response
            case ("authors", 1): # POST /authors
                response = self.validate_author(data)
                if response["status_code"] != 200:
                    return response
                self.controller.create_author(data)
                return response
            case ("authors", 4): # POST /authors/{id}/books/{book_id}
                author = self.controller.get_author(path[1])
                book = self.controller.get_book(path[3])
                if author is not None and book is not None:
                    if author.books[path[3]] is None and book["author_id"] is None:
                        self.controller.create_association(path[1], path[3])
                        return {"status_code": 200}
                    else:
                        return {"status_code": 409} # já tem o link
                else:
                    return {"status_code": 404} # autor ou livro não existe                    

            # Requests post inválidos
            case _: # POST num livro, autor, ou livro de autor
                if self.get(path)["status_code"] != 200:
                    return {"status_code": 403}

        # Retorna 404 Not Found se o alvo do request POST não for encontrado no match case
        return {"status_code": 404}

    # TODO: Adapta os requests PUT pro controller
    def put(self, path: list, data: any) -> dict:
        pass


    # TODO: Adapta os requests DELETE pro controller
    def delete(self, path: list, data: any = None) -> dict:
        pass